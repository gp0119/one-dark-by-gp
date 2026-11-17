package gp.theme;

import com.intellij.ide.projectView.PresentationData;
import com.intellij.ide.projectView.ProjectViewNode;
import com.intellij.ide.projectView.ProjectViewNodeDecorator;
import com.intellij.openapi.project.DumbAware;
import com.intellij.openapi.vcs.FileStatus;
import com.intellij.openapi.vcs.FileStatusManager;
import com.intellij.util.IconUtil;
import javax.swing.UIManager;
import org.jetbrains.annotations.NotNull;

public final class IgnoredDirectoryDecorator implements ProjectViewNodeDecorator, DumbAware {
    @Override
    public void decorate(@NotNull ProjectViewNode<?> node, @NotNull PresentationData presentation) {
        if (!UIManager.getBoolean("OneDarkByGP.dimIgnoredDirectories")) {
            return;
        }

        var file = node.getVirtualFile();
        var project = node.getProject();
        if (project == null || file == null || !file.isDirectory()) {
            return;
        }

        var status = FileStatusManager.getInstance(project).getStatus(file);
        if (status != FileStatus.IGNORED && !"IGNORE.PROJECT_VIEW.IGNORED".equals(status.getId())) {
            return;
        }

        var icon = presentation.getIcon(false);
        var color = status.getColor();
        if (icon != null && color != null) {
            // Tint the existing icon so icon plugins and folder badges keep their shapes.
            presentation.setIcon(IconUtil.colorize(icon, color));
        }
    }
}
