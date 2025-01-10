pkgname = "go-task"
pkgver = "3.40.1"
pkgrel = 0
build_style = "go"
make_build_args = ["./cmd/task"]
hostmakedepends = ["go"]
pkgdesc = "Task runner / simpler Make alternative written in Go"
maintainer = "Mathijs Rietbergen <mathijs.rietbergen@proton.me>"
license = "MIT"
url = "https://taskfile.dev"
source = f"https://github.com/go-task/task/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e80cdfa2afefa69238e5078960d50a8e703de1043740b277946629ca5f3bde85"


def post_install(self):
    self.install_license("LICENSE")

    self.install_files("website/docs/", "usr/share/doc", name=pkgname)
    self.uninstall(f"usr/share/doc/{pkgname}/reference/_category_.yml")

    self.install_completion("completion/fish/task.fish", "fish", "task")
    self.install_completion("completion/bash/task.bash", "bash", "task")
    self.install_completion("completion/zsh/_task", "zsh", "task")
