pkgname = "u-boot-qemu-riscv64_smode"
pkgver = "2025.01"
pkgrel = 0
build_style = "u_boot"
hostmakedepends = [
    "bison",
    "dtc",
    "flex",
    "gcc-riscv64-unknown-elf",
    "gnutls-devel",
    "openssl3-devel",
    "python-setuptools",
    "util-linux-uuid-devel",
]
pkgdesc = "U-Boot for qemu-riscv64 supervisor mode"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only AND BSD-3-Clause"
url = "https://www.denx.de/wiki/U-Boot"
source = f"https://ftp.denx.de/pub/u-boot/u-boot-{pkgver}.tar.bz2"
sha256 = "cdef7d507c93f1bbd9f015ea9bc21fa074268481405501945abc6f854d5b686f"
env = {
    "U_BOOT_TRIPLET": "riscv64-unknown-elf",
    "U_BOOT_TARGETS": "u-boot",
}
hardening = ["!int"]
# not relevant
options = ["!strip", "!check", "!lto", "!debug", "foreignelf", "execstack"]
