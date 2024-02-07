# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-contextlib2
Epoch: 100
Version: 21.6.0
Release: 1%{?dist}
BuildArch: noarch
Summary: Backports and enhancements for the contextlib module
License: PSF-2.0
URL: https://github.com/jazzband/contextlib2/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
contextlib2 is a backport of the standard library’s contextlib module to
earlier Python versions.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-contextlib2
Summary: Backports and enhancements for the contextlib module
Requires: python3
Provides: python3-contextlib2 = %{epoch}:%{version}-%{release}
Provides: python3dist(contextlib2) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-contextlib2 = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(contextlib2) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-contextlib2 = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(contextlib2) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-contextlib2
contextlib2 is a backport of the standard library’s contextlib module to
earlier Python versions.

%files -n python%{python3_version_nodots}-contextlib2
%license LICENSE.txt
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-contextlib2
Summary: Backports and enhancements for the contextlib module
Requires: python3
Provides: python3-contextlib2 = %{epoch}:%{version}-%{release}
Provides: python3dist(contextlib2) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-contextlib2 = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(contextlib2) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-contextlib2 = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(contextlib2) = %{epoch}:%{version}-%{release}

%description -n python3-contextlib2
contextlib2 is a backport of the standard library’s contextlib module to
earlier Python versions.

%files -n python3-contextlib2
%license LICENSE.txt
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-contextlib2
Summary: Backports and enhancements for the contextlib module
Requires: python3
Provides: python3-contextlib2 = %{epoch}:%{version}-%{release}
Provides: python3dist(contextlib2) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-contextlib2 = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(contextlib2) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-contextlib2 = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(contextlib2) = %{epoch}:%{version}-%{release}

%description -n python3-contextlib2
contextlib2 is a backport of the standard library’s contextlib module to
earlier Python versions.

%files -n python3-contextlib2
%license LICENSE.txt
%{python3_sitelib}/*
%endif

%changelog
