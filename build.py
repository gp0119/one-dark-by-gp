#!/usr/bin/env python3
"""Compile the project-tree extension and package the theme plugin."""

import os
from pathlib import Path
import shutil
import subprocess
from tempfile import TemporaryDirectory
from zipfile import ZIP_DEFLATED, ZipFile


ROOT = Path(__file__).resolve().parent
RESOURCES = ROOT / "resources"


def webstorm_contents():
    if "WEBSTORM_APP" in os.environ:
        app = Path(os.environ["WEBSTORM_APP"]).expanduser()
    else:
        app = next((path for path in [
            Path.home() / "Applications/WebStorm.app", Path("/Applications/WebStorm.app"),
        ] if path.exists()), Path("/Applications/WebStorm.app"))
    contents = app / "Contents"
    if not (contents / "MacOS/webstorm").is_file():
        raise SystemExit("找不到 WebStorm，请设置 WEBSTORM_APP 为 WebStorm.app 路径。")
    return contents


def main():
    contents = webstorm_contents()
    with TemporaryDirectory(prefix="one-dark-build-") as temporary:
        directory = Path(temporary)
        classes = directory / "classes"
        classes.mkdir()
        subprocess.run([
            str(contents / "jbr/Contents/Home/bin/javac"),
            "--release", "11", "-proc:none", "-classpath", str(contents / "lib/*"),
            "-d", str(classes),
            *map(str, sorted((ROOT / "src").rglob("*.java"))),
        ], check=True)

        archive_path = directory / "one-dark-by-gp.jar"
        with ZipFile(archive_path, "w", ZIP_DEFLATED) as archive:
            for root in (RESOURCES, classes):
                for path in sorted(root.rglob("*")):
                    if path.is_file():
                        archive.write(path, path.relative_to(root).as_posix())
            archive.write(ROOT / "LICENSE", "LICENSE")
        destination = ROOT / archive_path.name
        shutil.copyfile(archive_path, destination)
        print(f"插件已打包：{destination}")


if __name__ == "__main__":
    main()
