Summary:	Clink estimates the latency and bandwidth of network links
Summary(pl):	Clink okre�la przybli�one op�nienie i pasmo po��czenia sieciowego
Name:		clink
Version:	1.0
Release:	3
License:	GPL
Group:		Applications/Networking
Source0:	http://rocky.wellesley.edu/research/clink/%{name}.%{version}.tar.gz
Patch0:		ftp://ftp.6bone.pl/pub/ipv6/set-glibc-2.1.new/%{name}.1.0a.diff
URL:		http://rocky.wellesley.edu/research/clink/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
clink (Characterize Links) is a utility that estimates the latency and
bandwidth of network links by sending UDP packets from a single source
and measuring round-trip times. The basic mechanism is similar to ping
and traceroute, except that clink generally has to send many more
packets.

%description -l pl
clink (Characterize Links) jest narz�dziem, kt�re okre�la op�nienie i
pasmo (przepustowo��) ��cz w sieci przy u�yciu pakiet�w UDP wysy�anych
z pojedynczego �r�d�a.

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
