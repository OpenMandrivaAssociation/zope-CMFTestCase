%define Product CMFTestCase
%define product cmftestcase
%define name    zope-%{Product}
%define version 0.9.7
%define release %mkrel 1

%define zope_minver     2.7
%define zope_home       %{_prefix}/lib/zope
%define software_home   %{zope_home}/lib/python

Name:       %{name}
Version:    %{version}
Release:    %{release}
Summary:    A test framework for CMF-based applications and products
License:    GPL
Group:      System/Servers
URL:        http://plone.org/products/%{product}
Source:     http://plone.org/products/%{product}/releases/%{version}/%{Product}-%{version}.tar.gz
Requires:   zope >= %{zope_minver}
Requires:   zope-CMF
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
CMFTestCase is a thin layer on top of the ZopeTestCase package. It has
been developed to simplify testing of CMF-based applications and
products.

The CMFTestCase package provides:

- The function 'installProduct' to install a Zope product into the
  test environment.

- The function 'installPackage' to install a Python package registered
  via five:registerPackage into the test environment.  Requires Zope
  2.10.4 or higher.

- The function 'setupCMFSite' to create a CMF portal in the test db.
  Note: 'setupCMFSite' accepts an optional 'products' argument, which
  allows you to specify a list of products that will be added to the
  portal. Product installation is performed via the canonical
  'Extensions.Install.install' function. Since 0.8.2 you can also pass
  an 'extension_profiles' argument to import GS extension profiles.

- The class 'CMFTestCase' of which to derive your test cases.

- The class 'FunctionalTestCase' of which to derive your test cases
  for functional unit testing.

- The classes 'Sandboxed' and 'Functional' to mix-in with your own
  test cases.

- The constants 'portal_name', 'portal_owner', 'default_products',
  'default_base_profile', 'default_extension_profiles',
  'default_user', and 'default_password'.

- The constant 'CMF15' which evaluates to true for CMF 
  versions >= 1.5.

- The constant 'CMF16' which evaluates to true for CMF
  versions >= 1.6.

- The constant 'CMF20' which evaluates to true for CMF
  versions >= 2.0.

- The constant 'CMF21' which evaluates to true for CMF
  versions >= 2.1.

- The module 'utils' which contains all utility functions from the
  ZopeTestCase package.


%prep
%setup -c -q

%build
# Not much, eh? :-)

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}/%{software_home}/Products
%{__cp} -a * %{buildroot}%{software_home}/Products/
rm -rf %{buildroot}%{software_home}/Products/%{product}/debian

%clean
%{__rm} -rf %{buildroot}

%post
if [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
        service zope restart
fi

%postun
if [ -f "%{_prefix}/bin/zopectl" ] && [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
        service zope restart
fi

%files
%defattr(-,root,root)
%{software_home}/Products/*

