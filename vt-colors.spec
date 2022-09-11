# SPDX-FileCopyrightText: 2022 Paweł Marciniak
#
# SPDX-License-Identifier: GPL-2.0-or-later

Name:           vt-colors
Version:        1.0.0
Release:        1%{?dist}
Summary:        An easy to use tool to change vt colors.
License:        GPL-2.0-or-later
URL:            https://github.com/sunwire/vt-colors
Source0:        https://github.com/sunwire/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch

Requires:       kbd
Requires:       systemd


%description
An easy to use tool to change vt colors.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_datadir}/vt-colors
mkdir -p %{buildroot}%{_sysconfdir}/vt-colors
%__install -Dm0644 vt-colors.service -t %{buildroot}%{_unitdir}
%__install -Dm0644 vt.palette -t %{buildroot}%{_sysconfdir}/vt-colors
%__install -Dm0644 palettes/default.palette -t %{buildroot}%{_datadir}/vt-colors

%preun
%systemd_preun vt-colors.service

%postun
%systemd_postun vt-colors.service

%files
%{_sysconfdir}/vt-colors/*
%{_unitdir}/vt-colors.service
%{_datadir}/vt-colors/*
%license LICENSE
%doc README.md

%changelog
* Sun Sep 11 2022 Paweł Marciniak <sunwire+repo@gmail.com> - 1.0.0-1
- The first release

