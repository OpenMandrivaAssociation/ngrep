Summary:	Network Traffic sniffer, with pattern matching like grep
Name:		ngrep
Version:	1.45
Release:	7
License:	BSD
Group:		Networking/Other
Url:		http://ngrep.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/ngrep/%{name}-%{version}.tar.bz2
Patch0:		%{name}-1.43-no-locincpth.diff
Patch1:		ngrep-1.45-no-strip.patch
BuildRequires:	pcap-devel

%description
ngrep strives to provide most of GNU grep's common features,
applying them to the network layer.  ngrep is a pcap-aware tool
that will allow you to specify extended regular or hexadecimal
expressions to match against data payloads of packets. It
currently recognizes TCP, UDP and ICMP across Ethernet, PPP, SLIP,
FDDI, Token Ring and null interfaces, and understands bpf filter
logic in the same fashion as more common packet sniffing tools,
such as tcpdump and snoop.

%files
%doc doc/*
%{_bindir}/%{name}
%{_mandir}/man8/*

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p0
%patch1 -p1

find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

find . -name "Makefile*" -o -name "*.m4" -o -name "configure*" |xargs sed -i -e 's,configure.in,configure.ac,g'

%build
autoreconf -fis

%configure2_5x \
	--enable-ipv6 \
	--with-pcap-includes=%{_includedir}/pcap

%make

%install
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man8

install -m0755 %{name} %{buildroot}%{_bindir}/%{name}
install -m0644 %{name}.8 -D %{buildroot}%{_mandir}/man8/%{name}.8

