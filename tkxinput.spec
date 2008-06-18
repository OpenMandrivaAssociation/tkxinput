%define	name	tkxinput
%define	version	1.0

Summary:	A Tk extension to handle additional input devices in X11
Name:		%{name}
Version:	%{version}
Release:	%mkrel 12
Source0:	%{name}-%{version}.tar.bz2
Patch0:		tkxinput-1.0.tk8.3.patch
Patch1:		tkxinput-1.0.wacom.patch
License:	GPL
Group:		System/X11
Url:		http://freshmeat.net/redir/tkxinput/22191/url_homepage/tkxinput/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libx11-devel libxi-devel tk tk-devel tcl tcl-devel

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

%build
%make CFLAGS="$RPM_OPT_FLAGS -fPIC" TCL_LIB=tcl8.5 TK_LIB=tk8.5 X11_LIB_PATH=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_prefix}/lib/TkXInput $RPM_BUILD_ROOT%{_bindir}
make install prefix=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README*
%{_prefix}/lib/TkXInput
%{_bindir}/*
