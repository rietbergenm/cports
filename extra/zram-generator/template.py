pkgname = "zram-generator"
pkgver = "1.1.2"
pkgrel = 0
build_style = "makefile"
make_env = {
    "NOMAN":'1',
    #"SYSTEMD_UTIL_DIR":"
    "SYSTEMD_UTIL_DIR":"/usr/lib/systemd",
    "SYSTEMD_SYSTEM_GENERATOR_DIR":"/usr/lib/systemd/system-generators",
}
make_build_target = "build"
make_build_args = [
    "SYSTEMD_UTIL_DIR=/usr/lib/systemd",
    "SYSTEMD_SYSTEM_GENERATOR_DIR=/usr/lib/systemd/system-generators",
]
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
pkgdesc = "Systemd unit generator for zram devices"
maintainer = "Mathijs Rietbergen <mathijs.rietbergen@proton.me>"
license = "MIT"
url = "https://github.com/systemd/zram-generator"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "506d47acbabffa7013bb40a1f61c6edfa758a7bd55820d06ef49c7bc83dba762"
