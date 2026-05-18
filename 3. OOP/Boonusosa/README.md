# Ülesanne: Loomaaed

*NB: Siin ülesandes ära palun kasuta list comprehensionit ega for-tsüklit. Kõik funktsioonid tuleks lahendada üherealise lahendusega, mis kasutab nimetatud sisseehitatud funktsioone ja anonüümseid funktsioone.*

Selles ülesandes on meil tegemist loomaaiaga, kus elavad erinevad loomaliigid. Selleks, et kõik loomad saaks ära kirjeldatud, on defineeritud Animal objekt, mis kannab endas infot loomaliigi kohta. Ülesandes tuleb realiseerida järgmised funktsioonid:

`find_smallest_animal_by_weight` - tuleb leida kõige väiksem (kõige vähem kaaluv) loom. Kuna soovime kõige väiksemat võimalikku varianti, siis võtame võrdlusel aluseks looma kaaluvahemiku alguse. Kui mitme looma kaal on sama suur, tuleks tagastada see loom, kes esineb listis enne.

`list_species_and_scientific_names` - tuleb teha list tuple'itest, kus esimesel kohal on looma liigi nimi ja teisel kohal liigi teaduslik nimi.

`find_how_many_pumpkins_are_needed_to_feed_animals` - meie loomaaed kogub headelt inimestelt talveks loomadele kõrvitsaid. Kuigi loomad kindlasti ainult kõrvitsatest ei toitu, oleks huvitav teada, mitu kõrvitsat meil läheks vaja, et loomad ainult nendega üle talve ära toita. Kõrvitsa keskmine kaal on 3kg, talv kestab 90 päeva. Selle arvutuse jaoks võtame arvesse, et meil on igast liigist looma loomaaias 2 tükki ja et iga loom sööb 6% jagu oma (kaaluvahemiku keskmine) kehakaalust kõrvitsaid. Lihatoidulised loomad kõrvitsaid ei söö. Tagastada tuleb kõrvitsate hulk (ümmardatud üles).

`sort_alphabetically_by_scientific_name` - tuleb tagastada loomade nimekiri sorteerituna teadusliku nime alusel tähestiku järjekorras.

`find_animals_whose_height_is_less_than` - tuleb tagastada loomad, kelle turjakõrgus on väiksem või võrdne etteantud kõrgusega (meetrites)

`filter_animals_based_on_diet` - tuleb tagastada vastava toitumisharjumusega loomad. Toitumisharjumustest on võimalikud 3 varianti - herbivorous, omnivorous ja carnivorous.

`find_animal_with_longest_lifespan` - tuleb tagastada kõige pikema võimaliku elueaga loom. Kui mitmel loomal on sama pikim võimalik eluiga, siis tuleb tagastada see, kes leitakse listist esimesena.

`create_animal_descriptions` - tahame loomaaias loomade juurde panna nende kohta väikesed kirjeldused. Selleks tuleks teha iga loomaliigi kohta kirjeldav sõne järgmises formaadis. Nurksulgudes olev parameeter tuleks asendada infoga Animal objektist. "[Species name] ([Scientific name]) lives in [habitat] and its diet is [diet]. These animals can live up to [max age] years and they weigh between [min weight] kg and [max weight] kg as adults."


# Ülesanne: Pinumälu

`class Stack` Programmi eesmärk on koostada pinumälu. Klassil peavad olema defineeritud järgnevad meetodid.

`__init__(self, capacity)` Konstructor, mis loob pinumälu objekti. Parameeter capacity näitab, mitu objekti saab pinus maksimaalselt salvestada. Siin meetodis on mõistlik luua ka muutuja, kus hoitakse pinu elemente.

`push(self, item)` Lisab item objekti pinumällu. Kui pinus pole objekti salvestamiseks ruumi tõstab programm StackOverflowException erindi.

`pop(self)` Tagastab kõige viimati pinumällu lisatud objekti, mida pole sealt veel välja võetud. Kui pinu on tühi siis tõstab programm StackUnderflowException erindi.

Esimese kolme meetodi eest on võimalik saada kuni 4 punkti. Järgnevate Stack klassi meetodite defineerimisel on võimalik veel üks punkt saada.

`peek(self)` Tagastab pinu kõige pealmise elemendi, ilma seda pinust eemaldamata. Kui pinu on tühi tagastab None Seda on võimalik defineerida pop ja push baasil.

`is_empty(self)` Tagastab tõeväärtuse, kas pinu on tühi.

`is_full(self)` Tagastab tõeväärtuse, kas pinu on täis.

`__str__(self)` Eriline meetod, mis tagastab pinu sõnelise representatsiooni. Seda meetotit kutsub välja str(object). Kui pinus on olemas kõige pealmine element (pinu ei ole tühi) siis peab funktsioon tagastama sõne kujul: "Stack(capacity={capacity}, top_element={top_element})" Kui pinu on tühi peab funktsioon tagastama sõne kujul: "Stack(capacity={capacity})"

`class StackOverflowException(Exception)` Erind, mis tõstetakse, kui täis stacki püütakse panna elementi.

`class StackUnderflowException(Exception)` Erind, mis tõstetakse, kui tühjast stackist püütakse elementi võtta.