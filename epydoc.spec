%define name epydoc
%define version 3.0.1
%define release %mkrel 10

Summary: Edward Loper's API Documentation Generation Tool
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://prdownloads.dl.sourceforge.net/sourceforge/epydoc/%{name}-%{version}.tar.gz
# https://qa.mandriva.com/show_bug.cgi?id=62543
Patch0: epydoc_restructuredtext_Bug_62543.patch
License: IBM Open Source License
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildArchitectures: noarch
Url: http://epydoc.sourceforge.net/
%py_requires -d
Requires: tkinter
Requires: python-docutils

%description
Epydoc is a tool for generating API documentation for Python modules,
based on their docstrings. A lightweight markup language called
epytext can be used to format docstrings, and to add information about
specific fields, such as parameters and instance variables. Epydoc
also understands docstrings written in ReStructuredText, Javadoc, and
plaintext.


%prep
%setup -q
%apply_patches

%build
python setup.py build

%install
rm -rf %buildroot
python setup.py install --root=$RPM_BUILD_ROOT
mkdir -p %buildroot%_mandir/man1
install -m 644 man/*.1 %buildroot%_mandir/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc *.txt doc/
%_bindir/epydoc
%_bindir/epydocgui
%_bindir/apirst2html.py
%_mandir/man1/*
%py_puresitedir/*




%changelog
* Tue Feb 28 2012 Götz Waschk <waschk@mandriva.org> 3.0.1-10mdv2012.0
+ Revision: 781222
- rebuild

* Sun Feb 27 2011 Funda Wang <fwang@mandriva.org> 3.0.1-9
+ Revision: 640431
- rebuild to obsolete old packages

* Thu Feb 17 2011 Götz Waschk <waschk@mandriva.org> 3.0.1-8
+ Revision: 638199
- add missing dep on python-docutils

* Thu Feb 17 2011 Götz Waschk <waschk@mandriva.org> 3.0.1-7
+ Revision: 638147
- add patch to fix crash (bug #62543)

* Sun Oct 31 2010 Funda Wang <fwang@mandriva.org> 3.0.1-6mdv2011.0
+ Revision: 590792
- rebuild for py2.7

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 3.0.1-5mdv2011.0
+ Revision: 437481
- rebuild

* Thu Dec 25 2008 Funda Wang <fwang@mandriva.org> 3.0.1-4mdv2009.1
+ Revision: 318948
- rebuild for new python

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 3.0.1-3mdv2009.0
+ Revision: 244930
- rebuild

* Tue Feb 05 2008 Götz Waschk <waschk@mandriva.org> 3.0.1-1mdv2008.1
+ Revision: 162561
- new version

* Thu Jan 31 2008 Götz Waschk <waschk@mandriva.org> 3.0-1mdv2008.1
+ Revision: 160648
- new version
- update file list

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Nov 29 2006 Götz Waschk <waschk@mandriva.org> 2.1-5mdv2007.0
+ Revision: 88342
- Import epydoc

* Wed Nov 29 2006 Götz Waschk <waschk@mandriva.org> 2.1-5mdv2007.1
- update file list

* Fri Aug 25 2006 G�tz Waschk <waschk@mandriva.org> 2.1-4mdv2007.0
- spec fixes

* Mon Dec 05 2005 Götz Waschk <waschk@mandriva.org> 2.1-3mdk
- Rebuild

* Sat Dec 04 2004 Michael Scherer <misc@mandrake.org> 2.1-2mdk
- Rebuild for new python

* Thu Oct 21 2004 G�tz Waschk <waschk@linux-mandrake.com> 2.1-1mdk
- initial package

