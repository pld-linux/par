Summary:	palm's pdb/prc file manipulator
Summary(pl):	program do manipulacji palmowymi plikami pdb/prc
Name:		par
Version:	00.05.01
Release:	0.1
License:	MPL
Group:		-
Group:		Development/Building
Source0:	http://www.djw.org/product/palm/par/prc.tgz
URL:		http://www.djw.org/product/palm/par/
Vendor:		David Williams <djw@djw.org>
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

%prep
%setup -q -n %{name}-%{version}.orig -a 1
%patch0 -p1

%build
rm -f missing
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
