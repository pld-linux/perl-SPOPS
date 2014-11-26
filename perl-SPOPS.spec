#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pnam	SPOPS
%include	/usr/lib/rpm/macros.perl
Summary:	Simple Perl Object Persistence with Security
Summary(pl.UTF-8):	Simple Perl Object Persistence with Security - bezpieczne zachowywanie obiektów
Name:		perl-SPOPS
Version:	0.87
Release:	4
License:	GPL v2+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/C/CW/CWINTERS/%{pnam}-%{version}.tar.gz
# Source0-md5:	22bdc965f05167b31b97772fd8a72b27
URL:		http://search.cpan.org/dist/SPOPS/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-Accessor >= 0.17
BuildRequires:	perl-Class-Date >= 1.00
BuildRequires:	perl-Class-Factory >= 1.00
BuildRequires:	perl-Class-ISA >= 0.32
BuildRequires:	perl-Devel-StackTrace >= 0.90
BuildRequires:	perl-Log-Dispatch >= 2
BuildRequires:	perl-Log-Log4perl >= 0.35
BuildRequires:	perl-Test-Simple >= 0.41
BuildRequires:	perl-Time-Piece >= 1.07
%endif
Requires:	perl-Class-Date >= 1.00
Requires:	perl-Class-Factory >= 1.00
Requires:	perl-Class-ISA >= 0.32
Requires:	perl-Devel-StackTrace >= 0.90
Requires:	perl-GDBM_File
Requires:	perl-Time-Piece >= 1.07
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SPOPS allows you to easily define how an object is composed and save,
retrieve or remove it any time thereafter. It is intended for SQL
databases (using the DBI), but you should be able to adapt it to use
any storage mechanism for accomplishing these tasks.

%description -l pl.UTF-8
SPOPS pozwala na łatwe definiowanie, jak obiekt jest składany i
zachowywany, odtwarzany lub usuwany później w dowolnej chwili. Jest
przeznaczony do baz danych SQL (przy użyciu DBI), ale powinien dać się
zaadaptować do używania z dowolnym mechanizmem przechowywania danych.

%prep
%setup -q -n %{pnam}-%{version}

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
%dir %{perl_vendorlib}/SPOPS
%{perl_vendorlib}/SPOPS/[!M]*
%{perl_vendorlib}/SPOPS.pm
%{_mandir}/man3/*
