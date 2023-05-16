%global octpkg statistics-bootstrap

# NOTE: conseder to move *mex to %{octpkglibdir}

Summary:	A statistics package for GNU Octave with a variety of bootstrap resampling tools
Name:		octave-statistics-bootstrap
Version:	5.2.5
Release:	1
License:	GPLv3+
Group:		Sciences/Mathematics
#Url:		https://packages.octave.org/statistics-bootstrap/
Url:		https://github.com/gnu-octave/statistics-bootstrap/
Source0:	https://github.com/gnu-octave/statistics-bootstrap/archive/v%{version}/%{octpkg}-%{version}.tar.gz

BuildRequires:  octave-devel >= 6.1.0
BuildRequires:  octave-statistics >= 1.5.0

Requires:	octave(api) = %{octave_api}
Requires:  	octave-statistics >= 1.5.0

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
#dir %{octpkglibdir}
#{octpkglibdir}/*
#{_metainfodir}/*.metainfo.xml

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

%build
%set_build_flags
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

