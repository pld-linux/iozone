Summary:	IO Zone Benchmark Program
Summary(pl):	Program testuj±cy wydajno¶æ I/O
Name:		iozone
Version:	3.9
Release:	3
License:	distributable 
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	ftp://ftp.freebsd.org/pub/FreeBSD/distfiles/%{name}3_9.tar.gz
Patch0:		%{name}-3.9-make.patch
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
cd src
%{__make} linux OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/iozone,%{_mandir}/man1}

install src/iozone $RPM_BUILD_ROOT%{_bindir}
install src/iozone.1 $RPM_BUILD_ROOT%{_mandir}/man1
install src/*.dem $RPM_BUILD_ROOT%{_datadir}/iozone

gzip -d docs/*.gz

gzip -9nf docs/* src/Changes.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*.gz src/*.gz
%attr(750,root,root) %{_bindir}/iozone
%dir %{_datadir}/iozone
%{_datadir}/iozone/*.dem
%{_mandir}/man1/iozone.1*
