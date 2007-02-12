Summary:	Clink estimates the latency and bandwidth of network links
Summary(pl.UTF-8):	Clink określa przybliżone opóźnienie i pasmo połączenia sieciowego
Name:		clink
Version:	1.0
Release:	5
License:	GPL
Group:		Applications/Networking
Source0:	http://allendowney.com/research/clink/%{name}.%{version}.tar.gz
# Source0-md5:	9bfb957d7733e434a5e902dccad89c56
Patch0:		ftp://ftp.6bone.pl/pub/ipv6/set-glibc-2.1.new/%{name}.1.0a.diff
URL:		http://allendowney.com/research/clink/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
clink (Characterize Links) is a utility that estimates the latency and
bandwidth of network links by sending UDP packets from a single source
and measuring round-trip times. The basic mechanism is similar to ping
and traceroute, except that clink generally has to send many more
packets.

%description -l pl.UTF-8
clink (Characterize Links) jest narzędziem, które określa opóźnienie i
pasmo (przepustowość) łącz w sieci przy użyciu pakietów UDP wysyłanych
z pojedynczego źródła.

%prep
%setup -q -n %{name}.%{version}
%patch0 -p1
%build

%{__make} CFLAGS="%{rpmcflags} -D_GNU_SOURCE"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install clink $RPM_BUILD_ROOT%{_bindir}/clink

mv -f clink.doc clink.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc clink.txt
%attr(755,root,root) %{_bindir}/clink
