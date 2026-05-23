# read the spec file documentation before you break things.
# this file generates trinity-lang-template.in file
# which contains lines to be inserted in the spec file.
language=$(cat <<'EOF'
Bulgarian bg
Catalan ca
Czech cs
Welsh cy
Danish da
German de
Greek el
British en_GB
Spanish es
Estonian et
Basque eu
Farsi fa
Finnish fi
French fr
Irish ga
Galician gl
Hungarian hu
Italian it
Japanese ja
Khmer km
Latvian lv
Malay ms
Norwegian-Bokmal nb
Low-Saxon nds
Nepali ne
Dutch nl
Polish pl
Portuguese pt
Brazil pt_BR
Russian ru
Slovak sk
Slovenian sl
Serbian sr
Serbian-Latin sr@Latn sr-Latn
Swedish sv
Turkish tr
Ukrainian uk
Chinese zh_CN
Chinese-Big5 zh_TW
EOF
)

while IFS= read -r line;
do
LANG=$(echo $line | tr -s ' ' | cut -d " " -f1)
ABBR=$(echo $line | tr -s ' ' | cut -d " " -f2)
ALT=$(echo $line | tr -s ' ' | cut -d " " -f3)

if [[ -n $ALT ]]; then
echo %_trinity_koffice_lang_template_alt $LANG $ABBR $ALT >> trinity_koffice_lang_template.in;
else
echo %_trinity_koffice_lang_template $LANG $ABBR >> trinity_koffice_lang_template.in;
fi
sed -i '/^$/d' trinity_koffice_lang_template.in
done <<< "$language"

