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
    "-DLIBCPUID_BUILD_DRIVERS=OFF" # only available on arm?
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

@subpackage("libcpuid-devel")
def _(self):
    return self.default_devel()

@subpackage("libcpuid-progs")
def _(self):
    return self.default_progs()
