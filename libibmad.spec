#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libibmad
Version  : 1.3.12
Release  : 1
URL      : https://www.openfabrics.org/downloads/management/libibmad-1.3.12.tar.gz
Source0  : https://www.openfabrics.org/downloads/management/libibmad-1.3.12.tar.gz
Summary  : OpenFabrics Alliance InfiniBand MAD library
Group    : Development/Tools
License  : BSD-2-Clause GPL-2.0
Requires: libibmad-lib
BuildRequires : libibumad-dev

%description
libibmad provides low layer IB functions for use by the IB diagnostic
and management programs. These include MAD, SA, SMP, and other basic
IB functions.

%package dev
Summary: dev components for the libibmad package.
Group: Development
Requires: libibmad-lib
Provides: libibmad-devel

%description dev
dev components for the libibmad package.


%package lib
Summary: lib components for the libibmad package.
Group: Libraries

%description lib
lib components for the libibmad package.


%prep
%setup -q -n libibmad-1.3.12

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/infiniband/mad.h
/usr/include/infiniband/mad_osd.h
/usr/lib64/*.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
