%define pkgname notcouriersans

Summary:	Re-interpretation of Nimbus Mono
Name:		fonts-ttf-notcouriersans
Version:	1.1
Release:	1
License:	GPLv2 with font exception
Group:		System/Fonts/True type
URL:		http://ospublish.constantvzw.org
Source0:	%{pkgname}.zip
BuildArch:	noarch
BuildRequires:	freetype-tools

%description
NotCourierSans is a re-interpretation of Nimbus Mono whose design began
in Wroclaw at the occasion of the Libre Graphics Meeting 2008. For more
detailed information explore the files included in the font package
(FONTLOG.txt). The 1.1 version has been expanded by a work on Cyrillic
glyphs by Paulo Silva aka nitrofurano. NotCourierSans 1.1 contains 2 ornamental
glyphs encoded in the private use characters: - in U+E000, the OSP frog mascot
- in U+E001, the 75 ligature added during an OSP workshop in Le 75, École
Supérieure des Arts de l’Image, on Wednesday 17 December. These sugars are
accessible through the Ornament Open Type features.

%prep
%setup -q -n OSP_NotCourierSans

%build

%install
%__rm -rf %{buildroot}

%__mkdir_p %{buildroot}%{_xfontdir}/TTF/notcouriersans

%__install -m 644 *.ttf %{buildroot}%{_xfontdir}/TTF/notcouriersans
ttmkfdir %{buildroot}%{_xfontdir}/TTF/notcouriersans -o %{buildroot}%{_xfontdir}/TTF/notcouriersans/fonts.dir
%__ln_s fonts.dir %{buildroot}%{_xfontdir}/TTF/notcouriersans/fonts.scale

%__mkdir_p %{buildroot}%_sysconfdir/X11/fontpath.d/
%__ln_s ../../..%{_xfontdir}/TTF/notcouriersans \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-notcouriersans:pri=50

%files
%doc FONTLOG.txt COPYING.txt
%dir %{_xfontdir}/TTF/notcouriersans
%{_xfontdir}/TTF/notcouriersans/*.ttf
%verify(not mtime) %{_datadir}/fonts/TTF/notcouriersans/fonts.dir
%{_xfontdir}/TTF/notcouriersans/fonts.scale
%{_sysconfdir}/X11/fontpath.d/ttf-notcouriersans:pri=50


%changelog
* Wed Dec 14 2011 Dmitry Mikhirev <dmikhirev@mandriva.org> 1.1-1
+ Revision: 741073
- imported package fonts-ttf-notcouriersans

