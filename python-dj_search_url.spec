#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Use Search URLs in your Django Haystack Application
Summary(pl.UTF-8):	Korzystanie z URL-i silnika wyszukiwarki w aplikacji Django Haystack
Name:		python-dj_search_url
Version:	0.1
Release:	2
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/dj-search-url/
Source0:	https://files.pythonhosted.org/packages/source/d/dj-search-url/dj-search-url-%{version}.tar.gz
# Source0-md5:	6b38916aae4905fd1ecd53c505b26d55
URL:		https://pypi.org/project/dj-search-url/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module allows to utilize the 12factor inspired SEARCH_URL
environment variable to configure Django Haystack application.

%description -l pl.UTF-8
Ten moduł pozwala na konfigurowanie aplikacji Django Haystack przy
użyciu zmiennej środowiskowej SEARCH_URL, zainspirowanej przez
12factor.

%package -n python3-dj_search_url
Summary:	Use Search URLs in your Django Haystack Application
Summary(pl.UTF-8):	Korzystanie z URL-i silnika wyszukiwarki w aplikacji Django Haystack
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-dj_search_url
This module allows to utilize the 12factor inspired SEARCH_URL
environment variable to configure Django Haystack application.

%description -n python3-dj_search_url -l pl.UTF-8
Ten moduł pozwala na konfigurowanie aplikacji Django Haystack przy
użyciu zmiennej środowiskowej SEARCH_URL, zainspirowanej przez
12factor.

%prep
%setup -q -n dj-search-url-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py_sitescriptdir}/dj_search_url.py[co]
%{py_sitescriptdir}/dj_search_url-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-dj_search_url
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/dj_search_url.py
%{py3_sitescriptdir}/__pycache__/dj_search_url.cpython-*.py[co]
%{py3_sitescriptdir}/dj_search_url-%{version}-py*.egg-info
%endif
