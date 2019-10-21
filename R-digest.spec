#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-digest
Version  : 0.6.22
Release  : 81
URL      : https://cran.r-project.org/src/contrib/digest_0.6.22.tar.gz
Source0  : https://cran.r-project.org/src/contrib/digest_0.6.22.tar.gz
Summary  : Create Compact Hash Digests of R Objects
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-digest-lib = %{version}-%{release}
BuildRequires : R-knitr
BuildRequires : R-markdown
BuildRequires : buildreq-R
BuildRequires : util-linux

%description
## digest: Compact hash representations of arbitrary R objects
[![Build Status](https://travis-ci.org/eddelbuettel/digest.svg)](https://travis-ci.org/eddelbuettel/digest)
[![License](http://img.shields.io/badge/license-GPL%20%28%3E=%202%29-brightgreen.svg?style=flat)](http://www.gnu.org/licenses/gpl-2.0.html)
[![CRAN](http://www.r-pkg.org/badges/version/digest)](https://cran.r-project.org/package=digest)
[![Dependencies](https://tinyverse.netlify.com/badge/digest)](https://cran.r-project.org/package=digest)
[![Downloads](http://cranlogs.r-pkg.org/badges/digest?color=brightgreen)](http://www.r-pkg.org/pkg/digest)
[![CRAN use](https://jangorecki.gitlab.io/rdeps/digest/CRAN_usage.svg?sanitize=true)](https://cran.r-project.org/package=digest)
[![CRAN indirect](https://jangorecki.gitlab.io/rdeps/digest/indirect_usage.svg?sanitize=true)](https://cran.r-project.org/package=digest)
[![BioConductor use](https://jangorecki.gitlab.io/rdeps/digest/BioC_usage.svg?sanitize=true)](https://cran.r-project.org/package=digest)
[![Code Coverage](https://img.shields.io/codecov/c/github/eddelbuettel/digest/master.svg)](https://codecov.io/gh/eddelbuettel/digest)

%package lib
Summary: lib components for the R-digest package.
Group: Libraries

%description lib
lib components for the R-digest package.


%prep
%setup -q -c -n digest

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571683960

%install
export SOURCE_DATE_EPOCH=1571683960
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library digest
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library digest
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library digest
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc digest || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/digest/DESCRIPTION
/usr/lib64/R/library/digest/GPL-2
/usr/lib64/R/library/digest/INDEX
/usr/lib64/R/library/digest/Meta/Rd.rds
/usr/lib64/R/library/digest/Meta/demo.rds
/usr/lib64/R/library/digest/Meta/features.rds
/usr/lib64/R/library/digest/Meta/hsearch.rds
/usr/lib64/R/library/digest/Meta/links.rds
/usr/lib64/R/library/digest/Meta/nsInfo.rds
/usr/lib64/R/library/digest/Meta/package.rds
/usr/lib64/R/library/digest/Meta/vignette.rds
/usr/lib64/R/library/digest/NAMESPACE
/usr/lib64/R/library/digest/R/digest
/usr/lib64/R/library/digest/R/digest.rdb
/usr/lib64/R/library/digest/R/digest.rdx
/usr/lib64/R/library/digest/demo/vectorised.R
/usr/lib64/R/library/digest/doc/index.html
/usr/lib64/R/library/digest/doc/sha1.R
/usr/lib64/R/library/digest/doc/sha1.Rmd
/usr/lib64/R/library/digest/doc/sha1.html
/usr/lib64/R/library/digest/help/AnIndex
/usr/lib64/R/library/digest/help/aliases.rds
/usr/lib64/R/library/digest/help/digest.rdb
/usr/lib64/R/library/digest/help/digest.rdx
/usr/lib64/R/library/digest/help/paths.rds
/usr/lib64/R/library/digest/html/00Index.html
/usr/lib64/R/library/digest/html/R.css
/usr/lib64/R/library/digest/include/pmurhashAPI.h
/usr/lib64/R/library/digest/tests/tinytest.R
/usr/lib64/R/library/digest/tinytest/test_aes.R
/usr/lib64/R/library/digest/tinytest/test_crc32.R
/usr/lib64/R/library/digest/tinytest/test_digest.R
/usr/lib64/R/library/digest/tinytest/test_digest2int.R
/usr/lib64/R/library/digest/tinytest/test_encoding.R
/usr/lib64/R/library/digest/tinytest/test_hmac.R
/usr/lib64/R/library/digest/tinytest/test_misc.R
/usr/lib64/R/library/digest/tinytest/test_num2hex.R
/usr/lib64/R/library/digest/tinytest/test_raw.R
/usr/lib64/R/library/digest/tinytest/test_sha1.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/digest/libs/digest.so
/usr/lib64/R/library/digest/libs/digest.so.avx2
