# TODO
# - something wrong for doc/ps,pdf generation on my build host. remove completely duplicated doc formats?
#
# Conditional build:
%bcond_with	pwexport	# enable pam_pwexport module (needs hacked pam_unix)
%bcond_without	cap		# don't build pam_cap module
%bcond_without	doc		# don't build documentation
%bcond_without	opie		# don't build pam_opie module
%bcond_with	prelude		# build without Prelude IDS support
%bcond_without	pwdb		# don't build pam_pwdb and pam_radius modules
%bcond_without	selinux		# build without SELinux support
%bcond_without	skey		# don't build pam_skey module
%bcond_without	tcpd		# don't build pam_tcpd module
#
Summary:	Pluggable Authentication Modules: modular, incremental authentication
Summary(de.UTF-8):	Einsteckbare Authentifizierungsmodule: modulare, inkrementäre Authentifizierung
Summary(es.UTF-8):	Módulos de autentificación plugables (PAM)
Summary(fr.UTF-8):	PAM : Pluggable Authentication Modules: modular, incremental authentication
Summary(pl.UTF-8):	Modularny system uwierzytelniania
Summary(pt_BR.UTF-8):	Módulos de autenticação plugáveis (PAM)
Summary(ru.UTF-8):	Интструмент, обеспечивающий аутентификацию для приложений
Summary(tr.UTF-8):	Modüler, artımsal doğrulama birimleri
Summary(uk.UTF-8):	Інструмент, що забезпечує аутентифікацію для програм
Name:		pam
Version:	0.80.1
Release:	19
Epoch:		0
License:	GPL or BSD
Group:		Base
Source0:	ftp://ftp.pld-linux.org/software/pam/%{name}-pld-%{version}.tar.gz
# Source0-md5:	df374f625e7178f43a263a32e376dd46
Source1:	system-auth.pamd
Patch0:		%{name}-pam_pwgen_app.patch
Patch1:		%{name}-modutil_mem_limit.patch
Patch2:		%{name}-link.patch
URL:		http://www.kernel.org/pub/linux/libs/pam/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	cracklib-devel
BuildRequires:	db-devel
BuildRequires:	flex
%{?with_cap:BuildRequires:	libcap-devel}
%{?with_prelude:BuildRequires:	libprelude-devel}
%{?with_selinux:BuildRequires:	libselinux-devel}
BuildRequires:	libtool >= 2:1.5
%{?with_tcpd:BuildRequires:	libwrap-devel >= 7.6-32}
%{?with_opie:BuildRequires:	opie-devel}
%{?with_pwdb:BuildRequires:	pwdb-devel}
BuildRequires:	sgml-tools
%{?with_skey:BuildRequires:	skey-devel}
%if %{with doc}
BuildRequires:	sp
BuildRequires:	tetex-fonts-jknappen
BuildRequires:	tetex-format-latex
BuildRequires:	tetex-metafont
BuildRequires:	tetex-tex-babel
%endif
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	awk
Requires:	cracklib
Requires:	cracklib-dicts
Requires:	make
Provides:	pam-pld
Obsoletes:	pam-doc
Obsoletes:	pam_make
Obsoletes:	pamconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fno-strict-aliasing

%description
PAM (Pluggable Authentication Modules) is a powerful, flexible,
extensible authentication system which allows the system administrator
to configure authentication services individually for every
pam-compliant application without recompiling any of the applications.

%description -l de.UTF-8
PAM (Pluggable Authentication Modules) ist ein leistungsfähiges,
flexibles und erweiterbares Authentifizierungssystem, mit dem der
Systemverwalter Authentifizierungs-Dienste individuell für jede
pam-kompatible Anwendung konfigurieren kann, ohne diese neu
kompilieren zu müssen.

%description -l es.UTF-8
PAM (Módulos de Autenticación Plugables) es un potente, flexible y
extensible sistema de autentificación, que permite al administrador
del sistema configurar servicios de autentificación individualmente
para cada aplicación pam compatible, sin la necesidad de recompilar
cualquier una de las aplicaciones.

%description -l fr.UTF-8
PAM (Pluggable Authentication Modules) est un systéme
d'authentification puissant, souple et extensible permettant à
l'administrateur système de configurer les individuellement les
services d'authentification pour chaque application conforme à PAM,
sans recompiler aucune application.

%description -l pl.UTF-8
PAM (Pluggable Authentication Modules) jest silnym i łatwo
dostosowywalnym do potrzeb systemem uwierzytelniania, który umożliwia
administratorowi indywidualne konfigurowanie poszczególnych usług,
które są dostosowane i skonsolidowane z bibliotekami PAM, bez
późniejszej ich rekompilacji w momencie zmiany sposobu
uwierzytelniania tychże usług.

%description -l pt_BR.UTF-8
PAM (Módulos de Autenticação Plugáveis) é um poderoso, flexível e
extensível sistema de autenticação, que permite o administrador do
sistema configurar serviços de autenticação individualmente para cada
aplicação pam compatível, sem necessidade de recompilar qualquer uma
das aplicações.

%description -l uk.UTF-8
PAM (Pluggable Authentication Modules) - це потужна, гнучка, здатна до
розширення система аутентикації, яка дозволяє системному
адміністратору налагоджувати севіси авторизації доступу (аутентикації)
індивідуально для кожної pam-сумісної програми без необхідності
перекомпіляції самої програми. Це базовий механізм аутентикації в PLD
Linux.

%description -l tr.UTF-8
PAM (Pluggable Authentication Modules) sistem yöneticilerinin
uygulamalardan herhangi birini yeniden derlemeksizin bütün PAM uyumlu
uygulamalar için doğrulama hizmetlerini ayarlamalarına yardımcı olan,
güclü, esnek ve kapsamlı bir doğrulama sistemidir.

%description -l ru.UTF-8
PAM (Pluggable Authentication Modules) - это мощная, гибкая,
расширяемая система аутентикации, позволяющая системному
администратору конфигурировать сервисы авторизации доступа
(аутентикации) индивидуально для каждой pam-совместимой программы без
необходимости перекомпилляции самой программы. Это базовый механизм
аутентикации в PLD Linux.

%package libs
Summary:	PAM modules and libraries
Summary(pl.UTF-8):	Moduły i biblioteki PAM
Group:		Libraries
Conflicts:	pam < 0:0.80.1-2

%description libs
Core PAM modules and libraries.

%description libs -l pl.UTF-8
Moduły i biblioteki PAM.

%package devel
Summary:	PAM header files
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja programisty do PAM
Summary(pt_BR.UTF-8):	Bibliotecas e arquivos de inclusão para desenvolvimento com PAM
Summary(ru.UTF-8):	Библиотеки разработчика для PAM
Summary(uk.UTF-8):	Бібліотеки програміста для PAM
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	filesystem >= 2.0-1

%description devel
Header files for developing PAM based applications.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja programisty do PAM.

%description devel -l pt_BR.UTF-8
Bibliotecas e arquivos de inclusão para desenvolvimento com PAM

%description devel -l ru.UTF-8
Этот пакет содержит хедеры и библиотеки разработчика для PAM.

%description devel -l uk.UTF-8
Цей пакет містить хедери та бібліотеки програміста для PAM.

%package static
Summary:	PAM static libraries
Summary(pl.UTF-8):	Biblioteki statyczne PAM
Summary(ru.UTF-8):	Статические библиотеки разработчика для PAM
Summary(uk.UTF-8):	Статичні бібліотеки програміста для PAM
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
PAM static libraries.

%description static -l pl.UTF-8
Biblioteki statyczne PAM.

%description static -l ru.UTF-8
Этот пакет содержит статические библиотеки разработчика для PAM.

%description static -l uk.UTF-8
Цей пакет містить статичні бібліотеки програміста для PAM.

%package pam_pwdb
Summary:	pam_pwdb module
Summary(pl.UTF-8):	Moduł pam_pwdb
Group:		Base
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	pwdb >= 0.54-2

%description pam_pwdb
pam_pwdb module.

%description pam_pwdb -l pl.UTF-8
Moduł pam_pwdb.

%package pam_radius
Summary:	pam_radius module
Summary(pl.UTF-8):	Moduł pam_radius
Group:		Base
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	pwdb >= 0.54-2

%description pam_radius
pam_radius module.

%description pam_radius -l pl.UTF-8
Moduł pam_radius.

%package pam_skey
Summary:	pam_skey module
Summary(pl.UTF-8):	Moduł pam_skey
Group:		Base
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	skey

%description pam_skey
pam_skey module.

%description pam_skey -l pl.UTF-8
Moduł pam_skey.

%package pam_opie
Summary:	pam_opie module
Summary(pl.UTF-8):	Moduł pam_opie
Group:		Base
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	opie

%description pam_opie
pam_opie module.

%description pam_opie -l pl.UTF-8
Moduł pam_opie.

%package pam_tcpd
Summary:	pam_tcpd module
Summary(pl.UTF-8):	Moduł pam_tcpd
Group:		Base
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	libwrap >= 7.6-32

%description pam_tcpd
pam_tcpd module.

%description pam_tcpd -l pl.UTF-8
Moduł pam_tcpd.

%package pam_cap
Summary:	pam_cap module
Summary(pl.UTF-8):	Moduł pam_cap
Group:		Base
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	libcap

%description pam_cap
pam_cap module.

%description pam_cap -l pl.UTF-8
Moduł pam_cap.

%package pam_selinux
Summary:	PAM module - SELinux support
Summary(pl.UTF-8):	Moduł PAM pozwalający na zmianę kontekstów SELinuksa
Group:		Base

%description pam_selinux
PAM module - SELinux support.

%description pam_selinux -l pl.UTF-8
Moduł PAM pozwalający na zmianę kontekstów SELinuksa.

%prep
%setup -q -n %{name}-pld-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
mkdir m4
%{!?with_prelude:echo 'AC_DEFUN([AM_PATH_LIBPRELUDE],[/bin/true])' > m4/prelude.m4}
find doc/ -type f | xargs %{__perl} -pi -e 's#/lib/security#/%{_lib}/security#g'

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-maintainer-mode \
	%{!?with_doc:--without-docs} \
	%{!?with_cap:--disable-cap} \
	%{!?with_opie:--disable-opie} \
	%{!?with_pwdb:--disable-pwdb} \
	%{!?with_skey:--disable-skey} \
	%{!?with_tcpd:--disable-tcpd} \
	%{?with_pwexport:--enable-want-pwexport-module} \
	%{!?with_selinux:--disable-selinux} \
	%{!?with_prelude:--disable-prelude} \
	--enable-strong-crypto

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_lib}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf docs
cp -a doc docs
rm -f docs/{ps,txts}/{README,*.log} \
	docs/{html,txts}/Makefile*

:> $RPM_BUILD_ROOT/etc/security/opasswd
:> $RPM_BUILD_ROOT/etc/security/blacklist

mv -f $RPM_BUILD_ROOT%{_libdir}/lib*.so.* $RPM_BUILD_ROOT/%{_lib}

install pamcrypt/.libs/libpamcrypt.a $RPM_BUILD_ROOT%{_libdir}

cd $RPM_BUILD_ROOT/%{_lib}
ln -sf /%{_lib}/$(echo libpam.so.*.*.*) $RPM_BUILD_ROOT%{_libdir}/libpam.so
ln -sf /%{_lib}/$(echo libpam_misc.so.*.*.*) $RPM_BUILD_ROOT%{_libdir}/libpam_misc.so
ln -sf /%{_lib}/$(echo libpamc.so.*.*.*) $RPM_BUILD_ROOT%{_libdir}/libpamc.so

cp %{SOURCE1} $RPM_BUILD_ROOT/etc/pam.d/system-auth

# useless - shut up check-files
rm -f $RPM_BUILD_ROOT/%{_lib}/security/*.{la,a}
rm -f $RPM_BUILD_ROOT%{_libdir}/libpamcrypt.a

%if %{without selinux}
rm -rf $RPM_BUILD_ROOT{/%{_lib}/security/pam_selinux.so,%{_sbindir}/pam_selinux_check,%{_mandir}/man8/pam_selinux*.8*}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGELOG ChangeLog Copyright doc/CREDITS
%if %{with doc}
%doc docs/{html,txts,specs/*.{raw,txt}}
# FIXME: doesn't build for me! missing BR!:
#builder@pld-i686 ps $  sgml2latex -o ps ../psgml2latex -o ps ../pam
#Processing file ../pam
#load_char_maps: no entity maps found
#parse_data: no entity map for `[lowbar]'
#sh: latex: not found
#sh: latex: not found
#dvips: ! DVI file can't be opened.
#%doc docs/ps/*.ps
%endif
%dir /etc/pam.d
%dir /sbin/pam_filter
%dir /var/lock/console
%dir /etc/security/console.apps
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/other
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/system-auth
%config(noreplace) %verify(not md5 mtime size) /etc/security/access.conf
%config(noreplace) %verify(not md5 mtime size) /etc/security/pam_env.conf
%config(noreplace) %verify(not md5 mtime size) /etc/security/group.conf
%config(noreplace) %verify(not md5 mtime size) /etc/security/limits.conf
%config(noreplace) %verify(not md5 mtime size) /etc/security/time.conf
%config(noreplace) %verify(not md5 mtime size) /etc/security/consoles
%config(noreplace) %verify(not md5 mtime size) /etc/security/trigram*
%config(noreplace) %verify(not md5 mtime size) /etc/security/blacklist
%config(noreplace) %verify(not md5 mtime size) /etc/security/pam_mail.conf
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/security/opasswd
%attr(755,root,root) /sbin/pam_filter/upperLOWER
%attr(4755,root,root) /sbin/unix_chkpwd
%attr(755,root,root) %{_bindir}/pam_pwgen
%attr(755,root,root) %{_sbindir}/pam_tally
%attr(755,root,root) %{_sbindir}/pwgen_trigram
%{_mandir}/man5/*
%{_mandir}/man8/pam.*
%{_mandir}/man8/pam_localuser*
%{_mandir}/man8/pam_succeed_if*
%{_mandir}/man8/pam_xauth*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) /%{_lib}/libpam.so.*.*.*
%attr(755,root,root) %ghost /%{_lib}/libpam.so.0
%attr(755,root,root) /%{_lib}/libpam_misc.so.*.*.*
%attr(755,root,root) %ghost /%{_lib}/libpam_misc.so.0
%attr(755,root,root) /%{_lib}/libpamc.so.*.*.*
%attr(755,root,root) %ghost /%{_lib}/libpamc.so.0
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
%config(noreplace) %verify(not md5 mtime size) /etc/security/capability.conf
%attr(755,root,root) /%{_lib}/security/pam_cap.so
%endif

%if %{with selinux}
%files pam_selinux
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) /%{_lib}/security/pam_selinux.so
%attr(755,root,root) %{_sbindir}/pam_selinux_check
#TODO: %config(noreplace) %verify(not size mtime md5) /etc/pam.d/pam_selinux_check
%{_mandir}/man8/pam_selinux*.8*
%endif
