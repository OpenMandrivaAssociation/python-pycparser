%define module pycparser

# Tests need pytest, which is not rebuilt for this Python yet.
%bcond tests 0

Name:		python-%{module}
Version:	3.11
Release:	1
Summary:	C parser in Python
License:	BSD-3-Clause
Group:		Development/Python
URL:		https://github.com/eliben/pycparser
Source0:	https://files.pythonhosted.org/packages/source/p/pycparser/pycparser-%{version}.tar.gz

BuildSystem:	python
BuildArch:		noarch
BuildRequires:	dos2unix
BuildRequires:	pkgconfig(python3)
BuildRequires:  python%{pyver}dist(pip)
BuildRequires:  python%{pyver}dist(setuptools)
BuildRequires:  python%{pyver}dist(wheel)
%if %{with tests}
BuildRequires:	python%{pyver}dist(pytest)
%endif

# Obsolete and replace python-cparser package
%rename python-cparser
# Obsolete python2 packge
Obsoletes: python2-%{module} < %{version}-%{release}

%description
pycparser is a complete parser of the C language, written in
pure Python.

It parses C code into an AST and can serve as a front-end for
C compilers or analysis tools.

%prep -a
dos2unix LICENSE

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
%{python_sitelib}/%{module}-%{version}.dist-info
