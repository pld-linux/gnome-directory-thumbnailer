Summary:	GNOME thumbnailer utility to generate thumbnails for directories
Summary(pl.UTF-8):	Narzędzie GNOME do tworzenia miniaturek dla katalogów
Name:		gnome-directory-thumbnailer
Version:	0.1.11
Release:	4
License:	LGPL v2.1+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/gnome-directory-thumbnailer/0.1/%{name}-%{version}.tar.xz
# Source0-md5:	3433de424a1967c3d469521d1bc73aa2
Patch0:		%{name}-gnome-desktop.patch
URL:		https://wiki.gnome.org/Projects/GnomeDirectoryThumbnailer
BuildRequires:	autoconf >= 2.65
BuildRequires:	automake >= 1:1.11
BuildRequires:	gdk-pixbuf2-devel >= 2.36.5
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.36.0
BuildRequires:	gnome-desktop-devel >= 43
BuildRequires:	gtk+3-devel >= 3.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.35
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.36.0
Requires:	gdk-pixbuf2 >= 2.36.5
Requires:	glib2 >= 1:2.36.0
Requires:	gnome-desktop >= 43
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gnome-directory-thumbnailer is a GNOME thumbnailer utility which will
generate a thumbnail for a directory. It is intended to be called by
gnome-desktop's thumbnailer code, but can be called manually as well.

%description -l pl.UTF-8
gnome-directory-thumbnailer to narzędzie GNOME do generowania
miniaturek dla katalogów. W zamierzeniu ma być wywoływany przez kod
miniaturek pakietu gnome-desktop, ale można go uruchamiać także
ręcznie.

%prep
%setup -q
%patch0 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gnome-directory-thumbnailer
%{_datadir}/thumbnailers/gnome-directory-thumbnailer.thumbnailer
