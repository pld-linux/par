Summary:	Palm's pdb/prc file manipulator
Summary(pl.UTF-8):	Program do manipulacji palmowymi plikami pdb/prc
Name:		par
Version:	00.05.01
Release:	0.1
License:	MPL
Vendor:		David Williams <djw@djw.org>
Group:		Development/Building
Source0:	http://www.djw.org/product/palm/par/prc.tgz
# Source0-md5:	c20a295b05c598322d037ecd36a28e38
URL:		http://www.djw.org/product/palm/par/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Palm's pdb/prc file manipulator.

%description -l pl.UTF-8
Program do manipulacji palmowymi plikami pdb/prc.

%prep
%setup -q -n prc

%build
rm -f missing
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall -I."

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir},%{_libdir},%{_bindir},%{_mandir}/man1}

install prc.h $RPM_BUILD_ROOT%{_includedir}
install libprc.a $RPM_BUILD_ROOT%{_libdir}
install par $RPM_BUILD_ROOT%{_bindir}
install par.man $RPM_BUILD_ROOT%{_mandir}/man1/par.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_libdir}/lib*.a
%{_includedir}/prc.h
%{_mandir}/man1/*.1*
