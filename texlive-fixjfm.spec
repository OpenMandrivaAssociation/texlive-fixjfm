Name:		texlive-fixjfm
Version:	63967
Release:	2
Summary:	Fix JFM (for *pTeX)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fixjfm
License:	knuth
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fixjfm.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fixjfm.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package fixes several bugs in the JFM format. Both LaTeX
and plain TeX are supported.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/generic/fixjfm
%doc %{_texmfdistdir}/doc/generic/fixjfm

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
