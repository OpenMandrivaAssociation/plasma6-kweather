%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
#define git 20210826
#define commit dccfaa0fea063c6a79b1f8d41261e6632e6387dc

Name:		kweather
Version:	24.01.95
Release:	%{?git:0.%{git}.}1
%if 0%{?git:1}
Source0:        https://invent.kde.org/plasma-mobile/kweather/-/archive/master/kweather-master.tar.bz2
%else
Source0:        https://download.kde.org/%{stable}/release-service/%{version}/src/kweather-%{version}.tar.xz
%endif
Summary:	Weather applet for Plasma Mobile
License:	GPLv3
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6Charts)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6Kirigami2)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6QuickCharts)
BuildRequires:	cmake(KF6KirigamiAddons)
BuildRequires:	cmake(KWeatherCore)
BuildRequires:	cmake(OpenSSL)
BuildRequires:	pkgconfig(openssl)

%description
Weather applet for Plasma Mobile

%prep
%if 0%{?git}
%autosetup -p1 -n kweather-master-%{commit}
%else
%autosetup -p1
%endif
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang kweather

%files -f kweather.lang
%{_bindir}/kweather
%{_datadir}/applications/org.kde.kweather.desktop
%{_datadir}/dbus-1/services/org.kde.kweather.service
%{_datadir}/icons/*/scalable/apps/org.kde.kweather.svg
%{_datadir}/metainfo/org.kde.kweather.appdata.xml
%{_libdir}/qt6/plugins/plasma/applets/plasma_applet_kweather_1x4.so
%{_datadir}/metainfo/org.kde.plasma.kweather_1x4.appdata.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kweather_1x4
