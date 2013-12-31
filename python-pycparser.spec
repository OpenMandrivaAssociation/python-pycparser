%define	oname	pycparser
%define	module	cparser

Name:		python-%{module}
Version:	2.10
Release:	1
Summary:	C parser in Python
Source0:	http://pypi.python.org/packages/source/p/%{oname}/%{oname}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		https://github.com/eliben/pycparser
BuildArch:	noarch
BuildRequires:  pkgconfig(python)
BuildRequires:  pythonegg(setuptools)



%description
pycparser is a complete parser of the C language, written in
        pure Python using the PLY parsing library.
        It parses C code into an AST and can serve as a front-end for
        C compilers or analysis tools.

%prep
%setup -q -n %{oname}-%{version}
perl -i -pe 's/\r\n/\n/gs' LICENSE

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}



%check
cd tests
python all_tests.py
cd -

%files
%doc CHANGES LICENSE README.rst
%{py_puresitedir}/pycparser/*.py*
%{py_puresitedir}/pycparser/ply/*.py*
%{py_puresitedir}/pycparser*.egg-info
%{py_puresitedir}/pycparser/_c_ast.cfg