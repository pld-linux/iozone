Summary:	IO Zone Benchmark Program
Name:		iozone
Version:	3.9
Release:	1
Group:		Utilities/System
Source:		ftp://ftp.freebsd.org/pub/FreeBSD/distfiles/iozone3_9.tar
Copyright:	distributable 
Patch:		iozone-3.9-make.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Iozone benchmarks IO performance. By default it benchmarks the speed of
sequential I/O to files, but it also supports a raw mode that attempts
a measurement of speed when accessing a raw device.

%prep
%setup -q -c
%patch -p1

%build
cd src
make linux OPT="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/iozone,%{_mandir}/man1}

install -s src/iozone $RPM_BUILD_ROOT%{_bindir}
install src/iozone.1 $RPM_BUILD_ROOT%{_mandir}/man1
install src/*.dem $RPM_BUILD_ROOT%{_datadir}/iozone

gzip -d docs/*.gz

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* docs/* src/Changes.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc docs/*.gz src/*.gz
%attr(750, root, root) %{_bindir}/iozone
%{_datadir}/iozone/*.dem
%{_mandir}/man1/iozone.1*
