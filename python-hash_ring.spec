%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           python3-hash_ring
Version:        1.3.1
Release:        1%{?dist}
Summary:        Python implementation of consistent hashing

Group:          Development/Languages
License:        BSD
URL:            http://pypi.python.org/pypi/hash_ring
Source0:        http://pypi.python.org/packages/source/h/hash_ring/hash_ring-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python3-memcached

%description
hash_ring implements consistent hashing that can be used when the number of
server nodes can increase or decrease. Consistent hashing is a scheme that
provides a hash table functionality in a way that the adding or removing of one
slot does not significantly change the mapping of keys to slots.

%prep
%setup -q -n hash_ring-%{version}
# Remove bootstrap for setuptools which is provided in BuildRequires
sed -i '/^import\ ez_setup$/,+1 d' setup.py

%build
%{__python3} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc PKG-INFO
%{python3_sitelib}/hash_ring/
%{python3_sitelib}/hash_ring-%{version}-*.egg-info

%changelog
* Fri Jul 02 2021 Tim Shelton <tshelton@hawkdefense.com> - 1.3.1-1
- Migrated to python3, since py2 is dead to me

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Apr 11 2009 Silas Sewell <silas at sewell ch> - 1.2-2
- Fix license
- Make files section more explicit

* Fri Apr 10 2009 Silas Sewell <silas at sewell ch> - 1.2-1
- Initial package
