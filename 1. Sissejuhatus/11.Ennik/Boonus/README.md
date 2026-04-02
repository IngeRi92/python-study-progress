# Insert a tuple inside another tuple
Funktsioonile antakse ette välimine ennik, positsioon ja sisemine ennik. Sisemine ennik pannakse tervenisti välimise enniku sisse vastavale positsioonile. Kõik välimise enniku elemendid alates märgitud positsioonist nihkuvad edasi sisemise enniku pikkuse võrra.
Kui välimine ennik on (0, 1, 2) ja positsioonile 1 lisame sisemise enniku (3, 4), siis need 3 ja 4 lisatakse positsioonile 1. Välimises ennikus sellest positsioonilt 1 ja 2 nihutatakse vastavalt edasi: (0, 3, 4, 1, 2).
Positsiooni väärtus on mitte-negatiivne ja maksimaalne väärtus on välimise enniku pikkus. Kui positsioon on välimise enniku pikkus, siis lisatakse sisemine ennik välimise enniku lõppu.

# Väikseim ja suurim
Kirjuta funktsioon, mis saab sisendiks kaks täisarvuliste elementidega ennikut tuple1 ja `tuple2. Funktsioon peab tagastama kahe enniku peale väikseima ja suurima elemendi summa. Kui mõlemad ennikud on tühjad, tagasta 0.
Näiteks: tuple_min_and_max((1, 2), (3, 4)) --> 5

# Statistika arvutamine
Kirjuta funktsioon calculate_stats(*numbers), mis võtab sisendina suvalise arvu täisarve ning tagastab tulemuse ennikuna (tuple), kus:
Esimene element on väikseim arv.
Teine element on suurim arv.
Kolmas element on keskmine väärtus.
Neljas element on arvude summa.
