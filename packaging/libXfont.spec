Name:           libXfont
Version:        1.4.5
Release:        0
License:        MIT
Summary:        X font handling library for server and utilities
Url:            http://xorg.freedesktop.org/
Group:          Development/Libraries/C and C++

#Git-Clone:	git://anongit.freedesktop.org/xorg/lib/libXfont
#Git-Web:	http://cgit.freedesktop.org/xorg/lib/libXfont/
Source:         %{name}-%{version}.tar.bz2
Source1001: 	libXfont.manifest
#git#BuildRequires:	autoconf >= 2.60, automake, libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fontenc)
BuildRequires:  pkgconfig(fontsproto)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(xorg-macros) >= 1.10
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xtrans)
BuildRequires:  pkgconfig(zlib)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
libXfont provides the core of the legacy X11 font system, handling
the index files (fonts.dir, fonts.alias, fonts.scale), the various
font file formats, and rasterizing them. It is used by the X servers,
the X Font Server (xfs), and some font utilities (bdftopcf for
instance), but should not be used by normal X11 clients. X11 clients
access fonts via either the new APIs in libXft, or the legacy APIs in
libX11.

%package devel
Summary:        Development files for the X font handling library
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
libXfont provides the core of the legacy X11 font system, handling
the index files (fonts.dir, fonts.alias, fonts.scale), the various
font file formats, and rasterizing them. It is used by the X servers,
the X Font Server (xfs), and some font utilities (bdftopcf for
instance), but should not be used by normal X11 clients. X11 clients
access fonts via either the new APIs in libXft, or the legacy APIs in
libX11.

This package contains the development headers for the library found
in %{name}.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%reconfigure --disable-static
make %{?_smp_mflags}

%install
%make_install

%post  -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%manifest %{name}.manifest
%license COPYING
%defattr(-,root,root)
%{_libdir}/libXfont.so.1*

%files devel
%manifest %{name}.manifest
%defattr(-,root,root)
%{_includedir}/X11/*
%{_libdir}/libXfont.so
%{_libdir}/pkgconfig/xfont.pc

%changelog
