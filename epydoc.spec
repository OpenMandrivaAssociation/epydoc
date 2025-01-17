Summary:	Edward Loper's API Documentation Generation Tool
Name:		epydoc
Version:	3.0.1
Release:	2
License:	IBM Open Source License
Group:		Development/Python
BuildArch:	noarch
Url:		https://epydoc.sourceforge.net/
Source0:	http://prdownloads.dl.sourceforge.net/sourceforge/epydoc/%{name}-%{version}.tar.gz
# https://qa.mandriva.com/show_bug.cgi?id=62543
Patch0:		epydoc_restructuredtext_Bug_62543.patch

BuildRequires: python2-devel
Requires:	python2-docutils
Requires:	tkinter

%description
Epydoc is a tool for generating API documentation for Python modules,
based on their docstrings. A lightweight markup language called
epytext can be used to format docstrings, and to add information about
specific fields, such as parameters and instance variables. Epydoc
also understands docstrings written in ReStructuredText, Javadoc, and
plaintext.

%prep
%setup -q
%autopatch -p1

%build
python2 setup.py build

%install
python2 setup.py install --root=%{buildroot}
mkdir -p %{buildroot}%{_mandir}/man1
install -m 644 man/*.1 %{buildroot}%{_mandir}/man1

%files
%doc *.txt doc/
%{_bindir}/epydoc
%{_bindir}/epydocgui
%{_bindir}/apirst2html.py
%{_mandir}/man1/*
%{py2_puresitedir}/*

