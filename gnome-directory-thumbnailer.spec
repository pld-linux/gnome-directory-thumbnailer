Summary:	GNOME thumbnailer utility to generate thumbnails for directories
Summary(pl.UTF-8):	Narzędzie GNOME do tworzenia miniaturek dla katalogów
Name:		gnome-directory-thumbnailer
Version:	0.1.6
Release:	1
License:	LGPL v2.1+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-directory-thumbnailer/0.1/%{name}-%{version}.tar.xz
# Source0-md5:	dac98a3becbc71015a927fa3a1621038
URL:		https://wiki.gnome.org/Projects/GnomeDirectoryThumbnailer
BuildRequires:	autoconf >= 2.65
BuildRequires:	autoconf-archive >= 2015.09.25
BuildRequires:	automake >= 1:1.11
BuildRequires:	gdk-pixbuf2-devel >= 2.6.0
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.36.0
BuildRequires:	gnome-desktop-devel >= 3.0
BuildRequires:	gtk+3-devel >= 3.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.35
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.36.0
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

# force new version from autoconf-archive (original one uses non-POSIX ${V:N} syntax)
%{__rm} m4/ax_compiler_flags_{c,cxx}flags.m4

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
