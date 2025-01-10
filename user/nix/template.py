pkgname = "nix"
pkgver = "2.25.3"
pkgrel = 0
pkgdesc = "Purely functional package manager"
maintainer = "Mathijs Rietbergen <mathijs.rietbergen@proton.me>"
license = "LGPL-2.1-or-later"
url = "https://github.com/NixOS/nix"

build_style = "meson"

configure_args = [
    "--libexecdir=/usr/lib", #XXX: no /usr/libexec
    "-Dnix:profile-dir=/etc/profile.d", # defaults to etc/profile.d which becomes /usr/etc/profile.d with the prefix
    "-Dlibcmd:readline-flavor=readline",
    # next one fixes "ERROR: clang does not know how to do prelinking."
    "-Ddefault_library=shared",
    "-Ddoc-gen=false",
    "-Dbindings=false",
    "-Dunit-tests=false"
]
hostmakedepends = [
    "meson",
    "bison",
    "flex",
    "cmake",
    "pkgconf",
    "bash",

    # doc-gen target (wip)
    #"doxygen",
    #"mdbook", not in cports yet

    # bindings target (wip)
    # generates bindings for perl language
    #"perl",
    #"curl"
    # needs libdbi for perl, but not packaged yet
]
makedepends = [
    "boost-devel",
    "openssl-devel",
    "libarchive-devel",
    "libsodium-devel",
    "brotli-devel",
    "nlohmann-json",
    "curl-devel",
    "libseccomp-devel",
    "sqlite-devel",
    "libgit2-devel", # XXX: should be newer that 1.9.0
    "gc-devel",
    #"toml11",
    "libedit-readline-devel",
    "lowdown-devel",
    #"libcpuid-devel" # TODO: check if only for x86_64 or for all
]
checkdepends = [
    # unit-tests target (wip)
    #"rapidcheck", not in cports yet
]
options = [ "!check" ]

source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "8d7af0d25371da32783f0b46bce8ff4f0d1dd996db6dee272faf306fcb8e2073"


def post_install(self):
    # remove installed systemd files
    self.uninstall("usr/lib/systemd/*/*", glob = True)
    self.uninstall("usr/lib/systemd")



@subpackage("nix-devel")
def _(self):
    return self.default_devel()
