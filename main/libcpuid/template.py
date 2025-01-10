pkgname = "libcpuid"
pkgver = "0.7.1"
pkgrel = 0
pkgdesc = "Small C library for x86 CPU detection and feature extraction"
maintainer = "Mathijs Rietbergen <mathijs.rietbergen@proton.me>"
license = "custom:libcpuid"
url = "https://github.com/anrieff/libcpuid"

build_style = "cmake"
configure_args = [
    "-DLIBCPUID_ENABLE_TESTS=ON",
    "-DLIBCPUID_DRIVER_ARM_LINUX_DKMS=ON" # ship the arm dkms module
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "doxygen"
]
checkdepends = [
    "python"
]
make_check_target = "test-old test-fast" # do all test there are
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "c54879ea33b68a2e752c20fb0e3cd04439a9177eab23371f709f15a45df43644"
archs = [ "x86_64" ]

def post_install(self):
    self.install_license("COPYING")

    # the kernel module is called "cpuid", not "libcpuid"
    src_path = f"usr/src/cpuid-{pkgver}"
    self.install_file(self.files_path / "ckms.ini", src_path)
    self.uninstall(src_path + "/dkms.conf")

@subpackage("libcpuid-devel")
def _(self):
    return self.default_devel()

@subpackage("libcpuid-progs")
def _(self):
    return self.default_progs()

# x86_64 does not need kernel modules (they are in-tree),
# but there is a dkms module for aarch32/64
@subpackage("libcpuid-ckms", self.profile().arch == "aarch64")
def _(self):
    self.subdesc = "kernel sources"
    self.install_if = [ self.parent, "ckms" ]
    self.depends = [
        self.parent,
        "ckms",
        "gmake"
    ]

    return [ "usr/src" ]
