Summary:	Xournal - application for notetaking, sketching, keeping a journal using a stylus
Summary(pl.UTF-8):	Xournal - aplikacja do tworzenia notatek, szkicowania i prowadzenia dziennika pisakiem
Name:		xournal
Version:	0.4.1
Release:	2
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/xournal/%{name}-%{version}.tar.gz
# Source0-md5:	b3d352d08e71606383c31da5790b8d60
URL:		http://xournal.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
Buildrequires:	rpmbuild(macros) >= 1.357
BuildRequires:	gtk+2-devel >= 2:2.4
BuildRequires:	libgnomecanvas-devel >= 2.4
BuildRequires:	libgnomeprint-devel >= 2.2
BuildRequires:	libgnomeprintui-devel >= 2.2
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
