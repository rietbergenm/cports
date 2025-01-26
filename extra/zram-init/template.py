pkgname = "zram-init"
pkgver = "12.1"
pkgrel = 0
build_style = "makefile"
make_build_args = [
    "PREFIX=/usr",
    "GETTEXT=false", # couldn't get locales to work
]
make_install_args = [
    # PREFIX is set to /usr by default in install phase
    "BINDIR=$(DESTDIR)$(PREFIX)/bin",
    "GETTEXT=false",
    "MODPROBED=false",
    "SYSTEMD=false",
    "OPENRC=false",
]
#hostmakedepends = [ "gettext" ]
depends = [
    # chimerautils
    "cmd:sh!chimerautils",
    "cmd:sleep!chimerautils",
    "cmd:test!chimerautils",
    "cmd:chown!chimerautils",
    "cmd:chmod!chimerautils",
    # "cmd:logger", # optional, but part of chimerautils, so installed anyways?

    # gettext TODO: can't get it to work
    #"gettext", # optional, but translations won't work
    
    # zramctl
    "cmd:zramctl!zramctl",
    # kmod
    "cmd:modprobe!kmod",
    # mount
    "cmd:swapoff!mount",
    "cmd:swapon!mount",
    "cmd:mount!mount",
    "cmd:umount!mount",
    # mkfs
    "cmd:mkswap!mkfs",
    # e2fsprogs
    "cmd:mkfs.ext2!e2fsprogs",
    "cmd:mkfs.ext3!e2fsprogs",
    "cmd:mkfs.ext4!e2fsprogs",
    "cmd:tune2fs!e2fsprogs",
    # xfsprogs
    "cmd:mkfs.xfs!xfsprogs",
    # btrfs-progs
    "cmd:mkfs.btrfs!btrfs-progs",
]
pkgdesc = "Wrapper script for the zram linux kernel module with zsh support"
maintainer = "Mathijs Rietbergen <mathijs.rietbergen@proton.me>"
license = "GPL-2.0-only"
url = "https://github.com/vaeth/zram-init"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d5e095adafbe1cfd9b1e22c60ee0e32fe802c3616ddfc2ef32a559848f97bf5a"
# there are no checks
options = ["!check"]

def post_install(self):
    self.install_file(self.files_path / 'zram-init', 'usr/lib/dinit.d')
