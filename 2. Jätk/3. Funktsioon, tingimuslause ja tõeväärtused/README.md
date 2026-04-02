# Õige pikkusega parool

Kirjuta funktsioon is_correct_length(password: str), mis kontrollib, kas funktsioonile argumendina antud parool on sobiva pikkusega. Funktsioon tagastab True kui parooli pikkus on vahemikus 8-64 sümbolit, False kui parool on lühem kui 8 või pikem kui 64 tähemärki.

# Sooduspakkumine

Liiga palju inimesi on kurtunud, et R-kioski hotdogi hind on liiga kalliks läinud ja normaalse hinnaga saab ainult õpilaspakkumise. R-kiosk otsustas luua uue sooduspakkumise ka töötajatele. Soodustuse saamiseks on kriteeriumid järgmised:

Isik peab olema vähemalt 18-aastane.
Isikul peab olema kehtiv ID-kaart.
Isik peab olema kas õpilane või töötaja.
Kirjuta funktsioon is_eligible(age, has_valid_id, is_student, is_employed), mis võtab sisendiks järgmised parameetrid:

age (int): Inimese vanus.
has_valid_id (bool): Kas inimesel on kehtiv ID-kaart.
is_student (bool): Kas inimene on õpilane.
is_employed (bool): Kas inimene on töötaja.
Funktsioon peaks tagastama True, kui inimene on soodustuse jaoks sobilik, ja muul juhul False.

# Kehamassiindeksi kalkulaator
Kirjuta funktsioon bmi_calculator(height, weight), mis arvutab kaalu ja pikkuse põhjal välja kehamassiindeksi. Funktsioon võtab argumendiks inimese pikkuse meetrites ja kaalu kilogrammides.
KMI(BMI) = kaal / pikkus^2
Kui BMI on väiksem võo võrdne 18.5 tagastab "Alakaaluline"
Kui BMI on väiksem või võrdne 25.0 tagastab "Normaalkaalus"
Kui BMI on väiksem või võrdne 30.0 tagastab "Ülekaaluline"
Kui BMI on suurem kui 30 tagastab "Rasvunud"

# Kalkulaator Pythonis
Kirjuta funktsiooni calculator, mis toimib lihtsa kalkulaatorina. Funktsioon saab sisendina kaks arvu täisarvudena ja matemaatilise operatsiooni sõnena.
Programmi tulemus peab olema vastavalt valitud operatsioonile arvutatud väärtus, mis on ümardatud lähima täisarvuni.
Kui kasutaja üritab jagada nulliga, peab programm tagastama "Error".

#  Arvu teisendamine
Kirjeldus
Kirjuta funktsioon modify_number, mis võtab sisendiks täisarvu x ja teeb erinevaid teisendusi sõltuvalt arvu omadustest:
Kui arv x jagub viiega, kahekordista see.
Kui arv x jagub kahega, kolmekordista see.
Kui arv x jagub nii kahe kui viiega, korruta arv sajaga.
Kui arv x on null, tagasta 0.
Kui ükski eelnevatest tingimustest ei kehti, lisa arvule 10.
Funktsioon peab tagastama teisendatud väärtuse.

# Isikukoodi numbrid, nende tähendused ja piirangud
Siin on vikipeedia artikkel, kus on 2. - 4. osa ülesannete lahendamiseks kõik vajalik olemas.
Isikukood koosneb täpselt 11 numbrist. Numbrite tähendused:
esimene number:
1 - aastatel 1800-1899 sündinud mees
2 - aastatel 1800-1899 sündinud naine
3 - aastatel 1900-1999 sündinud mees
4 - aastatel 1900-1999 sündinud naine
5 - aastatel 2000-2099 sündinud mees
6 - aastatel 2000-2099 sündinud naine
teine ja kolmas number:
sünniaasta 2 viimast numbrit (nt 01, 75 jne kuni 99)
neljas ja viies number:
sünnikuu number (nt jaanuar - 01, veebruar - 02 jne, kuni 12)
kuues ja seitsmes number:
sünnikuupäeva number (nt 01, 08, 20 jne kuni 28, 29, 30 või 31 vastavalt sünnikuule)
kaheksas, üheksas ja kümnes number: Isikukoodi väljastava asutuse tunnus
kaheksas ja üheksas number tähistab haigla tunnuseid _(nt 001...010 = Kuressaare Haigla), kümnes number on järjekorra number.
Siin on välja toodud mõned võimalikud asukohad, kus inimene on sündinud. Need asukohad peavad olema kasutatud ID code 3. osa funktsioonis get_birth_place, kus tuleb tagastada üks allolevatest linnadest.
001...010 = Kuressaare
011...020 = Tartu
021...220 = Tallinn
221...270 = Kohtla-Järve
271...370 = Tartu
371...420 = Narva
421...470 = Pärnu
471...710 = Tallinn
711...999 = undefined
Ülesandes lähtume sellest, et kaheksas, üheksas ja kümnes number moodustavad kolmekohalise koodi. Kõige väiksem võimalik kood on 001, kõige suurem 999. See kood tähistab sünnikohta vastavalt eelnevale tabelile.
Täienda faili järgnevate funktsioonidega
Allpool leiduvas mallis on olemas ka näited
Funktsioonid, mis tuleb ise kirjutada
Kirjuta funktsioon nimega is_valid_gender_number, mis saab sisendiks isikukoodi esimese numbri arvuna (int) ning kontrollib soo numbrit, tagastab True või False vastavalt sellele, kas isikukoodi esimene number on õige.
Kirjuta funktsioon get_gender, mis saab sisendiks isikukoodi esimese numbri arvuna (int) ning tuvastab isiku soo isikukoodi esimese numbri põhjal, tagastab sõne, milleks on: female või male
Funktsioonid, mis on juba mallis kaasas
is_valid_year_number(year_number: int) - kontrollib aasta numbreid, tagastab True või False
is_valid_month_number(month_number: int) - kontrollib kuu numbreid, tagastab True või False
is_valid_serial_number(serial_number: int) - kontrollib sündinu järjekorranumbrit, tagastab True või False
Kirjuta funktsioon is_leap_year, mis saab sisendiks aasta numbri arvuna ning tagastab True, kui tegu on liigaastaga ning False, kui tegu pole liigaastaga.
Liigaasta
Aasta, mis jagub neljasajaga, on alati liigaasta.
Liigaasta on ka aasta, mis jagub neljaga, kuid ei jagu samal ajal sajaga.
Kui aasta jagub sajaga ja ei jagu neljasajaga, siis ta ei ole liigaasta.
Funktsioonid, mis on juba mallis kaasas
get_full_year(gender_number: int, year_number: int) - tuvastab isikukoodi soo number ja 2-kohalise aasta numbrite abil 4-kohalise aastanumbri - 1839, 1948 või 2000.
get_birth_place(birth_number: int) - Tagastab linna nime, kus inimene on sündinud. Vajalikud linnade nimed on üleval pool välja toodud. Kui linnanime ei leidud, siis tagastab undefined. NB! Vaata, et linnade nimed algaksid suurte algustähtedega. Siin on hea kasutada funktsiooni is_valid_birth_number, et kontrollida, kas tegu on korrektse numbriga. Kui tegu on ebakorrektse numbriga, siis tagastada string - Wrong input! .