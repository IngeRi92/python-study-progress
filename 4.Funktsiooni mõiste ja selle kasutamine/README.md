# Tere funktsioon
Hello function
Samm 1:
Kirjuta funktsioon print_hello(), mis prindib ekraanile "Hello". Funktsioonil parameetreid pole.
Samm 2:
Kirjuta funktsioon get_hello(), mis tagastab sõne "Hello". Funktsioonil parameetreid pole.

# Funktsiooni sees
Inside the function
Loo funktsioon inside_the_function().
Kirjutada funktsiooni "sisemus" nii, et igakord kui funktsiooni välja kutsuda, prinditakse konsooli I´m inside the function

# Tüübivihjed
Samm 1:
Kirjuta funktsioon function_string(), mis tagastab sõne. Tagastatava sõne võid ise valida.
Samm 2:
Kirjuta funktsioon function_int(), mis tagatan täisarvu. Tagastatava täisarvu võid ise valida.
Samm 3:
Kirjuta funktsioon function_float(), mis tagastab reaalarvu. Tagastatava reaalarvu võid ise valida.
Samm 4:
Kirjuta funktsioon function_bool(), mis tagastab tõeväärtuse. Tagastatava tõeväärtuse võid ise valida.
Samm 5:
Kirjuta funktsioon function_none(), mis ei tagasta midagi.

# Tabeli printimine
Ülesande eesmärk on kirjutada funktsioon print_table, mis prindib ekraanile tabeli. Tabeli laiuse saad ise määrata (peaks olema vähemalt 5 sümbolit lai). Tabeli read:
Tabeli esimene rida koosneb miinusmärkidest (-).
Tabeli teine rida algab püstkriipsuga (|), sisaldab sinu nime ja lõppeb püstkriipsuga (|).
Tabelis kolmas rida koosneb jälle miinusmärkidest.
Tabeli neljas rida algab püstkriipsuga (|), sisaldab sinu hobi ja lõppeb püstkriipsuga (|).
Tabelis viies rida koosneb jälle miinusmärkidest.
Tabeli ääred peavad olema joondatud (st kõik read sama pikad). Tekst ei pea olema joondatud.
Kuna tabeli jaoks on kolm korda vaja printida täpselt samasugust joont, siis kasutame selleks funktsiooni print_line.
Selleks, et joone printimine print_table funktsioonis välja kutsuda, tuleb õigel hetkel pöörduda funktsiooni poole: print_line() (ehk siis funktsiooni nimi, millele järgnevad sulud).

# Tabeli tagastamine sõnena
Tagasta tabeli sõne
Ülesande eesmärk on kirjutada funktsioon get_table, mis tagastab tabeli sõnena. Tabeli laiuse saad ise määrata (peaks olema vähemalt 5 sümbolit lai). Tabeli read:
Tabeli esimene rida koosneb miinusmärkidest (-).
Tabeli teine rida algab püstkriipsuga (|), sisaldab sinu nime ja lõppeb püstkriipsuga (|).
Tabelis kolmas rida koosneb jälle miinusmärkidest.
Tabeli neljas rida algab püstkriipsuga (|), sisaldab sinu hobi ja lõppeb püstkriipsuga (|).
Tabelis viies rida koosneb jälle miinusmärkidest.
Tabeli ridade vahel (ehk siis iga rea lõpus) on reavahetuse sümbol \n.
Tabeli ääred peavad olema joondatud (st kõik read sama pikad). Tekst ei pea olema joondatud.
Kuna tabeli jaoks on kolm korda vaja kasutada täpselt samasugust joont, siis kasutame selleks funktsiooni get_line.
Selleks, et joone koostamist get_table funktsioonis välja kutsuda, tuleb õigel hetkel pöörduda funktsiooni poole: get_line() (ehk siis funktsiooni nimi, millele järgnevad sulud).
Ladusamaks ülesande lahendamiseks loo muutuja, kus hoiad tabelit, millele lisad read += operaatorit kasutades üks haaval. Reavahetuse saad lisada kasutades sümboleid \n. Tagasta loodud muutuja.