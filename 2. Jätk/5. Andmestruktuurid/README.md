# Parooli valideerimine

Funktsioon includes_uppercase(password: str) kontrollib, kas funktsioonile argumendina antud parool sisaldab vähemalt ühte suurtähte. Siin sobiks kasutada näiteks sõne sisseehitatud meetodit .isupper(). Funktsioon tagastab True kui parool sisaldab vähemalt ühte suurtähte, False kui ei sisalda.
Funktsioon includes_lowercase(password: str) kontrollib, kas funktsioonile argumendina antud parool sisaldab vähemalt ühte väiketähte. Sarnaselt eelmise funktsiooniga on ka selle kontrolli tegemiseks Pythonis sissehitatud meetod olemas - .islower(). Funktsioon tagastab True kui parool sisaldab vähemalt ühte väiketähte, False kui ei sisalda.
Funktsioon includes_number(password: str) kontrollib, kas funktsioonile argumendina antud parool sisaldab vähemalt ühte numbrit. Kontrolli tegemisel on abiks meetod .isdigit(). Funktsioon tagastab True kui parool sisaldab vähemalt ühte numbrit, False kui ei sisalda.

# Leia paaritud arvud

Kirjuta funktsioon, mis tagastab hulga, kus on kõik paaritud arvud, mis on kas hulgas set_a või hulgas set_b, aga mitte mõlemas korraga.

# Poole järjendi summa

Kirjuta funktsioon, mis saab sisendiks täisarvude järjendi. Tagastab summa esimesest poolest paarisarvudest. Kui paarisarve on paaritu arv, siis keskmine arv läheb summas arvesse.

# Sõnastik

unique_dict_items
Funktsioon saab sisendiks kaks sõnastikku. Tuleb leida kahest sõnastikust kõik sellised võti-väärtus paarid, mis on unikaalsed mõlema sõnastiku jaoks (ehk leiduvad ainult ühes või teises sõnastikus).
Võite olla kindlad, et kui mõlemas sõnastikus esineb sama võti, siis nende väärtused on samad ehk sellist olukorda ei saa tekkida:
dict1 = {"a": 1}, dict2 = {"a": 2}

# Leia Kõige Sagedamini Esinev Täht

Sulle on antud sõne s, mis sisaldab nii tähti kui ka sümboleid. Sinu ülesanne on kirjutada funktsioon, mis leiab ja tagastab tähe, mis esineb sõnes kõige sagedamini.
Suur- ja väiketähed loetakse samaks tähtedeks.
Sümboleid ei loeta tähtedeks.

# Hulk

Sümbolite kogus sõnes
Kirjuta funktsioon, mis leiab erinevate sümbolite koguse sõnes. Suur ja väiketäht lähevad eraldi arvesse.
Tähtede kogus sõnes
Kirjuta funktsioon, mis leiab erinevate ladina tähtede (a-z) koguse sõnes. Siin suur ja väiketäht lähevad ühena arvesse. Ehk siis "hH" sisaldab ühte erinevat tähte.
Siin on mõistlik leida ühisosa ladina tähestikuga. Tähestiku saab importida näiteks string moodulist: string.ascii_lowercase annab kõik väikesed ladina tähed tähestikulises järjestuses.
Täpselt kaks külastust
Kirjuta funktsioon, mis leiab üles inimesed, kes on külastanud täpselt kahte sündmust kolmest. Ette antakse kolm listi. Iga list tähistab, kes vastaval sündmusel käis. Tuleb neida need nimed, mis einevad kahes listis, aga ei esine kolmandas. Nimed ühes nimekirjas võivad korduda (kui John on kaks või rohkem korda nimekirjas, siis ta on seda sündmust külastanud). Siin john ja John on erinevad nimed.
Siin on mõistlik kaustada hulgaoperatsioone, muidu läheb lahendus pikaks ja arvatavasti aeglaseks.

# Lennujaam

Lõpetamise nõuded
Tehtud: Läbi tegevus
Ülesande teemad on sõnastik (dictionary) ja hulk (set).
Ülesandes saad sõnastikke ja hulkasid kasutades organiseerida ühe lennujaama lennugraafikut.
Abimaterjalid
Sõnastik
Hulk
Ülesanne
Ülesande funktsioonides kasutame lendude infot järgmisel kujul:
[
"Tallinn,08:00,01h30m,OWL1234",
"Helsinki,10:35,01h00m,BHM5678",
]
Tegemist on järjendiga, kus igal real on ühe lennu andmed sõnena. Lennu andmed on komaga eraldatud ning järjestus on selline:
sihtkoht
lennu väljumisaeg (kogu andmestikus pole korduvaid kellaaegu)
lennu kestus
lennu number, kus esimesed kolm tähte tähistavad lennufirma koodi
Vaja on realiseerida järgmised funktsioonid:
destinations_and_times - funktsioon loob (ja tagastab) sõnastiku, kus võti on sihtkoht ja väärtus on järjend kõikidest väljumisaegadest sellesse sihtkohta. Võtmete ja väärtuste järjekord ei ole oluline. Mõte: kuna väärtuste järjekord ei ole oluline, võivad need olla ka juba järjestatud kasvavalt.
sort_dict_values - funktsioon tagastab sõnastiku, kus algse sõnastiku võtmed on järjestatud kasvavalt. Seda funktsiooni saab rakendada eelmise funktsiooni tulemuse peal, et kõik väljumisajad ühe sihtkoha jaoks oleksid järjestatud kasvavalt.
flights_to_destination - funktsioon tagastab järjendi väljumisaegadest (kasvavad järjekorras) otsitud sihtpunkti. Kui otsitud sihtpunkti ei välju ühtegi lendu, siis tagastab tühja listi.
