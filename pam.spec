Summary:	Pluggable Authentication Modules: modular, incremental authentication
Summary(de):	Einsteckbare Authentifizierungsmodule: modulare, inkrement�re Authentifizierung
Summary(fr):	PAM : Pluggable Authentication Modules: modular, incremental authentication
Summary(pl):	Modularny system autentykacji
Summary(tr):	Mod�ler, art�msal do�rulama birimleri
Name:		pam
Version:	0.71
Release:	2
Copyright:	GPL or BSD
Group:		Base
Source0:	ftp://ftp.pld.org.pl/packages/pam-pld-%{version}.tar.gz
URL:		http://parc.power.net/morgan/Linux-PAM/index.html
BuildRequires:	sp
BuildRequires:	sgml-tools
BuildRequires:	pwdb-devel
BuildRequires:	cracklib-devel
Requires:	cracklib
Requires:	cracklib-dicts
Requires:	pwdb >= 0.54-2
Obsoletes:	pamconfig
Obsoletes:	pam_make
Buildroot:	/tmp/%{name}-%{version}-root

%description
PAM (Pluggable Authentication Modules) is a powerful, flexible, extensible
authentication system which allows the system administrator to configure
authentication services individually for every pam-compliant application
without recompiling any of the applications.

%description -l de
PAM (Pluggable Authentication Modules) ist ein leistungsf�higes, flexibles
und erweiterbares Authentifizierungssystem, mit dem der Systemverwalter
Authentifizierungs-Dienste individuell f�r jede pam-kompatible Anwendung
konfigurieren kann, ohne diese neu kompilieren zu m�ssen.

%description -l fr
PAM (Pluggable Authentication Modules) est un syst�me d'authentification
puissant, souple et extensible permettant � l'administrateur syst�me de
configurer les individuellement les services d'authentification pour chaque
application conforme � PAM, sans recompiler aucune application.

%description -l pl
PAM (Pluggable Authentication Modules) jest silnym i �atwo dostosowywalnym
do potrzeb systemem autentykacji, kt�ry umo�liwia administratorowi
indywidualne konfigurowanie poszczeg�lnych serwis�w, kt�re s� dostosowane i
zlinkowane z bibliotekami PAM bez p�niejszej ich rekompilacji w momencie
zmiany sposobu autentykacji tych�e serwis�w.

%description -l tr
PAM (Pluggable Authentication Modules) sistem y�neticilerinin uygulamalardan
herhangi birini yeniden derlemeksizin b�t�n PAM uyumlu uygulamalar i�in
do�rulama hizmetlerini ayarlamalar�na yard�mc� olan, g�cl�, esnek ve kapsaml�
bir do�rulama sistemidir.

%package devel
Summary:	PAM header files
Summary(pl):	Pliki nag��wkowe i dokumentacja do PAM
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files for developing PAM based applications.

%description devel
Header files for developing PAM based applications.

%description devel -l pl
Pliki nag��wkowe i dokumentacja do PAM.

%package static
Summary:	PAM static libraries
Summary(pl):	Biblioteki statyczne PAM
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
PAM static libraries.

%description static -l pl
Biblioteki statyczne PAM.

%prep
%setup -q -n %{name}-pld-%{version}

%build
%configure \
	--enable-strong-crypto
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}

make install DESTDIR=$RPM_BUILD_ROOT

touch $RPM_BUILD_ROOT/etc/security/blacklist

ln -sf /lib/libpam.so.0 $RPM_BUILD_ROOT%{_libdir}/libpam.so
ln -sf /lib/libpamc.so.0 $RPM_BUILD_ROOT%{_libdir}/libpamc.so
ln -sf /lib/libpam_misc.so.0 $RPM_BUILD_ROOT%{_libdir}/libpam_misc.so

mv $RPM_BUILD_ROOT/lib/lib*.{la,a} $RPM_BUILD_ROOT%{_libdir}/

strip --strip-unneeded $RPM_BUILD_ROOT/lib/lib*.so.*.* \
	$RPM_BUILD_ROOT%{_sbindir}/pwgen_trigram \
	$RPM_BUILD_ROOT/sbin/pwdb_chkpwd \
	$RPM_BUILD_ROOT/sbin/unix_chkpwd \
	$RPM_BUILD_ROOT/lib/security/*.so

# Removed due to chicken-egg problem
#	$RPM_BUILD_ROOT/sbin/pam_tally \

gzip -9fn $RPM_BUILD_ROOT%{_mandir}/man[358]/* Copyright \
	doc/txts/*.txt doc/specs/*.{raw,txt}

rm -f doc/{ps,txts}/{README,*.log}
rm -f doc/{html,txts}/Makefile*

touch $RPM_BUILD_ROOT/etc/security/opasswd

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
%config /etc/security/*.conf
%config /etc/security/consoles
%config /etc/security/trigram*
%config(noreplace) /etc/security/blacklist
%attr(0600,root,root) %config(noreplace) /etc/security/opasswd
%attr(0755,root,root) /lib/lib*.so.*.*
%attr(0755,root,root) /lib/security/*.so
%attr(0755,root,root) /sbin/pam_filter/upperLOWER
%attr(4755,root,root) /sbin/pwdb_chkpwd
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
