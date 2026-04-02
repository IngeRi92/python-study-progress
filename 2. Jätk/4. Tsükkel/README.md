#  Lühim alamsõne
Kirjuta funktsioon, mis saab sisendiks sõne. Leiab lühima järjestikuse alamsõne, mis koosneb samadest sümbolitest ja tagastab selle pikkuse.

# Liida või lahuta
Kirjuta funktsioon, mille sisendiks on järjend täisarvudest. Tagastab summa järjendi elementidest arvestades järgmisi reegleid:
alustatakse elementide liitmisega
alates esimesest 0 väärtusega elemendist hakatakse arve lahutama
alates teisest 0 väärtusega elemendist hakatakse arve jälle liitma
ehk siis iga 0 väärtusega element pöörab operatsiooni (liitmine, lahutamine)

#  Inflatsioon
On antud funktsioon, mille parameetriteks on positiivsed täisarvud (int) n ja goal. Sinu ülesanne on suurendada etteantud arvu n kuni see jõuab vähemalt eesmärgini goal. Juhul kui arv on piisavalt suur, tuleb see esimesel võimalusel tagastada - seda ei tohi enam suurendada. Siin ülesandes tuleb kasutada While-tsüklit. Arvu suurendamiseks on ettenähtud reeglid. Igal tsükli iteratsioonil (käivitumisel) tuleb arvu suurendada vaid ühe korra, mis tähendab, et käivitub ainult üks tingimuslause (vaata if-elif-else).
Reeglid arvu suurendamiseks:
Kui n on parasjagu täpselt poole väiksem eesmärgist goal, tuleb n läbi korrutada kahega (Tähtsaim).
Kui n parasjagu neljakohaline arv, tuleb ta läbi korrutada 2-ga.
Kui n on parasjagu kolmekohaline arv, tuleb ta läbi korrutada 3-ga.
Kui n on parasjagu kahekohaline arv, tuleb ta läbi korrutada 4-ga.
Kui n on parsajagu ühekohaline arv, tuleb ta läbi korrutada 5-ga.
Muul juhul tuleb n läbi korrutada 7-ga.

#  Algarv
is_prime_number(number: int) -> bool:
Funktsioon saab argumendina ühe täisarvu, ning peab kontrollima, kas see arv on algarv. Funktsioon tagastab vastavalt kas True või False.
Algarv on arv, mis jagub ainult 1 ja iseendaga
0 ega 1 ei ole algarvud
