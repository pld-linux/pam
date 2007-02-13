#		
# Conditional build:
%bcond_without	doc		# don't build documentation
%bcond_with	prelude		# build with Prelude IDS support
%bcond_without	selinux		# build without SELinux support
%bcond_without	audit		# build with Linux Auditing library support
#
%define		pam_pld_version	0.99.7.1-3
#
%define		_sbindir	/sbin
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
Version:	0.99.7.1
Release:	0.5
License:	GPL or BSD
Group:		Base
Source0:	http://ftp.kernel.org/pub/linux/libs/pam/pre/library/Linux-PAM-%{version}.tar.bz2
# Source0-md5:	385458dfb4633071594e255a6ebec9da
Source1:	http://ftp.kernel.org/pub/linux/libs/pam/pre/library/Linux-PAM-%{version}.tar.bz2.sign
# Source1-md5:	259c57009369eda92a00d1a153776ac6
Source2:	ftp://ftp.pld-linux.org/software/pam/pam-pld-%{pam_pld_version}.tar.gz
# Source2-md5:	04d42fee1701f78bdd115c0944a34238
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
Patch17:	%{name}-db-gdbm.patch
Patch18:	%{name}-exec-failok.patch
URL:		http://www.kernel.org/pub/linux/libs/pam/
%{?with_audit:BuildRequires:	audit-libs-devel >= 1.0.8}
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	cracklib-devel >= 2.8.3
# gdbm due to db pulling libpthread
BuildRequires:	gdbm-devel >= 1.8.3-7
BuildRequires:	flex
BuildRequires:	glibc-devel >= 2.5-0.5
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
Requires:	/usr/bin/make
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
Requires(triggerpostun):	sed >= 4.0
Requires:	cracklib >= 2.8.3
Requires:	cracklib-dicts >= 2.8.3
Requires:	gdbm >= 1.8.3-7
Requires:	glibc >= 2.5-0.5
%{?with_audit:Requires:	audit-libs >= 1.0.8}
%{?with_selinux:Requires:	libselinux >= 1.33.2}

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
Requires:	filesystem >= 3.0-11

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

%package pam_selinux
Summary:	PAM module - SELinux support
Summary(pl.UTF-8):	Moduł PAM pozwalający na zmianę kontekstów SELinuksa
Group:		Base

%description pam_selinux
PAM module - SELinux support.

%description pam_selinux -l pl.UTF-8
Moduł PAM pozwalający na zmianę kontekstów SELinuksa.

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
%patch17 -p1
%patch18 -p1

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
	--enable-db=gdbm \
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

%if %{with selinux}
install modules/pam_selinux/.libs/pam_selinux_check $RPM_BUILD_ROOT%{_sbindir}
install modules/pam_selinux/pam_selinux_check.8 $RPM_BUILD_ROOT%{_mandir}/man8
install %{SOURCE6} $RPM_BUILD_ROOT/etc/pam.d/pam_selinux_check
%endif

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

mv -f $RPM_BUILD_ROOT/%{_lib}/lib*.a $RPM_BUILD_ROOT/%{_libdir}

cd $RPM_BUILD_ROOT/%{_lib}
for f in lib*.la ; do
	sed -e 's|/%{_lib}/libpam|%{_libdir}/libpam|g' $f > $RPM_BUILD_ROOT/%{_libdir}/$f
	rm -f $f
done
ln -sf /%{_lib}/$(echo libpam.so.*.*.*) $RPM_BUILD_ROOT%{_libdir}/libpam.so
ln -sf /%{_lib}/$(echo libpam_misc.so.*.*.*) $RPM_BUILD_ROOT%{_libdir}/libpam_misc.so
ln -sf /%{_lib}/$(echo libpamc.so.*.*.*) $RPM_BUILD_ROOT%{_libdir}/libpamc.so
cd -

install %{SOURCE3} $RPM_BUILD_ROOT/etc/pam.d/other
install %{SOURCE4} $RPM_BUILD_ROOT/etc/pam.d/system-auth
install %{SOURCE5} $RPM_BUILD_ROOT/etc/pam.d/config-util

install %{SOURCE7} $RPM_BUILD_ROOT%{_mandir}/man5/system-auth.5
install %{SOURCE8} $RPM_BUILD_ROOT%{_mandir}/man5/config-util.5

# Make sure every module subdirectory gave us a module.  Yes, this is hackish.
for dir in modules/pam_* ; do
%if %{without selinux}
[ ${dir} = "modules/pam_selinux" ] && continue
%endif
	if [ -d ${dir} ] ; then
		if ! ls -1 $RPM_BUILD_ROOT/%{_lib}/security/`basename ${dir}`*.so ; then
			echo ERROR `basename ${dir}` did not build a module.
			exit 1
		fi
	fi
done

for module in $RPM_BUILD_ROOT/%{_lib}/security/pam*.so ; do
# Check for module problems.  Specifically, check that every module we just
# installed can actually be loaded by a minimal PAM-aware application.
	if ! env LD_LIBRARY_PATH=$RPM_BUILD_ROOT/%{_lib} \
			./dlopen.sh -ldl -lpam -L$RPM_BUILD_ROOT/%{_lib} ${module} ; then
		echo ERROR module: ${module} cannot be loaded.
		exit 1
	fi
# And for good measure, make sure that none of the modules pull in threading
# libraries, which if loaded in a non-threaded application, can cause Very
# Bad Things to happen.
	if env LD_LIBRARY_PATH=$RPM_BUILD_ROOT/%{_lib} \
			LD_PRELOAD=$RPM_BUILD_ROOT/%{_lib}/libpam.so ldd -r ${module} | \
			fgrep -q libpthread ; then
		echo ERROR module: ${module} pulls threading libraries.
		exit 1
	fi
done

# useless - shut up check-files
rm -f $RPM_BUILD_ROOT/%{_lib}/security/*.{la,a}
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/Linux-PAM

%if %{without selinux}
rm -rf $RPM_BUILD_ROOT{/%{_lib}/security/pam_selinux.so,%{_sbindir}/pam_selinux_check,%{_mandir}/man8/pam_selinux*.8*}
%endif

%find_lang Linux-PAM

%clean
rm -rf $RPM_BUILD_ROOT

%triggerpostun libs -- %{name}-libs < 0.99.7.1
for f in `grep -l "\(pam_make\|pam_homedir\)" /etc/pam.d/*` ; do
	case "$f" in
	*rpmorig|*rpmnew|*rpmsave|*~|*.orig)
		continue
		;;
	*)
		cp -f "$f" "$f.rpmorig"
		sed -i -e 's/pam_make\.so \(.*\)/pam_exec.so failok seteuid \/usr\/bin\/make -C \1/g' \
		       -e 's/pam_homedir\.so/pam_mkhomedir.so/g' "$f"
		;;
	esac
done
if [ -d /var/lock/console -a -d /var/run/console ]; then
	cp -a /var/lock/console/* /var/run/console/
	rm -rf /var/lock/console
fi

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
%config(noreplace) %verify(not md5 mtime size) /etc/environment
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/other
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/system-auth
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/config-util
%config(noreplace) %verify(not md5 mtime size) /etc/security/access.conf
%config(noreplace) %verify(not md5 mtime size) /etc/security/blacklist
%config(noreplace) %verify(not md5 mtime size) /etc/security/console.handlers
%config(noreplace) %verify(not md5 mtime size) /etc/security/console.perms
%config(noreplace) %verify(not md5 mtime size) /etc/security/group.conf
%config(noreplace) %verify(not md5 mtime size) /etc/security/limits.conf
%config(noreplace) %verify(not md5 mtime size) /etc/security/namespace.conf
%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/security/namespace.init
%config(noreplace) %verify(not md5 mtime size) /etc/security/pam_env.conf
%config(noreplace) %verify(not md5 mtime size) /etc/security/time.conf
%config(noreplace) %verify(not md5 mtime size) /etc/security/trigram*
%config /etc/security/console.perms.d/50-default.perms
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
%dir /%{_lib}/security/pam_filter
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
%attr(755,root,root) /%{_lib}/security/pam_namespace.so
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
