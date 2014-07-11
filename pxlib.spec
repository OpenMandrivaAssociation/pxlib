%define major 0
%define libname %mklibname px %{major}
%define devname %mklibname -d px

Summary:	A library to read Paradox DB files
Name:		pxlib
Version:	0.6.5
Release:	7
License:	GPLv2
Group:		System/Libraries
Url:		http://pxlib.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/pxlib/%{name}-%{version}.tar.gz
BuildRequires:	docbook-to-man
BuildRequires:	docbook-utils
BuildRequires:	intltool
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libgsf-1)
BuildRequires:	pkgconfig(sqlite)

%description
pxlib is a simply and still small C library to read Paradox DB files. It
supports all versions starting from 3.0. It currently has a very limited set of
functions like to open a DB file, read its header and read every single record.

%package -n %{libname}
Group:		System/Libraries
Summary:	A library to read Paradox DB files
Requires:	%{name} >= %{version}

%description -n %{libname}
pxlib is a simply and still small C library to read Paradox DB files. It
supports all versions starting from 3.0. It currently has a very limited set of
functions like to open a DB file, read its header and read every single record.

%package -n %{devname}
Summary:	A library to read Paradox DB files (Development)
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	libpx-devel = %{version}-%{release}

%description -n %{devname}
pxlib is a simply and still small C library to read Paradox DB files. It
supports all versions starting from 3.0. It currently has a very limited set of
functions like to open a DB file, read its header and read every single record.

%prep
%setup -q

%build
export CPPFLAGS=`pkg-config --cflags glib-2.0`
%configure2_5x \
	--disable-static \
	--with-sqlite \
	--with-gsf

%make LIBS=-lm

%install
%makeinstall_std
%find_lang %{name}

%files -f %{name}.lang
%doc README AUTHORS ChangeLog

%files -n %{libname}
%{_libdir}/libpx.so.%{major}*

%files -n %{devname}
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_mandir}/man3/*

