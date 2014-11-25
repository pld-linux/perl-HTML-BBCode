#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define	pdir	HTML
%define	pnam	BBCode
%include	/usr/lib/rpm/macros.perl
Summary:	HTML::BBCode - Perl extension for converting BBcode to HTML
Summary(pl.UTF-8):	HTML::BBcode - rozszerzenie Perla do konwersji kodu BBcode na HTML
Name:		perl-HTML-BBCode
Version:	2.06
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	03a3d80848402bb82bdd8fb443a718e8
URL:		http://search.cpan.org/dist/HTML-BBCode/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(HTML::StripScripts) >= 1.04
BuildRequires:	perl(HTML::StripScripts::Parser)
BuildRequires:	perl-URI
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML::BBCode converts BBCode - as used on the phpBB bulletin boards -
to it's HTML equivalent.

%description -l pl.UTF-8
HTML::BBCode konwertuje BBCode - używany w forach phpBB - na
odpowiedniki HTML.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/HTML
%dir %{perl_vendorlib}/HTML/BBCode
%{perl_vendorlib}/HTML/BBCode.pm
%{perl_vendorlib}/HTML/BBCode/StripScripts.pm
%{_mandir}/man3/*
