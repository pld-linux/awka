Summary:	Translator of the AWK programming language to ANSI-C
Summary(pl.UTF-8):	Konwerter programów w języku AWK na programy w języku C
Name:		awka
Version:	0.7.4
Release:	4
License:	GPL
Group:		Applications/Text
Source0:	http://awka.sourceforge.net/%{name}-%{version}.tar.gz
# Source0-md5:	80da40555d79d78cf96d8e3a03e1b94f
Patch0:		%{name}-DESTDIR.patch
URL:		http://awka.sourceforge.net/
BuildRequires:	perl-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Awka comprises a translator of the AWK programming language to ANSI-C,
and a library against which translated programs may be linked.

%description -l pl.UTF-8
Awka składa się z programu tłumaczącego kod w języku AWK na kod w
języku C i biblioteki z którą przetłumaczone programy mogą być
skonsolidowane.

%package static
Summary:	Static awka library
Summary(pl.UTF-8):	Statyczna bibliotka awka
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description static
Static awka library.

%description static -l pl.UTF-8
Statyczna biblioteka awka.

%prep
%setup -q
%patch -P0 -p1

%{__perl} -pi -e 's/^(CFLAGS.*)/$1 -fPIC/' lib/Makefile.in

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGELOG.txt README.txt TODO.txt 
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*
%{_mandir}/man[15]/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
