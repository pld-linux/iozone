Summary:	IO Zone Benchmark Program
Summary(pl):	Program testuj±cy wydajno¶æ I/O
Name:		iozone
Version:	3.109
Release:	1
License:	distributable
Group:		Applications/System
Source0:	http://www.iozone.org/src/current/%{name}%(echo %{version} | tr . _).tar
#Source0:	ftp://ftp.freebsd.org/pub/FreeBSD/distfiles/%{name}3_9.tar.gz
Patch0:		%{name}-make.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Iozone benchmarks IO performance. By default it benchmarks the speed
of sequential I/O to files, but it also supports a raw mode that
attempts a measurement of speed when accessing a raw device.

%description -l pl
Iozone testuje wydajno¶æ I/O. Domy¶lnie testuje szybko¶æ sekwencyjnego
odczytu/zapisu do plików, ale obs³uguje tak¿e tryb surowy, w którym
próbuje okre¶liæ szybko¶æ dostêpu do samego urz±dzenia.

%prep
%setup -q -c
%patch -p1

%build
cd src/current
%{__make} linux OPT="%{rpmcflags} -O3" CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/iozone,%{_mandir}/man1}

install src/current/iozone $RPM_BUILD_ROOT%{_bindir}
install docs/iozone.1 $RPM_BUILD_ROOT%{_mandir}/man1
install src/current/*.dem $RPM_BUILD_ROOT%{_datadir}/iozone

gzip -d docs/*ps.gz
mv -f docs/Iozone_ps docs/IOzone.ps
mv -f docs/IOzone_msword_98.pdf docs/IOzone.pdf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*.ps docs/*.pdf src/current/Changes.txt
%attr(750,root,root) %{_bindir}/iozone
%dir %{_datadir}/iozone
%{_datadir}/iozone/*.dem
%{_mandir}/man1/iozone.1*
