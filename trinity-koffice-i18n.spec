%bcond clang 1

# TDE variables
%define tde_pkg koffice-i18n
%define tde_prefix /opt/trinity

%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%undefine _debugsource_template

%define tarball_name %{tde_pkg}-trinity


Name:		trinity-%{tde_pkg}
Version:	14.1.6
Release:	1
Summary:	Internationalization support for Koffice [Trinity]
Group:		User Interface/Desktops
URL:		http://www.trinitydesktop.org/

License:	GPLv2+

BuildArch:	noarch

# Speed build options
%undefine debug_package
%undefine __spec_install_post
AutoReq: no

Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{version}/main/applications/office/%{tarball_name}-%{version}.tar.xz
Source1:	  trinity_koffice_lang.macro

# NOTE This load's the template macro definitions
# NOTE which includes the _trinity_koffice_lang_template* macros use in this spec file
# NOTE do not delete this line, else everything using these defines will break.
%{load:%{S:1}}

BuildSystem:    cmake
BuildOption:    -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DINCLUDE_INSTALL_DIR=%{tde_prefix}/include/tde
BuildOption:    -DPKGCONFIG_INSTALL_DIR=%{tde_prefix}/%{_lib}/pkgconfig
BuildOption:    -DBUILD_ALL=ON
BuildOption:    -DBUILD_DOC=ON
BuildOption:    -DBUILD_DATA=ON
BuildOption:    -DBUILD_MESSAGES=ON

BuildRequires:	trinity-tdelibs-devel >= %{version}
BuildRequires:	trinity-tdebase-devel >= %{version}
BuildRequires:  trinity-tde-cmake >= %{version}
BuildRequires:	desktop-file-utils
BuildRequires:	findutils
BuildRequires:	gettext

%{!?with_clang:BuildRequires:    gcc-c++}

BuildRequires:	pkgconfig


%description
%{summary}.

# NOTE In order to generate these, check and run the create_language_templates.sh
# NOTE script which generates the trinity_koffice_lang_template.in file.
# NOTE If any entries have @ symbols, check its ISO 639 language code and
# NOTE insert the ISO-639 languiage code as a third entry in-
# NOTE create_language_templates.sh, replacing those @ symbils with hyphens -
# NOTE then change the remplate type to %%_trinity_koffice_lang_template_alt which
# NOTE handles 3 parameter values, then copy and paste the contents of-
# NOTE trinity_koffice_lang_template.in and paste here to overwrite the below.
# NOTE This creates %%package entries for all languages provided.
%_trinity_koffice_lang_template Bulgarian bg
%_trinity_koffice_lang_template Catalan ca
%_trinity_koffice_lang_template Czech cs
%_trinity_koffice_lang_template Kashubian csb
%_trinity_koffice_lang_template Welsh cy
%_trinity_koffice_lang_template Danish da
%_trinity_koffice_lang_template German de
%_trinity_koffice_lang_template Greek el
%_trinity_koffice_lang_template British en_GB
%_trinity_koffice_lang_template Spanish es
%_trinity_koffice_lang_template Estonian et
%_trinity_koffice_lang_template Basque eu
%_trinity_koffice_lang_template Farsi fa
%_trinity_koffice_lang_template Finnish fi
%_trinity_koffice_lang_template French fr
%_trinity_koffice_lang_template Irish ga
%_trinity_koffice_lang_template Galician gl
%_trinity_koffice_lang_template Hungarian hu
%_trinity_koffice_lang_template Italian it
%_trinity_koffice_lang_template Japanese ja
%_trinity_koffice_lang_template Khmer km
%_trinity_koffice_lang_template Latvian lv
%_trinity_koffice_lang_template Malay ms
%_trinity_koffice_lang_template Norwegian-Bokmal nb
%_trinity_koffice_lang_template Low-Saxon nds
%_trinity_koffice_lang_template Nepali ne
%_trinity_koffice_lang_template Dutch nl
%_trinity_koffice_lang_template Polish pl
%_trinity_koffice_lang_template Portuguese pt
%_trinity_koffice_lang_template Brazil pt_BR
%_trinity_koffice_lang_template Russian ru
%_trinity_koffice_lang_template Slovak sk
%_trinity_koffice_lang_template Slovenian sl
%_trinity_koffice_lang_template Serbian sr
%_trinity_koffice_lang_template_alt Serbian-Latin sr@Latn sr-Latn
%_trinity_koffice_lang_template Swedish sv
%_trinity_koffice_lang_template Turkish tr
%_trinity_koffice_lang_template Ukrainian uk
%_trinity_koffice_lang_template Chinese zh_CN
%_trinity_koffice_lang_template Chinese-Big5 zh_TW

##########
%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_prefix}/bin:${PATH}"

%install -a
# remove zero-length file
find "%{buildroot}%{tde_prefix}/share/doc/tde/HTML" -size 0 -exec rm -f {} \;

# remove obsolete KDE 3 application data translations
%__rm -rf "%{buildroot}%{tde_prefix}/share/apps"
