Name:           gnome-platform
Version:        0.1
Release:        1%{?dist}
Summary:        Gnome platform

License: Various
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch

Requires: gnome-platform-base
Requires: gtk3
Requires: hicolor-icon-theme
Requires: adwaita-icon-theme

%description
Meta package for Gnome SDK dependencies

%prep


%build


%install

%files
%doc

%changelog
* Fri Nov  7 2014 Alexander Larsson <alexl@redhat.com>
- Initial version

