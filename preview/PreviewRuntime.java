package gp.preview;

import com.google.gson.JsonParseException;
import com.google.gson.JsonParser;
import com.intellij.ide.AppLifecycleListener;
import com.intellij.ide.ui.LafManager;
import com.intellij.ide.ui.UITheme;
import com.intellij.ide.ui.laf.UIThemeLookAndFeelInfoImpl;
import com.intellij.openapi.application.ApplicationManager;
import com.intellij.openapi.diagnostic.Logger;
import com.intellij.openapi.editor.colors.EditorColorsManager;
import com.intellij.openapi.editor.colors.impl.EditorColorsSchemeImpl;
import com.intellij.openapi.util.Disposer;
import com.intellij.openapi.util.InvalidDataException;
import com.intellij.openapi.util.JDOMUtil;
import com.intellij.util.concurrency.AppExecutorUtil;
import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.concurrent.TimeUnit;
import javax.swing.UIManager;
import org.jdom.JDOMException;

public final class PreviewRuntime implements AppLifecycleListener {
    private static final Logger LOG = Logger.getInstance(PreviewRuntime.class);
    private byte[] previousTheme;
    private byte[] previousScheme;

    @Override
    public void appStarted() {
        var app = ApplicationManager.getApplication();
        var resources = Path.of(System.getProperty("one.dark.preview.resources"));
        var refresh = AppExecutorUtil.getAppScheduledExecutorService().scheduleWithFixedDelay(() -> {
            try {
                var theme = Files.readAllBytes(resources.resolve("onedarkbygp.theme.json"));
                var scheme = Files.readAllBytes(resources.resolve("onedarkbygp.xml"));
                if (Arrays.equals(theme, previousTheme) && Arrays.equals(scheme, previousScheme)) {
                    return;
                }
                previousTheme = theme;
                previousScheme = scheme;
                app.invokeLater(() -> applyTheme(theme, scheme));
            }
            catch (IOException error) {
                LOG.warn("Cannot read preview source files", error);
            }
        }, 0, 500, TimeUnit.MILLISECONDS);
        Disposer.register(app, () -> refresh.cancel(false));
    }

    private static void applyTheme(byte[] themeSource, byte[] schemeSource) {
        var colors = EditorColorsManager.getInstance();
        var scheme = new EditorColorsSchemeImpl(colors.getScheme("Darcula"));
        final UITheme theme;
        try {
            scheme.readExternal(JDOMUtil.load(new ByteArrayInputStream(schemeSource)));
            var json = JsonParser.parseString(new String(themeSource, StandardCharsets.UTF_8)).getAsJsonObject();
            json.addProperty("editorScheme", scheme.getName());
            theme = UITheme.Companion.loadTempThemeFromJson(
                new ByteArrayInputStream(json.toString().getBytes(StandardCharsets.UTF_8)), "one-dark-preview"
            );
        }
        catch (IOException | JDOMException | InvalidDataException | JsonParseException | IllegalStateException error) {
            LOG.warn("Preview source is invalid; keeping the last applied theme", error);
            return;
        }

        // A fresh scheme and theme avoid the editable-copy and plugin-resource caches.
        colors.addColorScheme(scheme);
        var laf = LafManager.getInstance();
        laf.setAutodetect(false);
        laf.setCurrentUIThemeLookAndFeel(new UIThemeLookAndFeelInfoImpl(theme));
        colors.setGlobalScheme(scheme);
        laf.updateUI();
        LOG.info(String.format(
            "Preview applied: panel=#%06X editor=#%06X scheme=%s",
            UIManager.getColor("Panel.background").getRGB() & 0xffffff,
            colors.getGlobalScheme().getDefaultBackground().getRGB() & 0xffffff,
            colors.getGlobalScheme().getName()
        ));
    }
}
