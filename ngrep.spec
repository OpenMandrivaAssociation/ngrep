Summary:	Network Traffic sniffer, with pattern matching like grep
Name:		ngrep
Version:	1.45
Release:	%mkrel 4
License:	BSD
Group:		Networking/Other
URL:		http://ngrep.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/ngrep/%{name}-%{version}.tar.bz2
Patch0:		%{name}-1.43-no-locincpth.diff.bz2
BuildRequires:	libpcap-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
ngrep strives to provide most of GNU grep's common features,
applying them to the network layer.  ngrep is a pcap-aware tool
that will allow you to specify extended regular or hexadecimal
expressions to match against data payloads of packets. It
currently recognizes TCP, UDP and ICMP across Ethernet, PPP, SLIP,
FDDI, Token Ring and null interfaces, and understands bpf filter
logic in the same fashion as more common packet sniffing tools,
such as tcpdump and snoop.

%prep

%setup -q
%patch0 -p0

find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

%build
autoconf

%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man8

install -m0755 %{name} %{buildroot}%{_bindir}/%{name}
install -m0644 %{name}.8 -D %{buildroot}%{_mandir}/man8/%{name}.8

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc doc/*
%{_bindir}/%{name}
%{_mandir}/man8/*
