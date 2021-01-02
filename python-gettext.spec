%define module	gettext

Name:		python-%{module}
Version:	4.0
Release:	%mkrel 3
Summary:	Python Gettext po to mo file compiler
License:	BSD
Group:		Development/Python
Url:		https://pypi.org/project/python-gettext/
Source0:	https://pypi.io/packages/source/p/python-gettext/%{name}-%{version}.tar.gz
BuildArch:	noarch

%description
This implementation of Gettext for Python includes a Msgfmt class which can be
used to generate compiled mo files from Gettext po files and includes support
for the newer msgctxt keyword.

%package -n	python3-%{module}
Summary:	Python 3 Gettext po to mo file compiler
Group:		Development/Python
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3dist(setuptools)
%{?python_provide:%python_provide python3-%{module}}

%description -n	python3-%{module}
This implementation of Gettext for Python 3 includes a Msgfmt class which can be
used to generate compiled mo files from Gettext po files and includes support
for the newer msgctxt keyword.

%prep
%setup -q
%autopatch -p1

# Remove bundled egg-info
rm -rf python_gettext.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{module}
%doc CHANGES.rst README.rst
%license LICENSE.rst
%{python3_sitelib}/pythongettext/
%{python3_sitelib}/python_gettext-%{version}-py%{python3_version}.egg-info/
