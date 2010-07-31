Summary:	Xournal - application for notetaking, sketching, keeping a journal using a stylus
Summary(pl.UTF-8):	Xournal - aplikacja do tworzenia notatek, szkicowania i prowadzenia dziennika pisakiem
Name:		xournal
Version:	0.4.5
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/xournal/%{name}-%{version}.tar.gz
# Source0-md5:	795e4396ded2b67766eb2926be1fb4a9
Patch0:		%{name}-zlib.patch
URL:		http://xournal.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.4
BuildRequires:	libgnomecanvas-devel >= 2.4
BuildRequires:	pkgconfig
BuildRequires:	poppler-glib-devel
BuildRequires:	rpmbuild(macros) >= 1.357
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xournal is an application for notetaking, sketching, keeping a journal
using a stylus. It is similar to Microsoft Windows Journal or to other
alternatives such as Jarnal and Gournal.

%description -l pl.UTF-8
Xournal to aplikacja do tworzenia notatek, szkicowania i prowadzenia
dziennika przy użyciu pisaka. Jest podobna do Microsoft Windows
Journal czy innych alternatyw takich jak Jarnal i Gournal.

%prep
%setup -q
%patch0 -p0

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_desktopdir}
install %{name}.desktop $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop
install %{name}.glade $RPM_BUILD_ROOT%{_datadir}/%{name}/%{name}.glade

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README src/TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
