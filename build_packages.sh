#!/usr/bin/env bash
set -e

VERSION="0.1.0"
LINUX_GUI_BIN="$2"

if [[ -z "$VERSION" || -z "$LINUX_GUI_BIN" ]]; then
  echo "Usage: $0 <version> <path-to-linux-gui-binary>"
  exit 1
fi

ARCH=$(dpkg --print-architecture)
DEB_OUT="cloudfuse-gui_${VERSION}_${ARCH}.deb"
RPM_OUT="cloudfuse-gui-${VERSION}-${ARCH}.rpm"

#--- Build DEB ---
rm -rf deb_build
mkdir -p deb_build/DEBIAN
mkdir -p deb_build/usr/lib/cloudfuse-gui
mkdir -p deb_build/usr/bin
mkdir -p deb_build/usr/share/applications
mkdir -p deb_build/usr/share/doc/cloudfuse-gui

cp -r "$LINUX_GUI_BIN"/* deb_build/usr/lib/cloudfuse-gui

# Substitute version and ensure Depends: cloudfuse is present
sed "s/@@VERSION@@/${VERSION}/g" packaging/deb/control >  deb_build/DEBIAN/control

cp cloudfuse.desktop deb_build/usr/share/applications/
cp packaging/deb/copyright deb_build/usr/share/doc/cloudfuse-gui/

# Strip binaries and libraries to reduce size and fix lintian errors
find deb_build/usr/lib/cloudfuse-gui -type f \( -name "*.so*" -o -executable \) -exec strip --strip-unneeded {} +

# Fix all directory and file permissions
find deb_build -type d -exec chmod 0755 {} +
find deb_build -type f -exec chmod 0644 {} +

chmod +x deb_build/usr/lib/cloudfuse-gui/cloudfuseGUI
ln -s "../lib/cloudfuse-gui/cloudfuseGUI" "deb_build/usr/bin/cloudfuse-gui"

fakeroot dpkg-deb --build deb_build "$DEB_OUT"

# --- Build RPM ---
rm -rf rpm_build
mkdir -p rpm_build/{BUILD,RPMS,SOURCES,SPECS,SRPMS}

TMP_SRC_DIR="cloudfuse-gui-${VERSION}"
rm -rf "${TMP_SRC_DIR}"
mkdir -p "${TMP_SRC_DIR}"
cp -r "${LINUX_GUI_BIN}"/* "${TMP_SRC_DIR}/"
tar -czf rpm_build/SOURCES/cloudfuse-gui.tar.gz "${TMP_SRC_DIR}"
cp cloudfuse.desktop rpm_build/SOURCES/
cp README.md rpm_build/SOURCES/
cp LICENSE rpm_build/SOURCES/

# Substitute version
sed "s/@@VERSION@@/${VERSION}/g" packaging/rpm/cloudfuse-gui.spec > rpm_build/SPECS/cloudfuse-gui.spec

rpmbuild -bb --define "_topdir $(pwd)/rpm_build" --define "dist .$(lsb_release -cs)" rpm_build/SPECS/cloudfuse-gui.spec
find rpm_build/RPMS -name '*.rpm' | xargs -I {} mv {} "$RPM_OUT"
