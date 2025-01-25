pkgname = "toml11"
pkgver = "4.2.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DTOML11_BUILD_TESTS=ON",
    "-DTOML11_BUILD_TOML_TESTS=ON",
]
hostmakedepends = ["cmake", "ninja", "doctest", "nlohmann-json"]
pkgdesc = "Feature-rich TOML language library for C++11/14/17/20"
maintainer = "Mathijs Rietbergen <mathijs.rietbergen@proton.me>"
license = "MIT"
url = "https://github.com/ToruNiina/toml11"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "9287971cd4a1a3992ef37e7b95a3972d1ae56410e7f8e3f300727ab1d6c79c2c"
hardening = ["!int"]  # if enabled, test_parse_integer fails...


def post_install(self):
    self.install_license("LICENSE")
