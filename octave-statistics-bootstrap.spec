%global octpkg statistics-bootstrap

Summary:	A statistics package for GNU Octave with a variety of bootstrap resampling tools
Name:		octave-%{octpkg}
Version:	3.6.4
Release:	1
Url:		https://github.com/gnu-octave/%{octpkg}
Source0:	%{url}/archive/v%{version}/%{octpkg}-%{version}.tar.gz
License:	GPLv3+
Group:		Sciences/Mathematics
BuildArch:	noarch

BuildRequires:	octave-devel >= 3.6.0
BuildRequires:	octave-statistics >= 1.0.0

Requires:	octave(api) = %{octave_api}
Requires:	octave-statistics >= 1.0.0

Requires(post): octave
Requires(postun): octave

%description
This package of functions can be used to estimate uncertainty (confidence
intervals) and test hypotheses (p-values) using bootstrap. Variations of the
bootstrap are included that improve the accuracy of bootstrap statistics for
small samples and samples with complex dependence structures.

The Octave statistics-bootstrap package is forked from the GitHub repository iboot.

%files
%license COPYING
#doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

# remove backup files
#find . -name \*~ -delete

%build
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

