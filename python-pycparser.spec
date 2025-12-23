%define module pycparser
%bcond tests 1

Name:		python-%{module}
Version:	2.23
Release:	1
Summary:	C parser in Python
License:	BSD-3-Clause
Group:		Development/Python
URL:		https://github.com/eliben/pycparser
Source0:	%{URL}/archive/release_v%{version}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildArch:		noarch
BuildRequires:	dos2unix
BuildRequires:	pkgconfig(python)
BuildRequires:  python%{pyver}dist(pip)
BuildRequires:  python%{pyver}dist(setuptools)
BuildRequires:  python%{pyver}dist(wheel)
%if %{with tests}
BuildRequires:	python%{pyver}dist(pytest)
%endif

Obsoletes: python2-%{module} < %{version}-%{release}

%description
pycparser is a complete parser of the C language, written in
pure Python using the PLY parsing library.

It parses C code into an AST and can serve as a front-end for
C compilers or analysis tools.

%prep
%autosetup -n %{module}-release_v%{version} -p1
dos2unix LICENSE

%build
%py_build

%install
%py_install

%if %{with tests}
%check
export CI=true
export PYTHONPATH=%{buildroot}%{python_sitelib}:%{python_sitelib}
pytest
%endif

%files
%doc README.rst examples/
%license LICENSE
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}*.*-info
