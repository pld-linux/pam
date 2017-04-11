# TODO
# - check and package docs: https://fedorahosted.org/releases/l/i/linux-pam/Linux-PAM-1.1.8-docs.tar.bz2
# - fix pdf gen or disable it: No fo2pdf processor installed, skip PDF generation
#
# Conditional build:
%bcond_without	doc		# don't build documentation
%bcond_with	prelude		# build with Prelude IDS support (in libpam)
%bcond_without	selinux		# build without SELinux support
%bcond_without	audit		# build with Linux Auditing library support

%define		pam_pld_version	1.1.2-1
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
Version:	1.3.0
Release:	2
Epoch:		1
License:	GPL or BSD
Group:		Base
Source0:	http://www.linux-pam.org/library/Linux-PAM-%{version}.tar.bz2
# Source0-md5:	da4b2289b7cfb19583d54e9eaaef1c3a
Source1:	http://www.linux-pam.org/library/Linux-PAM-%{version}-docs.tar.bz2
# Source1-md5:	30fa7fa696a5b3b8d2c3c41d9373a8f3
Source2:	ftp://ftp.pld-linux.org/software/pam/%{name}-pld-%{pam_pld_version}.tar.gz
# Source2-md5:	f9ec6fcafcf1801bf318e60040244f2e
Source3:	other.pamd
Source4:	system-auth.pamd
Source5:	config-util.pamd
Source6:	%{name}_selinux_check.pamd
Source7:	system-auth.5
Source8:	config-util.5
Source9:	%{name}.tmpfiles
Source10:	postlogin.pamd
Patch0:		%{name}-pld-modules.patch
Patch2:		%{name}-tally-fail-close.patch
Patch3:		%{name}-mkhomedir-notfound.patch
Patch4:		%{name}-db-gdbm.patch
Patch5:		%{name}-exec-failok.patch
Patch6:		update-motd.patch
URL:		http://www.linux-pam.org/
%{?with_audit:BuildRequires:	audit-libs-devel >= 1.6.9}
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	cracklib-devel >= 2.8.3
# gdbm due to db pulling libpthread
BuildRequires:	flex
BuildRequires:	gdbm-devel >= 1.8.3-7
BuildRequires:	gettext-tools >= 0.18.3
BuildRequires:	glibc-devel >= 6:2.10.1
%{?with_prelude:BuildRequires:	libprelude-devel >= 0.9.0}
%{?with_selinux:BuildRequires:	libselinux-devel >= 2.1.9}
BuildRequires:	libtirpc-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	libxcrypt-devel
%{?with_audit:BuildRequires:	linux-libc-headers >= 2.6.23.1}
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel
%if %{with doc}
BuildRequires:	docbook-dtd412-xml
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
%{?with_audit:Requires:	audit-libs >= 1.0.8}
Requires:	awk
Requires:	cracklib >= 2.8.3
Requires:	cracklib-dicts >= 2.8.3
Requires:	crypt(blowfish)
Requires:	glibc >= 6:2.5-0.5
%{?with_selinux:Requires:	libselinux >= 2.1.9}
Suggests:	make
Suggests:	pam-pam_userdb = %{epoch}:%{version}-%{release}
Obsoletes:	pam-doc
Obsoletes:	pam-pam_opie
Obsoletes:	pam-pam_pwdb
Obsoletes:	pam-pam_radius
Obsoletes:	pam-pam_skey
Obsoletes:	pam-pam_tcpd
Obsoletes:	pam_make
Obsoletes:	pamconfig
Conflicts:	dev < 3.4-4
Conflicts:	pam < 0:0.80.1-2
Conflicts:	udev < 1:138-5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

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
Summary:	PAM libraries
Summary(pl.UTF-8):	Moduły PAM
Group:		Libraries
Requires(triggerpostun):	sed >= 4.0

%description libs
PAM libraries.

%description libs -l pl.UTF-8
Moduły PAM.

%package devel
Summary:	PAM header files
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja programisty do PAM
Summary(pt_BR.UTF-8):	Bibliotecas e arquivos de inclusão para desenvolvimento com PAM
Summary(ru.UTF-8):	Библиотеки разработчика для PAM
Summary(uk.UTF-8):	Бібліотеки програміста для PAM
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
%{?with_audit:Requires:	audit-libs-devel >= 1.0.8}
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
Requires:	libselinux >= 2.1.9

%description pam_selinux
PAM module - SELinux support.

%description pam_selinux -l pl.UTF-8
Moduł PAM pozwalający na zmianę kontekstów SELinuksa.

%package pam_userdb
Summary:	PAM module - authenticate against db database
Group:		Base
Requires:	gdbm >= 1.8.3-7
Conflicts:	pam-libs < 1:1.1.8-3.1

%description pam_userdb
pam_userdb - PAM module to authenticate against a Berkeley DB database

%prep
%setup -q -a2 -n Linux-PAM-%{version}
%patch0 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	ac_cv_path_FO2PDF= \
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
%{__make} \
	DEFS="-DHAVE_CONFIG_H -D_GNU_SOURCE"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},/etc/pam.d,/var/{log,run/sepermit}} \
	$RPM_BUILD_ROOT%{systemdtmpfilesdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with selinux}
install -p modules/pam_selinux/.libs/pam_selinux_check $RPM_BUILD_ROOT%{_sbindir}
cp -p modules/pam_selinux/pam_selinux_check.8 $RPM_BUILD_ROOT%{_mandir}/man8
cp -p %{SOURCE6} $RPM_BUILD_ROOT/etc/pam.d/pam_selinux_check
%endif

cp -p %{SOURCE9} $RPM_BUILD_ROOT%{systemdtmpfilesdir}/%{name}.conf

install -d doc/txts
for r in modules/pam_*/README; do
	cp -pf $r doc/txts/README.$(basename $(dirname $r))
done
%{__rm} doc/txts/README.pam_userdb
install -d doc/html
cp -pf doc/index.html doc/html/

# fix PAM/pam man page
echo ".so PAM.8" > $RPM_BUILD_ROOT%{_mandir}/man8/pam.8

:> $RPM_BUILD_ROOT/etc/security/opasswd
:> $RPM_BUILD_ROOT/etc/security/blacklist

:> $RPM_BUILD_ROOT/var/log/tallylog

%{__mv} $RPM_BUILD_ROOT/%{_lib}/lib*.a $RPM_BUILD_ROOT%{_libdir}

cd $RPM_BUILD_ROOT/%{_lib}
for f in lib*.la ; do
	%{__sed} -e 's|/%{_lib}/libpam|%{_libdir}/libpam|g' \
		 -e "s|libdir='/%{_lib}|libdir='%{_libdir}|g" $f > $RPM_BUILD_ROOT%{_libdir}/$f
	%{__rm} $f
done
ln -sf /%{_lib}/$(echo libpam.so.*.*.*) $RPM_BUILD_ROOT%{_libdir}/libpam.so
ln -sf /%{_lib}/$(echo libpam_misc.so.*.*.*) $RPM_BUILD_ROOT%{_libdir}/libpam_misc.so
ln -sf /%{_lib}/$(echo libpamc.so.*.*.*) $RPM_BUILD_ROOT%{_libdir}/libpamc.so
cd -

cp -p %{SOURCE3} $RPM_BUILD_ROOT/etc/pam.d/other
cp -p %{SOURCE4} $RPM_BUILD_ROOT/etc/pam.d/system-auth
cp -p %{SOURCE5} $RPM_BUILD_ROOT/etc/pam.d/config-util
cp -p %{SOURCE10} $RPM_BUILD_ROOT/etc/pam.d/postlogin

cp -p %{SOURCE7} $RPM_BUILD_ROOT%{_mandir}/man5/system-auth.5
cp -p %{SOURCE8} $RPM_BUILD_ROOT%{_mandir}/man5/config-util.5

# Make sure every module subdirectory gave us a module.  Yes, this is hackish.
for dir in modules/pam_* ; do
%if %{without selinux}
[ ${dir} = "modules/pam_selinux" ] && continue
[ ${dir} = "modules/pam_sepermit" ] && continue
%endif
%if %{without audit}
[ ${dir} = "modules/pam_tty_audit" ] && continue
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
done

# useless - shut up check-files
%{__rm} $RPM_BUILD_ROOT/%{_lib}/security/*.{la,a}
%{__rm} $RPM_BUILD_ROOT/%{_lib}/lib*.so
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/Linux-PAM

%if %{without selinux}
rm -rf $RPM_BUILD_ROOT{/%{_lib}/security/pam_selinux.so,%{_sbindir}/pam_selinux_check,%{_mandir}/man8/pam_selinux*.8*}
%endif

%find_lang Linux-PAM

%clean
rm -rf $RPM_BUILD_ROOT

%triggerpostun libs -- %{name}-libs < 0.99.7.1
for f in $(grep -l "\(pam_make\|pam_homedir\)" /etc/pam.d/*); do
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
	cp -a /var/lock/console/* /var/run/console/ 2> /dev/null
	rm -rf /var/lock/console
fi

%triggerin -- cronie,vixie-cron,hc-cron,fcron,mcron
# restart crond if pam is upgraded
# (crond is linked with old libpam but tries to open modules linked with new libpam)
if [ "$1" != 1 ]; then
	%service -q crond restart
fi
exit 0

%triggerpostun -- %{name} < 1:1.1.5-8
# removed in 1.1.4
if grep -qs change_uid /etc/pam.d/system-auth; then
	%{__sed} -i -e '/session/ s/change_uid//' /etc/pam.d/system-auth
fi

# We want it added for painless upgarde even if it mean log pollution for non-systemd
# enabled systems,
# If this module is not present on systemd enabled system then `systemctl restart sshd.service`
# will kill all sessions.
if ! grep -qs pam_systemd /etc/pam.d/system-auth; then
	echo "-session	optional	pam_systemd.so" >>/etc/pam.d/system-auth
fi

%post -p <lua>
fh, error = io.open("/var/log/tallylog")
if fh ~= nil then
	io.close(fh)
else
	fh = io.open("/var/log/tallylog", "w+")
	io.close(fh)
	posix.chmod("/var/log/tallylog", "rw-------")
end

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f Linux-PAM.lang
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG ChangeLog Copyright NEWS doc/txts/README*
%if %{with doc}
%doc doc/specs/*.txt doc/sag/Linux-PAM_*.txt doc/{sag,}/html
%endif
%dir /etc/pam.d
%dir /etc/security/console.apps
%dir /etc/security/console.perms.d
%dir /var/run/console
%{systemdtmpfilesdir}/%{name}.conf
%config(noreplace) %verify(not md5 mtime size) /etc/environment
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/other
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/system-auth
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/config-util
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/postlogin
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
%config(noreplace) %verify(not md5 mtime size) /etc/security/trigram
%config(noreplace) %verify(not md5 mtime size) /etc/security/trigram.en
%config(noreplace) %verify(not md5 mtime size) /etc/security/trigram.de
%config(noreplace) %verify(not md5 mtime size) /etc/security/trigram.dk
%config(noreplace) %verify(not md5 mtime size) /etc/security/trigram.es
%config(noreplace) %verify(not md5 mtime size) /etc/security/trigram.fi
%config(noreplace) %verify(not md5 mtime size) /etc/security/trigram.it
%config(noreplace) %verify(not md5 mtime size) /etc/security/trigram.ja
%config(noreplace) %verify(not md5 mtime size) /etc/security/trigram.no
%config(noreplace) %verify(not md5 mtime size) /etc/security/trigram.pl
%config(noreplace) %verify(not md5 mtime size) /etc/security/console.perms.d/50-default.perms
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/security/opasswd
%attr(755,root,root) %{_bindir}/pam_pwgen
%attr(755,root,root) %{_sbindir}/mkhomedir_helper
%attr(755,root,root) %{_sbindir}/pam_console_apply
%attr(755,root,root) %{_sbindir}/pam_tally
%attr(755,root,root) %{_sbindir}/pam_tally2
%attr(755,root,root) %{_sbindir}/pam_timestamp_check
%attr(755,root,root) %{_sbindir}/pwgen_trigram
%attr(4755,root,root) %{_sbindir}/unix_chkpwd
%attr(4755,root,root) %{_sbindir}/unix_update
%{_mandir}/man5/access.conf.5*
%{_mandir}/man5/config-util.5*
%{_mandir}/man5/console.apps.5*
%{_mandir}/man5/console.handlers.5*
%{_mandir}/man5/console.perms.5*
%{_mandir}/man5/environment.5*
%{_mandir}/man5/group.conf.5*
%{_mandir}/man5/limits.conf.5*
%{_mandir}/man5/namespace.conf.5*
%{_mandir}/man5/pam.conf.5*
%{_mandir}/man5/pam.d.5*
%{_mandir}/man5/pam_env.conf.5*
%{_mandir}/man5/system-auth.5*
%{_mandir}/man5/time.conf.5*
%{_mandir}/man8/PAM.8*
%{_mandir}/man8/mkhomedir_helper.8*
%{_mandir}/man8/pam.8*
%{_mandir}/man8/pam_*.8*
%{_mandir}/man8/unix_chkpwd.8*
%{_mandir}/man8/unix_update.8*
%if %{with selinux}
%exclude %{_mandir}/man8/pam_selinux*.8*
%exclude %{_mandir}/man8/pam_sepermit.8*
%endif
%exclude %{_mandir}/man8/pam_userdb.8*
%ghost %verify(not md5 mtime size) /var/log/tallylog

# PAM modules
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
%attr(755,root,root) /%{_lib}/security/pam_pwhistory.so
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
%{?with_audit:%attr(755,root,root) /%{_lib}/security/pam_tty_audit.so}
%attr(755,root,root) /%{_lib}/security/pam_umask.so
%attr(755,root,root) /%{_lib}/security/pam_unix.so
%attr(755,root,root) /%{_lib}/security/pam_warn.so
%attr(755,root,root) /%{_lib}/security/pam_wheel.so
%attr(755,root,root) /%{_lib}/security/pam_xauth.so

%files libs
%defattr(644,root,root,755)
%dir /%{_lib}/security/pam_filter
%attr(755,root,root) /%{_lib}/libpam.so.*.*.*
%attr(755,root,root) %ghost /%{_lib}/libpam.so.0
%attr(755,root,root) /%{_lib}/libpam_misc.so.*.*.*
%attr(755,root,root) %ghost /%{_lib}/libpam_misc.so.0
%attr(755,root,root) /%{_lib}/libpamc.so.*.*.*
%attr(755,root,root) %ghost /%{_lib}/libpamc.so.0

%files devel
%defattr(644,root,root,755)
%if %{with doc}
%doc doc/{adg,mwg}/Linux-PAM_*.txt doc/{adg,mwg,}/html
%endif
%attr(755,root,root) %{_libdir}/libpam.so
%attr(755,root,root) %{_libdir}/libpam_misc.so
%attr(755,root,root) %{_libdir}/libpamc.so
%{_libdir}/libpam.la
%{_libdir}/libpam_misc.la
%{_libdir}/libpamc.la
%{_includedir}/security/_pam_*.h
%{_includedir}/security/pam*.h
%{_mandir}/man3/misc_conv.3*
%{_mandir}/man3/pam*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libpam.a
%{_libdir}/libpamc.a
%{_libdir}/libpam_misc.a

%if %{with selinux}
%files pam_selinux
%defattr(644,root,root,755)
%attr(755,root,root) /%{_lib}/security/pam_selinux.so
%attr(755,root,root) /%{_lib}/security/pam_sepermit.so
%attr(755,root,root) %{_sbindir}/pam_selinux_check
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/pam_selinux_check
%config(noreplace) %verify(not md5 mtime size) /etc/security/sepermit.conf
%{_mandir}/man5/sepermit.conf.5*
%{_mandir}/man8/pam_selinux*.8*
%{_mandir}/man8/pam_sepermit.8*
%dir /var/run/sepermit
%endif

%files pam_userdb
%defattr(644,root,root,755)
%doc modules/pam_userdb/README
%attr(755,root,root) /%{_lib}/security/pam_userdb.so
%{_mandir}/man8/pam_userdb.8*
