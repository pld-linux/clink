Summary:	Clink estimates the latency and bandwidth of network links
Summary(pl):	Clink okre¶la przybli¿one opó¼nienie i pasmo po³aczenia sieciowego
Name:		clink
Version:	1.0
Release:	1
License:	GPL
Group:		Applications/Networking
Group(de):	Applikationen/Netzwerkwesen
Group(pl):	Aplikacje/Sieciowe
Source0:	http://rocky.wellesley.edu/downey/clink/%{name}.%{version}.tar.gz
URL:		http://rocky.wellesley.edu/downey/clink/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description 
clink (Characterize Links) is a utility that estimates the latency and
bandwidth of network links by sending UDP packets from a single source
and measuring round-trip times. The basic mechanism is similar to ping
and traceroute, except that clink generally has to send many more
packets.

%description -l pl
clink (Characterize Links) jest narzêdziem, które okre¶la opó¼nienie i
pasmo (przepustowo¶æ) ³±cz w sieci przy u¿yciu pakietów UDP wysy³anych
z pojedynczego ¼ród³a.

%prep
%setup -q -n %{name}.%{version}
%build

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install clink $RPM_BUILD_ROOT%{_bindir}/clink

mv -f clink.doc clink.txt

gzip -9nf clink.txt
	
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/clink
