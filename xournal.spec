Summary:	Xournal - application for notetaking, sketching, keeping a journal using a stylus.
Summary(pl):	Xournal - 
Name:		xournal
Version:	0.3.1
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/sourceforge/xournal/%{name}-%{version}.tar.gz
# Source0-md5:	5c5077afff8ef41aa296d5b68504f73b
URL:		http://xournal.sourceforge.net		
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2.4
BuildRequires:	libgnomecanvas-devel >= 2.4
BuildRequires:	libgnomeprint-devel >= 2.2
BuildRequires:	libgnomeprintui-devel >= 2.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xournal is an application for notetaking, sketching, keeping a journal
using a stylus. It is similar to Microsoft Windows Journal or to other
alternatives such as Jarnal and Gournal.

%description -l pl
Xournal

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
