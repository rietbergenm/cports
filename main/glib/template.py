pkgname = "glib"
_mver = "2.70"
pkgver = f"{_mver}.0"
pkgrel = 0
build_style = "meson"
# TODO: gtk-doc
configure_args = ["-Dfam=false", "-Dman=true", "-Dselinux=disabled"]
hostmakedepends = [
    "meson", "gettext-tiny", "pkgconf", "docbook-xsl-nons", "xsltproc"
]
makedepends = [
    "zlib-devel", "pcre-devel", "libffi-devel", "dbus-devel",
    "elftoolchain-devel", "libmount-devel",
]
# not yet all available
checkdepends = [
    "desktop-file-utils", "shared-mime-info", "dbus", "python-pytest"
]
pkgdesc = "GLib library of C routines"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/GLib"
source = f"$(GNOME_SITE)/{pkgname}/{_mver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "200d7df811c5ba634afbf109f14bb40ba7fde670e89389885da14e27c0840742"
# missing checkdepends
options = ["!check"]

def do_check(self):
    self.do("dbus-run-session", ["ninja", "-C", "build", "test"])

def post_install(self):
    self.install_license("COPYING")

@subpackage("libglib-devel")
def _libdevel(self):
    self.pkgdesc = f"{pkgdesc} (library development files)"

    return [
        "usr/include",
        "usr/lib/glib-2.0",
        "usr/lib/pkgconfig",
        "usr/lib/*.so",
        "usr/lib/*.a",
    ]

@subpackage("glib-devel")
def _devel(self):
    self.depends += [f"libglib-devel={pkgver}-r{pkgrel}"]

    return self.default_devel(extra = [
        "usr/bin/glib-compile-resources",
        "usr/bin/glib-genmarshal",
        "usr/bin/glib-gettextize",
        "usr/bin/glib-mkenums",
        "usr/bin/gtester",
        "usr/bin/gtester-report",
        "usr/bin/gdbus-codegen",
        "usr/share/man/man1/glib-compile-resources.1",
        "usr/share/man/man1/glib-genmarshal.1",
        "usr/share/man/man1/glib-gettextize.1",
        "usr/share/man/man1/glib-mkenums.1",
        "usr/share/man/man1/gtester.1",
        "usr/share/man/man1/gtester-report.1",
        "usr/share/man/man1/gdbus-codegen.1",
        "usr/share/glib-2.0",
        "usr/share/gdb",
    ])
