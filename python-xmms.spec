%define		module	xmms

Summary:	Python bindings for XMMS
Summary(pl):	Dowi±zania do XMMS dla Pythona
Name:		python-%{module}
Version:	2.04
Release:	0.1
License:	GPL
Group:		Development/Languages/Python
Source0:	http://people.via.ecp.fr/~flo/2002/PyXMMS/dist/pyxmms-%{version}.tar.bz2
# Source0-md5:	841cf6ae30d219f5509063f7008f0109
URL:		http://people.via.ecp.fr/~flo/
BuildRequires:	pydoc
BuildRequires:	xmms-devel
%pyrequires_eq	python-libs
Requires:	xmms
Obsoletes:	python-pyxmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is PyXMMS, a Python interface to XMMS (the X MultiMedia System),
an audio (and video) player running on Unix platforms.

PyXMMS is a set of Python bindings for all the xmms_remote_* functions
accessible through the libxmms library (which comes with XMMS), plus a
few useful higher-level functions.

%description -l pl
Jest to interfejs Pythona do XMMS-a - odtwarzacza multimediów na
systemach uniksowych.

PyXMMS to dowi±zania Pythona do wszystkich funkcji z serii
xmms_remote_* dostêpnych poprzez bibliotekê libxmms, jak równie¿
kilku przydatnych funkcji wysokiego poziomu.

%prep
%setup -q -n pyxmms-%{version}
cat << EOF > setup.cfg
[sdist]
formats=bztar,gztar,zip
[bdist]
formats=bztar,gztar,zip
[install]
prefix=/usr
EOF

%build
python setup.py build
python build-documentation.py

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README NEWS doc/*.html
%dir %{py_sitedir}/%{module}
%attr(755,root,root) %{py_sitedir}/%{module}/*.so
%{py_sitedir}/%{module}/*.py[co]
