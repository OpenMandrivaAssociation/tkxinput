%define _enable_debug_packages	%{nil}
%define debug_package		%{nil}

Summary:	A Tk extension to handle additional input devices in X11
Name:		tkxinput
Version:	1.0
Release:	19
Source0:	%{name}-%{version}.tar.bz2
Patch0:		tkxinput-1.0.tk8.3.patch
Patch1:		tkxinput-1.0.wacom.patch
License:	LGPLv2+
Group:		System/X11
URL:		http://freshmeat.net/redir/tkxinput/22191/url_homepage/tkxinput/
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xi)
BuildRequires:	tk-devel
BuildRequires:	tcl-devel

%description
The package provides an extension to Tk that add input device
management capabilities. It is possible to bind extended input
events to tcl scripts, to get information about the devices, to
change devices parameters and to change the default pointer and
keyborad devices. It is also possible to send input events from
one application to an other one.

%prep
%setup -q
%patch0 -p1 -b .tk8
%patch1 -p1 -b .wacom
# quick hack to fix install location...the makefile is way too simple
# to make a proper fix easy without completely re-doing it - AdamW
# 2008/12
sed -i -e 's,$(prefix)/lib,%{buildroot}%{tcl_sitearch},g' Makefile

%build
%make CFLAGS="%{optflags} -fPIC" TCL_LIB=tcl%{tcl_version} TK_LIB=tk%{tcl_version} X11_LIB_PATH=%{_libdir}

%install
mkdir -p %{buildroot}%{tcl_sitearch}/TkXInput %{buildroot}%{_bindir}
make install prefix=%{buildroot}%{_prefix}

%files
%doc README*
%{tcl_sitearch}/TkXInput
%{_bindir}/*


%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0-16mdv2011.0
+ Revision: 670711
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-15mdv2011.0
+ Revision: 608028
- rebuild

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-14mdv2010.1
+ Revision: 520288
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0-13mdv2010.0
+ Revision: 427393
- rebuild

* Sat Dec 06 2008 Adam Williamson <awilliamson@mandriva.org> 1.0-12mdv2009.1
+ Revision: 311005
- use the macros, Luke!
- rebuild for new tcl
- install to new location per policy
- correct license, new license policy
- spec clean

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.0-12mdv2009.0
+ Revision: 225774
- rebuild

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0-11mdv2008.1
+ Revision: 179655
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Sep 07 2007 Anssi Hannula <anssi@mandriva.org> 1.0-10mdv2008.0
+ Revision: 82051
- rebuild for new soname of tcl

* Fri Jun 15 2007 Adam Williamson <awilliamson@mandriva.org> 1.0-9mdv2008.0
+ Revision: 40202
- refine and update buildrequires; rebuild for new era
- Import tkxinput



* Wed Jan 04 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0-8mdk
- rebuilt against soname aware deps (tcl/tk)
- fix deps

* Tue May 03 2005 Per Ã˜yvind Karlsen <pkarlsen@mandriva.com> 1.0-7mdk
- compile with -fPIC (fixes build on x86_64)
- lib64 path fix
- fix non-standard-group

* Fri May 21 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.0-6mdk
- fix buildrequires
- added url
- cleanups

* Fri May  2 2003 Frederic Lepied <flepied@mandrakesoft.com> 1.0-5mdk
- rebuilt for new rpm

* Sat Jan 22 2002 Stefan van der Eijk <stefan@eijk.nu> 1.0-4mdk
- BuildRequires
- Copyright --> License

* Sun Jun 17 2001 Stefan van der Eijk <stefan@eijk.nu> 1.0-3mdk
- BuildRequires: XFree86-devel

* Fri Apr 13 2001 Frederic Lepied <flepied@mandrakesoft.com> 1.0-2mdk
- activated wacom support

* Tue Mar  6 2001 Frederic Lepied <flepied@mandrakesoft.com> 1.0-1mdk
- first version

# tkxinput.spec ends here
