pkgname = "nix"
pkgver = "2.25.3"
pkgrel = 0
build_style = "meson"
configure_args = [
    # Use /usr/lib instead of /usr/libexec
    "--libexecdir=/usr/lib",

    # profile-dir defaults to etc/profile.d which becomes
    # /usr/etc/profile.d with the prefix /usr. This is wrong,
    # we want these system files to go in /etc/profile.d.
    "-Dnix:profile-dir=/etc/profile.d",

    # We need the below to fix "ERROR: clang does not know how to do prelinking."
    "-Ddefault_library=shared",

    # The doc-gen target requires network to download from nixpkgs.
    # We don't have network in the build phase, so we don't do it.
    "-Ddoc-gen=false",

    # We don't need the perl bindings (and don't have the dependencies to build it).
    "-Dbindings=false",

    # We don't do test as it requires network, so don't build them.
    "-Dunit-tests=false",

    # Use libedit instead of editline or readline.
    "-Dlibcmd:readline-flavor=readline",
]
hostmakedepends = [
    "meson",
    "bison",
    "flex",
    "cmake",
    "pkgconf",
    "bash",

    # These are needed for the doc-gen target,
    # but we are currently not building that as
    # it requires network.
    #"doxygen",
    #"mdbook", # not upstreamed
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
    "lowdown-devel",
    "libgit2-devel",    # should be newer that 1.9.0 (1.8.9 in upstream)
    "toml11",           # not upstreamed


    # use libedit from chimera, instead of editline or readline which
    # nix supports. It works, but tab completion and history in nix repl
    # don't work on both realine and libedit...
    "libedit-devel",


    # libcpuid is an optional dependency:
    # On x86_64 it can be used to determine microarchitecture levels,
    # but I couldn't find where nix really makes use of this, so there
    # seemed to be very little benefit to porting an architecture dependent
    # library to chimera just to include as an optional dependency of nix for
    # only one architecture.
    #"libcpuid-devel", # not upstreamed
]
# We don't actually use these at the moment, because checks are disabled.
checkdepends = [
    "rapidcheck",       # not upstreamed
    "gtest-devel",
]
pkgdesc = "Purely functional package manager"
maintainer = "Mathijs Rietbergen <mathijs.rietbergen@proton.me>"
license = "LGPL-2.1-or-later"
url = "https://github.com/NixOS/nix"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "8d7af0d25371da32783f0b46bce8ff4f0d1dd996db6dee272faf306fcb8e2073"
# Without `int` enabled, all nix tools constantly fail with "Illegal instruction".
hardening = [ "!int" ]
# Checks require network to download from nixpkgs, but network is not available
# in check phase.
options = [ "!check" ]

def post_install(self):
    # remove installed systemd files
    self.uninstall("usr/lib/systemd/*/*", glob = True)
    self.uninstall("usr/lib/systemd")


@subpackage("nix-devel")
def _(self):
    return self.default_devel()
