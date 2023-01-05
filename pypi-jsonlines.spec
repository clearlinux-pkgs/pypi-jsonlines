#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-jsonlines
Version  : 3.1.0
Release  : 35
URL      : https://files.pythonhosted.org/packages/2a/c8/efdb87403dae07cf20faf75449eae41898b71d6a8d4ebaf9c80d5be215f5/jsonlines-3.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/2a/c8/efdb87403dae07cf20faf75449eae41898b71d6a8d4ebaf9c80d5be215f5/jsonlines-3.1.0.tar.gz
Summary  : Library with helpers for the jsonlines file format
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-jsonlines-license = %{version}-%{release}
Requires: pypi-jsonlines-python = %{version}-%{release}
Requires: pypi-jsonlines-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(attrs)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
.. image:: https://travis-ci.org/wbolster/jsonlines.svg?branch=master
:target: https://travis-ci.org/wbolster/jsonlines

%package license
Summary: license components for the pypi-jsonlines package.
Group: Default

%description license
license components for the pypi-jsonlines package.


%package python
Summary: python components for the pypi-jsonlines package.
Group: Default
Requires: pypi-jsonlines-python3 = %{version}-%{release}

%description python
python components for the pypi-jsonlines package.


%package python3
Summary: python3 components for the pypi-jsonlines package.
Group: Default
Requires: python3-core
Provides: pypi(jsonlines)
Requires: pypi(attrs)

%description python3
python3 components for the pypi-jsonlines package.


%prep
%setup -q -n jsonlines-3.1.0
cd %{_builddir}/jsonlines-3.1.0
pushd ..
cp -a jsonlines-3.1.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672284734
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-jsonlines
cp %{_builddir}/jsonlines-%{version}/LICENSE.rst %{buildroot}/usr/share/package-licenses/pypi-jsonlines/959c240e9ef9350dfc07d6c941ebe009a859268f || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-jsonlines/959c240e9ef9350dfc07d6c941ebe009a859268f

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
