#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
#
%include	/usr/lib/rpm/macros.perl
Summary:	OpenSync Plugin for Java Enterprise System Calendar
Name:		libopensync-plugin-jescs
Version:	0.22
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://www.opensync.org/attachment/wiki/download/%{name}-%{version}.tar.bz2?format=raw
# Source0-md5:	f52fff134553f63d40194cdb9cef39e7
URL:		http://www.opensync.org/
BuildRequires:	libopensync-devel >= %{version}
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps}
BuildRequires:	perl-libwww
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenSync Plugin for Java Enterprise System Calendar.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%{_libdir}/wcaptool
%attr(755,root,root) %{_libdir}/opensync/plugins/*.so
%{_libdir}/opensync/plugins/*.la
%{_datadir}/opensync/defaults/*
