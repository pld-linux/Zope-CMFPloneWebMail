%define		zope_subname	PloneWebMail
Summary:	E-mail client for Plone (IMAP)
Summary(pl):	Klient poczty elektronicznej (IMAP) dla Plone
Name:		Zope-CMF%{zope_subname}
Version:	1.0
Release:	3
License:	GPL v2
Group:		Development/Tools
Source0:	http://plonewebmail.openprojects.it/Members/admin/%{zope_subname}-%{version}final.tar.gz
# Source0-md5:	255541e6a43c9de4fa6fccce523c5ffa
URL:		http://plonewebmail.openprojects.it/
Requires(post,postun):	/usr/sbin/installzopeproduct
%pyrequires_eq	python-modules
Requires:	Zope
Requires:	Zope-CMF >= 1:1.4
Requires:	Zope-CMFPlone >= 2.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PloneWebMail is a e-mail client for Plone (IMAP).

%description -l pl
PloneWebMail jest klientem poczty elektronicznej (IMAP) dla Plone.

%prep
%setup -q -n %{zope_subname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -af {Extensions,i18n,skins,*.py,VERSION.TXT,refresh.txt,*.gif} $RPM_BUILD_ROOT%{_datadir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/installzopeproduct %{_datadir}/%{name} %{zope_subname}
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	if [ -f /var/lock/subsys/zope ]; then
		/etc/rc.d/init.d/zope restart >&2
	fi
fi

%files
%defattr(644,root,root,755)
%doc CHANGES.TXT README.TXT INSTALL.TXT CREDITS.txt
%{_datadir}/%{name}
