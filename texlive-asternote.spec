Name:		texlive-asternote
Version:	63838
Release:	2
Summary:	Annotation symbols enclosed in square brackets and marked with an asterisk
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/asternote
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/asternote.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/asternote.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX package can output annotation symbols enclosed in
square brackets and marked with an asterisk.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/asternote
%doc %{_texmfdistdir}/doc/latex/asternote

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
