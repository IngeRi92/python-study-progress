# Failioperatsioonid
Selles ülesandes opereerime failidega: loeme andmeid failidest ja kirjutame andmeid failidesse.

Failide kohta saab lugeda PyDocist:

Failist lugemine
Faili kirjutamine
# Failioperatsioonid
Loome baasfunktsioonid, et failidega opereerida.

Siin osas võib eeldada, et failid on alati olemas - ehk siis pole vaja vigadega tegeleda. Kõik failid sisaldavad vaid ascii sümboleid.

read_file_contents - ette antud failist loetakse andmed sisse ja tagastatakse sõnena
read_file_contents_to_list - ette antud failist loetakse andmed sisse. Funktsioon tagastab järjendi, kus iga rida on eraldi element. Ridade lõpus ei tohi reavahetust olla.
read_csv_file - ette antud CSV-failist loetakse andmed sisse. Failis on ridadel komaga eraldatud väärtused. Iga rida on eraldi element järjendis. Ja iga selline element on omakorda järjend, kus väärtused on loetud failist komade vahelt. Failis on igal real sama palju "välju".
write_contents_to_file - funktsioonile antakse ette faili asukoht, kuhu tuleb kirjtuada kaasa antud sõne.
write_lines_to_file - funktsioonile antakse ette järjend sõnedest. Need sõned tuleb kirjutada faili eraldi ridadele. Viimase rea lõpus ei tohi reavahetust olla (kui just viimane järjendi element ei sisalda reavahetust).
write_csv_file - funktsioonile antakse ette järjend järjenditest. Järjendis on ridade info. Ja iga selline järjend omakorda sisaldab infot, mis väljad sellele reale lähevad. Igal real on sama palju välju. Kõik elemendid on sõned. Kõik andmed tuleb kirjutada faili ning väljade eraldaja on koma.

# Näidisfailid
```
write_lines_to_file("file.txt", ["hello", "world"])
```
Tulemus on järgmine (lõpus ei ole reavahetust):

file.txt:
```
hello
world
```
Kui sisendfail on selline data.csv:
```
id,name,town,birthday
1,ago,tallinn,01.01.2021
2,mari,kuressaare,02.02.2021
```
read_csv_file("data.csv") tulemusena tekib list:
```
[
    ["id", "name", "town", "birthday"],
    ["1", "ago", "tallinn", "01.01.2021"],
    ["2", "mari", "kuressaare", "02.02.2021"],
]
```
Ja vastupidi write_csv_file() funktsiooni tulemusena saab sellest listist selline fail nagu üleval data.csv juures näidatud.

# Vihjed
kasutame liste
Lõpuks soovime CSV-faili kirjutamiseks kasutada write_csv_file. Selleks oleks vaja luua list, kus on kõik read omakorda listina. Näiteks võiks sisend csv-faili kirjutamiseks olla: [["name", "town", "date"], ["mary", "tallinn", "01.01.2021"], ["mart", "london", "02.02.2021"]]. Seega, proovime kohe sellise listi luua.

Oluline on tähele panna, et nimi on see, mille järgi saab andmed kahest failist kokku panna. Ühes failis on inimese kuupäev (näiteks sünnikuupäev) ja teises tema asukoht. Tulemusfailis on ridade järjekord oluline. Kõigepealt tuleb võtta kuupäevade failist inimeste järjekord. Seejärel tulevad need inimesed, kes on vaid asukohtade failis.

Mõistlik on andmete lugemisel kasutada funktsioon read_csv_file. Aga tuleb arvestada, et väljade eraldajaks on siin ülesandes koolon :. Seega, peaks sinna funktsiooni andma kaasa eraldaja (vaikimisi koma). Selleks saab lisada vaikeväärtusega parameetri, mille vaikeväärtus on koma. Ja siis siin funktsioonis saab väljakutsumisel kaasa anda kooloni.

Teine variant on kasutada read_file_contents_to_list funktsiooni, kus read pannakse eraldi listi. Sellisel juhul tuleks kõik listi elemendid läbi käia ja need tükeldada kooloni järgi. Ehk siis üks element on näiteks "mary:tallinn", siis tükeldades saab ["mary", "tallinn"]

Seega peaks meil tekkima kaks listi: üks kuupäevadega, teine linnadega.
```
dates = [
    ["mary", "01.01.2021"], 
    ["mart", "02.02.2021"]
]

towns = [
    ["mary", "tallinn"],
    ["mart", "london"]
]
```
Kogume tulemused listi, mille anname pärast faili kirjutamise funktsiooni:
```
result = []
```
Mõistlik on kohe lisada päis:

```
result = [["name", "town", "date"]]
```

Algoritm võiks olla järgnev:

```
käime läbi kõik read dates järjendist
    iga rea korral lisame result järjendisse uue kolmekohalise elemendi: [name, "-", date], kus name ja date on vastalt realt esimene ja teine element
    
käime läbi kõik read towns järjendist:
    otsime, kas selline nimi on juba result tabelis
    kui on, siis:
        muudame vastava rea kolmanda elemendi ära: row[2] = town, kus town on vastava rea teine element
    kui ei ole, siis:
        lisame uue kolmekohalise elemendi: [nimi, town, "-"], kus name ja town on vastavalt realt esimene ja teine element
        
kirjutame result listi faili kasutades write_csv_file funktsiooni
```