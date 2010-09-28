Name:           myisam_defrag
Version:        0.2 
Release:        1%{?dist}
Summary:        mySQL myisam defragmentation tool, can be used to automate defragmentation of myisam tables.

Group:        	Applications/System 
License:        GNU v3
URL:            http://svn.saiweb.co.uk/branches/myisam_defrag
Source0:        http://svn.saiweb.co.uk/branches/myisam_defrag/tags/0.2/myisam_defrag-0.2.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:       python,MySQL-python

%description

This tool was created to aid in the automated defragmentation of myisam engine tables, configurations are stored in the myisam_defrag.conf file
it can be used as a standalone run when required app, or setup to run from the crontab
%prep
%setup -q


%build

%install
rm -rf $RPM_BUILD_ROOT
cp $RPM_BUILD_ROOT/myisam_defrag %{_bindir}/myisam_defrag
mkdir -p /etc/myisam_defrag
cp $RPM_BUILD_ROOT/myisam_defrag.conf /etc/myisam_defrag/myisam_defrag.conf

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_bindir}/myisam_defrag
%doc %{_mandir}/man7/myisam_defrag.conf.7
%doc %{_mandir}/man8/myisam_defrag.8


%changelog

* Thur Sep 28 2010 David Busby <d.busby@saiweb.co.uk> - 0.2
- Initial verison for packaging
