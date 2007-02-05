#
# TODO:
#	triggers:
#		s/pam_make\.so \(.*\)/pam_exec.so make -C \1/g
#		s/pam_homedir\.so/pam_mkhomedir.so/g
#		/var/lock/console -> /var/run/console
#		
# Conditional build:
%bcond_without	doc		# don't build documentation
%bcond_with	prelude		# build with Prelude IDS support
%bcond_without	selinux		# build without SELinux support
%bcond_without	audit		# build with Linux Auditing library support
#
%define		pam_pld_version	0.99.7.1-1
#
Summary:	Pluggable Authentication Modules: modular, incremental authentication
Summary(de):	Einsteckbare Authentifizierungsmodule: modulare, inkrementДre Authentifizierung
Summary(es):	MСdulos de autentificaciСn plugables (PAM)
Summary(fr):	PAM : Pluggable Authentication Modules: modular, incremental authentication
Summary(pl):	Modularny system uwierzytelniania
Summary(pt_BR):	MСdulos de autenticaГЦo plugАveis (PAM)
Summary(ru):	Интструмент, обеспечивающий аутентификацию для приложений
Summary(tr):	ModЭler, artЩmsal doПrulama birimleri
Summary(uk):	╤нструмент, що забезпечу╓ аутентиф╕кац╕ю для програм
Name:		pam
Version:	0.99.7.1
Release:	0.1
License:	GPL or BSD
Group:		Base
Source0:	http://ftp.kernel.org/pub/linux/libs/pam/pre/library/Linux-PAM-%{version}.tar.bz2
# Source0-md5:	385458dfb4633071594e255a6ebec9da
Source1:	http://ftp.kernel.org/pub/linux/libs/pam/pre/library/Linux-PAM-%{version}.tar.bz2.sign
# Source1-md5:	259c57009369eda92a00d1a153776ac6
Source2:	ftp://ftp.pld-linux.org/software/pam/pam-pld-%{pam_pld_version}.tar.gz
# Source2-md5:	62ee3a41c59000c78a3d6aa024ee55bd
Source3:	other.pamd
Source4:	system-auth.pamd
Source5:	config-util.pamd
Source6:	pam_selinux_check.pamd
Source7:	system-auth.5
Source8:	config-util.5
Patch0:		%{name}-pld-modules.patch
Patch1:		%{name}-modutil_mem_limit.patch
Patch2:		%{name}-cracklib-try-first-pass.patch
Patch3:		%{name}-cracklib-enforce.patch
Patch4:		%{name}-tally-fail-close.patch
Patch5:		%{name}-selinux-nofail.patch
Patch6:		%{name}-selinux-drop-multiple.patch
Patch7:		%{name}-selinux-keycreate.patch
Patch8:		%{name}-selinux-select-context.patch
Patch9:		%{name}-selinux-use-current-range.patch
Patch10:	%{name}-namespace-no-unmount.patch
Patch11:	%{name}-namespace-preserve-uid.patch
Patch12:	%{name}-namespace-level.patch
Patch13:	%{name}-namespace-unmnt-override.patch
Patch14:	%{name}-unix-nullcheck.patch
Patch15:	%{name}-unix-blowfish.patch
Patch16:	%{name}-mkhomedir-new-features.patch
URL:		http://www.kernel.org/pub/linux/libs/pam/
%{?with_audit:BuildRequires:	audit-libs-devel >= 1.0.8}
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	cracklib-devel
BuildRequires:	db-devel
BuildRequires:	flex
%{?with_prelude:BuildRequires:	libprelude-devel}
%{?with_selinux:BuildRequires:	libselinux-devel >= 1.33.2}
BuildRequires:	libtool >= 2:1.5
%if %{with doc}
BuildRequires:	docbook-dtd43-xml
BuildRequires:	docbook-dtd44-xml
BuildRequires:	docbook-style-xsl >= 1.69.1
# For building PDFs
#BuildRequires:	fop
BuildRequires:	libxml2-progs
BuildRequires:	libxslt-progs
BuildRequires:	w3m
%endif
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	awk
Requires:	cracklib
Requires:	cracklib-dicts
Requires:	make
Provides:	pam-pld
Obsoletes:	pamconfig
Obsoletes:	pam_make
Obsoletes:	pam-doc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fno-strict-aliasing

%define		_sbindir	/sbin

%description
PAM (Pluggable Authentication Modules) is a powerful, flexible,
extensible authentication system which allows the system administrator
to configure authentication services individually for every
pam-compliant application without recompiling any of the applications.

%description -l de
PAM (Pluggable Authentication Modules) ist ein leistungsfДhiges,
flexibles und erweiterbares Authentifizierungssystem, mit dem der
Systemverwalter Authentifizierungs-Dienste individuell fЭr jede
pam-kompatible Anwendung konfigurieren kann, ohne diese neu
kompilieren zu mЭssen.

%description -l es
PAM (MСdulos de AutenticaciСn Plugables) es un potente, flexible y
extensible sistema de autentificaciСn, que permite al administrador
del sistema configurar servicios de autentificaciСn individualmente
para cada aplicaciСn pam compatible, sin la necesidad de recompilar
cualquier una de las aplicaciones.

%description -l fr
PAM (Pluggable Authentication Modules) est un systИme
d'authentification puissant, souple et extensible permettant Ю
l'administrateur systХme de configurer les individuellement les
services d'authentification pour chaque application conforme Ю PAM,
sans recompiler aucune application.

%description -l pl
PAM (Pluggable Authentication Modules) jest silnym i Ёatwo
dostosowywalnym do potrzeb systemem uwierzytelniania, ktСry umo©liwia
administratorowi indywidualne konfigurowanie poszczegСlnych usЁug,
ktСre s╠ dostosowane i skonsolidowane z bibliotekami PAM, bez
pС╪niejszej ich rekompilacji w momencie zmiany sposobu
uwierzytelniania tych©e usЁug.

%description -l pt_BR
PAM (MСdulos de AutenticaГЦo PlugАveis) И um poderoso, flexМvel e
extensМvel sistema de autenticaГЦo, que permite o administrador do
sistema configurar serviГos de autenticaГЦo individualmente para cada
aplicaГЦo pam compatМvel, sem necessidade de recompilar qualquer uma
das aplicaГУes.

%description -l uk
PAM (Pluggable Authentication Modules) - це потужна, гнучка, здатна до
розширення система аутентикац╕╖, яка дозволя╓ системному
адм╕н╕стратору налагоджувати сев╕си авторизац╕╖ доступу (аутентикац╕╖)
╕ндив╕дуально для кожно╖ pam-сум╕сно╖ програми без необх╕дност╕
перекомп╕ляц╕╖ само╖ програми. Це базовий механ╕зм аутентикац╕╖ в PLD
Linux.

%description -l tr
PAM (Pluggable Authentication Modules) sistem yЖneticilerinin
uygulamalardan herhangi birini yeniden derlemeksizin bЭtЭn PAM uyumlu
uygulamalar iГin doПrulama hizmetlerini ayarlamalarЩna yardЩmcЩ olan,
gЭclЭ, esnek ve kapsamlЩ bir doПrulama sistemidir.

%description -l ru
PAM (Pluggable Authentication Modules) - это мощная, гибкая,
расширяемая система аутентикации, позволяющая системному
администратору конфигурировать сервисы авторизации доступа
(аутентикации) индивидуально для каждой pam-совместимой программы без
необходимости перекомпилляции самой программы. Это базовый механизм
аутентикации в PLD Linux.

%package libs
Summary:	PAM modules and libraries
Summary(pl):	ModuЁy i biblioteki PAM
Group:		Libraries
Conflicts:	pam < 0:0.80.1-2
%{?with_audit:Requires:	audit-libs >= 1.0.8}
%{?with_selinux:Requires:	libselinux >= 1.33.2}

%description libs
Core PAM modules and libraries.

%description libs -l pl
ModuЁy i biblioteki PAM.

%package devel
Summary:	PAM header files
Summary(pl):	Pliki nagЁСwkowe i dokumentacja programisty do PAM
Summary(pt_BR):	Bibliotecas e arquivos de inclusЦo para desenvolvimento com PAM
Summary(ru):	Библиотеки разработчика для PAM
Summary(uk):	Б╕бл╕отеки програм╕ста для PAM
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	filesystem >= 3.0-11

%description devel
Header files for developing PAM based applications.

%description devel -l pl
Pliki nagЁСwkowe i dokumentacja programisty do PAM.

%description devel -l pt_BR
Bibliotecas e arquivos de inclusЦo para desenvolvimento com PAM

%description devel -l ru
Этот пакет содержит хедеры и библиотеки разработчика для PAM.

%description devel -l uk
Цей пакет м╕стить хедери та б╕бл╕отеки програм╕ста для PAM.

%package static
Summary:	PAM static libraries
Summary(pl):	Biblioteki statyczne PAM
Summary(ru):	Статические библиотеки разработчика для PAM
Summary(uk):	Статичн╕ б╕бл╕отеки програм╕ста для PAM
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
PAM static libraries.

%description static -l pl
Biblioteki statyczne PAM.

%description static -l ru
Этот пакет содержит статические библиотеки разработчика для PAM.

%description static -l uk
Цей пакет м╕стить статичн╕ б╕бл╕отеки програм╕ста для PAM.

%package pam_selinux
Summary:	PAM module - SELinux support
Summary(pl):	ModuЁ PAM pozwalaj╠cy na zmianЙ kontekstСw SELinuksa
Group:		Base

%description pam_selinux
PAM module - SELinux support.

%description pam_selinux -l pl
ModuЁ PAM pozwalaj╠cy na zmianЙ kontekstСw SELinuksa.

%prep
%setup -q -a2 -n Linux-PAM-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-static \
	--enable-shared \
	--libdir=/%{_lib} \
	--includedir=%{_includedir}/security \
	--enable-isadir=../../%{_lib}/security \
	%{!?with_selinux:--disable-selinux} \
	%{!?with_prelude:--disable-prelude} \
	%{!?with_audit:--disable-audit}

# we must explicitely update-gmo as we patch a po file
%{__make} -C po update-gmo
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},/etc/pam.d,/var/log}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install modules/pam_selinux/.libs/pam_selinux_check $RPM_BUILD_ROOT%{_sbindir}
install modules/pam_selinux/pam_selinux_check.8 $RPM_BUILD_ROOT%{_mandir}/man8

mkdir -p doc/txts
for r in modules/pam_*/README ; do
	cp -f $r doc/txts/README.$(basename $(dirname $r))
done
mkdir -p doc/html
cp -f doc/index.html doc/html/

# fix PAM/pam man page
echo ".so PAM.8" > $RPM_BUILD_ROOT%{_mandir}/man8/pam.8

:> $RPM_BUILD_ROOT/etc/security/opasswd
:> $RPM_BUILD_ROOT/etc/security/blacklist

#:> $RPM_BUILD_ROOT/var/log/faillog
:> $RPM_BUILD_ROOT/var/log/tallylog

mv -f $RPM_BUILD_ROOT/%{_lib}/lib*.{la,a} $RPM_BUILD_ROOT/%{_libdir}

cd $RPM_BUILD_ROOT/%{_lib}
ln -sf /%{_lib}/$(echo libpam.so.*.*.*) $RPM_BUILD_ROOT%{_libdir}/libpam.so
ln -sf /%{_lib}/$(echo libpam_misc.so.*.*.*) $RPM_BUILD_ROOT%{_libdir}/libpam_misc.so
ln -sf /%{_lib}/$(echo libpamc.so.*.*.*) $RPM_BUILD_ROOT%{_libdir}/libpamc.so
cd -

install %{SOURCE3} $RPM_BUILD_ROOT/etc/pam.d/other
install %{SOURCE4} $RPM_BUILD_ROOT/etc/pam.d/system-auth
install %{SOURCE5} $RPM_BUILD_ROOT/etc/pam.d/config-util
install %{SOURCE6} $RPM_BUILD_ROOT/etc/pam.d/pam_selinux_check

install %{SOURCE7} $RPM_BUILD_ROOT%{_mandir}/man5/system-auth.5
install %{SOURCE8} $RPM_BUILD_ROOT%{_mandir}/man5/config-util.5

# useless - shut up check-files
rm -f $RPM_BUILD_ROOT/%{_lib}/security/*.{la,a}
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/Linux-PAM

%if !%{with selinux}
rm -rf $RPM_BUILD_ROOT{/%{_lib}/security/pam_selinux.so,%{_sbindir}/pam_selinux_check,%{_mandir}/man8/pam_selinux*.8*}
%endif

%find_lang Linux-PAM

%clean
rm -rf $RPM_BUILD_ROOT

%triggerpostun libs -- %{name}-libs < 0.99.7.1
#	s/pam_make\.so \(.*\)/pam_exec.so make -C \1/g
#	s/pam_homedir\.so/pam_mkhomedir.so/g
#	/var/lock/console -> /var/run/console

%post
#if [ ! -a /var/log/faillog ] ; then
#	install -m 600 /dev/null /var/log/faillog
#fi
if [ ! -a /var/log/tallylog ] ; then
	install -m 600 /dev/null /var/log/tallylog
fi

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f Linux-PAM.lang
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG ChangeLog Copyright NEWS
%doc doc/txts/README*
%if %{with doc}
%doc doc/specs/*.txt
%doc doc/sag/Linux-PAM_*.txt
%doc doc/{sag,}/html
%endif
%dir %attr(755,root,root) /etc/pam.d
%dir %attr(755,root,root) /etc/security/console.apps
%dir %attr(755,root,root) /etc/security/console.perms.d
%dir %attr(755,root,root) /var/run/console
%config /etc/security/console.perms.d/50-default.perms
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/other
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/system-auth
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/config-util
%config(noreplace) %verify(not md5 mtime size) /etc/security/access.conf
%config(noreplace) %verify(not md5 mtime size) /etc/security/pam_env.conf
%config(noreplace) %verify(not md5 mtime size) /etc/security/group.conf
%config(noreplace) %verify(not md5 mtime size) /etc/security/limits.conf
%config(noreplace) %verify(not md5 mtime size) /etc/security/time.conf
%config(noreplace) %verify(not md5 mtime size) /etc/security/console.handlers
%config(noreplace) %verify(not md5 mtime size) /etc/security/console.perms
%config(noreplace) %verify(not md5 mtime size) /etc/security/trigram*
%config(noreplace) %verify(not md5 mtime size) /etc/security/blacklist
%config(noreplace) %verify(not md5 mtime size) /etc/environment
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/security/opasswd
%attr(4755,root,root) /sbin/unix_chkpwd
%attr(755,root,root) %{_bindir}/pam_pwgen
%attr(755,root,root) %{_sbindir}/pam_console_apply
%attr(755,root,root) %{_sbindir}/pam_tally
%attr(755,root,root) %{_sbindir}/pam_tally2
%attr(755,root,root) %{_sbindir}/pam_timestamp_check
%attr(755,root,root) %{_sbindir}/pwgen_trigram
%{_mandir}/man5/*
%{_mandir}/man8/PAM.*
%{_mandir}/man8/pam.*
%{_mandir}/man8/pam_[a-r]*
%{_mandir}/man8/pam_securetty*
%{_mandir}/man8/pam_shells*
%{_mandir}/man8/pam_succeed_if*
%{_mandir}/man8/pam_[t-x]*
%{_mandir}/man8/unix_chkpwd*
#%ghost %verify(not md5 size mtime) /var/log/faillog
%ghost %verify(not md5 size mtime) /var/log/tallylog

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) /%{_lib}/lib*.so.*.*
%attr(755,root,root) /%{_lib}/security/pam_access.so
%attr(755,root,root) /%{_lib}/security/pam_console.so
%attr(755,root,root) /%{_lib}/security/pam_cracklib.so
%attr(755,root,root) /%{_lib}/security/pam_debug.so
%attr(755,root,root) /%{_lib}/security/pam_deny.so
%attr(755,root,root) /%{_lib}/security/pam_echo.so
%attr(755,root,root) /%{_lib}/security/pam_env.so
%attr(755,root,root) /%{_lib}/security/pam_exec.so
%attr(755,root,root) /%{_lib}/security/pam_faildelay.so
%attr(755,root,root) /%{_lib}/security/pam_filter.so
%attr(755,root,root) /%{_lib}/security/pam_filter/upperLOWER
%attr(755,root,root) /%{_lib}/security/pam_ftp.so
%attr(755,root,root) /%{_lib}/security/pam_group.so
%attr(755,root,root) /%{_lib}/security/pam_issue.so
%attr(755,root,root) /%{_lib}/security/pam_keyinit.so
%attr(755,root,root) /%{_lib}/security/pam_lastlog.so
%attr(755,root,root) /%{_lib}/security/pam_limits.so
%attr(755,root,root) /%{_lib}/security/pam_listfile.so
%attr(755,root,root) /%{_lib}/security/pam_localuser.so
%attr(755,root,root) /%{_lib}/security/pam_loginuid.so
%attr(755,root,root) /%{_lib}/security/pam_mail.so
%attr(755,root,root) /%{_lib}/security/pam_mkhomedir.so
%attr(755,root,root) /%{_lib}/security/pam_motd.so
%attr(755,root,root) /%{_lib}/security/pam_nologin.so
%attr(755,root,root) /%{_lib}/security/pam_permit.so
%attr(755,root,root) /%{_lib}/security/pam_pwexport.so
%attr(755,root,root) /%{_lib}/security/pam_pwgen.so
%attr(755,root,root) /%{_lib}/security/pam_rhosts_auth.so
%attr(755,root,root) /%{_lib}/security/pam_rhosts.so
%attr(755,root,root) /%{_lib}/security/pam_rootok.so
%attr(755,root,root) /%{_lib}/security/pam_rps.so
%attr(755,root,root) /%{_lib}/security/pam_securetty.so
%attr(755,root,root) /%{_lib}/security/pam_shells.so
%attr(755,root,root) /%{_lib}/security/pam_stress.so
%attr(755,root,root) /%{_lib}/security/pam_succeed_if.so
%attr(755,root,root) /%{_lib}/security/pam_tally2.so
%attr(755,root,root) /%{_lib}/security/pam_tally.so
%attr(755,root,root) /%{_lib}/security/pam_time.so
%attr(755,root,root) /%{_lib}/security/pam_timestamp.so
%attr(755,root,root) /%{_lib}/security/pam_umask.so
%attr(755,root,root) /%{_lib}/security/pam_unix.so
%attr(755,root,root) /%{_lib}/security/pam_userdb.so
%attr(755,root,root) /%{_lib}/security/pam_warn.so
%attr(755,root,root) /%{_lib}/security/pam_wheel.so
%attr(755,root,root) /%{_lib}/security/pam_xauth.so

%files devel
%defattr(644,root,root,755)
%if %{with doc}
%doc doc/{adg,mwg}/Linux-PAM_*.txt
%doc doc/{adg,mwg,}/html
%endif
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/security/*.h
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libpam.a
%{_libdir}/libpamc.a
%{_libdir}/libpam_misc.a

%if %{with selinux}
%files pam_selinux
%defattr(644,root,root,755)
%attr(755,root,root) /%{_lib}/security/pam_selinux.so
%attr(755,root,root) %{_sbindir}/pam_selinux_check
%config(noreplace) %verify(not size mtime md5) /etc/pam.d/pam_selinux_check
%{_mandir}/man8/pam_selinux*.8*
%endif
