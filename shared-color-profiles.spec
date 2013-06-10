Summary:	Color profiles to be used in color management aware applications
Name:		shared-color-profiles
Version:	0.1.6
Release:	1
URL:		http://github.com/hughsie/shared-color-profiles
Source0:	http://people.freedesktop.org/~hughsient/releases/%{name}-%{version}.tar.xz
License:	GPLv2+ and Public Domain
Group:		System/Libraries
BuildRequires:	argyllcms
BuildRequires:	colord
BuildArch:	noarch

%description 
The shared-color-profiles package contains various profiles which are 
useful for programs that are color management aware.

%package extra
Summary:	More profiles for color management that are less commonly used
Requires:	%{name} >= %{version}-%{release}
Group:		System/Libraries

%description extra
More color profiles for color management that are less commonly used.
This may be useful for CMYK soft-proofing or for extra device support.

%prep
%setup -q

%build
%configure2_5x

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog
%{_datadir}/color/icc/*.ic?
%dir %{_datadir}/shared-color-profiles

# Argyll
#%{_datadir}/shared-color-profiles/Argyll/

# common colorspaces
#%{_datadir}/color/icc/Argyll/

# so we can display at least something in the CMYK dropdown
#%{_datadir}/color/icc/Fogra27L.icc

# monitor test profiles
#%{_datadir}/color/icc/bluish.icc
#%{_datadir}/color/icc/AdobeGammaTest.icm

%files extra
%defattr(-,root,root,-)

# Oysonar
%dir %{_datadir}/color/icc/Oysonar
%{_datadir}/color/icc/Oysonar/*
%{_datadir}/shared-color-profiles/Oysonar/

%_datadir/color/icc/Yamma
%_datadir/%name/Yamma


%changelog
* Wed Nov 09 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.5-1mdv2012.0
+ Revision: 729462
- update to new version 0.1.5

* Thu Jun 16 2011 Götz Waschk <waschk@mandriva.org> 0.1.4-1
+ Revision: 685501
- update to new version 0.1.4

* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1.3-2
+ Revision: 669976
- mass rebuild

* Thu Jan 13 2011 Götz Waschk <waschk@mandriva.org> 0.1.3-1
+ Revision: 630988
- new version
- rename Oyranos to Oysonar

* Thu Nov 11 2010 Götz Waschk <waschk@mandriva.org> 0.1.2-1mdv2011.0
+ Revision: 595982
- new version
- add new data to file list

* Tue Apr 06 2010 Frederic Crozat <fcrozat@mandriva.com> 0.1.1-2mdv2010.1
+ Revision: 532203
- split main package, move uncommon profiles to extra subpackage, to save space on default install (Fedora)

* Tue Apr 06 2010 Frederic Crozat <fcrozat@mandriva.com> 0.1.1-1mdv2010.1
+ Revision: 532111
- Release 0.1.1

* Fri Jan 08 2010 Frederic Crozat <fcrozat@mandriva.com> 0.1.0-1mdv2010.1
+ Revision: 487472
- import shared-color-profiles


