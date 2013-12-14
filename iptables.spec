Summary:	IPv4 packet filtering CLI programs
Name:		iptables
Version:	1.4.21
Release:	1
License:	GPL v2
Group:		Applications/Networking
Source0:	http://www.netfilter.org/projects/iptables/files/%{name}-%{version}.tar.bz2
# Source0-md5:	536d048c8e8eeebcd9757d0863ebb0c0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
iptables is the userspace command line program used
to configure the Linux 2.4.x and 2.6.x IPv4 packet
filtering ruleset.
It is targeted towards system administrators.
Since Network Address Translation is also configured
from the packet filter ruleset, iptables is used for
this, too.

%package ipv6
Summary:	IPv6 packet filtering CLI programs
Group:		Applications/Networking
Requires:	%{name}-libs = %{version}-%{release}

%description ipv6
The iptables package includes ip6tables. ip6tables is
used for configuring the IPv6 packet filter.

%package libs
Summary:	iptables libraries
Group:		Libraries

%description libs
iptables libraries

%package devel
Summary:	Header files for iptables libraries
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This is the package containing the header files for iptables
libraries.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-static	\
	--enable-devel
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /usr/sbin/ldconfig
%postun	libs -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%dir %{_libdir}/xtables
%attr(755,root,root) %{_bindir}/iptables-xml
%attr(755,root,root) %{_libdir}/xtables/libipt_*.so
%attr(755,root,root) %{_libdir}/xtables/libxt_*.so
%attr(755,root,root) %{_sbindir}/iptables*
%attr(755,root,root) %{_sbindir}/xtables-multi
%{_mandir}/man1/iptables*.1*
%{_mandir}/man8/iptables*.8*

%files ipv6
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/ip6tables*
%attr(755,root,root) %{_libdir}/xtables/libip6t_*.so
%{_mandir}/man8/ip6tables*.8*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?
%attr(755,root,root) %ghost %{_libdir}/lib*.so.??
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/libiptc
%{_includedir}/*.h
%{_pkgconfigdir}/*.pc

