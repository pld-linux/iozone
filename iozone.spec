Summary:	IO Zone Benchmark Program
Name:		iozone
Version:	3.9
Release:	2
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	ftp://ftp.freebsd.org/pub/FreeBSD/distfiles/%{name}3_9.tar.gz
Copyright:	distributable 
Patch0:		%{name}-3.9-make.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Iozone benchmarks IO performance. By default it benchmarks the speed
of sequential I/O to files, but it also supports a raw mode that
attempts a measurement of speed when accessing a raw device.

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
%{_datadir}/iozone/*.dem
%{_mandir}/man1/iozone.1*
