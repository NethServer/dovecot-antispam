%define vhash 5ebc6aae4d7c
%define packdir %{name}-plugin-%{vhash}

Name: dovecot-antispam
Summary: Train the spam filter by moving email messages in and out of the IMAP spam folder
Version: 0.0.49
Release: 3%{?dist}
License: GPL2
URL: http://wiki2.dovecot.org/Plugins/Antispam
Source0: %{name}-%{version}.tar.gz
Source1: http://hg.dovecot.org/dovecot-antispam-plugin/archive/%{vhash}.tar.gz

BuildRequires: autoconf, automake, gcc
BuildRequires: dovecot-devel >= 2.2.36
BuildRequires: openssl-devel >= 1.0.0

%description 

The antispam plugin for dovecot allows you to retrain the
spam filter by simply moving emails in and out of the Spam
folder. This is the fork of the analogous plugin for Dovecot versions
prior to v2.0. The original project can be found at
http://johannes.sipsolutions.net/Projects/dovecot-antispam

%prep
%setup -b 1 -n %packdir

%build
./autogen.sh
%configure --prefix=/usr --with-dovecot=%{_libdir}/dovecot
make

%install
%make_install

%files
%defattr(-,root,root,-)
%doc README
%doc COPYING
%{_mandir}/man7/dovecot-antispam.7*
%{_libdir}/dovecot/lib90_antispam_plugin.so

%changelog
* Sun Apr 17 2016 Mark Verlinde <mark@havak.nl> - 0.0.49-3
- spec: Fix build for multibit acrh

* Fri Mar 27 2015 Davide Principi <davide.principi@nethesis.it> - 0.0.49-2
- Rebuild for NethServer 6.6

* Fri May 24 2013 Davide Principi <davide.principi@nethesis.it> - 0.0.49-1
- New version, for dovecot 2.1

* Wed Nov 21 2012 Davide Principi <davide.principi@nethesis.it> - 0.0.48-1
- Build 0.0.48 - hash 7f94cc6b4d8e



