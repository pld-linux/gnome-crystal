Summary:	Visualizer for crystal structures
Summary(pl):	Narzêdzie s³u¿±ce do wizualizacji struktur kryszta³u
Name:		gnome-crystal
Version:	0.5.4
Release:	1
License:	GPL
Group:		X11/Applications/Science
Source0:	http://savannah.nongnu.org/download/gcrystal/%{name}-%{version}.tar.bz2
# Source0-md5:	42992758ccf502688205642b0b8ccc14
Patch0:		%{name}-desktop.patch
URL:		http://www.nongnu.org/gcrystal/
BuildRequires:	gnome-chemistry-utils-devel >= 0.2.3
BuildRequires:	libgnomeui-devel >= 2.2.0
BuildRequires:	libgnomeprintui-devel >= 2.2.0
BuildRequires:	libjpeg-devel
BuildRequires:	libglade2-devel >= 2.0.1
BuildRequires:	libpng-devel
Requires(post):	GConf2
Requires(post):	scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Visualizer for crystal structures.

%description -l pl
Narzêdzie s³u¿±ce do wizualizacji struktur kryszta³u.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--disable-schemas-install \
	--with-png \
	--with-jpeg

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/scrollkeeper-update
%gconf_schema_install

%postun -p /usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/gconf/schemas/*.schemas
%{_libdir}/bonobo/servers/*.server
%{_desktopdir}/*.desktop
%{_datadir}/gcrystal
%{_datadir}/gnome-2.0/ui/*
%{_datadir}/mime-info/*
%{_omf_dest_dir}/%{name}
%{_pixmapsdir}/*
