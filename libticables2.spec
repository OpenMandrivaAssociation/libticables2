%define major 5
%define libname %mklibname ticables2 %{major}
%define develname %mklibname ticables2 -d

Name: libticables2
Version: 1.3.3
Release: 1
Url: http://sourceforge.net/projects/tilp
Source0: http://downloads.sourceforge.net/project/tilp/tilp2-linux/tilp2-1.16/%{name}-%{version}.tar.bz2
Group: System/Libraries
License: GPLv2+
BuildRequires: libusb1-devel, pkgconfig(glib-2.0)
BuildRequires: autoconf automake libtool gettext-devel pkgconfig(libusb)
Requires: udev >= 154
Summary: Library for handling TI link cables
%description
Library for handling TI link cables

%package  -n %develname
Summary: Development files for %{name}
Group: Development/C
Requires: %libname = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release} 

%description -n %develname
This package contains the files necessary to develop applications using the
%{name} library.

%package  -n %libname
Summary: Development files for %{name}
Group: System/Libraries

%description -n %libname
This package contains the files necessary to develop applications using the
%{name} library.

%prep
%setup -q
autoreconf -i -f

%build
%configure2_5x --enable-libusb10
%make

%install
%makeinstall_std
rm -f %buildroot%{_libdir}/libticables2.la


mkdir -p %buildroot/lib/udev/rules.d
cat >%buildroot/lib/udev/rules.d/69-libticables.rules <<EOF
# This file was installed by the libticables2 Fedora package.

ACTION!="add", GOTO="libticables_end"

# serial device (assume TI calculator)
KERNEL=="ttyS[0-3]", TAG+="udev-acl"
# parallel device (assume TI calculator)
SUBSYSTEM=="ppdev", TAG+="udev-acl"
# SilverLink
SUBSYSTEM=="usb", ATTR{idVendor}=="0451", ATTR{idProduct}=="e001", TAG+="udev-acl"
# TI-84+ DirectLink
SUBSYSTEM=="usb", ATTR{idVendor}=="0451", ATTR{idProduct}=="e003", TAG+="udev-acl"
# TI-89 Titanium DirectLink
SUBSYSTEM=="usb", ATTR{idVendor}=="0451", ATTR{idProduct}=="e004", TAG+="udev-acl"
# TI-84+ SE DirectLink
SUBSYSTEM=="usb", ATTR{idVendor}=="0451", ATTR{idProduct}=="e008", TAG+="udev-acl"
# TI-Nspire DirectLink
SUBSYSTEM=="usb", ATTR{idVendor}=="0451", ATTR{idProduct}=="e012", TAG+="udev-acl"

LABEL="libticables_end"
EOF



%files -n %libname
%{_libdir}/libticables2.so.%{major}*
/lib/udev/rules.d/69-libticables.rules

%files -n %develname
%{_includedir}/tilp2
%{_libdir}/libticables2.so
%{_libdir}/pkgconfig/ticables2.pc
%{_datadir}/locale/fr/LC_MESSAGES/%{name}.mo


%changelog
* Mon Feb 20 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.3.3-1
+ Revision: 778066
- setup is quiet

* Mon Feb 20 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.3.3-1
+ Revision: 778061
- %libname description fix
- major version fix \n
- imported package libticables2

