Summary:     Pluggable Authentication Modules: modular, incremental authentication
Summary(de): Einsteckbare Authentifizierungsmodule: modulare, inkrementäre Authentifizierung
Summary(fr): PAM : Pluggable Authentication Modules: modular, incremental authentication
Summary(pl): Modularny system autentypacji
Summary(tr): Modüler, artýmsal doðrulama birimleri
Name:        pam
Version:     0.65
Release:     4
Copyright:   GPL or BSD
Group:       Base
Source:      ftp://linux.kernel.org/linux/libs/pam/pre/Linux-PAM-%{version}.tar.gz
Source1:     other.pamd
Source2:     ftp://sysadm.dntis.ro/pub/devel/pam/pam_make-0.1.tar.gz
Patch1:      Linux-PAM-dirs.patch
Patch2:      Linux-PAM-prompt.patch
Patch3:      Linux-PAM-nopasswd+.patch
Patch4:      Linux-PAM-bothconfs.patch
Patch5:      Linux-PAM-nopedantic.patch
Patch6:      Linux-PAM-rhlock.patch
Patch7:      Linux-PAM-strerror.patch
Patch8:      Linux-PAM-pwdb.patch
Patch9:      Linux-PAM-glibc.patch
Patch10:     Linux-PAM-noansi.patch
Patch11:     Linux-PAM-shlib.patch
Patch12:     Linux-PAM-sgml.patch
Patch13:     Linux-PAM-makefile.patch
Patch14:     Linux-PAM-shadow_faillog.patch
Patch15:     Linux-PAM-new_options.patch
Patch16:     Linux-PAM-add_time.patch
Patch17:     Linux-PAM-rhost_and_time.patch
Patch18:     Linux-PAM-Maildir.patch
Patch19:     Linux-PAM-unix-md5.patch
Patch20:     Linux-PAM-unix-NIS.patch
Patch21:     Linux-PAM-umask.patch
Patch22:     Linux-PAM-pam_make.patch
Patch23:     Linux-PAM-cleanup.patch

URL:         http://parc.power.net/morgan/Linux-PAM/index.html
Requires:    cracklib, cracklib-dicts, pwdb >= 0.54-2
Obsoletes:   pamconfig
Obsoletes:   pam_make
Buildroot:   /tmp/%{name}-%{version}-root

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
Summary:     PAM header files
Summary(pl): Pliki nag³ówkowe i dokumentacja do PAM
Group:       Libraries
Group(pl):   Biblioteki
Requires:    %{name} = %{version}

%description devel
Header files for developing PAM based applications.

%description devel
Header files for developing PAM based applications.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja do PAM.

%package static
Summary:     PAM static libraries
Summary(pl): Biblioteki statyczne PAM
Group:       Libraries
Group(pl):   Biblioteki
Requires:    %{name}-devel = %{version}

%description static
PAM static libraries.

%description static -l pl
Biblioteki statyczne PAM.

%prep
%setup -q -n Linux-PAM-%{version}
%patch1 -p1 -b .dirs
%patch2 -p1 -b .prompt
%patch3 -p1 -b .nopasswd+
%patch4 -p1 -b .bothconfs
%patch5 -p1 -b .nopedantic
%patch6 -p1 -b .rhlock
%patch7 -p1 -b .strerror
%patch8 -p1 -b .pwdb
%patch9 -p1 -b .glibc
%patch10 -p1 -b .noansi
%patch11 -p1 -b .shlib
%patch12 -p1 -b .shml
%patch13 -p1 -b .makefile
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p0
%patch19 -p1
%patch20 -p1
%patch21 -p1
tar zxf %{SOURCE2} -C $RPM_BUILD_DIR/Linux-PAM-%{version}/modules/
%patch22 -p1
%patch23 -p1

%ifos Linux
rm -f default.defs
ln -s defs/redhat.defs default.defs
%endif

%build
touch .freezemake
make

(cd doc ; make; gzip -9 ps/*.ps)

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/pam.d,lib/security,usr/{include/security,lib,man/man{3,8}}}
make -i install FAKEROOT=$RPM_BUILD_ROOT
install ${RPM_SOURCE_DIR}/other.pamd $RPM_BUILD_ROOT/etc/pam.d/other
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

strip $RPM_BUILD_ROOT/lib/lib*.so.*.*
strip --strip-debug $RPM_BUILD_ROOT/lib/security/*.so || :
strip $RPM_BUILD_ROOT/sbin/pwdb_chkpwd
mv $RPM_BUILD_ROOT/lib/lib*.a $RPM_BUILD_ROOT/usr/lib/

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644, root, root, 755)
%doc Copyright doc/{html,ps,txts,specs/rfc86.0.txt}
%dir /etc/pam.d
%config /etc/pam.d/other
%config /etc/security/*
%attr(755 , root, root) /lib/lib*.so.*.*
%dir /sbin/pam_filter
%attr(511 , root, root) /sbin/pam_filter/upperLOWER
%attr(4555, root, root) /sbin/pwdb_chkpwd
%attr(755 , root, root) /lib/security
%attr(644 , root, root) /usr/man/man8/*

%files devel
%defattr(644, root, root, 755)
/lib/lib*.so
/usr/include/security
%attr(644, root, root) /usr/man/man3/*

%files static
%attr(644, root, root) /usr/lib/lib*.a

%changelog
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
