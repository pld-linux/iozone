Summary:	IO Zone Benchmark Program
Summary(es.UTF-8):	El IOzone es una ferramenta para prueba de rendimiento em sistemas de archivos
Summary(pl.UTF-8):	Program testujący wydajność I/O
Summary(pt_BR.UTF-8):	O IOzone é uma ferramenta para testes de performance em sistemas de arquivos
Name:		iozone
Version:	3.408
Release:	1
License:	distributable
Group:		Applications/System
Source0:	http://www.iozone.org/src/current/%{name}%(echo %{version} | tr . _).tar
# Source0-md5:	ff3bc9a075db68b028e6cd5a833353d8
Patch0:		%{name}-make.patch
URL:		http://www.iozone.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	target linux
%ifarch arm
%define	target linux-arm
%endif
%ifarch %{x8664}
%define	target linux-AMD64
%endif
%ifarch ia64
%define	target linux-ia64
%endif
%ifarch ppc
%define	target linux-powerpc
%endif
%ifarch ppc64
%define	target linux-powerpc64
%endif
%ifarch sparc sparc64 sparcv9
%define	target linux-sparc
%endif

%description
Iozone benchmarks IO performance. By default it benchmarks the speed
of sequential I/O to files, but it also supports a raw mode that
attempts a measurement of speed when accessing a raw device.

%description -l es.UTF-8
El IOzone es útil para prueba de rendimiento en sistemas de archivos.
Genera y medi una variedad de operacións en archivos.

%description -l pl.UTF-8
Iozone testuje wydajność I/O. Domyślnie testuje szybkość sekwencyjnego
odczytu/zapisu do plików, ale obsługuje także tryb surowy, w którym
próbuje określić szybkość dostępu do samego urządzenia.

%description -l pt_BR.UTF-8
O IOzone é uma ferramenta para testes de performance em sistemas de
arquivos. Gera e mede uma variedade de operações em arquivos.

%prep
%setup -q -n %{name}%(echo %{version} | tr . _)
%{__sed} -i -e 's,-O[23],,' src/current/makefile
%patch0 -p1

gzip -d docs/Iozone_ps.gz
mv -f docs/Iozone_ps docs/IOzone.ps
mv -f docs/IOzone_msword_98.pdf docs/IOzone.pdf

%build
%{__make} -C src/current \
	%{target} \
	LDFLAGS="%{rpmldflags}" \
	CFLAGS="%{rpmcflags}" \
	CC="%{__cc}" \
	GCC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/iozone,%{_mandir}/man1}

install -p src/current/iozone $RPM_BUILD_ROOT%{_bindir}
cp -p docs/iozone.1 $RPM_BUILD_ROOT%{_mandir}/man1
cp -p src/current/*.dem $RPM_BUILD_ROOT%{_datadir}/iozone

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*.ps docs/*.pdf src/current/Changes.txt
%attr(755,root,root) %{_bindir}/iozone
%dir %{_datadir}/iozone
%{_datadir}/iozone/*.dem
%{_mandir}/man1/iozone.1*
