Summary:	Pluggable Authentication Modules: modular authentication
Summary(de):	Einsteckbare Authentifizierungsmodule
Summary(fr):	PAM : Pluggable Authentication Modules: modular authentication
Summary(pl):	Pluggable Authentication Modules: modu³y autentykacji 
Summary(tr):	Modüler, artýmsal doðrulama birimleri
Name:		pam
Version:	0.66
Release:	5d
Copyright:	GPL or BSD
Group:		Libraries
Group(pl):	Biblioteki
########	ftp://linux.kernel.org/linux/libs/pam/pre/
Source0:	Linux-PAM-0.66.tar.bz2
Source1:	other.pamd
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-defs.patch
Patch2:		%{name}-filter.patch
Patch3:		%{name}-group.patch
Patch4:		%{name}-lastlog.patch
Patch5:		%{name}-libpam.patch
Patch6:		%{name}-limits.patch
Patch7:		%{name}-mail.patch
Patch8:		%{name}-pwdb.patch
Patch9:		%{name}-radius.patch
Patch10:	%{name}-rhosts.patch
Patch11:	%{name}-sgml.patch
Patch12:	%{name}-unix.patch
Patch13:	%{name}-wheel.patch
Patch14:	%{name}-faillog.patch
Patch15:	%{name}-umask.patch
Patch16:	%{name}-deflimit.patch
Patch17:	%{name}-priority.patch
Buildroot:	/tmp/%{name}-%{version}-root
Url:		http://parc.power.net/morgan/Linux-PAM/index.html
Prereq:		/sbin/ldconfig
Requires:	cracklib
Requires:	cracklib-dicts
Requires:	pwdb 

%description
PAM (Pluggable Authentication Modules) is a powerful, flexible,
extensible authentication system which allows the system administrator
to configure authentication services individually for every pam-compliant
application without recompiling any of the applications.

%description -l pl 
PAM (Pluggable Authentication Modules) s± doskona³ym systemem autentykacji
pozwalaj±cym administratorowi systemu na skonfigurowanie dowolnego serwisu
(kompilowanego ze wsparciem dla PAM), jak równie¿ okre¶lnie jakie osoby mog±
z nich korzystaæ. Pakiet ten zawiera podstawowe modu³y autentykacji dla 
twojego Linuxa i nigdy nie powinien byæ odinstalowany.

%description -l de
PAM (Pluggable Authentication Modules) ist ein leistungsfähiges, flexibles
und erweiterbares Authentifizierungssystem, mit dem der Systemverwalter
Authentifizierungs-Dienste individuell für jede pam-kompatible
Anwendung konfigurieren kann, ohne diese neu kompilieren zu müssen.

%description -l fr
PAM (Pluggable Authentication Modules) est un systéme d'authentification
puissant, souple et extensible permettant à l'administrateur système de
configurer les individuellement les services d'authentification pour
chaque application conforme à PAM, sans recompiler aucune application.

%description -l tr
PAM (Pluggable Authentication Modules) sistem yöneticilerinin uygulamalardan
herhangi birini yeniden derlemeksizin bütün PAM uyumlu uygulamalar için
doðrulama hizmetlerini ayarlamalarýna yardýmcý olan, güclü, esnek ve kapsamlý
bir doðrulama sistemidir.

%package	devel
Summary:	pam headers and static library
Summary(pl):	Pliki nag³ówkowe i biblioteka statyczna PAM
Group:		Libraries
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description devel
PAM headers and static library for developers.

%description -l pl devel
Pliki nag³ówkowe i biblioteka statyczna PAM.

%prep
%setup -q -n Linux-PAM
%patch0  -p1
%patch1  -p1
%patch2  -p1
%patch3  -p1
%patch4  -p1
%patch5  -p1
%patch6  -p1
%patch7  -p1
%patch8  -p1
%patch9  -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1

%build
touch .freezemake
ln -sf defs/linux-pld.defs default.defs
ln -sf libpam/include include

make OPTIMIZE="$RPM_OPT_FLAGS -DWITH_PRIORITY"

(cd doc; make)

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/{/usr/include/security,lib/security}
make install FAKEROOT=$RPM_BUILD_ROOT 

install -d $RPM_BUILD_ROOT/{etc/pam.d,usr/man/{man3,man8}}

install %{SOURCE1} $RPM_BUILD_ROOT/etc/pam.d/other

install doc/man/pam.8	$RPM_BUILD_ROOT/usr/man/man8
install doc/man/*.3	$RPM_BUILD_ROOT/usr/man/man3

echo .so pam.8 > $RPM_BUILD_ROOT/usr/man/man8/pam.conf.8
echo .so pam.8 > $RPM_BUILD_ROOT/usr/man/man8/pam.d.8

gzip -9fn $RPM_BUILD_ROOT/usr/man/man[38]/* 
bzip2 -9 doc/ps/*.ps doc/txts/*.txt doc/specs/rfc86.0.txt

strip $RPM_BUILD_ROOT/lib/*.so.*.*
chmod 755 $RPM_BUILD_ROOT/lib/*.so.*

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc doc/html doc/ps/*.ps.bz2 doc/txts/*.txt.bz2
%doc doc/specs/rfc86.0.txt.bz2

%attr(750,root,root) %dir /etc/pam.d
%attr(640,root,root) %config %verify(not size mtime md5) /etc/pam.d/other

%attr(755,root,root) /lib/*.so.*

%dir /sbin/pam_filter
%attr(755,root,root) /sbin/pam_filter/*

%attr(755,root,root) /sbin/pwdb_chkpwd
%attr(755,root,root) /lib/security/*

%attr(750,root,root) %dir /etc/security
%attr(640,root,root) %config %verify(not size mtime md5) /etc/security/*.conf
%attr(644,root, man) /usr/man/man[38]/*

%files devel
%defattr(644,root,root,755)

%attr(755,root,root) /lib/*.so

/lib/*.a

%dir /usr/include/security
/usr/include/security/*

%changelog
* Sun Feb 14 1999 Marcin Korzonek <mkorz@shadow.eu.org>
  [0.66-5d]
- added pam-priority patch (setting priority for user processes 
  if build with -DWITH_PRIORITY flag)

* Tue Feb 02 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [0.66-2d]
- added default limits for users,
  by Robert Mi³kowski <milek@rudy.mif.pg.gda.pl>
- added pam-faillog.patch,
  by Micha³ Zalewski <lcamtuf@dione.ids.pl>
- set default limits (pam-deflimits.patch).

* Mon Jan 04 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [0.66-1d]
- updated to version 0.66,
- added man pages,
- added more documentations,
- cosmetic changes ;)

* Wed Dec 30 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [0.65-3d]
- added patch against pam_tally.c. 

* Mon Oct 19 1998 Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
  [0.65-2d]
- removed 2> from make but added Linux-PAM-0.65.cast-ldconfig patch
- corrected making of documentation
- removed ps and txt from documentation

* Tue Oct 06 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [0.65-1d]
- translation modified for pl,
- fixed files permissions,
- macro %%{name} in Source & Patch,
- buildroot moved to /var/tmp/%{name}-%{version}-%{release}-root,
- added devel subpackage,
- build from root's account,
- minor modifications of the spec file.

* Mon Jun 15 1998 Marcin Korzonek <mkorz@shadow.eu.org>
  [0.65-1]
- updated to 0.65
- build against glibc 2.1.

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
