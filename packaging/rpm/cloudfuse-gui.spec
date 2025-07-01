Name:           cloudfuse-gui
Version:        @@VERSION@@
Release:        1%{?dist}
Summary:        Cloudfuse GUI

License:        MIT
Packager:       Seagate Technology <cloudfuse@seagate.com>
URL:            https://github.com/Seagate/cloudfuse-gui
Source0:        cloudfuse-gui.tar.gz
Source1:        cloudfuse.desktop
Source2:        README.md
Source3:        LICENSE

Requires:       cloudfuse

%description
An easy to use graphical interface for cloudfuse.

%prep
%setup -q

%install
install -d %{buildroot}%{_libdir}/%{name}
cp -r ./* %{buildroot}%{_libdir}/%{name}/

# Strip binaries and shared objects
find %{buildroot}%{_libdir}/%{name} -type f \( -name "*.so*" -o -executable \) -exec strip --strip-unneeded {} +

install -d %{buildroot}%{_bindir}
ln -s ../lib/%{name}/cloudfuseGUI %{buildroot}%{_bindir}/%{name}

install -d -m 755 %{buildroot}%{_datadir}/applications
install -m 644 %{SOURCE1} %{buildroot}/usr/share/applications/cloudfuse-gui.desktop

install -d %{buildroot}%{_defaultdocdir}/%{name}
install -m 644 %{SOURCE2} %{buildroot}%{_defaultdocdir}/%{name}/README.md
install -m 644 %{SOURCE3} %{buildroot}%{_defaultdocdir}/%{name}/LICENSE

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%{_libdir}/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%doc %{_defaultdocdir}/%{name}
