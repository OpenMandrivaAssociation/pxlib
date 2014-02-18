%define major 0
%define libname %mklibname px %major
%define develname %mklibname -d px

Summary: A library to read Paradox DB files
Name: pxlib
Version: 0.6.5
Release: 2
License: GPL
Group: System/Libraries
Url: http://pxlib.sourceforge.net/
Source: http://prdownloads.sourceforge.net/pxlib/%{name}-%{version}.tar.gz
BuildRoot: %_tmppath/%name-%version-root
BuildRequires:  docbook-to-man
BuildRequires:  docbook-utils
BuildRequires:  intltool
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libgsf-1)
BuildRequires:  pkgconfig(sqlite)

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
rm -rf %{buildroot}
%makeinstall_std
%find_lang %name

%clean
rm -rf %{buildroot}

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
%_libdir/pkgconfig/*
%_includedir/*
%_mandir/man3/*



%changelog
* Thu Jan 12 2012 GÃ¶tz Waschk <waschk@mandriva.org> 0.6.5-1mdv2012.0
+ Revision: 760263
- new version
- remove libtool archive

* Thu May 05 2011 Funda Wang <fwang@mandriva.org> 0.6.4-4
+ Revision: 669105
- fix br

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6.4-3mdv2011.0
+ Revision: 607255
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6.4-2mdv2010.1
+ Revision: 521161
- rebuilt for 2010.1

* Mon Jun 08 2009 GÃ¶tz Waschk <waschk@mandriva.org> 0.6.4-1mdv2010.0
+ Revision: 383975
- new version
- fix build

* Fri May 22 2009 GÃ¶tz Waschk <waschk@mandriva.org> 0.6.3-4mdv2010.0
+ Revision: 378699
- fix build deps
- add man pages

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.6.3-3mdv2009.1
+ Revision: 351586
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.6.3-2mdv2009.0
+ Revision: 225122
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed Oct 10 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.6.3-1mdv2008.1
+ Revision: 96661
- new version
- move translations to main package
- new devel name


* Sun Jan 28 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.6.1-1mdv2007.0
+ Revision: 114688
- Import pxlib

* Sun Jan 28 2007 Götz Waschk <waschk@mandriva.org> 0.6.1-1mdv2007.1
- rebuild

* Thu Mar 30 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.6.1-1mdk
- New release 0.6.1

* Tue Mar 07 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.6.0-2mdk
- rebuild with new libgsf

* Mon Feb 06 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.6.0-1mdk
- New release 0.6.0

* Fri Dec 09 2005 GÃ¶tz Waschk <waschk@mandriva.org> 0.5.1-3mdk
- rebuild for new libgsf
- use mkrel

* Wed Oct 12 2005 GÃ¶tz Waschk <waschk@mandriva.org> 0.5.1-2mdk
- rebuild for new libgsf

* Fri Aug 12 2005 GÃ¶tz Waschk <waschk@mandriva.org> 0.5.1-1mdk
- New release 0.5.1

* Fri Jul 15 2005 Götz Waschk <waschk@mandriva.org> 0.5.0-1mdk
- New release 0.5.0

* Thu May 26 2005 Götz Waschk <waschk@mandriva.org> 0.4.4-1mdk
- fix build on x86_64
- drop patches
- New release 0.4.4

* Wed Mar 09 2005 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 0.4.3-2mdk
- lib64 & 64-bit fixes

* Tue Jan 04 2005 Lenny Cartier <lenny@mandrakesoft.com> 0.4.3-1mdk
- 0.4.3

* Mon Nov 08 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.4.0-1mdk
- 0.4.0

* Wed Oct 13 2004 Götz Waschk <waschk@linux-mandrake.com> 0.3.1-1mdk
- fix source URL
- New release 0.3.1

* Mon Sep 20 2004 Götz Waschk <waschk@linux-mandrake.com> 0.3.0-2mdk
- fix buildrequires

* Wed Sep 01 2004 Götz Waschk <waschk@linux-mandrake.com> 0.3.0-1mdk
- initial mdk package

