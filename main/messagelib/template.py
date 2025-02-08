pkgname = "messagelib"
pkgver = "24.12.2"
pkgrel = 0
build_style = "cmake"
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "akonadi-contacts-devel",
    "akonadi-devel",
    "akonadi-mime-devel",
    "akonadi-search-devel",
    "gpgme-qt-devel",
    "grantleetheme-devel",
    "karchive-devel",
    "kcodecs-devel",
    "kcolorscheme-devel",
    "kcompletion-devel",
    "kconfig-devel",
    "kcontacts-devel",
    "kcoreaddons-devel",
    "kdbusaddons-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kidentitymanagement-devel",
    "kio-devel",
    "kitemviews-devel",
    "kjobwidgets-devel",
    "kmailtransport-devel",
    "kmbox-devel",
    "kmime-devel",
    "knewstuff-devel",
    "knotifications-devel",
    "kservice-devel",
    "ktextaddons-devel",
    "ktexttemplate-devel",
    "ktextwidgets-devel",
    "kwidgetsaddons-devel",
    "kxmlgui-devel",
    "libgravatar-devel",
    "libkdepim-devel",
    "libkleo-devel",
    "pimcommon-devel",
    "qca-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtwebengine-devel",
    "sonnet-devel",
    "syntax-highlighting-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE PIM messaging library"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later AND GPL-2.0-or-later"
url = "https://api.kde.org/kdepim/messagelib/html"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/messagelib-{pkgver}.tar.xz"
sha256 = "f41112745fee178a476b6bfbf6e027db027f5701b474a7a6b8ea61d4983495f5"
# fails a ton of tests due to not finding its own plugins from build tree
options = ["!check"]


@subpackage("messagelib-devel")
def _(self):
    self.depends += [
        "akonadi-devel",
        "akonadi-mime-devel",
        "kcontacts-devel",
        "kidentitymanagement-devel",
        "kmime-devel",
        "kservice-devel",
        "ktextaddons-devel",
        "libkleo-devel",
        "pimcommon-devel",
        "qt6-qtwebengine-devel",
    ]
    return self.default_devel()
