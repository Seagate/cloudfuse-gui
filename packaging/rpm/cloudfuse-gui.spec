Name:           cloudfuse-gui
Version:        @@VERSION@@
Release:        1%{?dist}
Summary:        Cloudfuse GUI

License:        MIT
Packager:       Seagate Technology <cloudfuse@seagate.com>
URL:            <https://github.com/Seagate/cloudfuse-gui>
Source0:        cloudfuseGUI
Source1:        cloudfuse.desktop
Source2:        README.md
Source3:        LICENSE
Group:          Applications/System

Requires:       cloudfuse

%description
An easy to use gr cloudfuse.

%install
mkdir -p %{buildroot}/usr/bin
install -m 755 %{SOURCE0} %{buildroot}/usr/bin/cloudfuseGUI

mkdir -p %{buildroot}/usr/share/applications
install -m 644 %{SOURCE1} %{buildroot}/usr/share/applications/cloudfuse-gui.desktop

# Create a doc directory in the buildroot and install the doc files

install -d %{buildroot}%{_defaultdocdir}/%{name}
install -m 644 %{SOURCE2} %{buildroot}%{_defaultdocdir}/%{name}/README.md
install -m 644 %{SOURCE3} %{buildroot}%{_defaultdocdir}/%{name}/LICENSE

%files
/usr/bin/cloudfuseGUI
/usr/share/applications/cloudfuse-gui.desktop

# Mark the entire installed documentation directory as documentation

%doc %{_defaultdocdir}/%{name}
