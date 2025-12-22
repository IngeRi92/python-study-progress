# Create dictionary with names and years
Funktsiooni sisendiks on kaks list people_list ja year_list.
Esimeses listis on inimeste nimed ja teises aastad, millal nad sündisid.
Tagastada sõnastik, kus võtmeteks on nimed ja väärtusteks aastad.

# Shortest way back
Ülesande eesmärk on leida lühim tee alguspunkti.
Abimaterjalid ülesande lahendamiseks
Sõnastik (dict)
For-tsükkel (for loop)
Silumine (debug)
Manhattani kaugus
Ülesanne
Selles praktikumis peame aitama kantpeade maailma Kallet, kes tahab peale pikka õhtut linnas taas koju jõuda.
Kantpeade mõtlemisvõime on piiratud, seetõttu oskavad nad liikuda vaid põhja, lõuna, ida ja lääne suunas.
Kui kantpea Kalle on väsinud, annab ta meile paberi, kus on kirjas kõik tema sammud kodust kuni hetkese asukohani.
Näiteks NNEESEW tähendab, et Kalle astus kodust:
kaks sammu põhja poole,
seejärel tegi kaks sammu itta,
ühe sammu lõunasse,
astus taaskord sammu itta
ning viimaks ka ühe sammu läände.
Meie ülesanne on välja pakkuda kõige lühem tee tagasi koju.
Selleks saame me pidada kantpea koordinaatide üle järgnevat arvestust.
Siin kirjeldatud näites kasutame koordinaate, kus esimene väärtus tähistab põhja-lõuna suunalist liikumist, teine koordinaat tähistab ida-lääne suunalist liikumist. Ülesandes ei ole vahet, kuidas te lahendate.
Kuna me teame, et lõpppunkt on (1, 2), siis tagasi koju jõudmiseks (0, 0) peab astuma ühe sammu lõuna suunas ja kaks sammu läände ehk SWW.
Lahenduses ei ole sammude järjekord tähtis, see tähendab, et õiged variandid on SWW, WSW, WWS.

# Organise by first symbol
Funktsiooni sisendiks on sõnede järjend.
Tagastab sõnastiku, kus võti on täht ja väärtus on selle tähega algavate sõnede järjend (esinemise järjekorras).
