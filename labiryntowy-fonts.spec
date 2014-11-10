%global fontname labiryntowy
%global shortname flabi
# wersja 1.1

Name:          %{fontname}-fonts
Version:       1.541
Release:       1%{?dist}
Summary:       Conscript (artifical font) letters consist of vertical and horizontal bars. No matter their thickness.
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
%setup -q -c %{fontname}-%{version}-ttf

%build

%install
# This was wrong:
# mkdir -p %{buildroot}-%{shortname}
# cp -p *.ttf %{buildroot}-%{shortname}
# _fontdir expands to /usr/share/fonts/labirintowy
mkdir -p %{buildroot}%{_fontdir}
cp -p *.ttf %{buildroot}%{_fontdir}

# This generates the files section:
%{_font_pkg} %{_fontdir}
# This is useless -- it gets generated with _font_pkg too:
# %files %{buildroot}-%{shortname}/*.ttf
%doc opis.txt opis.pdf

%changelog
* Tue Nov 4 2014 <adres jest niedostepny pl> 1.53
- Initial packaging.
