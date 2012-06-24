Summary:	Translator of the AWK programming language to ANSI-C
Summary(pl):	Konwerter program�w w j�zyku AWK na programy w j�zyku C
Name:		awka
Version:	0.7.4
Release:	1
License:	GPL
Group:		Applications/Text
Group(de):	Applikationen/Text
Group(fr):	Utilitaires/Texte
Group(pl):	Aplikacje/Tekst
Source0:	http://awka.sourceforge.net/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
URL:		http://awka.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Awka comprises a translator of the AWK programming language to ANSI-C,
and a library against which translated programs may be linked.

%description -l pl
Awka sk�ada si� z programu t�umacz�cego kod w j�zyku AWK na kod w
j�zyku C i biblioteki z kt�r� przet�umaczone programy mog� by�
zlinkowane.

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
