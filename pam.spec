Summary:	Pluggable Authentication Modules: modular, incremental authentication
Summary(de):	Einsteckbare Authentifizierungsmodule: modulare, inkrementäre Authentifizierung
Summary(fr):	PAM : Pluggable Authentication Modules: modular, incremental authentication
Summary(pl):	Modularny system autentypacji
Summary(tr):	Modüler, artýmsal doðrulama birimleri
Name:		pam
Version:	0.66
Release:	27
Copyright:	GPL or BSD
Group:		Base
%define		date	19990614
Source0:	ftp://ftp.pld.org.pl/packages/pam-pld-%{version}.%{date}.tar.bz2
URL:		http://parc.power.net/morgan/Linux-PAM/index.html
BuildPrereq:	/usr/bin/nsgmls
BuildPrereq:	pwdb-devel
BuildPrereq:	cracklib-devel
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
PAM (Pluggable Authentication Modules) ist ein leistungsfähiges, flexibles
und erweiterbares Authentifizierungssystem, mit dem der Systemverwalter
Authentifizierungs-Dienste individuell für jede pam-kompatible Anwendung
konfigurieren kann, ohne diese neu kompilieren zu müssen.

%description -l fr
PAM (Pluggable Authentication Modules) est un systéme d'authentification
puissant, souple et extensible permettant à l'administrateur système de
configurer les individuellement les services d'authentification pour chaque
application conforme à PAM, sans recompiler aucune application.

%description -l pl
PAM (Pluggable Authentication Modules) jest silnym i ³atwo dostosowywalnym
do potrzeb systemem autentykacji, który umo¿liwia administratorowi
indywidualne konfigurowanie poszczególnych serwisów, które s± dostosowane i
zlinkowane z bibliotekami PAM bez pó¼niejszej ich rekompilacji w momencie
zmiany sposobu autentykacji tych¿e serwisów.

%description -l tr
PAM (Pluggable Authentication Modules) sistem yöneticilerinin uygulamalardan
herhangi birini yeniden derlemeksizin bütün PAM uyumlu uygulamalar için
doðrulama hizmetlerini ayarlamalarýna yardýmcý olan, güclü, esnek ve kapsamlý
bir doðrulama sistemidir.

%package devel
Summary:	PAM header files
Summary(pl):	Pliki nag³ówkowe i dokumentacja do PAM
Group:		Development/Libraries
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
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
PAM static libraries.

%description static -l pl
Biblioteki statyczne PAM.

%prep
%setup -q -n pam

ln -sf defs/linux-pld.defs default.defs
ln -sf libpam/include include

%build
touch .freezemake
make
make -C doc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/pam.d,lib/security} \
	$RPM_BUILD_ROOT{%{_includedir}/security,%{_libdir},%{_mandir}/man{3,8}}

make install FAKEROOT=$RPM_BUILD_ROOT

install conf/other.pamd $RPM_BUILD_ROOT/etc/pam.d/other

install doc/man/pam.8 $RPM_BUILD_ROOT%{_mandir}/man8
install doc/man/*.3 $RPM_BUILD_ROOT%{_mandir}/man3
chmod u+w $RPM_BUILD_ROOT%{_mandir}/man3/*
echo ".so pam.8" > $RPM_BUILD_ROOT%{_mandir}/man8/pam.conf.8
echo ".so pam.8" > $RPM_BUILD_ROOT%{_mandir}/man8/pam.d.8
echo ".so pam_start.3" > $RPM_BUILD_ROOT%{_mandir}/man3/pam_end.3
echo ".so pam_open_session.3" > $RPM_BUILD_ROOT%{_mandir}/man3/pam_close_session.3

# make sure the modules built...
[ -f $RPM_BUILD_ROOT/lib/security/pam_deny.so ] || {
	echo "You have LITTLE or NOTHING in your /lib/security directory:"
	echo $RPM_BUILD_ROOT/lib/security/*
	echo ""
	echo "Fix it before you install this package, while you still can!"
	exit 1
}

strip --strip-debug $RPM_BUILD_ROOT/lib/lib*.so.*.* \
	$RPM_BUILD_ROOT/sbin/pwdb_chkpwd \
	$RPM_BUILD_ROOT/sbin/unix_chkpwd \
	$RPM_BUILD_ROOT/lib/security/*.so

ln -sf /lib/libpam.so.0 $RPM_BUILD_ROOT%{_libdir}/libpam.so
ln -sf /lib/libpam_misc.so.0 $RPM_BUILD_ROOT%{_libdir}/libpam_misc.so

mv $RPM_BUILD_ROOT/lib/lib*.a $RPM_BUILD_ROOT%{_libdir}

gzip -9fn $RPM_BUILD_ROOT%{_mandir}/man[358]/* Copyright \
	doc/txts/*.txt doc/specs/*.{raw,txt}

rm -f doc/{ps,txts}/{README,*.log}

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
%attr(0600,root,root) %config(noreplace) /etc/security/opasswd
%attr(0755,root,root) /lib/lib*.so.*.*
%attr(0755,root,root) /lib/security/*.so
%attr(0755,root,root) /sbin/pam_filter/upperLOWER
%attr(4755,root,root) /sbin/pwdb_chkpwd
%attr(4755,root,root) /sbin/unix_chkpwd
/sbin/pam_pwdb_helper
%{_mandir}/man5/*
%{_mandir}/man8/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/security
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%changelog
* Thu Jun  3 1999 Jan Rêkorajski <baggins@pld.org.pl>
  [0.66-24]
- added pam_console module - stripped version

* Thu May 27 1999 Jan Rêkorajski <baggins@hunter.mimuw.edu.pl>
  [0.66-21]
- spec cleanup

* Fri May 14 1999 Jan Rêkorajski <baggins@hunter.mimuw.edu.pl>
  [0.66-20]
- added unix_chkpwd and pam_pwdb_helper symlink

* Thu May 13 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.66-19]
- initial version which bases on on pam from RedHat.
