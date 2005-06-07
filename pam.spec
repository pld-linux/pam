#
# Conditional build:
%bcond_with	pwexport	# enable pam_pwexport module (needs hacked pam_unix)
%bcond_without	cap		# don't build pam_cap module
%bcond_without	doc		# don't build documentation
%bcond_without	opie		# don't build pam_opie module
%bcond_without	pwdb		# don't build pam_pwdb and pam_radius modules
%bcond_without	selinux		# build without SELinux support
%bcond_without	skey		# don't build pam_skey module
%bcond_without	tcpd		# don't build pam_tcpd module
#
Summary:	Pluggable Authentication Modules: modular, incremental authentication
Summary(de):	Einsteckbare Authentifizierungsmodule: modulare, inkrementäre Authentifizierung
Summary(es):	Módulos de autentificación plugables (PAM)
Summary(fr):	PAM : Pluggable Authentication Modules: modular, incremental authentication
Summary(pl):	Modularny system uwierzytelniania
Summary(pt_BR):	Módulos de autenticação plugáveis (PAM)
Summary(ru):	éÎÔÓÔÒÕÍÅÎÔ, ÏÂÅÓÐÅÞÉ×ÁÀÝÉÊ ÁÕÔÅÎÔÉÆÉËÁÃÉÀ ÄÌÑ ÐÒÉÌÏÖÅÎÉÊ
Summary(tr):	Modüler, artýmsal doðrulama birimleri
Summary(uk):	¶ÎÓÔÒÕÍÅÎÔ, ÝÏ ÚÁÂÅÚÐÅÞÕ¤ ÁÕÔÅÎÔÉÆ¦ËÁÃ¦À ÄÌÑ ÐÒÏÇÒÁÍ
Name:		pam
Version:	0.79.1
Release:	2
Epoch:		0
License:	GPL or BSD
Group:		Base
Source0:	ftp://ftp.pld-linux.org/software/pam/%{name}-pld-%{version}.tar.gz
# Source0-md5:	fc029c41d960eeaf9736df3aeb2d41b2
Source1:	system-auth.pamd
Patch0:		%{name}-selinux-1.patch
Patch1:		%{name}-gcc4.patch
Patch2:		%{name}-fPIC.patch
URL:		http://www.kernel.org/pub/linux/libs/pam/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	cracklib-devel
BuildRequires:	db-devel
BuildRequires:	flex
%{?with_cap:BuildRequires:	libcap-devel}
%{?with_selinux:BuildRequires:	libselinux-devel}
BuildRequires:	libtool >= 2:1.5
%{?with_tcpd:BuildRequires:	libwrap-devel >= 7.6-32}
%{?with_opie:BuildRequires:	opie-devel}
%{?with_pwdb:BuildRequires:	pwdb-devel}
%{?with_skey:BuildRequires:	skey-devel}
%if %{with doc}
BuildRequires:	sgml-tools
BuildRequires:	sp
BuildRequires:	tetex-fonts-jknappen
BuildRequires:	tetex-format-latex
BuildRequires:	tetex-metafont
BuildRequires:	tetex-tex-babel
%else
BuildRequires:	sed >= 4.0
%endif
Requires:	awk
Requires:	cracklib
Requires:	cracklib-dicts
Requires:	make
Provides:	pam-pld
Obsoletes:	pamconfig
Obsoletes:	pam_make
Obsoletes:	pam-doc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
dostosowywalnym do potrzeb systemem uwierzytelniania, który umo¿liwia
administratorowi indywidualne konfigurowanie poszczególnych us³ug,
które s± dostosowane i skonsolidowane z bibliotekami PAM, bez
pó¼niejszej ich rekompilacji w momencie zmiany sposobu
uwierzytelniania tych¿e us³ug.

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
ÐÅÒÅËÏÍÐ¦ÌÑÃ¦§ ÓÁÍÏ§ ÐÒÏÇÒÁÍÉ. ãÅ ÂÁÚÏ×ÉÊ ÍÅÈÁÎ¦ÚÍ ÁÕÔÅÎÔÉËÁÃ¦§ × PLD
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
ÁÕÔÅÎÔÉËÁÃÉÉ × PLD Linux.

%package devel
Summary:	PAM header files
Summary(pl):	Pliki nag³ówkowe i dokumentacja programisty do PAM
Summary(pt_BR):	Bibliotecas e arquivos de inclusão para desenvolvimento com PAM
Summary(ru):	âÉÂÌÉÏÔÅËÉ ÒÁÚÒÁÂÏÔÞÉËÁ ÄÌÑ PAM
Summary(uk):	â¦ÂÌ¦ÏÔÅËÉ ÐÒÏÇÒÁÍ¦ÓÔÁ ÄÌÑ PAM
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	FHS >= 2.2-9

%description devel
Header files for developing PAM based applications.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja programisty do PAM.

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
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

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
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	pwdb >= 0.54-2

%description pam_pwdb
pam_pwdb module.

%description pam_pwdb -l pl
Modu³ pam_pwdb.

%package pam_radius
Summary:	pam_radius module
Summary(pl):	Modu³ pam_radius
Group:		Base
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	pwdb >= 0.54-2

%description pam_radius
pam_radius module.

%description pam_radius -l pl
Modu³ pam_radius.

%package pam_skey
Summary:	pam_skey module
Summary(pl):	Modu³ pam_skey
Group:		Base
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	skey

%description pam_skey
pam_skey module.

%description pam_skey -l pl
Modu³ pam_skey.

%package pam_opie
Summary:	pam_opie module
Summary(pl):	Modu³ pam_opie
Group:		Base
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	opie

%description pam_opie
pam_opie module.

%description pam_opie -l pl
Modu³ pam_opie.

%package pam_tcpd
Summary:	pam_tcpd module
Summary(pl):	Modu³ pam_tcpd
Group:		Base
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	libwrap >= 7.6-32

%description pam_tcpd
pam_tcpd module.

%description pam_tcpd -l pl
Modu³ pam_tcpd.

%package pam_cap
Summary:	pam_cap module
Summary(pl):	Modu³ pam_cap
Group:		Base
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	libcap

%description pam_cap
pam_cap module.

%description pam_cap -l pl
Modu³ pam_cap.

%prep
%setup -q -n %{name}-pld-%{version}
%{?with_selinux:%patch0 -p1}
%patch1 -p1
#%patch2 -p1

%{!?with_doc:sed -i -e '/all-local:/d' doc/Makefile.am}

%build
find . -name Makefile.am | xargs %{__perl} -pi -e 's#modulesdir.*=.*\@prefix\@/lib#modulesdir = \@libdir\@#g'
find . -type f | xargs %{__perl} -pi -e 's#/lib/security#/%{_lib}/security#g'
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
CFLAGS="%{rpmcflags} -D_FILE_OFFSET_BITS=64"
%configure \
	%{!?with_cap:ac_cv_lib_cap_cap_init=no} \
	%{!?with_opie:ac_cv_lib_opie_opieverify=no} \
	%{!?with_pwdb:ac_cv_lib_pwdb_pwdb_posix_getlogin=no} \
	%{!?with_skey:ac_cv_lib_skey_skeyaccess=no} \
	%{!?with_tcpd:libwrap=no} \
	%{?with_pwexport:--enable-want-pwexport-module} \
	--enable-strong-crypto
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_lib}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f doc/{ps,txts}/{README,*.log} \
	doc/{html,txts}/Makefile*

:> $RPM_BUILD_ROOT/etc/security/opasswd
:> $RPM_BUILD_ROOT/etc/security/blacklist

mv -f $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*.* $RPM_BUILD_ROOT/%{_lib}

install pamcrypt/.libs/libpamcrypt.a $RPM_BUILD_ROOT%{_libdir}

cd $RPM_BUILD_ROOT/%{_lib}
ln -sf /%{_lib}/$(echo libpam.so.*.*.*) $RPM_BUILD_ROOT%{_libdir}/libpam.so
ln -sf /%{_lib}/$(echo libpam_misc.so.*.*.*) $RPM_BUILD_ROOT%{_libdir}/libpam_misc.so
ln -sf /%{_lib}/$(echo libpamc.so.*.*.*) $RPM_BUILD_ROOT%{_libdir}/libpamc.so

cp %{SOURCE1} $RPM_BUILD_ROOT/etc/pam.d/system-auth

# useless - shut up check-files
rm -f $RPM_BUILD_ROOT/%{_lib}/security/*.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGELOG ChangeLog Copyright doc/CREDITS %{?with_doc:doc/{html,txts,specs/*.{raw,txt}}}
%dir /etc/pam.d
%dir /sbin/pam_filter
%dir /var/lock/console
%dir /etc/security/console.apps
%config(noreplace) %verify(not md5 size mtime) /etc/pam.d/other
%config(noreplace) %verify(not md5 size mtime) /etc/pam.d/system-auth
%config(noreplace) %verify(not md5 size mtime) /etc/security/access.conf
%config(noreplace) %verify(not md5 size mtime) /etc/security/pam_env.conf
%config(noreplace) %verify(not md5 size mtime) /etc/security/group.conf
%config(noreplace) %verify(not md5 size mtime) /etc/security/limits.conf
%config(noreplace) %verify(not md5 size mtime) /etc/security/time.conf
%config(noreplace) %verify(not md5 size mtime) /etc/security/consoles
%config(noreplace) %verify(not md5 size mtime) /etc/security/trigram*
%config(noreplace) %verify(not md5 size mtime) /etc/security/blacklist
%config(noreplace) %verify(not md5 size mtime) /etc/security/pam_mail.conf
%attr(600,root,root) %config(noreplace) %verify(not md5 size mtime) /etc/security/opasswd
%attr(755,root,root) /%{_lib}/lib*.so.*.*
%attr(755,root,root) /%{_lib}/security/pam_access.so
%attr(755,root,root) /%{_lib}/security/pam_console.so
%attr(755,root,root) /%{_lib}/security/pam_cracklib.so
%attr(755,root,root) /%{_lib}/security/pam_debug.so
%attr(755,root,root) /%{_lib}/security/pam_deny.so
%attr(755,root,root) /%{_lib}/security/pam_env.so
%attr(755,root,root) /%{_lib}/security/pam_filter.so
%attr(755,root,root) /%{_lib}/security/pam_ftp.so
%attr(755,root,root) /%{_lib}/security/pam_group.so
%attr(755,root,root) /%{_lib}/security/pam_homedir.so
%attr(755,root,root) /%{_lib}/security/pam_issue.so
%attr(755,root,root) /%{_lib}/security/pam_lastlog.so
%attr(755,root,root) /%{_lib}/security/pam_limits.so
%attr(755,root,root) /%{_lib}/security/pam_listfile.so
%attr(755,root,root) /%{_lib}/security/pam_localuser.so
%attr(755,root,root) /%{_lib}/security/pam_mail.so
%attr(755,root,root) /%{_lib}/security/pam_make.so
%attr(755,root,root) /%{_lib}/security/pam_motd.so
%attr(755,root,root) /%{_lib}/security/pam_netid.so
%attr(755,root,root) /%{_lib}/security/pam_nologin.so
%attr(755,root,root) /%{_lib}/security/pam_permit.so
%attr(755,root,root) /%{_lib}/security/pam_pwgen.so
%attr(755,root,root) /%{_lib}/security/pam_rhosts.so
%attr(755,root,root) /%{_lib}/security/pam_rootok.so
%attr(755,root,root) /%{_lib}/security/pam_securetty.so
%attr(755,root,root) /%{_lib}/security/pam_shells.so
%attr(755,root,root) /%{_lib}/security/pam_stress.so
%attr(755,root,root) /%{_lib}/security/pam_succeed_if.so
%attr(755,root,root) /%{_lib}/security/pam_tally.so
%attr(755,root,root) /%{_lib}/security/pam_time.so
%attr(755,root,root) /%{_lib}/security/pam_unix.so
%attr(755,root,root) /%{_lib}/security/pam_userdb.so
%attr(755,root,root) /%{_lib}/security/pam_usertty.so
%attr(755,root,root) /%{_lib}/security/pam_utmp.so
%attr(755,root,root) /%{_lib}/security/pam_warn.so
%attr(755,root,root) /%{_lib}/security/pam_wheel.so
%attr(755,root,root) /%{_lib}/security/pam_xauth.so
%{?with_pwexport:%attr(755,root,root) /%{_lib}/security/pam_pwexport.so}
%attr(755,root,root) /sbin/pam_filter/upperLOWER
%attr(4755,root,root) /sbin/unix_chkpwd
%attr(755,root,root) %{_bindir}/pam_pwgen
%attr(755,root,root) %{_sbindir}/pam_tally
%attr(755,root,root) %{_sbindir}/pwgen_trigram
%{_mandir}/man5/*
%{_mandir}/man8/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_libdir}/libpammodutil.a
%{_includedir}/security/*.h
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libpam.a
%{_libdir}/libpamc.a
%{_libdir}/libpam_misc.a

%if %{with pwdb}
%files pam_pwdb
%defattr(644,root,root,755)
%attr(755,root,root) /%{_lib}/security/pam_pwdb.so
%attr(4755,root,root) /sbin/pwdb_chkpwd

%files pam_radius
%defattr(644,root,root,755)
%attr(755,root,root) /%{_lib}/security/pam_radius.so
%endif

%if %{with skey}
%files pam_skey
%defattr(644,root,root,755)
%attr(755,root,root) /%{_lib}/security/pam_skey.so
%endif

%if %{with opie}
%files pam_opie
%defattr(644,root,root,755)
%attr(755,root,root) /%{_lib}/security/pam_opie.so
%attr(755,root,root) /%{_lib}/security/pam_opietrust.so
%endif

%if %{with tcpd}
%files pam_tcpd
%defattr(644,root,root,755)
%attr(755,root,root) /%{_lib}/security/pam_tcpd.so
%endif

%if %{with cap}
%files pam_cap
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 size mtime) /etc/security/capability.conf
%attr(755,root,root) /%{_lib}/security/pam_cap.so
%endif
