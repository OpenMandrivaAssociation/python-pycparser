%define	oname	pycparser
%define	module	cparser

Name:		python-%{module}
Version:	2.10
Release:	3
Summary:	C parser in Python
Source0:	http://pypi.python.org/packages/source/p/%{oname}/%{oname}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		https://github.com/eliben/pycparser
BuildArch:	noarch
BuildRequires:  pkgconfig(python)
BuildRequires:	pkgconfig(python3)
BuildRequires:  pythonegg(setuptools)



%description
pycparser is a complete parser of the C language, written in
        pure Python using the PLY parsing library.
        It parses C code into an AST and can serve as a front-end for
        C compilers or analysis tools.

%package -n python2-%{module}
Summary:	C parser in Python
Group:		Development/Python

%description -n python2-%{module}
pycparser is a complete parser of the C language, written in
        pure Python using the PLY parsing library.
        It parses C code into an AST and can serve as a front-end for
        C compilers or analysis tools.


%prep
%setup -q -n %{oname}-%{version}
perl -i -pe 's/\r\n/\n/gs' LICENSE
cp -a . %{py2dir}
find %{py2dir} -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python2}|'

%build
%{__python} setup.py build

pushd %{py2dir}
%{__python2} setup.py build
popd


%install
%{__python} setup.py install --skip-build --root %{buildroot}

pushd %{py2dir}
%{__python2} setup.py install --skip-build --root %{buildroot}
popd


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

%files -n python2-%{module}
%{py2_puresitedir}/pycparser/*.py*
%{py2_puresitedir}/pycparser/ply/*.py*
%{py2_puresitedir}/pycparser*.egg-info
%{py2_puresitedir}/pycparser/_c_ast.cfg
