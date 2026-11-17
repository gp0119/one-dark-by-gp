#!/usr/bin/env python3
"""Run an isolated WebStorm instance that previews theme source files on save."""

import argparse
import fcntl
import os
from pathlib import Path
import shutil
import subprocess
from zipfile import ZIP_DEFLATED, ZipFile

from build import RESOURCES, ROOT, webstorm_contents


SANDBOX = ROOT / ".preview"


def build_runtime(contents):
    classes = SANDBOX / "classes"
    if classes.exists():
        shutil.rmtree(classes)
    classes.mkdir(exist_ok=True)
    subprocess.run([
        str(contents / "jbr/Contents/Home/bin/javac"),
        "-proc:none", "-classpath", str(contents / "lib/*"),
        "-d", str(classes), str(ROOT / "preview/PreviewRuntime.java"),
        *map(str, sorted((ROOT / "src").rglob("*.java"))),
    ], check=True)
    destination = SANDBOX / "plugins/one-dark-preview/lib/runtime.jar"
    destination.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(destination, "w", ZIP_DEFLATED) as archive:
        archive.writestr("META-INF/plugin.xml", '''<idea-plugin require-restart="true">
  <id>gp.one-dark-preview</id><name>One Dark Preview Runtime</name><version>1</version>
  <vendor>gp</vendor><depends>com.intellij.modules.lang</depends>
  <depends>com.intellij.modules.vcs</depends>
  <extensions defaultExtensionNs="com.intellij">
    <projectViewNodeDecorator implementation="gp.theme.IgnoredDirectoryDecorator" order="last" />
  </extensions>
  <applicationListeners>
    <listener class="gp.preview.PreviewRuntime" topic="com.intellij.ide.AppLifecycleListener" />
  </applicationListeners>
</idea-plugin>''')
        for path in classes.rglob("*.class"):
            archive.write(path, path.relative_to(classes).as_posix())


def main():
    parser = argparse.ArgumentParser(description="在 WebStorm 中实时预览主题")
    parser.add_argument("project", nargs="?", type=Path, help="预览项目目录；默认打开欢迎页，由你选择项目")
    parser.add_argument("--theme", choices=["dark", "light"], default="dark", help="预览配色；默认 dark")
    args = parser.parse_args()
    selected_project = args.project
    theme_name = f"one{args.theme}bygp"
    if selected_project is not None:
        selected_project = selected_project.expanduser().resolve()
        if not selected_project.is_dir():
            parser.error(f"项目目录不存在：{selected_project}")

    contents = webstorm_contents()
    launcher = contents / "MacOS/webstorm"

    SANDBOX.mkdir(exist_ok=True)
    with (SANDBOX / "preview.lock").open("w") as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise SystemExit("预览已在运行，请先关闭已有预览。")

        for folder in ["config/options", "system", "log", "plugins"]:
            (SANDBOX / folder).mkdir(parents=True, exist_ok=True)
        options = SANDBOX / "config/options"
        # The source-backed preview theme is created after startup, so boot with a bundled theme.
        (options / "laf.xml").write_text(
            '<application><component name="LafManager">'
            f'<laf themeId="{"Darcula" if args.theme == "dark" else "IntelliJ"}" /></component></application>'
        )

        # Keep the welcome screen available even after a previous preview opened a project.
        command = [str(launcher), "dontReopenProjects"]
        if selected_project is not None:
            command.append(str(selected_project))

        build_runtime(contents)
        vmoptions = SANDBOX / "webstorm.vmoptions"
        vmoptions.write_text(
            "\n".join([
                f"-Didea.config.path={SANDBOX / 'config'}",
                f"-Didea.system.path={SANDBOX / 'system'}",
                f"-Didea.plugins.path={SANDBOX / 'plugins'}",
                f"-Didea.log.path={SANDBOX / 'log'}",
                f"-Done.dark.preview.resources={RESOURCES}",
                f"-Done.dark.preview.theme={theme_name}",
                "-Didea.initially.ask.config=false",
                f"-XX:ErrorFile={SANDBOX / 'log/java_error_%p.log'}",
                f"-XX:HeapDumpPath={SANDBOX / 'log'}",
            ]) + "\n"
        )
        environment = {**os.environ, "WEBIDE_VM_OPTIONS": str(vmoptions)}
        with (SANDBOX / "launcher.log").open("a") as output:
            process = subprocess.Popen(
                command, env=environment,
                stdout=output, stderr=subprocess.STDOUT,
            )
            print("WebStorm 预览已启动；保存主题 JSON/XML 后约 0.5 秒自动刷新。Ctrl+C 停止。", flush=True)
            try:
                process.wait()
            except KeyboardInterrupt:
                process.terminate()
                process.wait()
                return
            if process.returncode:
                raise SystemExit(f"WebStorm 已退出，详情见 {SANDBOX / 'launcher.log'}")


if __name__ == "__main__":
    main()
