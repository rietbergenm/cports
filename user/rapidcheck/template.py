pkgname = "rapidcheck"
# upstream does not tag releases, there is only the master branch
pkgver = "0_git20231214"
_commit = "ff6af6fc683159deb51c543b065eba14dfcf329b"
pkgrel = 0
build_style = "cmake"
configure_args = [
    f"-DPKG_CONFIG_VERSION={pkgver}",
    "-DBUILD_SHARED_LIBS=ON"
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
pkgdesc = "Testing framework for C++"
maintainer = "Mathijs Rietbergen <mathijs.rietbergen@proton.me>"
license = "BSD-2-Clause"
url = "https://github.com/emil-e/rapidcheck"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "7ae7a8d59560f94eb68ed09fda59abd9871fe3b0cfc5acc60506de506289aa24"
# TODO: tests require cloning git submodules and first compiling catch2 and gtest
# they are in the repos, but the version of catch2 used in this project is over
# 7 years old, so it is completely incompatible with the current iteration.
options = [ "!check" ]

def post_install(self):
    self.install_license("LICENSE.md")
