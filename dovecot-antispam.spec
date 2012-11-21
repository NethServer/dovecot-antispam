%define vhash 7f94cc6b4d8e
%define packdir %{name}-plugin-%{vhash}

Name: dovecot-antispam
Summary: Train the spam filter by moving email messages in and out of the IMAP spam folder
Version: 0.0.48
Release: 1%{?dist}
License: GPL2
URL: http://wiki2.dovecot.org/Plugins/Antispam
Source0: %vhash.tar.gz
Patch0: 5e8351bcfb29.patch

BuildRequires: autoconf, automake, gcc, dovecot-devel >= 2.0.9

%description 

The antispam plugin for dovecot allows you to retrain the
spam filter by simply moving emails in and out of the Spam
folder. This is the fork of the analogous plugin for Dovecot versions
prior to v2.0. The original project can be found at
http://johannes.sipsolutions.net/Projects/dovecot-antispam

%prep
%setup -n %packdir
%patch0 -R -p1 

%build
./autogen.sh
%configure --prefix=/usr --with-dovecot=/usr/lib64/dovecot
make

%install
%make_install

%files
%defattr(-,root,root,-)
%doc README
%doc COPYING
%{_mandir}/man7/dovecot-antispam.7*
/usr/lib64/dovecot/lib90_antispam_plugin.so

%changelog
* Wed Nov 21 2012 Davide Principi <davide.principi@nethesis.it> - 0.0.48-1
- Build 0.0.48 - hash 7f94cc6b4d8e



