Summary:	comprises a translator of the AWK programming language to ANSI-C
Name:		awka
Version:	0.7.0
Release:	2
License:	GPL
Group:		Applications/Text
Group(de):	Applikationen/Text
Group(fr):	Utilitaires/Texte
Group(pl):	Aplikacje/Tekst
Source0:	http://members.linuxstart.com/~awka/%{name}-%{version}.tar.gz
PAtch0:		%{name}-DESTDIR.patch
URL:		http://members.linuxstart.com/~awka/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Awka comprises a translator of the AWK programming language to ANSI-C,
and a library against which translated programs may be linked.

%prep
%setup -q
%patch -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_includedir}/*
%{_libdir}/lib*.a
%{_mandir}/man[15]/*
