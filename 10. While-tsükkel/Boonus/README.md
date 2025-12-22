# Generate string with random length
Selles funktsioonis kasutame juhuslikke arve. Ülesande sõnastus on järgmine:
koosta sõne, mis koosneb miinusmärkidest (-);
võta üks juhuslik arv vahemikus 0 kuni 1 (random.random());
kui see arv on alla teatud piiri (threshold), siis lisame sõnesse ühe miinusmärgi;
kui see juhuslik arv on üle piiri või piiriga võrdne, siis lõpetame sõne koostamise ära.
Seega, me saame iga kord natuke erineva pikkusega tulemuse.
Juhuslikku arvu saab Pythonis random moodulist funktsiooniga random.random(). See tagastab meile arvu vahemikus 0 kuni 1 (0 on kaasa arvatud, 1 ei ole).

# Asking age from a user
Kirjuta funktsioon, mis küsib kasutajalt tema vanust (What is your age?). Funktsioonile antakse ette alumine vanuspiir. Kasutaja peab sisestama vanuse, mis on suurem-võrdne sellest vanusepiirist ning väiksem-võrdne 100-ga. Kui kasutaja ei sisesta sobivat vanust, prinditakse välja hoiatus ning küsitakse vanust uuesti.
Hoiatused:
kui sisestatud vanus on liiga väike, prinditakse Too young!;
kui sisestatud vanus on liiga suur, prinditakse Too old!.
Kui vanus sobib, siis tagastatakse see arvuna (int).
Eeldame, et kasutaja sisestab ainult täisarve (ei pea kontrollima olukorda, kus sisend ei ole täisarv).
Kui me eelnevalt vaatasime, et while tsüklit on mõistlik kirjutada tingimusega, siis siin ülesandes võib tingimuse kirjelamine olla keerukas. Seda on võimalik teha, aga teine võimalus on kasutada tingimust, mis on alati tõene:
while True: # always repeat
break # the loop will be ended
while True tsükkel on lõputu tükkel - seda jäädaksegi kordama. Tsüklit saab lõpetada selle sees kasutades break korraldust. Samas, kuna return tagastab funktsiooni tulemuse, siis see ühtlasi lõpetab ka tsükli ära. Seega, võib kasutada siin ka lahendust:
while True: # code
if [something]:
return age
Seega, võiks mõelda nii, et meil on lõputu tsükkel, mille jooksul küsitakse kasutajalt tema vanust. Kui vanus sobib, siis võime selle kohe tagastada (ja tsükkel lõppeb sellega ära). Kui vanus ei sobi, siis prindime vastava hoiatuse ja while tsükkel alustab uuesti. Tsükli esimene tegevus peaks olema vanuse küsimine. Seejärel vastavalt tulemusele saab otsustada, mida edasi tehakse.

# Positiivsed arvud, negatiivsed arvud ja null
Kirjuta funktsioon categorize_numbers(numbers: list), mis saab sisendiks arvudest koosneva järjendi numbers. Funktsioon käib ükshaaval läbi järjendis olevad arvud ning türkib välja, mis tüüpi arvuga on tegu.
Kui arv X on nullist suurem, siis trükitakse konsooli X - Positiivne arv.
Kui arv X on nullist väiksem, siis trükitakse konsooli X - Negatiivne arv.
Kui arv X on null, siis trükitakse konsooli X - Null.
NB! Ülesannet tuleb lahendada kasutades while-tsüklit.
Näiteks categorize_numbers([17, -2, 1.7, 0]) korral on konsool järgnev:
17 - Positiivne arv
-2 - Negatiivne arv
1.7 - Positiivne arv
0 - Null
