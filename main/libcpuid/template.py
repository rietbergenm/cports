pkgname = "libcpuid"
pkgver = "0.7.1"
pkgrel = 0
pkgdesc = "Small C library for x86 CPU detection and feature extraction"
maintainer = "Mathijs Rietbergen <mathijs.rietbergen@proton.me>"
license = "custom:libcpuid"
url = "https://github.com/anrieff/libcpuid"

build_style = "configure"
hostmakedepends = [ "pkgconf" ]
configure_args = [ "--prefix=/usr" ]
source = f"{url}/releases/download/v{pkgver}/libcpuid-{pkgver}.tar.gz"
sha256 = "f5fc4ba4cf19e93e62d3ed130f47045245d682b10506ad29937dacae1bdccc35"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libcpuid-devel")
def _(self):
    return self.default_devel()

@subpackage("libcpuid-progs")
def _(self):
    return self.default_progs()
