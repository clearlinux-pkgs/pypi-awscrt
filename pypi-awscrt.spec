#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v26
# autospec commit: 99a7985
#
Name     : pypi-awscrt
Version  : 0.27.2
Release  : 21
URL      : https://files.pythonhosted.org/packages/2c/6d/570d1feba08c1006c8f47de3725e87b7b968a875e52a792b74d6598bef08/awscrt-0.27.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/2c/6d/570d1feba08c1006c8f47de3725e87b7b968a875e52a792b74d6598bef08/awscrt-0.27.2.tar.gz
Summary  : A common runtime for AWS Python projects
Group    : Development/Tools
License  : Apache-2.0 MIT
Requires: pypi-awscrt-license = %{version}-%{release}
Requires: pypi-awscrt-python = %{version}-%{release}
Requires: pypi-awscrt-python3 = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : openssl-dev
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
The perl scripts in this directory are my 'hack' to generate
multiple different assembler formats via the one origional script.

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
Requires: python3-core
Provides: pypi(awscrt)

%description python3
python3 components for the pypi-awscrt package.


%prep
%setup -q -n awscrt-0.27.2
cd %{_builddir}/awscrt-0.27.2
pushd ..
cp -a awscrt-0.27.2 buildavx2
popd

%build
## build_prepend content
export AWS_CRT_BUILD_USE_SYSTEM_LIBCRYPTO=1
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1747363371
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

pushd ../buildavx2/
## build_prepend content
export AWS_CRT_BUILD_USE_SYSTEM_LIBCRYPTO=1
## build_prepend end
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-awscrt
cp %{_builddir}/awscrt-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-awscrt/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/awscrt-%{version}/crt/aws-c-auth/LICENSE %{buildroot}/usr/share/package-licenses/pypi-awscrt/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/awscrt-%{version}/crt/aws-c-auth/NOTICE %{buildroot}/usr/share/package-licenses/pypi-awscrt/f0c158657d79888c4e766cfb01c16e47cbd41ee1 || :
cp %{_builddir}/awscrt-%{version}/crt/aws-c-cal/LICENSE %{buildroot}/usr/share/package-licenses/pypi-awscrt/57aed0b0f74e63f6b85cce11bce29ba1710b422b || :
cp %{_builddir}/awscrt-%{version}/crt/aws-c-common/LICENSE %{buildroot}/usr/share/package-licenses/pypi-awscrt/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/awscrt-%{version}/crt/aws-c-compression/LICENSE %{buildroot}/usr/share/package-licenses/pypi-awscrt/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/awscrt-%{version}/crt/aws-c-event-stream/LICENSE %{buildroot}/usr/share/package-licenses/pypi-awscrt/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/awscrt-%{version}/crt/aws-c-event-stream/NOTICE %{buildroot}/usr/share/package-licenses/pypi-awscrt/900859209a64230c0ebc769371ab73fb1eaf0312 || :
cp %{_builddir}/awscrt-%{version}/crt/aws-c-http/LICENSE %{buildroot}/usr/share/package-licenses/pypi-awscrt/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/awscrt-%{version}/crt/aws-c-io/LICENSE %{buildroot}/usr/share/package-licenses/pypi-awscrt/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/awscrt-%{version}/crt/aws-c-mqtt/LICENSE %{buildroot}/usr/share/package-licenses/pypi-awscrt/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/awscrt-%{version}/crt/aws-c-mqtt/NOTICE %{buildroot}/usr/share/package-licenses/pypi-awscrt/01d52ece533bea230977c4dfb958f2b51084b839 || :
cp %{_builddir}/awscrt-%{version}/crt/aws-c-s3/LICENSE %{buildroot}/usr/share/package-licenses/pypi-awscrt/57aed0b0f74e63f6b85cce11bce29ba1710b422b || :
cp %{_builddir}/awscrt-%{version}/crt/aws-c-sdkutils/LICENSE %{buildroot}/usr/share/package-licenses/pypi-awscrt/57aed0b0f74e63f6b85cce11bce29ba1710b422b || :
cp %{_builddir}/awscrt-%{version}/crt/aws-checksums/LICENSE %{buildroot}/usr/share/package-licenses/pypi-awscrt/92170cdc034b2ff819323ff670d3b7266c8bffcd || :
cp %{_builddir}/awscrt-%{version}/crt/aws-lc/LICENSE %{buildroot}/usr/share/package-licenses/pypi-awscrt/2512e9d601ad3766d89605e39d8d4617d44c6e36 || :
cp %{_builddir}/awscrt-%{version}/crt/aws-lc/third_party/fiat/LICENSE %{buildroot}/usr/share/package-licenses/pypi-awscrt/8b3da8b7b055147f8fd69781a7fd1ead8de1fc66 || :
cp %{_builddir}/awscrt-%{version}/crt/s2n/LICENSE %{buildroot}/usr/share/package-licenses/pypi-awscrt/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m installer --destdir=%{buildroot}-v3 dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-awscrt/01d52ece533bea230977c4dfb958f2b51084b839
/usr/share/package-licenses/pypi-awscrt/2512e9d601ad3766d89605e39d8d4617d44c6e36
/usr/share/package-licenses/pypi-awscrt/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/pypi-awscrt/57aed0b0f74e63f6b85cce11bce29ba1710b422b
/usr/share/package-licenses/pypi-awscrt/8b3da8b7b055147f8fd69781a7fd1ead8de1fc66
/usr/share/package-licenses/pypi-awscrt/900859209a64230c0ebc769371ab73fb1eaf0312
/usr/share/package-licenses/pypi-awscrt/92170cdc034b2ff819323ff670d3b7266c8bffcd
/usr/share/package-licenses/pypi-awscrt/f0c158657d79888c4e766cfb01c16e47cbd41ee1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/V3/usr/lib/python3*/*
/usr/lib/python3*/*
