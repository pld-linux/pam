Summary:	Pluggable Authentication Modules: modular, incremental authentication
Summary(de):	Einsteckbare Authentifizierungsmodule: modulare, inkrementäre Authentifizierung
Summary(fr):	PAM : Pluggable Authentication Modules: modular, incremental authentication
Summary(pl):	Modularny system autentykacji
Summary(tr):	Modüler, artýmsal doðrulama birimleri
Name:		pam
Version:	0.72.4
Release:	2
License:	GPL or BSD
Group:		Base
Group(de):	Gründsätzlich
Group(pl):	Podstawowe
Source0:	ftp://ftp.pld.org.pl/packages/%{name}-pld-%{version}.tar.gz
URL:		http://parc.power.net/morgan/Linux-PAM/index.html
BuildRequires:	sp
BuildRequires:	sgml-tools
BuildRequires:	pwdb-devel
BuildRequires:	cracklib-devel
BuildRequires:	skey-devel
BuildRequires:	opie-devel
BuildRequires:	libwrap-devel
BuildRequires:	libcap-devel
BuildRequires:	flex
BuildRequires:	bison
Requires:	cracklib
Requires:	cracklib-dicts
Requires:	make
Requires:	awk
Provides:	pam-pld
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	pamconfig
Obsoletes:	pam_make

%description
PAM (Pluggable Authentication Modules) is a powerful, flexible,
extensible authentication system which allows the system administrator
to configure authentication services individually for every
pam-compliant application without recompiling any of the applications.

%description -l de
PAM (Pluggable Authentication Modules) ist ein leistungsfähiges,
flexibles und erweiterbares Authentifizierungssystem, mit dem der
Systemverwalter Authentifizierungs-Dienste individuell für jede
pam-kompatible Anwendung konfigurieren kann, ohne diese neu
kompilieren zu müssen.

%description -l fr
PAM (Pluggable Authentication Modules) est un systéme
d'authentification puissant, souple et extensible permettant à
l'administrateur système de configurer les individuellement les
services d'authentification pour chaque application conforme à PAM,
sans recompiler aucune application.

%description -l pl
PAM (Pluggable Authentication Modules) jest silnym i ³atwo
dostosowywalnym do potrzeb systemem autentykacji, który umo¿liwia
administratorowi indywidualne konfigurowanie poszczególnych serwisów,
które s± dostosowane i zlinkowane z bibliotekami PAM bez pó¼niejszej
ich rekompilacji w momencie zmiany sposobu autentykacji tych¿e
serwisów.

%description -l tr
PAM (Pluggable Authentication Modules) sistem yöneticilerinin
uygulamalardan herhangi birini yeniden derlemeksizin bütün PAM uyumlu
uygulamalar için doðrulama hizmetlerini ayarlamalarýna yardýmcý olan,
güclü, esnek ve kapsamlý bir doðrulama sistemidir.

%package devel
Summary:	PAM header files
Summary(pl):	Pliki nag³ówkowe i dokumentacja do PAM
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files for developing PAM based applications.

%description devel
Header files for developing PAM based applications.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja do PAM.

%package static
Summary:	PAM static libraries
Summary(pl):	Biblioteki statyczne PAM
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
PAM static libraries.

%description static -l pl
Biblioteki statyczne PAM.

%package pam_pwdb
Summary:	pam_pwdb module
Group:		Base
Group(de):	Gründsätzlich
Group(pl):	Podstawowe
Requires:	%{name} = %{version}
Requires:	pwdb >= 0.54-2

%description pam_pwdb
pam_pwdb module.

%package pam_radius
Summary:	pam_radius module
Group:		Base
Group(de):	Gründsätzlich
Group(pl):	Podstawowe
Requires:	%{name} = %{version}
Requires:	pwdb >= 0.54-2

%description pam_radius
pam_radius module.

%package pam_skey
Summary:	pam_skey module
Group:		Base
Group(de):	Gründsätzlich
Group(pl):	Podstawowe
Requires:	%{name} = %{version}
Requires:	skey

%description pam_skey
pam_skey module.

%package pam_opie
Summary:	pam_opie module
Group:		Base
Group(de):	Gründsätzlich
Group(pl):	Podstawowe
Requires:	%{name} = %{version}
Requires:	opie

%description pam_opie
pam_opie module.

%package pam_tcpd
Summary:	pam_tcpd module
Group:		Base
Group(de):	Gründsätzlich
Group(pl):	Podstawowe
Requires:	%{name} = %{version}
Requires:	libwrap

%description pam_tcpd
pam_tcpd module.

%package pam_cap
Summary:	pam_cap module
Group:		Base
Group(de):	Gründsätzlich
Group(pl):	Podstawowe
Requires:	%{name} = %{version}
Requires:	libcap

%description pam_cap
pam_cap module.

%prep
%setup -q -n %{name}-pld-%{version}

%build
%configure \
	--enable-strong-crypto
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT/lib/lib*.{la,a,so} $RPM_BUILD_ROOT%{_libdir}/
ln -sf /lib/libpam.so.0.72.0 $RPM_BUILD_ROOT%{_libdir}/libpam.so
ln -sf /lib/libpam_misc.so.0.72.0 $RPM_BUILD_ROOT%{_libdir}/libpam_misc.so
ln -sf /lib/libpamc.so.0.72.0 $RPM_BUILD_ROOT%{_libdir}/libpamc.so

gzip -9nf Copyright doc/txts/*.txt doc/specs/*.{raw,txt}

rm -f doc/{ps,txts}/{README,*.log} \
	doc/{html,txts}/Makefile*

:> $RPM_BUILD_ROOT/etc/security/opasswd
:> $RPM_BUILD_ROOT/etc/security/blacklist

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright.gz doc/{html,txts,specs/*.gz}
%dir /etc/pam.d
%dir /sbin/pam_filter
%dir /var/lock/console
%dir /etc/security/console.apps
%config /etc/pam.d/other
%config /etc/security/access.conf
%config /etc/security/pam_env.conf
%config /etc/security/group.conf
%config /etc/security/limits.conf
%config /etc/security/time.conf
%config /etc/security/consoles
%config /etc/security/trigram*
%config(noreplace) /etc/security/blacklist
%attr(0600,root,root) %config(noreplace) /etc/security/opasswd
%attr(0755,root,root) /lib/lib*.so.*.*
%attr(0755,root,root) /lib/security/pam_access.so
%attr(0755,root,root) /lib/security/pam_console.so
%attr(0755,root,root) /lib/security/pam_cracklib.so
%attr(0755,root,root) /lib/security/pam_deny.so
%attr(0755,root,root) /lib/security/pam_env.so
%attr(0755,root,root) /lib/security/pam_filter.so
%attr(0755,root,root) /lib/security/pam_ftp.so
%attr(0755,root,root) /lib/security/pam_group.so
%attr(0755,root,root) /lib/security/pam_homedir.so
%attr(0755,root,root) /lib/security/pam_issue.so
%attr(0755,root,root) /lib/security/pam_lastlog.so
%attr(0755,root,root) /lib/security/pam_limits.so
%attr(0755,root,root) /lib/security/pam_listfile.so
%attr(0755,root,root) /lib/security/pam_mail.so
%attr(0755,root,root) /lib/security/pam_make.so
%attr(0755,root,root) /lib/security/pam_motd.so
%attr(0755,root,root) /lib/security/pam_netid.so
%attr(0755,root,root) /lib/security/pam_nologin.so
%attr(0755,root,root) /lib/security/pam_permit.so
%attr(0755,root,root) /lib/security/pam_pwgen.so
%attr(0755,root,root) /lib/security/pam_rhosts.so
%attr(0755,root,root) /lib/security/pam_rootok.so
%attr(0755,root,root) /lib/security/pam_securetty.so
%attr(0755,root,root) /lib/security/pam_shells.so
%attr(0755,root,root) /lib/security/pam_stress.so
%attr(0755,root,root) /lib/security/pam_tally.so
%attr(0755,root,root) /lib/security/pam_time.so
%attr(0755,root,root) /lib/security/pam_unix.so
%attr(0755,root,root) /lib/security/pam_userdb.so
%attr(0755,root,root) /lib/security/pam_usertty.so
%attr(0755,root,root) /lib/security/pam_utmp.so
%attr(0755,root,root) /lib/security/pam_warn.so
%attr(0755,root,root) /lib/security/pam_wheel.so
%attr(0755,root,root) /lib/security/pam_xauth.so
%attr(0755,root,root) /sbin/pam_filter/upperLOWER
%attr(4755,root,root) /sbin/unix_chkpwd
# Removed due to chicken-egg problem
# %attr(755,root,root) /sbin/pam_tally
%attr(755,root,root) %{_sbindir}/pwgen_trigram
%{_mandir}/man5/*
%{_mandir}/man8/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/security
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files pam_pwdb
%defattr(644,root,root,755)
%attr(0755,root,root) /lib/security/pam_pwdb.so
%attr(4755,root,root) /sbin/pwdb_chkpwd

%files pam_radius
%defattr(644,root,root,755)
%attr(755,root,root) /lib/security/pam_radius.so

%files pam_skey
%defattr(644,root,root,755)
%attr(755,root,root) /lib/security/pam_skey.so

%files pam_opie
%defattr(644,root,root,755)
%attr(755,root,root) /lib/security/pam_opie.so
%attr(755,root,root) /lib/security/pam_opietrust.so

%files pam_tcpd
%defattr(644,root,root,755)
%attr(755,root,root) /lib/security/pam_tcpd.so

%files pam_cap
%defattr(644,root,root,755)
%config /etc/security/capability.conf
%attr(755,root,root) /lib/security/pam_cap.so
