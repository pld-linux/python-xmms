%include	/usr/lib/rpm/macros.python

%define		module xmms

Summary:	Python bindings for XMMS
Summary(pl):	Dowiązania do XMMS dla Pythona
Name:		python-%{module}
Version:	2.02
Release:	1
License:	GPL
Group:		Development/Languages/Python
Source0:	http://www.via.ecp.fr/~flo/2002/PyXMMS/dist/pyxmms-%{version}.tar.gz
# Source0-md5:	d3ca937e3763c6432fd71c348cd60598
URL:		http://www.via.ecp.fr/~flo/
BuildRequires:	rpm-pythonprov
BuildRequires:	xmms-devel
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

PyXMMS to dowiązania Pythona do wszystkich funkcji z serii
xmms_remote_* dostępnych poprzez bibliotekę libxmms, jak również
kilku przydatych funkcji wysokiego poziomu.

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

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
    --root=$RPM_BUILD_ROOT \
    --optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README NEWS doc/xmms.html
%dir %{py_sitedir}/%{module}
%attr(755,root,root) %{py_sitedir}/%{module}/*.so
%{py_sitedir}/%{module}/*.py[co]
