%define libname %mklibname px 0

Summary: A library to read Paradox DB files
Name: pxlib
Version: 0.6.1
Release: %mkrel 1
License: GPL
Group: System/Libraries
Url: http://pxlib.sourceforge.net/
Source: http://prdownloads.sourceforge.net/pxlib/%{name}-%{version}.tar.bz2
BuildRoot: %_tmppath/%name-%version-root
BuildRequires: autoconf2.5 >= 2.54
BuildRequires: sqlite-devel
BuildRequires: libgsf-devel
BuildRequires: perl-XML-Parser
BuildRequires: libglib2.0-devel

%description
pxlib is a simply and still small C library to read Paradox DB files. It
supports all versions starting from 3.0. It currently has a very limited set of
functions like to open a DB file, read its header and read every single record.

%package -n %libname
Group: System/Libraries
Summary: A library to read Paradox DB files

%description -n %libname
pxlib is a simply and still small C library to read Paradox DB files. It
supports all versions starting from 3.0. It currently has a very limited set of
functions like to open a DB file, read its header and read every single record.

%package -n %libname-devel
Summary: A library to read Paradox DB files (Development)
Group: Development/C
Requires: %libname = %{version}
Provides: libpx-devel = %{version}-%release

%description -n %libname-devel
pxlib is a simply and still small C library to read Paradox DB files. It
supports all versions starting from 3.0. It currently has a very limited set of
functions like to open a DB file, read its header and read every single record.

%prep
%setup -q

%build
export CPPFLAGS=`pkg-config --cflags glib-2.0`
%configure2_5x  --with-sqlite --with-gsf
%make

%install
rm -rf ${RPM_BUILD_ROOT}
%makeinstall_std
%find_lang %name

%clean
rm -rf ${RPM_BUILD_ROOT}

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%files -n %libname -f %name.lang
%defattr(-,root,root)
%doc README AUTHORS ChangeLog
%_libdir/lib*.so.*

%files -n %libname-devel
%defattr(-,root,root)
%_libdir/lib*.so
%_libdir/*.a
%attr(644,root,root) %_libdir/*.la
%_libdir/pkgconfig/*
%_includedir/*


