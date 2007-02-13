Summary:	IO Zone Benchmark Program
Summary(es.UTF-8):	El IOzone es una ferramenta para prueba de rendimiento em sistemas de archivos
Summary(pl.UTF-8):	Program testujący wydajność I/O
Summary(pt_BR.UTF-8):	O IOzone é uma ferramenta para testes de performance em sistemas de arquivos
Name:		iozone
Version:	3.257
Release:	1
License:	distributable
Group:		Applications/System
Source0:	http://www.iozone.org/src/current/%{name}%(echo %{version} | tr . _).tar
# Source0-md5:	a4db361cd44e3273cc265a5cce08f938
Patch0:		%{name}-make.patch
URL:		http://www.iozone.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%patch0 -p1

gzip -d docs/Iozone_ps.gz
mv -f docs/Iozone_ps docs/IOzone.ps
mv -f docs/IOzone_msword_98.pdf docs/IOzone.pdf

%build
cd src/current
%{__make} \
%ifarch arm
	linux-arm
%else
%ifarch %{x8664}
	linux-AMD64
%else
%ifarch ia64
	linux-ia64
%else
%ifarch ppc
	linux-powerpc \
%else
%ifarch ppc64
	linux-powerpc64 \
%else
%ifarch sparc sparc64 sparcv9
	linux-sparc \
%else
	linux \
%endif
%endif
%endif
%endif
%endif
%endif
	LDFLAGS="%{rpmldflags}" \
	CFLAGS="%{rpmcflags}" \
	CC="%{__cc}" \
	GCC="%{__cc}"

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
%attr(755,root,root) %{_bindir}/iozone
%dir %{_datadir}/iozone
%{_datadir}/iozone/*.dem
%{_mandir}/man1/iozone.1*
