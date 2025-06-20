#!/usr/bin/env bash
set -e

VERSION="$1"
LINUX_GUI_BIN="$2"

if [[ -z "$VERSION" || -z "$LINUX_GUI_BIN" ]]; then
  echo "Usage: $0 <version> <path-to-linux-gui-binary>"
  exit 1
fi

ARCH=$(dpkg --print-architecture)
DEB_OUT="cloudfuse-gui_${VERSION}_${ARCH}.deb"
RPM_OUT="cloudfuse-gui-${VERSION}-1.${ARCH}.rpm"

# --- Build DEB ---
rm -rf deb_build
mkdir -p deb_build/DEBIAN
mkdir -p deb_build/usr/bin
mkdir -p deb_build/usr/share/applications
mkdir -p deb_build/usr/share/doc/cloudfuse-gui

cp "$LINUX_GUI_BIN" deb_build/usr/bin/cloudfuseGUI
chmod +x deb_build/usr/bin/cloudfuseGUI

# Substitute version and ensure Depends: cloudfuse is present
sed "s/@@VERSION@@/${VERSION}/g" packaging/deb/control >  deb_build/DEBIAN/control

cp cloudfuse.desktop deb_build/usr/share/applications/
cp packaging/deb/copyright deb_build/usr/share/doc/cloudfuse-gui/

chmod 0755 deb_build/usr/
chmod 0755 deb_build/usr/bin/
chmod 0755 deb_build/usr/share/
chmod 0755 deb_build/usr/share/applications/
chmod 0755 deb_build/usr/share/doc/
chmod 0755 deb_build/usr/share/doc/cloudfuse-gui/

chmod 0644 deb_build/usr/share/applications/cloudfuse.desktop
chmod 0644 deb_build/usr/share/doc/cloudfuse-gui/copyright

fakeroot dpkg-deb --build deb_build "$DEB_OUT"

# --- Build RPM ---
rm -rf rpm_build
mkdir -p rpm_build/{BUILD,RPMS,SOURCES,SPECS,SRPMS}

cp "$LINUX_GUI_BIN" rpm_build/SOURCES/cloudfuseGUI
cp cloudfuse.desktop rpm_build/SOURCES/
cp README.md rpm_build/SOURCES/
cp LICENSE rpm_build/SOURCES/

# Substitute version and ensure Requires: cloudfuse is present
sed "s/@@VERSION@@/${VERSION}/g" packaging/rpm/cloudfuse-gui.spec > rpm_build/SPECS/cloudfuse-gui.spec

rpmbuild -bb --define "_topdir $(pwd)/rpm_build" --define "dist .$(lsb_release -cs)" rpm_build/SPECS/cloudfuse-gui.spec
find rpm_build/RPMS -name '*.rpm' -exec mv {} "$RPM_OUT" \;

echo "$DEB_OUT"
echo "$RPM_OUT"