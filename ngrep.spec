Summary:	Network Traffic sniffer, with pattern matching like grep
Name:		ngrep
Version:	1.45
Release:	%mkrel 6
License:	BSD
Group:		Networking/Other
URL:		http://ngrep.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/ngrep/%{name}-%{version}.tar.bz2
Patch0:		%{name}-1.43-no-locincpth.diff
BuildRequires:	pcap-devel
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
autoreconf -fis

%configure2_5x \
    --enable-ipv6 \
    --with-pcap-includes=%{_includedir}/pcap

%make

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man8

install -m0755 %{name} %{buildroot}%{_bindir}/%{name}
install -m0644 %{name}.8 -D %{buildroot}%{_mandir}/man8/%{name}.8

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc doc/*
%{_bindir}/%{name}
%{_mandir}/man8/*


%changelog
* Mon Sep 14 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.45-6mdv2010.0
+ Revision: 440330
- rebuild

* Thu Oct 30 2008 Oden Eriksson <oeriksson@mandriva.com> 1.45-5mdv2009.1
+ Revision: 298739
- bump release
- bunzip the patch

* Wed Oct 29 2008 Oden Eriksson <oeriksson@mandriva.com> 1.45-4mdv2009.1
+ Revision: 298624
- fix build
- rebuilt against libpcap-1.0.0

* Tue Jul 29 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.45-3mdv2009.0
+ Revision: 253951
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.45-1mdv2008.1
+ Revision: 136631
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Mon May 21 2007 Antoine Ginies <aginies@mandriva.com> 1.45-1mdv2008.0
+ Revision: 29491
- release 1.45
- Import ngrep



* Tue Sep 12 2006 Oden Eriksson <oeriksson@mandriva.com> 1.44-3mdv2007.0
- rebuild

* Wed Jul 13 2005 Oden Eriksson <oeriksson@mandriva.com> 1.44-2mdk
- rebuilt against new libpcap-0.9.1 (aka. a "play safe" rebuild)

* Tue Jul 05 2005 Oden Eriksson <oeriksson@mandriva.com> 1.44-1mdk
- 1.44
- drop P1, it won't apply anymore

* Thu Jun 16 2005 Oden Eriksson <oeriksson@mandriva.com> 1.43-2mdk
- fix changelog mismatch

* Thu Jun 16 2005 Oden Eriksson <oeriksson@mandriva.com> 1.43-1mdk
- 1.43
- rediff P0 & P1, drop P2
- fix deps

* Fri Jun 03 2005 Oden Eriksson <oeriksson@mandriva.com> 1.41-3mdk
- rebuild

* Tue Mar 02 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.41-2mdk
- fix build with new libpcap (P2)
- use %%make macro
- compile regex with $RPM_OPT_FLAGS

* Sun Jan 04 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.41-1mdk
- 1.41
- drop explicit library dependency
- fix buildrequires (lib64..)
- fix compile (P1)
- cosmetics

* Thu Jan 16 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 1.40.1-3mdk
- build release

* Sun Aug  4 2002 Oden Eriksson <oden.eriksson@kvikkjokk.net> 1.40.1-2mdk
- rebuilt with gcc-3.2

* Sun Jun  9 2002 Oden Eriksson <oden.eriksson@kvikkjokk.net> 1.40.1-1mdk
- initial cooker contrib
- added P0
