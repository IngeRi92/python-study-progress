# Tähtede loetlemine

Funktsioon saab sisendiks järjendi sõnedest. See peab tagastama sõnastiku, kus võtmeks on sõne ning väärtuseks kui mitu erinevat tähte selles sõnes on.

# Leia ühised sõnad lausetest

Funktsioon saab sisendiks kaks lauset. Ülesandeks on leida sõnad, mis kuuluvad mõlemasse lausesse ning mis on ainulaadsed ainult kindlale lausele. Tagastada tuleks vastus ennikuna, mis sisaldab hulki, ehk (hulk1, hulk2, hulk3). Hulk1 on esimesest lauses ainulaadsed sõnad, hulk2 on mõlemast lauses olevad sõnad ja hulk3 on teises lauses ainulaadsed sõnad. Lausetest puuduvad komad, punktid ja muud kirjavahemärgid ehk sellega pole vaja arvestada.

Programm ei ole tõstutundlik ehk näiteks "The" ja "the" peab lugema samaks sõnaks.

# Unikaalsed sõnastiku elemendid

Funktsioon saab sisendiks kaks sõnastikku. Tuleb leida kahest sõnastikust kõik sellised võti-väärtus paarid, mis on unikaalsed mõlema sõnastiku jaoks (ehk leiduvad ainult ühes või teises sõnastikus).

Võite olla kindlad, et kui mõlemas sõnastikus esineb sama võti, siis nende väärtused on samad ehk sellist olukorda ei saa tekkida: dict1 = {"a": 1}, dict2 = {"a": 2}

# airlines_operating_today

Funktsioon tagastab hulga (set) erinevatest lennufirmadest, kes etteantud lennugraafiku järgi lendavad. Funktsiooni sisend on sõnastik kujul "kellaaeg": ("sihtkoht", "lennu tähis") ja sõnastik lennufirmadest kujul "firma kood": "firma nimi". Firma kood on märgitud lennu tähises esimese kolme tähega.
