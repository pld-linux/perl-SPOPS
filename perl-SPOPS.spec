#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pnam	SPOPS
Summary:	Simple Perl Object Persistence with Security
Name:		perl-SPOPS
Version:	0.75
Release:	2
License:	GPLv2+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/C/CW/CWINTERS/%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{!?_without_tests:1}0
BuildRequires:	perl-Class-Date >= 1.00
BuildRequires:	perl-Class-ISA >= 0.32
BuildRequires:	perl-Class-Factory >= 1.00
BuildRequires:	perl-Devel-StackTrace >= 0.90
BuildRequires:	perl-Storable >= 1.00
BuildRequires:	perl-Time-Piece >= 1.07
%endif
Requires:	perl-Class-Date >= 1.00
Requires:	perl-Class-ISA >= 0.32
Requires:	perl-Class-Factory >= 1.00
Requires:	perl-Devel-StackTrace >= 0.90
Requires:	perl-Storable >= 1.00
Requires:	perl-Time-Piece >= 1.07
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SPOPS allows you to easily define how an object is composed and save,
retrieve or remove it any time thereafter. It is intended for SQL
databases (using the DBI), but you should be able to adapt it to use
any storage mechanism for accomplishing these tasks.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README RELEASE
%dir %{perl_vendorlib}/SPOPS
%{perl_vendorlib}/SPOPS/[!M]*
%{perl_vendorlib}/SPOPS.pm
%{_mandir}/man3/*
