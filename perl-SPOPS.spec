%include	/usr/lib/rpm/macros.perl
%define	pnam	SPOPS
Summary:	Simple Perl Object Persistence with Security
Name:		perl-%{pnam}
Version:	0.71
Release:	0.1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/C/CW/CWINTERS/%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
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
perl Makefile.PL
%{__make}
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change*
%{perl_sitelib}/%{pnam}
%{perl_sitelib}/%{pnam}.pm
%{_mandir}/man3/*
