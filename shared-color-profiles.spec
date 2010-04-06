Summary: Color profiles to be used in color management aware applications
Name: shared-color-profiles
Version: 0.1.1
Release: %mkrel 1
URL: http://github.com/hughsie/shared-color-profiles
Source0: http://people.freedesktop.org/~hughsient/releases/%{name}-%{version}.tar.gz
License: GPLv2+ and Public Domain
Group: System/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

%description 
The shared-color-profiles package contains various profiles which are 
useful for programs that are color management aware.

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
%{_datadir}/color/icc/Argyll/*.ic?
%dir %{_datadir}/shared-color-profiles/Argyll
%{_datadir}/shared-color-profiles/Argyll/*

# Oyranos
%dir %{_datadir}/color/icc/Oyranos
%{_datadir}/color/icc/Oyranos/*.ic?
%dir %{_datadir}/shared-color-profiles/Oyranos
%{_datadir}/shared-color-profiles/Oyranos/*
