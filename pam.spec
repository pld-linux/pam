#
# Conditional build:
# _with_pwexport		- enable pam_pwexport module (needs hacked pam_unix)
Summary:	Pluggable Authentication Modules: modular, incremental authentication
Summary(de):	Einsteckbare Authentifizierungsmodule: modulare, inkrementäre Authentifizierung
Summary(es):	Módulos de autentificación plugables (PAM)
Summary(fr):	PAM : Pluggable Authentication Modules: modular, incremental authentication
Summary(pl):	Modularny system autentykacji
Summary(pt_BR):	Módulos de autenticação plugáveis (PAM)
Summary(ru):	éÎÔÓÔÒÕÍÅÎÔ, ÏÂÅÓÐÅÞÉ×ÁÀÝÉÊ ÁÕÔÅÎÔÉÆÉËÁÃÉÀ ÄÌÑ ÐÒÉÌÏÖÅÎÉÊ
Summary(tr):	Modüler, artýmsal doðrulama birimleri
Summary(uk):	¶ÎÓÔÒÕÍÅÎÔ, ÝÏ ÚÁÂÅÚÐÅÞÕ¤ ÁÕÔÅÎÔÉÆ¦ËÁÃ¦À ÄÌÑ ÐÒÏÇÒÁÍ
Name:		pam
Version:	0.77.0
Release:	1
License:	GPL/BSD
Group:		Base
Source0:	ftp://ftp.pld.org.pl/packages/%{name}-pld-%{version}.tar.gz
URL:		http://parc.power.net/morgan/Linux-PAM/index.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	cracklib-devel
BuildRequires:	db3-devel
BuildRequires:	flex
BuildRequires:	libcap-devel
BuildRequires:	libtool
BuildRequires:	libwrap-devel
BuildRequires:	opie-devel
BuildRequires:	pwdb-devel
BuildRequires:	skey-devel
BuildRequires:	sgml-tools
BuildRequires:	sp
Requires:	awk
Requires:	cracklib
Requires:	cracklib-dicts
Requires:	make
Provides:	pam-pld
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	pamconfig
Obsoletes:	pam_make
Obsoletes:	pam-doc

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

%description -l es
PAM (Módulos de Autenticación Plugables) es un potente, flexible y
extensible sistema de autentificación, que permite al administrador
del sistema configurar servicios de autentificación individualmente
para cada aplicación pam compatible, sin la necesidad de recompilar
cualquier una de las aplicaciones.

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
które s± dostosowane i zlinkowane z bibliotekami PAM, bez pó¼niejszej
ich rekompilacji w momencie zmiany sposobu autentykacji tych¿e
serwisów.

%description -l pt_BR
PAM (Módulos de Autenticação Plugáveis) é um poderoso, flexível e
extensível sistema de autenticação, que permite o administrador do
sistema configurar serviços de autenticação individualmente para cada
aplicação pam compatível, sem necessidade de recompilar qualquer uma
das aplicações.

%description -l uk
PAM (Pluggable Authentication Modules) - ÃÅ ÐÏÔÕÖÎÁ, ÇÎÕÞËÁ, ÚÄÁÔÎÁ ÄÏ
ÒÏÚÛÉÒÅÎÎÑ ÓÉÓÔÅÍÁ ÁÕÔÅÎÔÉËÁÃ¦§, ÑËÁ ÄÏÚ×ÏÌÑ¤ ÓÉÓÔÅÍÎÏÍÕ
ÁÄÍ¦Î¦ÓÔÒÁÔÏÒÕ ÎÁÌÁÇÏÄÖÕ×ÁÔÉ ÓÅ×¦ÓÉ Á×ÔÏÒÉÚÁÃ¦§ ÄÏÓÔÕÐÕ (ÁÕÔÅÎÔÉËÁÃ¦§)
¦ÎÄÉ×¦ÄÕÁÌØÎÏ ÄÌÑ ËÏÖÎÏ§ pam-ÓÕÍ¦ÓÎÏ§ ÐÒÏÇÒÁÍÉ ÂÅÚ ÎÅÏÂÈ¦ÄÎÏÓÔ¦
ÐÅÒÅËÏÍÐ¦ÌÑÃ¦§ ÓÁÍÏ§ ÐÒÏÇÒÁÍÉ. ãÅ ÂÁÚÏ×ÉÊ ÍÅÈÁÎ¦ÚÍ ÁÕÔÅÎÔÉËÁÃ¦§ × KSI
Linux.

%description -l tr
PAM (Pluggable Authentication Modules) sistem yöneticilerinin
uygulamalardan herhangi birini yeniden derlemeksizin bütün PAM uyumlu
uygulamalar için doðrulama hizmetlerini ayarlamalarýna yardýmcý olan,
güclü, esnek ve kapsamlý bir doðrulama sistemidir.

%description -l ru
PAM (Pluggable Authentication Modules) - ÜÔÏ ÍÏÝÎÁÑ, ÇÉÂËÁÑ,
ÒÁÓÛÉÒÑÅÍÁÑ ÓÉÓÔÅÍÁ ÁÕÔÅÎÔÉËÁÃÉÉ, ÐÏÚ×ÏÌÑÀÝÁÑ ÓÉÓÔÅÍÎÏÍÕ
ÁÄÍÉÎÉÓÔÒÁÔÏÒÕ ËÏÎÆÉÇÕÒÉÒÏ×ÁÔØ ÓÅÒ×ÉÓÙ Á×ÔÏÒÉÚÁÃÉÉ ÄÏÓÔÕÐÁ
(ÁÕÔÅÎÔÉËÁÃÉÉ) ÉÎÄÉ×ÉÄÕÁÌØÎÏ ÄÌÑ ËÁÖÄÏÊ pam-ÓÏ×ÍÅÓÔÉÍÏÊ ÐÒÏÇÒÁÍÍÙ ÂÅÚ
ÎÅÏÂÈÏÄÉÍÏÓÔÉ ÐÅÒÅËÏÍÐÉÌÌÑÃÉÉ ÓÁÍÏÊ ÐÒÏÇÒÁÍÍÙ. üÔÏ ÂÁÚÏ×ÙÊ ÍÅÈÁÎÉÚÍ
ÁÕÔÅÎÔÉËÁÃÉÉ × KSI Linux.

%package devel
Summary:	PAM header files
Summary(pl):	Pliki nag³ówkowe i dokumentacja do PAM
Summary(pt_BR):	Bibliotecas e arquivos de inclusão para desenvolvimento com PAM
Summary(ru):	âÉÂÌÉÏÔÅËÉ ÒÁÚÒÁÂÏÔÞÉËÁ ÄÌÑ PAM
Summary(uk):	â¦ÂÌ¦ÏÔÅËÉ ÐÒÏÇÒÁÍ¦ÓÔÁ ÄÌÑ PAM
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for developing PAM based applications.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja do PAM.

%description devel -l pt_BR
Bibliotecas e arquivos de inclusão para desenvolvimento com PAM

%description devel -l ru
üÔÏÔ ÐÁËÅÔ ÓÏÄÅÒÖÉÔ ÈÅÄÅÒÙ É ÂÉÂÌÉÏÔÅËÉ ÒÁÚÒÁÂÏÔÞÉËÁ ÄÌÑ PAM.

%description devel -l uk
ãÅÊ ÐÁËÅÔ Í¦ÓÔÉÔØ ÈÅÄÅÒÉ ÔÁ Â¦ÂÌ¦ÏÔÅËÉ ÐÒÏÇÒÁÍ¦ÓÔÁ ÄÌÑ PAM.

%package static
Summary:	PAM static libraries
Summary(pl):	Biblioteki statyczne PAM
Summary(ru):	óÔÁÔÉÞÅÓËÉÅ ÂÉÂÌÉÏÔÅËÉ ÒÁÚÒÁÂÏÔÞÉËÁ ÄÌÑ PAM
Summary(uk):	óÔÁÔÉÞÎ¦ Â¦ÂÌ¦ÏÔÅËÉ ÐÒÏÇÒÁÍ¦ÓÔÁ ÄÌÑ PAM
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
PAM static libraries.

%description static -l pl
Biblioteki statyczne PAM.

%description static -l ru
üÔÏÔ ÐÁËÅÔ ÓÏÄÅÒÖÉÔ ÓÔÁÔÉÞÅÓËÉÅ ÂÉÂÌÉÏÔÅËÉ ÒÁÚÒÁÂÏÔÞÉËÁ ÄÌÑ PAM.

%description static -l uk
ãÅÊ ÐÁËÅÔ Í¦ÓÔÉÔØ ÓÔÁÔÉÞÎ¦ Â¦ÂÌ¦ÏÔÅËÉ ÐÒÏÇÒÁÍ¦ÓÔÁ ÄÌÑ PAM.

%package pam_pwdb
Summary:	pam_pwdb module
Summary(pl):	Modu³ pam_pwdb
Group:		Base
Requires:	%{name} = %{version}
Requires:	pwdb >= 0.54-2

%description pam_pwdb
pam_pwdb module.

%description pam_pwdb -l pl
Modu³ pam_pwdb.

%package pam_radius
Summary:	pam_radius module
Summary(pl):	Modu³ pam_radius
Group:		Base
Requires:	%{name} = %{version}
Requires:	pwdb >= 0.54-2

%description pam_radius
pam_radius module.

%description pam_radius -l pl
Modu³ pam_radius.

%package pam_skey
Summary:	pam_skey module
Summary(pl):	Modu³ pam_skey
Group:		Base
Requires:	%{name} = %{version}
Requires:	skey

%description pam_skey
pam_skey module.

%description pam_skey -l pl
Modu³ pam_skey.

%package pam_opie
Summary:	pam_opie module
Summary(pl):	Modu³ pam_opie
Group:		Base
Requires:	%{name} = %{version}
Requires:	opie

%description pam_opie
pam_opie module.

%description pam_opie -l pl
Modu³ pam_opie.

%package pam_tcpd
Summary:	pam_tcpd module
Summary(pl):	Modu³ pam_tcpd
Group:		Base
Requires:	%{name} = %{version}
Requires:	libwrap

%description pam_tcpd
pam_tcpd module.

%description pam_tcpd -l pl
Modu³ pam_tcpd.

%package pam_cap
Summary:	pam_cap module
Summary(pl):	Modu³ pam_cap
Group:		Base
Requires:	%{name} = %{version}
Requires:	libcap

%description pam_cap
pam_cap module.

%description pam_cap -l pl
Modu³ pam_cap.

%prep
%setup -q -n %{name}-pld-%{version}

%build
rm -rf missing
%configure \
	%{?_with_pwexport:--enable-want-pwexport-module} \
	--enable-strong-crypto

%{__make}

# avoid relinking libpam_misc to allow building w/o pam-devel installed
sed s/^relink_command.*// libpam_misc/libpam_misc.la > libpam_misc.la.tmp
mv -f libpam_misc.la.tmp libpam_misc/libpam_misc.la

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib

%{__make} install DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*.* $RPM_BUILD_ROOT/lib/
ln -sf /lib/libpam.so.0.77.0 $RPM_BUILD_ROOT%{_libdir}/libpam.so
ln -sf /lib/libpam_misc.so.0.77.0 $RPM_BUILD_ROOT%{_libdir}/libpam_misc.so
ln -sf /lib/libpamc.so.0.77.0 $RPM_BUILD_ROOT%{_libdir}/libpamc.so

rm -f doc/{ps,txts}/{README,*.log} \
	doc/{html,txts}/Makefile*

:> $RPM_BUILD_ROOT/etc/security/opasswd
:> $RPM_BUILD_ROOT/etc/security/blacklist

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc Copyright doc/{html,txts,specs/*.{raw,txt}}
%dir /etc/pam.d
%dir /sbin/pam_filter
%dir /var/lock/console
%dir /etc/security/console.apps
%config(noreplace) %verify(not md5 size mtime) /etc/pam.d/other
%config(noreplace) %verify(not md5 size mtime) /etc/security/access.conf
%config(noreplace) %verify(not md5 size mtime) /etc/security/pam_env.conf
%config(noreplace) %verify(not md5 size mtime) /etc/security/group.conf
%config(noreplace) %verify(not md5 size mtime) /etc/security/limits.conf
%config(noreplace) %verify(not md5 size mtime) /etc/security/time.conf
%config(noreplace) %verify(not md5 size mtime) /etc/security/consoles
%config(noreplace) %verify(not md5 size mtime) /etc/security/trigram*
%config(noreplace) %verify(not md5 size mtime) /etc/security/blacklist
%config(noreplace) %verify(not md5 size mtime) /etc/security/pam_mail.conf
%attr(0600,root,root) %config(noreplace) %verify(not md5 size mtime) /etc/security/opasswd
%attr(0755,root,root) /lib/lib*.so.*.*
%attr(0755,root,root) /lib/security/pam_access.so
%attr(0755,root,root) /lib/security/pam_console.so
%attr(0755,root,root) /lib/security/pam_cracklib.so
%attr(0755,root,root) /lib/security/pam_debug.so
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
%{?_with_pwexport:%attr(0755,root,root) /lib/security/pam_pwexport.so}
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
%attr(755,root,root) %{_libdir}/lib*.la
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
%config(noreplace) %verify(not md5 size mtime) /etc/security/capability.conf
%attr(755,root,root) /lib/security/pam_cap.so
