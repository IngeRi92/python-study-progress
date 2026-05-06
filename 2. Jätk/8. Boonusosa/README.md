# Boonusülesanne 1: Regulaaravaldis

Regulaaravaldis (regular expression e. regex) on formaalne viis tekstis leiduva mustri kirja panemiseks. Mustriks võib olla näiteks meiliaadress või telefoninumber.

Regulaaravaldis tuleb ette pea igasugusel tehnilisel positsioonil, olgu see arendajana sisendi töötlemine või administraatorina käsureal konfiguratsioonifailide redigeerimine.

Pythonis on regulaaravaldistega töötamiseks tehtud moodul re. Moodulil re on palju erinevaid funktsioone regulaaravaldisele vastava alamsõne leidmiseks sõnest, näiteks search(), findall() ja finditer().

Regexi kirjutamiseks on hea abivahend lehel: https://regex101.com/

Ülesannete kirjeldused:
def find_a_triplets(string) - funktsioon, mis saab sisendiks sõne string ja tagastab järjendi selle sõne kõikidest "a" tähtedest koosnevatest kolmikutest. Siin loeme ainult "a" tähti, mis on kirjutatud väikse tähena.

def find_words(string) - funktsioon, mis saab sisendiks sõne string ja tagastab järjendi selle sõne kõikidest sõnadest. Sõnadeks loeme selles funktsioonis niisuguseid täheühendeid, mis algavad ühe suure tähega ning koosnevad veel vähemalt ühest (aga võib ka rohkemast) väiksest tähest. Tähed võivad olla ka täpitähed.

def find_address(string) - funktsioon, mis saab sisendiks sõne string ja tagastab järjendi kõikidest leitud aadressidest. Aadress koosneb tänavast, mis on kirjutatud ühe sõnaga, vahega ning maja numbriga, näiteks Kloostri 16 oleks sobiv aadress. Tänava nimi algab suure tähega ning tähed võivad olla ka täpitähed ('õäöü').

def find_birth_year_from_21st_century(string) - funktsioon, mis saab sisendiks sõne string ja tagastab järjendi kõikidest aastaarvudest alates 21. sajandist ehk algusega 2001 ja suuremad. Kõik numbrikombinatsioonid on eraldatud vahedega. Teie peate kõikidest numbritest filtreerima välja ülesandele sobivad aastaarvud. Järjendis esitada aastaarvud sõnena.

def find_sentences(string) - funktsioon, mis saab sisendiks sõne string ja tagastab järjendi selle sõne kõikidest lausetest. Lause algab alati suure tähega ja lõpeb lauselõpumärgiga (.!?). Lause sees võivad olla sõnad, komad, koolonid, kriipsud ja vahed. Tähed võivad olla ka täpitähed ('õäöü').

def capture_month_year_group(string) - funktsioon, mis saab sisendiks sõne string. See ülesanne hõlmab endas gruppe. Teie peate koostama funktsiooni, mis leiab sõnest kõik kuu ja aastaarvu funktsiooni. Kõik kuud on esitatud 3 tähelise lühendina (January - Jan, February - Feb, March - Mar, jne). 1. grupp koosneb kuust ja aastaarvust, näiteks (Jan 2003) ning 2. grupp ainult aastaarvust (2003).

def born_month_and_year(string) - funktsoon, mis saab sisendiks sõne string. Teie ülesandeks on tagastada list lausetest, kus iga lause on kujul "Born in {kuu} in {aastaarv}". Selle ülesande eesmärk on õpetada, kuidas gruppe välja kutsuda. Gruppide leidmiseks kasutage eelmist funktsiooni.

def search_for_id_code(string) - funktsoon, mis saab sisendiks sõne string. Teie ülesandeks on leida sõnest 21. sajandi ID kood, mis võib esineda ka see aasta, ehk tuleviku omad ei loe. Sobiv ID kood on selline, mis algab kas numbriga 5 või 6, aastaarvu number on vahemikus 01 - 23, kuu number vahemikus 01 - 12, päeva number vahemikus 01 - 31. Liigaastaid me siin ei kontrolli. Viimased 4 numbrit on ka suvalised. Siin ülesandes oleks mõistlik kasutada re.search, sest teie peate tagastama "Persons ID code is {id kood}." juhul kui ID kood on leitav. Kui ID koodi ei leita, tagastada sõne "ID code can't be found."

# Boonusülesanne 2: Ajatabel

Ajaplaan
Kirjuta programm, mis leiab tekstist kellaajaga märgistatud sõned ja koostab nende põhjal ajaplaani tabeli.

Tabel koostatakse järgmiste reeglite alusel:

tabelil on kaks veergu, mille pealkirjad on "time" ja "entries"
veeru laius otsustatakse sisu järgi, st veeru laius on kõige laiema sisu laius + 2 (mõlemal pool tühik)
tabeli päise rea ees (üleval) ja järel (all) on vaid - (miinus) märkidest koosnev rida
ülejäänud tabeli ridade ääred ja veergude eraldaja on püstkriips (|)
tabelis on kellaaeg kujul "01:12 PM", "12:00 AM" jne. Vt https://en.wikipedia.org/wiki/12-hour_clock
kellaaja minutid ja tunnid on kahekohalised ehk "1:1 PM" asemel on õige "01:01 PM"
tabelis on ajaplaani read sorditud kellaaja järgi kasvavalt (nagu on loogiline ajaplaani koostada)
tabelis kellaajale vastavad tegevused on väikeste tähtedega (isegi kui tekstis olid suured tähed), korduvaid elemente pole ning ühel kellaajal on ainult üks tegevus
kui ühtegi ajaplaani sobivat sisendit ei leidu tekstis, kuvatakse sisu ridade all vastav tekst No entries found:

---

## | time | entries |

## | No entries found |

Tekstist loetakse välja järgmised andmed:

kellaaeg peab sisaldama tunde ja minuteid
tund võib olla 1- või 2-kohaline (1, 01 ja 11)
minut võib olla 1- või 2-kohaline (2, 02 ja 22)
tekstis on kellaaeg 24-tunni formaadis
minimaalne kellaaeg on 00:00 (või 0:0 või 0,00 või 00-0 jne)
maksimaalne kellaaeg on 23:59 (või 23!59)
tunni ja minuti vahel võib olla ükskõik mis eraldaja, välja arvatud number (01:11, 1.2, 6,5, 1a4 on kõik lubatud, 12345 ei ole lubatud
kellaajale järgnev sõna loetakse selle kellaaja tegevuseks
kellaaja ja tegevuse vahel võib üks või rohkem tühikut olla
kellaajale eelneb alati tühik või reavahetus
tegevus sisaldab vaid ladina tähti, ehk siis tegevus lõppeb seal, kus tuleb mõni mitte ladina täht (näiteks "aa,aa" => "aa", "abc2de" => "abc", "tere!" => "tere", "12" => "")
tabelisse lähevad vaid need tegevused, mille pikkus on vähemalt 1 sümbol
Mall
"""Create schedule from the given text."""

def create_schedule_string(input_string: str) -> str:
"""Create schedule table string from the given input string."""
pass

if **name** == '**main**':
print(create_schedule_string("wat 11:00 teine tekst 12:0 jah ei 10:00 pikktekst "))
Kuigi mallis on ette antud vaid 3 funktsiooni, tuleks mugavamaks lahendamiseks luua lisafunktsioone. Mõtle siin kuidas sa saaksid loogiliselt koodi osadeks (funktsioonideks) jagada. Näiteks võiksid sul olla järgmised funktsioonid:

Võimalikud lisafunktsioonid

def create_table(...):
"""Create table."""
pass

def get_table_sizes(...):
"""Get the maximum sizes for table."""
pass

def normalize(...):
"""Add missing 0's to the minutes and remove extra 0's from hours."""
pass

def get_formatted_time(...):
"""Format 24 hour time to the 12 hour time."""
pass
Need on ainult võimalikud funktsioonid, kuid sinu loogika võib erineda sellest. Oluline on jälgida, et kood on jagatud loogilisteks (väikesteks) tükkideks ning üks tükk täidab ainult ühte (lihtsat) funktsiooni.

Sisendtekst
Näiteks võib proovida sellist sisendit:

A 11:00 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sed euismod nibh, non vehicula libero. Fusce ac eros
lectus. Pellentesque interdum nisl sem, eget facilisis mauris malesuada eget. Nullam 10:0 a bibendum enim. Praesent dictum
ante eget turpis tempor, porta placerat dolor ultricies. Mauris quis dui porttitor, ultrices turpis vitae, pulvinar nisl.
Suspendisse potenti. Ut nec cursus sapien, convallis sagittis purus. Integer mollis nisi sed fermentum efficitur.
Suspendisse sollicitudin sapien dui, vitae tempus lacus elementum ac. Curabitur id purus diam. 24:01 Donec blandit,
est nec semper convallis, arcu libero lacinia ex, eu placerat risus est non tellus.

Orci varius natoque penatibus et magnis dis 0:12 parturient montes, nascetur ridiculus mus. Curabitur pretium at metus
eget euismod. Nunc sit amet fermentum urna. Maecenas commodo ex turpis, et malesuada tellus sodales non. Fusce elementum
eros est. Phasellus nibh magna, tincidunt eget magna nec, rhoncus lobortis dui. Sed fringilla risus a justo tincidunt,
in tincidunt urna interdum. Morbi varius lobortis tellus, vitae accumsan justo commodo in. 12:001 Nullam eu lorem leo.
Vestibulum in varius magna. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.
0:00 Aliquam ac velit sit amet nunc dictum aliquam pulvinar at enim. Nulla aliquam est quis sem laoreet, eu venenatis
risus hendrerit. Donec ac enim lobortis, bibendum lacus quis, egestas nisi.

08:01 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sed euismod nibh, non vehicula libero. Fusce ac eros
lectus. Pellentesque interdum nisl sem, eget facilisis mauris malesuada eget. Nullam :19 a bibendum enim. Praesent
dictum ante eget turpis tempor, 30:0 porta placerat dolor ultricies. Mauris quis dui porttitor, ultrices turpis vitae,
pulvinar nisl. Suspendisse potenti. Ut nec cursus sapien, convallis sagittis purus. 8:8 Integer mollis nisi sed fermentum
efficitur. Suspendisse sollicitudin sapien dui, vitae tempus lacus elementum ac. Curabitur id 018:19 purus
diam. 18::9 Donec blandit, est nec semper convallis, arcu 7.01 libero lacinia ex, eu placerat risus est non tellus.

11:0 lorem
0:60 bad
1:2 goodone yes
15:0 nocomma,
18:19 Yes-minus
21:59 nopoint.
23-59 canuseminusthere 22,0 CommaIsAlsoOk
5:6
Väljund
Eelnev tekst annab järgmise tulemuse:

---

## | time | entries |

| 12:00 AM | aliquam |
| 12:12 AM | parturient |
| 01:02 AM | goodone |
| 07:01 AM | libero |
| 08:01 AM | lorem |
| 08:08 AM | integer |
| 10:00 AM | a |
| 11:00 AM | lorem |
| 03:00 PM | nocomma |
| 06:19 PM | yes |
| 09:59 PM | nopoint |
| 10:00 PM | commaisalsook |
| 11:59 PM | canuseminusthere |

---

Ja mallis toodud koodi käivitamisel annab printimine sellise:

---

## | time | entries |

| 10:00 AM | pikktekst |
| 11:00 AM | teine |
| 12:00 PM | jah |

---

Vihjeid
Arutleme, millised sammud oleksid mõistlikud ülesande lahendamiseks:

luua regulaaravaldis, millega saab kellaaegu leida
regulaaravaldisega leida kõik kellaajad ja vastavad tegevused
vajadusel tuleb ebasobivad kellaajad kõrvale jätta
luua sõnastik, kus kellaaeg on võti ja väärtus on tegevus
sõnastik sorteerida
koostada sorteeritud tulemuse pealt tabel sõnena ja see tagastada
Vaatame järgnevalt sammu natuke põhjalikumalt.

Regulaaravaldise koostamine
Kopeeri näidistekst (see pikem) regex101 lehele teksiosasse. Nüüd hakka üles regulaaravaldist kirjutama, mis kattuks vaid sobivate kohtadega tekstis. Soovitusi:

kasuta gruppe (sulge) näiteks tundide ja minutite ümber, sedasi on hiljem lihtsam vastavad väärtused kätte saada
ei pea tingimata valideerima kõike regexiga. Näiteks tundide/minutite lubatud piiri on pythonis palju lihtsam kontrollida
oma regexi kontrollimiseks on tarvis ja mõistlik kasutada regex101 keskkonda.
Regulaaravaldis Pythonisse
Võta järgnev kood:

import re

def create_schedule_string(input_string: str) -> str:
for match in re.finditer(r"REGEX", input_string):
print(match)
Seal tsükli sees on sul nüüd olemas kõik need kattumised tekstis, kus muster sobib. See tähendab, et saad loodetavasti kätte kellaaja ja vastava tegevuse. Nüüd sõltub sellest, kas oled gruppe kasutanud või mitte. Kui oled, siis võib-olla piisab täitsa sellest, et saad näiteks tundide arvu kätte match.group(1), minutite arvu match.group(2) ja tegevuse match.group(3) .

See tsükkel on ühtlasi ka koht, kus võid ignoreerida näiteks tundi, mille väärtus on 66.

Sõnastiku loomine
Eelnevalt loodud tsükli sees on mõistlik hakata täitma sõnastikku. Me proovime koostada sõnastiku, kus kellaajale vastab tegevus. Täpsemalt, kellaajale vastab sõne.

Siinkohal on mõistlik hoida kellaaegu mingil "normaalsel" kujul (mitte 12-tunni formaadis). Näiteks on sobilikud:

tunnid ja minutid sõnena ja kooloniga. Selleks, et hiljem oleks mugavam sortida, võiks ühekohalised olla 0-ga täiendatud. Näiteks: "01:01", "11:00", "12:22" jne.
minutid arvuna, näiteks 61, 660, 742 jne.
vms
Seega, kõigepealt peab tsüklis looma võtme. Näiteks võtate tunni ja minuti väärtused ja panete kokku sõnena "01:02".

Seejärel tuleb lisada selle võtmega uus tegevus.

Sõnastiku sortimine
Kui eelnevalt on sõnastiku võti valitud selliselt, et selle järgi saab loomulikult sortida, siis peaks see samm olema suhteliselt lihtne. Sortida saab umbes nii: sorted_items = sorted(schedule_dict.items(), key=...). key peaks arvatavasti olema lambda funktsioon, mis tagastab, millise väärtuse järgi elemente võrreldakse. Kuna elemendid on ennikud (esimene väärtus on võti, teine väärtus on sõnastiku väärtus sellel kohal), siis tuleks seal tagastada enniku see element, mida võrrelda oleks vaja (ehk siis enniku esimene element).

Tähelepanu, sõnastiku sortimisel on tulemus järjend (sõnastik ise ei ole sorditud).

Tabeli koostamine
Lõpuks tuleb teostada tabeli koostamine. Tuleb tähele panna, et tabel tuleb tagastada sõnena, mitte printida.

Mõistlik oleks luua üks järjend, kuhu iga tabeli rida eraldi lisada. Seega esimesena tuleks lisada ülemine "äär": table.append("-------"). Päis ja järgmine "äär" lisatakse umbes samamoodi. Seejärel tabeli sisu osad tuleb lisada vastavalt sorditud ajatabelile. Lõppu lisatakse alumine "äär".

Tabeli veeru laius tuleb arvutada välja vastavalt selles veerus olevale kõige laiemale väärtusele. Tabeli päise tekst on ka väärtus. Seega, kui tabelis on päises "entries" ja sisuosas "a" ja "b", siis laius on vastavalt päisele 7. Sellele tuleb lisaks veel mõlemale poole tühik lisada. Tasub vaadata näiteid.

Tabeli veeru vormindamiseks kasutada f-sõne, see ei tee teie koodi väga koledaks. Vihje, f-sõnes saab väärtusi joondada ning arvude puhul saab 0-e ette lisada vastavalt soovile/vajadusele.

Kellaaja konvertimine võiks toimuda alles siin tabeli koostamisel - eelnevalt 12-tunni peale üleminek teeb asjad keeruliseks.

# Boonusülesanne 3: OOP testimine

Ülesanne: OOP testimine
Selles ülesandes on ette antud testid. Ülesande kirjeldust ei ole. Ükski test esialgu läbi ei lähe. Proovige testide põhjal aru saada, mida mingi konkreetne meetod tagastama peab. Kui kõik testid läbivad, siis on ülesanne lahendatud.

Testid
import random
import pytest
from oop_testing import Factory, Cake, WrongIngredientsAmountException

@pytest.fixture
def factory() -> Factory:
return Factory()

def test_produce_cake_only_basic(factory):
amount = factory.bake_cake(1, 1)
assert amount == 1

@pytest.mark.dependency()
def test_produce_cake_only_medium(factory):
assert factory.bake_cake(2, 2) == 1
assert factory.bake_cake(4, 4) == 2

@pytest.mark.dependency()
def test_produce_cake_only_large(factory):
assert factory.bake_cake(5, 5) == 1
assert factory.bake_cake(10, 10) == 2

@pytest.mark.dependency(depends=["test_produce_cake_only_medium"])
def test_produce_cake_medium_remaining_ingredients_produce_more_cakes(factory):
assert factory.bake_cake(3, 3) != 1
assert factory.bake_cake(5, 5) != 2

@pytest.mark.dependency(depends=["test_produce_cake_only_large"])
def test_produce_cake_large_remaining_ingredients_produce_more_cakes(factory):
assert factory.bake_cake(6, 6) != 1
assert factory.bake_cake(11, 11) != 2

def test_produce_cake_get_cakes(factory):
factory.bake_cake(1, 1)
assert len(factory.get_cakes_baked()) == 1
cake = factory.get_last_cakes(1)[0]
assert cake is not None
assert type(cake) == Cake

def test_produce_cakes_get_last_cakes(factory):
amount = factory.bake_cake(3, 3)
assert amount == 2
cakes = factory.get_last_cakes(2)
assert type(cakes) == list
assert len(cakes) == 2
cakes = factory.get_last_cakes(1)
assert type(cakes) == list
assert len(cakes) == 1

def test_produce_cakes_order_medium_before(factory):
factory.bake_cake(3, 3)
cakes = factory.get_last_cakes(2)
assert cakes
assert cakes[0].type == "medium"
assert cakes[1].type != "medium"

def test_produce_cakes_order_large_before(factory):
factory.bake_cake(6, 6)
cakes = factory.get_last_cakes(2)
assert cakes[0].type == "large"
assert cakes[1].type != "large"

@pytest.mark.dependency()
def test_get_cakes_correct_amount(factory):
factory.bake_cake(9, 9)
assert len(factory.get_cakes_baked()) == 3

@pytest.mark.dependency()
def test_get_last_cakes_correct_amount(factory):
factory.bake_cake(9, 9)
for i in range(0, 3):
assert len(factory.get_last_cakes(i)) == i

@pytest.mark.dependency(depends=["test_get_cakes_correct_amount"])
def test_get_cakes_returns_cakes(factory):
factory.bake_cake(9, 9)
assert all(type(cake) == Cake for cake in factory.get_cakes_baked())

@pytest.mark.dependency(depends=["test_get_cakes_correct_amount"])
def test_get_last_cakes_returns_cakes(factory):
factory.bake_cake(9, 9)
assert all(type(cake) == Cake for cake in factory.get_last_cakes(4))

@pytest.mark.dependency(depends=["test_get_cakes_correct_amount", "test_get_last_cakes_correct_amount"])
def test_produce_cakes_order(factory):
factory.bake_cake(8, 8)
assert len(factory.get_cakes_baked()) == 3
cakes = factory.get_last_cakes(3)
assert cakes[2].type == "basic"
assert cakes[1].type == "medium"
assert cakes[0].type == "large"

def test_cake_basic():
basic_cake = Cake(1, 1)
assert basic_cake.type == "basic"

def test_cake_medium():
medium_cake = Cake(2, 2)
assert medium_cake.type == "medium"

def test_cake_large():
large_cake = Cake(5, 5)
assert large_cake.type == "large"

def test_cake_wrong_ingredients_throws_exception():
for i in {i for i in range(1000)} - {1, 2, 5}:
with pytest.raises(WrongIngredientsAmountException):
Cake(i, i)

def test_cake_equals():
cake_basic_1 = Cake(1, 1)
cake_basic_2 = Cake(1, 1)
cake_medium_1 = Cake(2, 2)
cake_medium_2 = Cake(2, 2)
cake_large_1 = Cake(5, 5)
cake_large_2 = Cake(5, 5)
assert cake_basic_1 == cake_basic_2
assert cake_medium_1 == cake_medium_2
assert cake_large_1 == cake_large_2

def test_cake_repr():
cake_basic = Cake(1, 1)
cake_medium = Cake(2, 2)
cake_large = Cake(5, 5)
assert cake_basic.**repr**() == "Cake(basic)"
assert cake_medium.**repr**() == "Cake(medium)"
assert cake_large.**repr**() == "Cake(large)"

def test*factory_str_amount(factory):
num = random.randint(3, 1000)
for x in [(1, 1) for * in range(2, num)]:
factory.bake_cake(\*x)
assert str(factory) == f"Factory with {num - 2} cakes."

def test_factory_str_single(factory):
factory.bake_cake(1, 1)
assert str(factory) == "Factory with 1 cake."
