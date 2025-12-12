%define module	gettext

Name:		python-%{module}
Version:	5.0
Release:	2
Summary:	Python Gettext po to mo file compiler
License:	BSD
Group:		Development/Python
Url:		https://pypi.org/project/python-gettext/
Source0:	https://pypi.io/packages/source/p/python-gettext/%{name}-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildSystem:	python

%description
This implementation of Gettext for Python includes a Msgfmt class which can be
used to generate compiled mo files from Gettext po files and includes support
for the newer msgctxt keyword.

%files
%doc CHANGES.rst README.rst
%license LICENSE.rst
%{python_sitelib}/pythongettext/
%{python_sitelib}/python_gettext-%{version}-py%{python_version}.egg-info/
