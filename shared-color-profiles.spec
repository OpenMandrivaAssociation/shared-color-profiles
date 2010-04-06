Summary: Color profiles to be used in color management aware applications
Name: shared-color-profiles
Version: 0.1.1
Release: %mkrel 2
URL: http://github.com/hughsie/shared-color-profiles
Source0: http://people.freedesktop.org/~hughsient/releases/%{name}-%{version}.tar.gz
License: GPLv2+ and Public Domain
Group: System/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

%description 
The shared-color-profiles package contains various profiles which are 
useful for programs that are color management aware.

%package extra
Summary: More profiles for color management that are less commonly used
Requires: %{name} >= %{version}-%{release}
Group: System/Libraries	

%description extra
More color profiles for color management that are less commonly used.
This may be useful for CMYK soft-proofing or for extra device support.

%prep
%setup -q

%build
%configure2_5x

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog
%{_datadir}/color/icc/*.ic?
%dir %{_datadir}/shared-color-profiles

# Argyll
%dir %{_datadir}/color/icc/Argyll
%dir %{_datadir}/shared-color-profiles/Argyll
%{_datadir}/shared-color-profiles/Argyll/*

# common colorspaces
%{_datadir}/color/icc/Argyll/ClayRGB1998.icm
%{_datadir}/color/icc/Argyll/lab2lab.icm
%{_datadir}/color/icc/Argyll/sRGB.icm

# so we can display at least something in the CMYK dropdown
%{_datadir}/color/icc/Fogra27L.icc

# monitor test profiles
%{_datadir}/color/icc/bluish.icc
%{_datadir}/color/icc/AdobeGammaTest.icm

%files extra
%defattr(-,root,root,-)

# Oyranos
%dir %{_datadir}/color/icc/Oyranos
%{_datadir}/color/icc/Oyranos/FOGRA*.icc
%{_datadir}/color/icc/Oyranos/GRACoL*.icc
%{_datadir}/color/icc/Oyranos/SNAP*.icc
%{_datadir}/color/icc/Oyranos/SWOP*.icc
%{_datadir}/shared-color-profiles/Oyranos/*
