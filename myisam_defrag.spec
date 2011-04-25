Name: myisam_defrag
Version: 0.2
Release: 1%{?dist}
Summary: mySQL myisam defragmentation tool, can be used to automate defragmentation of myisam tables.

Group: Applications/System
License: GNU v3
URL: https://github.com/Oneiroi/myisam_defrag
Source0: myisam_defrag-0.2.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

Requires: python,MySQL-python

%description

This tool was created to aid in the automated defragmentation of myisam engine tables, configurations are stored in the myisam_defrag.conf file
it can be used as a standalone run when required app, or setup to run from the crontab

%prep

%setup -q

%build

%install
[[ -d "$RPM_BUILD_ROOT" ]] && rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/myisam_defrag
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man7
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man8

install -D $RPM_BUILD_DIR/%{name}-%{version}/myisam_defrag.py $RPM_BUILD_ROOT%{_bindir}/myisam_defrag.py
install -D $RPM_BUILD_DIR/%{name}-%{version}/myisam_defrag.conf.7 $RPM_BUILD_ROOT%{_mandir}/man7/myisam_defrag.conf.7
install -D $RPM_BUILD_DIR/%{name}-%{version}/myisam_defrag.8 $RPM_BUILD_ROOT%{_mandir}/man8/myisam_defrag.8
install -D $RPM_BUILD_DIR/%{name}-%{version}/myisam_defrag.conf $RPM_BUILD_ROOT%{_sysconfdir}/myisam_defrag.conf

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_bindir}/myisam_defrag.py
%doc %{_mandir}/man7/myisam_defrag.conf.7.gz
%doc %{_mandir}/man8/myisam_defrag.8.gz
%config %{_sysconfdir}/myisam_defrag.conf

%changelog

* Thu Sep 28 2010 David Busby <d.busby@saiweb.co.uk> - 0.2
- Initial verison for packaging, 0.1 was never officialy tagged


