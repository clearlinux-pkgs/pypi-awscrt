#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-awscrt
Version  : 0.12.6
Release  : 11
URL      : https://files.pythonhosted.org/packages/6b/5a/2233365de38bee9b1d6e37f2ad18330a8ea0207843653217ff38ddf87527/awscrt-0.12.6.tar.gz
Source0  : https://files.pythonhosted.org/packages/6b/5a/2233365de38bee9b1d6e37f2ad18330a8ea0207843653217ff38ddf87527/awscrt-0.12.6.tar.gz
Summary  : A common runtime for AWS Python projects
Group    : Development/Tools
License  : Apache-2.0 MIT
Requires: pypi-awscrt-filemap = %{version}-%{release}
Requires: pypi-awscrt-lib = %{version}-%{release}
Requires: pypi-awscrt-license = %{version}-%{release}
Requires: pypi-awscrt-python = %{version}-%{release}
Requires: pypi-awscrt-python3 = %{version}-%{release}
BuildRequires : boto3-python
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : pkgconfig(libunwind-generic)
Patch1: 0001-Don-t-use-werror.patch

%description
The perl scripts in this directory are my 'hack' to generate
multiple different assembler formats via the one origional script.

%package filemap
Summary: filemap components for the pypi-awscrt package.
Group: Default

%description filemap
filemap components for the pypi-awscrt package.


%package lib
Summary: lib components for the pypi-awscrt package.
Group: Libraries
Requires: pypi-awscrt-license = %{version}-%{release}
Requires: pypi-awscrt-filemap = %{version}-%{release}

%description lib
lib components for the pypi-awscrt package.


%package license
Summary: license components for the pypi-awscrt package.
Group: Default

%description license
license components for the pypi-awscrt package.


%package python
Summary: python components for the pypi-awscrt package.
Group: Default
Requires: pypi-awscrt-python3 = %{version}-%{release}

%description python
python components for the pypi-awscrt package.


%package python3
Summary: python3 components for the pypi-awscrt package.
Group: Default
Requires: pypi-awscrt-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(awscrt)

%description python3
python3 components for the pypi-awscrt package.


%prep
%setup -q -n awscrt-0.12.6
cd %{_builddir}/awscrt-0.12.6
%patch1 -p1
pushd ..
cp -a awscrt-0.12.6 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656358805
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
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
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-awscrt
cp %{_builddir}/awscrt-0.12.6/LICENSE %{buildroot}/usr/share/package-licenses/pypi-awscrt/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/awscrt-0.12.6/crt/aws-c-auth/LICENSE %{buildroot}/usr/share/package-licenses/pypi-awscrt/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/awscrt-0.12.6/crt/aws-c-auth/NOTICE %{buildroot}/usr/share/package-licenses/pypi-awscrt/f0c158657d79888c4e766cfb01c16e47cbd41ee1
cp %{_builddir}/awscrt-0.12.6/crt/aws-c-cal/LICENSE %{buildroot}/usr/share/package-licenses/pypi-awscrt/57aed0b0f74e63f6b85cce11bce29ba1710b422b
cp %{_builddir}/awscrt-0.12.6/crt/aws-c-common/LICENSE %{buildroot}/usr/share/package-licenses/pypi-awscrt/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/awscrt-0.12.6/crt/aws-c-compression/LICENSE %{buildroot}/usr/share/package-licenses/pypi-awscrt/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/awscrt-0.12.6/crt/aws-c-event-stream/LICENSE %{buildroot}/usr/share/package-licenses/pypi-awscrt/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/awscrt-0.12.6/crt/aws-c-event-stream/NOTICE %{buildroot}/usr/share/package-licenses/pypi-awscrt/900859209a64230c0ebc769371ab73fb1eaf0312
cp %{_builddir}/awscrt-0.12.6/crt/aws-c-http/LICENSE %{buildroot}/usr/share/package-licenses/pypi-awscrt/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/awscrt-0.12.6/crt/aws-c-io/LICENSE %{buildroot}/usr/share/package-licenses/pypi-awscrt/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/awscrt-0.12.6/crt/aws-c-mqtt/LICENSE %{buildroot}/usr/share/package-licenses/pypi-awscrt/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/awscrt-0.12.6/crt/aws-c-mqtt/NOTICE %{buildroot}/usr/share/package-licenses/pypi-awscrt/01d52ece533bea230977c4dfb958f2b51084b839
cp %{_builddir}/awscrt-0.12.6/crt/aws-c-s3/LICENSE %{buildroot}/usr/share/package-licenses/pypi-awscrt/57aed0b0f74e63f6b85cce11bce29ba1710b422b
cp %{_builddir}/awscrt-0.12.6/crt/aws-c-sdkutils/LICENSE %{buildroot}/usr/share/package-licenses/pypi-awscrt/57aed0b0f74e63f6b85cce11bce29ba1710b422b
cp %{_builddir}/awscrt-0.12.6/crt/aws-checksums/LICENSE %{buildroot}/usr/share/package-licenses/pypi-awscrt/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/awscrt-0.12.6/crt/aws-lc/LICENSE %{buildroot}/usr/share/package-licenses/pypi-awscrt/a61a01065ae3a3bbf67bcd6f24d1cea6d410a83d
cp %{_builddir}/awscrt-0.12.6/crt/aws-lc/third_party/fiat/LICENSE %{buildroot}/usr/share/package-licenses/pypi-awscrt/b71c498e7e934dcfb176710d4f42e18b9e86fe85
cp %{_builddir}/awscrt-0.12.6/crt/s2n/LICENSE %{buildroot}/usr/share/package-licenses/pypi-awscrt/d22ee0b5d7dff4c54d798810ccc79e9b5c3b62ea
cp %{_builddir}/awscrt-0.12.6/crt/s2n/pq-crypto/bike_r1/LICENSE %{buildroot}/usr/share/package-licenses/pypi-awscrt/1128f8f91104ba9ef98d37eea6523a888dcfa5de
cp %{_builddir}/awscrt-0.12.6/crt/s2n/pq-crypto/bike_r2/LICENSE %{buildroot}/usr/share/package-licenses/pypi-awscrt/1128f8f91104ba9ef98d37eea6523a888dcfa5de
cp %{_builddir}/awscrt-0.12.6/crt/s2n/pq-crypto/bike_r3/LICENSE %{buildroot}/usr/share/package-licenses/pypi-awscrt/1128f8f91104ba9ef98d37eea6523a888dcfa5de
cp %{_builddir}/awscrt-0.12.6/crt/s2n/pq-crypto/sike_r1/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-awscrt/97c3ec6ae8c55b815274d2dda7f378b27146ad7d
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

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pypi-awscrt

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-awscrt/01d52ece533bea230977c4dfb958f2b51084b839
/usr/share/package-licenses/pypi-awscrt/1128f8f91104ba9ef98d37eea6523a888dcfa5de
/usr/share/package-licenses/pypi-awscrt/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/pypi-awscrt/57aed0b0f74e63f6b85cce11bce29ba1710b422b
/usr/share/package-licenses/pypi-awscrt/900859209a64230c0ebc769371ab73fb1eaf0312
/usr/share/package-licenses/pypi-awscrt/92170cdc034b2ff819323ff670d3b7266c8bffcd
/usr/share/package-licenses/pypi-awscrt/97c3ec6ae8c55b815274d2dda7f378b27146ad7d
/usr/share/package-licenses/pypi-awscrt/a61a01065ae3a3bbf67bcd6f24d1cea6d410a83d
/usr/share/package-licenses/pypi-awscrt/b71c498e7e934dcfb176710d4f42e18b9e86fe85
/usr/share/package-licenses/pypi-awscrt/d22ee0b5d7dff4c54d798810ccc79e9b5c3b62ea
/usr/share/package-licenses/pypi-awscrt/f0c158657d79888c4e766cfb01c16e47cbd41ee1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
