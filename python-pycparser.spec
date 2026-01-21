%define module pycparser
# release tag conditional added for 3.0 which uses is 3.00 numbering
# which confuses the build versioning.
# Set useoversion conditional to 0 to use regular release version numbering
# leave this set up
%bcond useoversion 1
%define oversion 3.00

%bcond tests 1

Name:		python-%{module}
Version:	3.0
Release:	1
Summary:	C parser in Python
License:	BSD-3-Clause
Group:		Development/Python
URL:		https://github.com/eliben/pycparser
%if %{with useoversion}
Source0:	%{URL}/archive/release_v%{oversion}/%{module}-%{oversion}.tar.gz#/%{name}-%{version}.tar.gz
%else
Source0:	%{URL}/archive/release_v%{version}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
%endif

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

# Obsolete and replace python-cparser package
%rename python-cparser
# Obsolete python2 packge
Obsoletes: python2-%{module} < %{version}-%{release}

%description
pycparser is a complete parser of the C language, written in
pure Python using the PLY parsing library.

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
