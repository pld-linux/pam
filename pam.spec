Summary:	Pluggable Authentication Modules: modular, incremental authentication
Summary(de):	Einsteckbare Authentifizierungsmodule: modulare, inkrementäre Authentifizierung
Summary(fr):	PAM : Pluggable Authentication Modules: modular, incremental authentication
Summary(pl):	Modularny system autentypacji
Summary(tr):	Modüler, artýmsal doðrulama birimleri
Name:		pam
Version:	0.66
Release:	13
Copyright:	GPL or BSD
Group:		Base
Source0:	ftp://linux.kernel.org/linux/libs/pam/pre/Linux-PAM-%{version}.tar.bz2
Source1:	other.pamd
Source2:	ftp://sysadm.dntis.ro/pub/devel/pam/pam_make-0.1.tar.gz
%define		date 990420
Source3:	ftp://hunter.mimuw.edu.pl/pub/users/baggins/pam_unix-%{date}.tar.gz
Source4:	ftp://hunter.mimuw.edu.pl/pub/users/baggins/pam_homedir-0.2.tar.gz
Source5:	ftp://ftp.debian.org/pub/debian/dists/unstable/main/source/admin/libpam-motd_0.1.tar.gz
Patch0:		Linux-PAM-Makefile.patch
Patch1:		Linux-PAM-defs.patch
Patch2:		Linux-PAM-deflimit.patch
Patch3:		Linux-PAM-prompt.patch
Patch4:		Linux-PAM-pwdb.patch
Patch5:		Linux-PAM-libpwdb.patch
Patch6:		Linux-PAM-glibc.patch
Patch7:		Linux-PAM-sgml.patch
Patch8:		Linux-PAM-priority.patch
Patch9:		Linux-PAM-tally-shadow_faillog.patch
Patch10:	Linux-PAM-tally-new_options.patch
Patch11:	Linux-PAM-tally-add_time.patch
Patch12:	Linux-PAM-tally-rhost_and_time.patch
Patch13:	Linux-PAM-tally-fstat.patch
Patch14:	Linux-PAM-Maildir.patch
Patch15:	Linux-PAM-pam_make.patch
Patch16:	Linux-PAM-cleanup.patch
Patch17:	Linux-PAM-motd.patch
Patch18:	Linux-PAM-stringh.patch
Patch19:	Linux-PAM-crypt16.patch
Patch20:	Linux-PAM-remember.patch
URL:		http://parc.power.net/morgan/Linux-PAM/index.html
BuildPrereq:	/usr/bin/nsgmls
BuildPrereq:	pwdb-devel
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
%setup -q -n Linux-PAM
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
tar zxf %{SOURCE2} -C modules/
%patch15 -p1
%patch16 -p1
rm -rf modules/pam_unix
tar zxf %{SOURCE3} -C modules/
tar zxf %{SOURCE4} -C modules/
tar zxf %{SOURCE5} -C modules/
mv modules/libpam-motd-0.1 modules/pam_motd
%patch17 -p1
%patch18 -p1
# If you need pam_pwdb to understand Ultrix passwords, uncoment this
%patch19 -p1
%patch20 -p1

ln -sf defs/linux-pld.defs default.defs
ln -sf libpam/include include

%build
touch .freezemake
make
make -C doc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/pam.d,lib/security,usr/{include/security,lib,man/man{3,8}}}

make install FAKEROOT=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/pam.d/other

install doc/man/pam.8 $RPM_BUILD_ROOT/usr/man/man8
install doc/man/*.3 $RPM_BUILD_ROOT/usr/man/man3
chmod u+w $RPM_BUILD_ROOT/usr/man/man3/*
echo ".so pam.8" > $RPM_BUILD_ROOT/usr/man/man8/pam.conf.8
echo ".so pam.8" > $RPM_BUILD_ROOT/usr/man/man8/pam.d.8
echo ".so pam_start.3" > $RPM_BUILD_ROOT/usr/man/man3/pam_end.3
echo ".so pam_open_session.3" > $RPM_BUILD_ROOT/usr/man/man3/pam_close_session.3

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
	$RPM_BUILD_ROOT/lib/security/*.so

ln -sf ../../lib/libpam.so.0 $RPM_BUILD_ROOT/usr/lib/libpam.so
ln -sf ../../lib/libpam_misc.so.0 $RPM_BUILD_ROOT/usr/lib/libpam_misc.so

mv $RPM_BUILD_ROOT/lib/lib*.a $RPM_BUILD_ROOT/usr/lib/

gzip -9fn $RPM_BUILD_ROOT/usr/man/man[38]/* Copyright \
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
%config /etc/pam.d/other
%config /etc/security/*.conf
%attr(0600,root,root) %config(noreplace) /etc/security/opasswd
%attr(0755,root,root) /lib/lib*.so.*.*
%attr(0755,root,root) /lib/security/*.so
%attr(0755,root,root) /sbin/pam_filter/upperLOWER
%attr(4755,root,root) /sbin/pwdb_chkpwd
/usr/man/man8/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) /usr/lib/lib*.so
/usr/include/security
/usr/man/man3/*

%files static
%defattr(644,root,root,755)
/usr/lib/lib*.a

%changelog
* Tue Apr 27 1999 Jan Rêkorajski <baggins@hunter.mimuw.edu.pl>
  [0.66-13]
- fix for remember patch, cracklib needed -lcrypt

* Tue Apr 23 1999 Jan Rêkorajski <baggins@hunter.mimuw.edu.pl>
  [0.66-12]
- new version of pam_unix modules - nasty BUG FIXED!
- added remember patch. Ever wondered how to stop lusers from having
  two passwords for a lifetime? Just add remember=N to pam_pwdb or
  pam_unix_passwd and your system will remember last N passwords for
  each user.
- uncommented crypt16 patch, if you want PAM to understand crypt16
  passwords add a crypt16 option to pam_pwdb.
- fixed crypt16 patch for pam_pwdb - now it really works, you need to
  add "crypt16" option in auth line with pam_pwdb

* Wed Apr 21 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.66-11]
- recompiles on new rpm.

* Fri Apr  9 1999 Jan Rêkorajski <baggins@hunter.mimuw.edu.pl>
  [0.66-10]
- pam_unix minor update (now understands Ultrix crypt16() passwords)
- added pam_motd module from Debian distribution
- added pam_homedir by me (based on pam_mkhomedir from Debian)
- minor spec cleanup
- added stringh patch, it fixes wrong include directives in
  tally and securetty modules
- crypt16 patch, it makes pam_pwdb understand Ultrix crypt16()
  passwords. It is not applied, added only because somebody may
  really need this - like me ;).

* Wed Mar 31 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.66-9]
- lib*.so links moved to /usr/lib,
- removed ps %doc.
 
* Sat Mar  21 1999 Jan Rêkorajski <baggins@hunter.mimuw.edu.pl>
  [0.66-3]
- still more fixes in pam_unix
- merged with RPM from PLD devel by Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
- merged -noansi, -nopedantic, -dirs and -shlib patches into -Makefile.patch
- merged -makefile, -rhlock and pwdb patches and split pam_pwdb changes
  and misc. Makefile -lpwdb changes from this patch
- updated glibc patch to handle glibc 2.1
- added deflimit patch by Robert Mi³kowski <milek@rudy.mif.pg.gda.pl>
- added defs/linux-pld.defs
- added pam-priority patch (setting priority for user processes
  if build with -DWITH_PRIORITY flag) by Marcin Korzonek <mkorz@shadow.eu.org>
- removed bothconfs and strerror patches

* Sat Jan  31 1999 Jan Rêkorajski <baggins@hunter.mimuw.edu.pl>
  [0.66-2]
- more fixes in pam_unix
- removed obsolete patches

* Sat Jan  31 1999 Jan Rêkorajski <baggins@hunter.mimuw.edu.pl>
  [0.66-1]
- updated to 0.66
- separated pam_unix modules - I got tired of patching this mess

* Sun Jan 18 1999 Jan Rêkorajski <baggins@hunter.mimuw.edu.pl>
- fixed NIS patch (coredumping passwd is not nice)

* Sun Jan 10 1999 Jan Rêkorajski <baggins@hunter.mimuw.edu.pl>
- added pam_make module
- cleaned up compiles time warnings in modules (-cleanup.patch)

* Sat Jan  9 1999 Jan Rêkorajski <baggins@hunter.mimuw.edu.pl>
  [0.65-4]
- fixed installation and packeging of man pages
- renamed alpha patch to noansi (NIS RPC won't compile with -ansi and -DPOSIX)
- added new patches:
  -- umask fix in pam_unix_passwd
  -- md5 passwords capability for pam_unix - new option "md5"
  -- support for setting passwords via NIS RPC for pam_unix_passswd - new option "nis"
    WARNING! if you set this, pam_unix_passwd will use ONLY NIS RPC for password
              setting. This is meant for NIS workstations.
  -- renamed strict/fascist=true/false option in pam_unix_passwd to simple
     no_strict/no_fasxist if someone wants relaxed passwd checking
  -- Maildir format recognition for pam_mail

* Thu Dec  3 1998 Robert Mi³kowski <milek@rudy.mif.pg.gda.pl>
  [0.65-3]
- added new patches:
  -- failure time logging,
  -- support for fail_line field,
  -- support for fail_locktime field with new option no_lock_time.

* Mon Nov 30 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.65-2]
- added %ifos Linux .. %endif around setting up default.defs,
- added pl translation.

* Mon Nov 30 1998 Robert Mi³kowski <milek@rudy.mif.pg.gda.pl>
- changed format of /var/log/faillog to one from
  shadow-utils,
- added new option "per_user" for pam_tally module.

* Sun Aug 22 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.64-4]
- added -q %setup parameter,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{version} in Source snd %setup,
- fixed %post{un},
- changeded dependences to "Requires: %%{name} = %%{version}" in devel
  subpackage,
- fiew simplification in %build and %install,
- added development manual pages (level 3) to devel,
- added missing %postun with runing ldconfig,
- /sbin/ldconfig is now runed as -p parameter in %post{un},
- fixed makin ps documentation,
- added static and devel subpackages,
- added ignore errors during "make install" (-i switch),
- added striping shared libraries,
- added striping /sbin/pwdb_chkpwd,
- added striping debug info on all modules,
- added "Obsoletes: pamconfig" (now it is not neccessary),
- added %attr and %defattr macros in %files (allow build package from
  non-root account).

* Sat May 23 1998 Jeff Johnson <jbj@redhat.com>
- Partial fix for new sgml syntax.
- Hack to get around failiing sgml2latex.

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Mar 10 1998 Cristian Gafton <gafton@redhat.com>
- updated to 0.64 for security reasons.
- handle correctly the buildroot

* Tue Oct 14 1997 Erik Troan <ewt@redhat.com>
- updated alpha patch

* Fri Oct 04 1997 Cristian Gafton <gafton@redhat.com>
- moved to 0.59preC, spec file cleaned up a little.

* Fri Oct 03 1997 Cristian Gafton <gafton@redhat.com>
- moved to 0.59preB, some attempts to stabilize this thing...
- and finally found THE BUG !

* Wed Oct 01 1997 Michael K. Johnson <johnsonm@redhat.com>
- Moved from .57 to .59, with slightly changed interfaces.
- Use a buildroot to avoid trashing build systems.

* Wed Oct 01 1997 Michael K. Johnson <johnsonm@redhat.com>
- Fixed .rhosts security hole with multi-IP hosts.

* Mon Apr 21 1997 Michael K. Johnson <johnsonm@redhat.com>
- Require a high enough version of pwdb

* Tue Apr 15 1997 Michael K. Johnson <johnsonm@redhat.com>
- Moved from .56 to .57

* Thu Feb 27 1997 Michael K. Johnson <johnsonm@redhat.com>
- Moved from .54 to .56, and from pam.conf to pam.d
