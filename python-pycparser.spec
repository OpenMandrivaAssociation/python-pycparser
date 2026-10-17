%define module pycparser

# Tests need pytest, which is not rebuilt for this Python yet.
%bcond tests 0

Name:		python-%{module}
Version:	3.11
Release:	2
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

# Obsolete python2 packge
Obsoletes: python2-%{module} < %{version}-%{release}

# python-cparser 2.23 is still the newest package of that name and
# requires Python 3.14. python-pycparser and python-cparser are one
# git repository, so the replacement is built here. 3.11-1 obsoletes
# python-cparser < 3.11-1; this subpackage is 3.11-2 and is not
# removed by that obsolete. It ships no Python modules.
%package -n python-cparser
Summary:	Transitional package replaced by python-pycparser
Group:		Development/Python
Requires:	python-%{module} = %{EVRD}

%description
pycparser is a complete parser of the C language, written in
pure Python.

It parses C code into an AST and can serve as a front-end for
C compilers or analysis tools.

%description -n python-cparser
python-cparser has been replaced by python-pycparser.
This package contains no Python modules. It exists so the
Python 3.14 build is no longer the newest version.

%prep -a
dos2unix LICENSE

%install -a
mkdir -p %{buildroot}%{_datadir}/doc/python-cparser
cat > %{buildroot}%{_datadir}/doc/python-cparser/README << 'EOF'
python-cparser has been replaced by python-pycparser.
EOF

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

%files -n python-cparser
%{_datadir}/doc/python-cparser/README
