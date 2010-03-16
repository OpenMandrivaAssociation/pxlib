%define major 0
%define libname %mklibname px %major
%define develname %mklibname -d px

Summary: A library to read Paradox DB files
Name: pxlib
Version: 0.6.4
Release: %mkrel 2
License: GPL
Group: System/Libraries
Url: http://pxlib.sourceforge.net/
Source: http://prdownloads.sourceforge.net/pxlib/%{name}-%{version}.tar.gz
BuildRoot: %_tmppath/%name-%version-root
BuildRequires: autoconf2.5 >= 2.54
BuildRequires: sqlite-devel
BuildRequires: libgsf-devel
BuildRequires: intltool
BuildRequires: docbook-to-man docbook-utils
BuildRequires: libglib2.0-devel

%description
pxlib is a simply and still small C library to read Paradox DB files. It
supports all versions starting from 3.0. It currently has a very limited set of
functions like to open a DB file, read its header and read every single record.

%package -n %libname
Group: System/Libraries
Summary: A library to read Paradox DB files
Requires: %name >= %version

%description -n %libname
pxlib is a simply and still small C library to read Paradox DB files. It
supports all versions starting from 3.0. It currently has a very limited set of
functions like to open a DB file, read its header and read every single record.

%package -n %develname
Summary: A library to read Paradox DB files (Development)
Group: Development/C
Requires: %libname = %{version}
Provides: libpx-devel = %{version}-%release
Obsoletes: %mklibname -d px 0

%description -n %develname
pxlib is a simply and still small C library to read Paradox DB files. It
supports all versions starting from 3.0. It currently has a very limited set of
functions like to open a DB file, read its header and read every single record.

%prep
%setup -q

%build
export CPPFLAGS=`pkg-config --cflags glib-2.0`
%configure2_5x  --with-sqlite --with-gsf
%make LIBS=-lm

%install
rm -rf ${RPM_BUILD_ROOT}
%makeinstall_std
%find_lang %name

%clean
rm -rf ${RPM_BUILD_ROOT}

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig
%endif

%files -f %name.lang
%defattr(-,root,root)
%doc README AUTHORS ChangeLog

%files -n %libname
%defattr(-,root,root)
%_libdir/libpx.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%_libdir/lib*.so
%_libdir/*.a
%attr(644,root,root) %_libdir/*.la
%_libdir/pkgconfig/*
%_includedir/*
%_mandir/man3/*

