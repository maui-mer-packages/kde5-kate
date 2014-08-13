# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       kate

# >> macros
# << macros

Summary:    Advanced KDE editor applications
Version:    5.0.0
Release:    1
Group:      System/Base
License:    GPLv2+
URL:        http://www.kde.org
Source0:    %{name}-%{version}.tar.xz
Source100:  kate.yaml
Source101:  kate-rpmlintrc
Requires:   kf5-filesystem
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Script)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-tools
BuildRequires:  kconfig-devel
BuildRequires:  kdoctools-devel
BuildRequires:  kguiaddons-devel
BuildRequires:  ki18n-devel
BuildRequires:  kinit-devel
BuildRequires:  kjobwidgets-devel
BuildRequires:  kio-devel
BuildRequires:  kparts-devel
BuildRequires:  ktexteditor-devel
BuildRequires:  kwindowsystem-devel
BuildRequires:  kitemmodels-devel
BuildRequires:  kxmlgui-devel

%description
An advanced editor component which is used in numerous KDE applications
requiring a text editing component.


%package doc
Summary:    Documentation and user manuals for %{name}
Group:      Documentation
Requires:   %{name} = %{version}-%{release}

%description doc
Documentation and user manuals for %{name}


%prep
%setup -q -n %{name}-%{version}/upstream

# >> setup
# << setup

%build
# >> build pre
%kf5_make
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
%kf5_make_install
# << install pre

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING-GPL3 COPYING-LGPL3 COPYING.LIB README.md
%{_kf5_bindir}/kwrite
%{_kf5_bindir}/kate
%{_kf5_libdir}/libkdeinit5_kate.so
%{_kf5_libdir}/libkdeinit5_kwrite.so
%{_kf5_plugindir}/*
%{_kf5_configdir}/katerc
%{_kf5_sharedir}/kate*
%{_kf5_sharedir}/kwrite*
%{_kf5_iconsdir}/hicolor/*/actions/*
%{_kf5_sharedir}/applications/*.desktop
%{_kf5_servicesdir}/*.desktop
# >> files
# << files

%files doc
%defattr(-,root,root,-)
%{_kf5_htmldir}/en/kate
%{_kf5_htmldir}/en/katepart
%{_mandir}/man1/kate.1.gz
# >> files doc
# << files doc
