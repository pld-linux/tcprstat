# TODO
# - fix bashism in configure.ac, and add --disable-static option
# - fix non-x86_64 build:
#   stats-hash.c:297:2: error: #error Cannot determine sizeof(unsigned long)
Summary:	Passive TCP response time analysis tool — Read more
Name:		tcprstat
Version:	0.3.1
Release:	1
License:	GPL v2 or v3
Group:		Applications/Networking
Source0:	https://github.com/downloads/Lowercases/tcprstat/%{name}-%{version}.tar.gz
# Source0-md5:	392ffc7a4bd676567728aee0b479c552
URL:		http://www.percona.com/docs/wiki/tcprstat:start
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libpcap-devel >= 1.0.0
BuildRequires:	libtool
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
tcprtime is a protocol-agnostic libpcap-based tool for measuring TCP
requests' response time in a server

%prep
%setup -q

# the libpcap detect is broken (wants static pcap)
%{__sed} -i -e 's/buildpcap == xyes/buildpcap = xno/' configure.ac

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--bindir=%{_sbindir}
%{__make} -C src \
	bin_PROGRAMS=tcprstat

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	bin_PROGRAMS=tcprstat \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_sbindir}/tcprstat
