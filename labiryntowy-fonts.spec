%global fontname labiryntowy
# wersja 1.2

Name:          %{fontname}-fonts
Version:       1.53
Release:       1%{?dist}
Summary:       Conscript (artifical font) letters consist of vertical and horizontal bars.
License:       OFL
URL:           http://alfabet-ozdobny.appspot.com/?str=labiryntowy
Source0:       https://alfabet-ozdobny.appspot.com/images/Labiryntowy_pl.tgz

BuildArch:     noarch
BuildRequires: fontpackages-devel

Requires:      fontpackages-filesystem

%description
Artifical alphabet. Conscript. Font was created by Jacek Szewczyk as a
practical realization of the idea of the alphabet the labyrinth.
This font contains over 300 ligatures and most of the characters
needed to complete the titles and monograms.

%prep
%setup -q -c

%build

%install
mkdir -p %{buildroot}%{_fontdir}
cp -p *.ttf %{buildroot}%{_fontdir}

%{_font_pkg} %{_fontdir}
%doc opis.txt opis.pdf

%changelog
* Tue Nov 4 2014 <adres jest niedostepny pl> 1.53
- Initial packaging.
