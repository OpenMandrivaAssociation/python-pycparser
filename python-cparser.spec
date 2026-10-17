Name:		python-cparser
Version:	3.11
Release:	2
Summary:	Transitional package replaced by python-pycparser
License:	BSD-3-Clause
Group:		Development/Python
URL:		https://github.com/eliben/pycparser
BuildArch:	noarch
# python-pycparser Obsoletes python-cparser < 3.11-1 and Provides
# the old name at 3.11-1. Stay above that bound so the extra tests
# can still install this package, and ship no Python modules.
Requires:	python-pycparser >= 3.11-1

%description
python-cparser has been replaced by python-pycparser.
This package contains no Python modules. It exists so the
Python 3.14 build is no longer the newest version in the
repository, and so an upgrade pulls in python-pycparser.

%prep
cat > README << 'EOF'
python-cparser has been replaced by python-pycparser.
EOF

%build

%install
mkdir -p %{buildroot}%{_datadir}/doc/%{name}
cp -p README %{buildroot}%{_datadir}/doc/%{name}/README

%files
%{_datadir}/doc/%{name}/README
