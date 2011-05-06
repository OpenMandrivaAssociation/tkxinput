Summary:	A Tk extension to handle additional input devices in X11
Name:		tkxinput
Version:	1.0
Release:	%mkrel 16
Source0:	%{name}-%{version}.tar.bz2
Patch0:		tkxinput-1.0.tk8.3.patch
Patch1:		tkxinput-1.0.wacom.patch
License:	LGPLv2+
Group:		System/X11
URL:		http://freshmeat.net/redir/tkxinput/22191/url_homepage/tkxinput/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libx11-devel
BuildRequires:	libxi-devel
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
rm -rf %{buildroot}
mkdir -p %{buildroot}%{tcl_sitearch}/TkXInput %{buildroot}%{_bindir}
make install prefix=%{buildroot}%{_prefix}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README*
%{tcl_sitearch}/TkXInput
%{_bindir}/*
