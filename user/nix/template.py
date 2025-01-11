pkgname = "nix"
pkgver = "2.25.3"
pkgrel = 0
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/lib", #XXX: no /usr/libexec
    "-Dnix:profile-dir=/etc/profile.d", # defaults to etc/profile.d which becomes /usr/etc/profile.d with the prefix
    #"-Dlibcmd:readline-flavor=readline",
    # next one fixes "ERROR: clang does not know how to do prelinking."
    "-Ddefault_library=shared",
    "-Ddoc-gen=false",   # needs internet
    "-Dbindings=false",  # we don't need the perl bindings
    "-Dunit-tests=false" # requires rapidcheck which is not packaged
]
hostmakedepends = [
    "meson",
    "bison",
    "flex",
    "cmake",
    "pkgconf",
    "bash",

    # doc-gen target requires internet because
    # it uses nix to run stuff and nix needs internet to download
    # dependecies (it has just been built)
    #"doxygen",
    #"mdbook", # packaged myself

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
    "gc-devel",
    #"libedit-readline-devel",
    "lowdown-devel",
    "libgit2-devel", # XXX: should be newer that 1.9.0
    "toml11", # packaged myself
    "editline-devel",
    # TODO: check if only for x86_64 or for all
    # seems to only use this library on x86_64
    #"libcpuid-devel" 
]
checkdepends = [
    # unit-tests target (wip)
    #"rapidcheck", not in cports yet
]
options = [ "!check" ]
pkgdesc = "Purely functional package manager"
maintainer = "Mathijs Rietbergen <mathijs.rietbergen@proton.me>"
license = "LGPL-2.1-or-later"
url = "https://github.com/NixOS/nix"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "8d7af0d25371da32783f0b46bce8ff4f0d1dd996db6dee272faf306fcb8e2073"
hardening = [ "!int" ] # without this, it constantly fails with illegal instructions


def post_install(self):
    # remove installed systemd files
    self.uninstall("usr/lib/systemd/*/*", glob = True)
    self.uninstall("usr/lib/systemd")



@subpackage("nix-devel")
def _(self):
    '''
    self.depends = [
        "pc:nlohmann_json>=3.9!nlohmann-json",
        "pc:libgit2!libgit2-devel",
        "pc:libarchive>=3.1.2!libarchive-devel",
        "pc:libcurl!curl-devel",
        "pc:libseccomp>=2.5.5!libseccomp-devel",
        "pc:sqlite3>=3.6.19!sqlite-devel",
        "pc:bdw-gc!gc-devel",
        "pc:libcrypto>=1.1.1!openssl-devel",
        "pc:libsodium!libsodium-devel",
        "pc:libbrotlicommon!brotli-devel",
        "pc:libbrotlidec!brotli-devel",
        "pc:libbrotlienc!brotli-devel",
        "pc:lowdown>=0.9.0!lowdown-devel",
        #"pc:libcpuid!libcpuid-devel",
        "libedit-readline-devel", # does not provide pc:readline according to apk, but does have the .pc file
        #"boost-devel",
        #"toml11",
    ]
    self.options = [ "!scanrundeps" ]
    '''
    return self.default_devel()
