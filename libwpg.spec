Name:           libwpg
Version:        0.1.3
Release:        4.1%{?dist}
Summary:        Library for reading WordPerfect Graphics images

Group:          System Environment/Libraries
License:        GPLv2+
URL:            http://libwpg.sourceforge.net/
Source0:        http://download.sourceforge.net/libwpg/%{name}-%{version}.tar.bz2
Patch0:         libwpg-0.1.3-nodate.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  libwpd-devel >= 0.8
BuildRequires:  doxygen

%description
Libwpg project is a library and to work with graphics in WPG
(WordPerfect Graphics) format. WPG is the format used among others
in Corel sofware, such as WordPerfect and Presentations.


%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package tools
Summary:        Tools to convert WordPerfect Graphics images
Group:          Applications/Multimedia

%description tools
This package contains tools to work with graphics in WPG (WordPerfect
Graphics) format. WPG is the format used among others in Corel sofware,
such as WordPerfect and Presentations.


%prep
%setup -q
%patch0 -p1 -b .nodate


%build
%configure
make %{?_smp_mflags}
sed 's/\r//' -i ChangeLog
find docs/doxygen/html |xargs touch -r docs/doxygen/doxygen.cfg


%install
rm -rf $RPM_BUILD_ROOT
# Documentation is intentionally not installed here,
# it is included as -devel %%doc
make SUBDIRS="" install DESTDIR=$RPM_BUILD_ROOT
make -C src install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING
%{_libdir}/*.so.*


%files devel
%defattr(-,root,root,-)
%doc COPYING docs/doxygen/html
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc


%files tools
%defattr(-,root,root,-)
%doc COPYING
%{_bindir}/*


%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.1.3-4.1
- Rebuilt for RHEL 6

* Tue Jul 28 2009 Lubomir Rintel <lkundrak@v3.sk> - 0.1.3-4
- Fix multilib problem with doxygen documentation (#508940)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 6 2009 Lubomir Rintel <lkundrak@v3.sk> - 0.1.3-1
- Initial packaging
