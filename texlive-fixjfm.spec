%global tl_name fixjfm
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.8
Release:	%{tl_revision}.1
Summary:	Fix JFM (for *pTeX)
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/jptex/generic/fixjfm
License:	knuth
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fixjfm.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fixjfm.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package fixes several bugs in the JFM format. Both LaTeX and plain
TeX are supported.

