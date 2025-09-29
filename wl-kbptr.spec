Name:           wl-kbptr
Version:        0.4.0
Release:        %autorelease
Summary:        Control the mouse pointer with the keyboard on Wayland

License:        GPL-3.0
URL:            https://github.com/moverest/wl-kbptr
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  wayland-protocols-devel
BuildRequires:  gcc
BuildRequires:  libwayland-client
BuildRequires:  cmake
BuildRequires:  wayland-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  cairo-devel

Requires:       libxkbcommon
Requires:       cairo

%description
wl-kbptr - short for Wayland Keyboard Pointer - is a utility to help move the mouse pointer with the keyboard.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop

%changelog
%autochangelog
