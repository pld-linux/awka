Summary:	Translator of the AWK programming language to ANSI-C
Summary(pl):	Konwerter programów w jêzyku AWK na programy w jêzyku C
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

%description -l pl
Awka sk³ada siê z programu t³umacz±cego kod w jêzyku AWK na kod w
jêzyku C i biblioteki z któr± przet³umaczone programy mog± byæ
skonsolidowane.

%package static
Summary:	Static awka library
Summary(pl):	Statyczna bibliotka awka
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description static
Static awka library.

%description static -l pl
Statyczna bibliotka awka.

%prep
%setup -q
%patch0 -p1

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
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*
%{_mandir}/man[15]/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
