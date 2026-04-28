# Vaheta alamsõnad
Saab sisendiks kaks sõne s ja subword. Kui subword sisaldub sõnes s, siis tuleb esimene vaste sõnest s tagurpidi pöörata. Kui subword ei sisaldu sõnes s, tagastatakse algne sõne s. len(subword) > 0. Sõnes võib subword esineda mitu korda, tagurpidi tuleb pöörata vaid esimene vaste.

# Pikim järjestikune alamsõne
Kirjuta funktsioon, mis saab sisendiks sõne. Leiab pikima järjestikuse alamsõne, mis koosneb samadest sümbolitest, ja tagastab selle pikkuse. 

# Sega sõned
Funktsioon saab sisendiks kaks sõne ja tagastab nendest kahest sõnest uue sõne, kus antud sõnede sümbolid on vaheldumisi. Kui üks sõne saab otsa, siis lisatakse sümbolid teisest sõnest.

# Salajane kiri
On antud funktsioon (vt. abimaterjale), mille parameetriks on sõne (String) letter. See kiri on aga kirjutatud salakirjas, millel on ranged reeglid, ja sinu ülesandeks on kontrollida selle õigsust. Õigesti vormistatud kirja puhul tuleb tagastada True, muul juhul False (vt. tõeväärtus). Siin ülesandes tuleb kasutada for-tsüklit, vaata ka for-each tsükkel.

Reeglid:
- Kirjas peab olema väikseid tähti vähem kui suuri tähti.
- Kõikide kirjas olevate numbrite summa peab olema väiksem või võrdne suurte tähtede arvuga.
- Kõikide kirjas olevate numbrite summa peab olema suurem või võrdne väikeste tähtede arvuga.