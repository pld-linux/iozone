Summary:	IO Zone Benchmark Program
Summary(es):	El IOzone es una ferramenta para prueba de rendimiento em sistemas de archivos
Summary(pl):	Program testuj±cy wydajno¶æ I/O
Summary(pt_BR):	O IOzone é uma ferramenta para testes de performance em sistemas de arquivos
Name:		iozone
Version:	3.167
Release:	1
License:	distributable
Group:		Applications/System
Source0:	http://www.iozone.org/src/current/%{name}%(echo %{version} | tr . _).tar
#Source0:	ftp://ftp.freebsd.org/pub/FreeBSD/distfiles/%{name}3_9.tar.gz
Patch0:		%{name}-make.patch
Patch1:		%{name}-ppc.patch
Patch2:		%{name}-errno.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Iozone benchmarks IO performance. By default it benchmarks the speed
of sequential I/O to files, but it also supports a raw mode that
attempts a measurement of speed when accessing a raw device.

%description -l es
El IOzone es útil para prueba de rendimiento en sistemas de archivos.
Genera y medi una variedad de operacións en archivos.

%description -l pl
Iozone testuje wydajno¶æ I/O. Domy¶lnie testuje szybko¶æ sekwencyjnego
odczytu/zapisu do plików, ale obs³uguje tak¿e tryb surowy, w którym
próbuje okre¶liæ szybko¶æ dostêpu do samego urz±dzenia.

%description -l pt_BR
O IOzone é uma ferramenta para testes de performance em sistemas de
arquivos. Gera e mede uma variedade de operações em arquivos.

%prep
%setup -q -c
%patch0 -p1
%patch1 -p1
%patch2 -p1

gzip -d docs/Iozone_ps.gz
mv -f docs/Iozone_ps docs/IOzone.ps
mv -f docs/IOzone_msword_98.pdf docs/IOzone.pdf

%build
cd src/current
%{__make} \
%ifarch ppc
	linux-powerpc \
%else
%ifarch sparc sparc64 sparcv9
	linux-sparc \
%else
	linux \
%endif
%endif
	OPT="%{rpmcflags}" CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/iozone,%{_mandir}/man1}

install src/current/iozone $RPM_BUILD_ROOT%{_bindir}
install docs/iozone.1 $RPM_BUILD_ROOT%{_mandir}/man1
install src/current/*.dem $RPM_BUILD_ROOT%{_datadir}/iozone

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*.ps docs/*.pdf src/current/Changes.txt
%attr(750,root,root) %{_bindir}/iozone
%dir %{_datadir}/iozone
%{_datadir}/iozone/*.dem
%{_mandir}/man1/iozone.1*
