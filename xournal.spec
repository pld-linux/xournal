Summary:	Xournal - application for notetaking, sketching, keeping a journal using a stylus
Summary(pl.UTF-8):	Xournal - aplikacja do tworzenia notatek, szkicowania i prowadzenia dziennika pisakiem
Name:		xournal
Version:	0.4.8.2016
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/xournal/%{name}-%{version}.tar.gz
# Source0-md5:	a594f475d9b93fbca0aac43d47c2de22
Patch0:		%{name}-zlib.patch
Patch1:		%{name}-poppler-api.patch
URL:		http://xournal.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	gtk+2-devel >= 2:2.10
BuildRequires:	libgnomecanvas-devel >= 2.4
BuildRequires:	pango-devel >= 1.0
BuildRequires:	pkgconfig
BuildRequires:	poppler-glib-devel >= 0.5.4
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
#%%patch1 -p0

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
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
