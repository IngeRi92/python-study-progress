# Kiiruse ületamine

Kirjuta funktsioon, mis saab sisendiks kiiruse (täisarv) ning tõeväärtuse, kas on sinu sünnipäev, ning tagastab mis kategooria trahvi sa saad. Kategooriad on:

- 0. Trahvi ei saa. Juhul, kui kiirus on 60 või väiksem.
- 1. Väike trahv. Juhul, kui kiirus on 61 ja 80 vahel (kaasa arvatud)
- 2. Suur trahv. Kui kiirus on üle 80.

Kui on sinu sünnipäev, siis võivad kiirused olla 5 võrra suuremad.

# Kommi söömine

Kirjuta funktsioon, mis tagastab, palju kommi jääb järele peale söömist.

Funktsioonile antakse sisse kommide kogus, tõeväärtus, kas tegemist on dieediga, ning tõeväärtus, kas on jõulud. Tavalisel päeval (ilma dieedita) süüakse 10 kommi. Kui on jõulud, siis süüakse topeltkogus kommi. Dieedi korral süüakse 5 kommi vähem kui muul juhul. Alati tuleb vähemalt 1 komm järele jätta.

# Rahatähed

Tuleb koostada raha väljamakse automaat, millega saab välja võtta kindlaid rahatähti. Sisendiks on summa, mis on vahemikus 1 - 500, ning funktsioon tagastab, mitu erinevat rahatähte on vaja, et sisestatud summa katta. Eesmärk on katta summa võimalikult väheste rahatähtedega. Masinas on järgmised rahatähed: 1€, 5€, 10€, 20€, 50€, 100€. Automaadis pole rahatähtede kogus piiratud.

Näide:
On antud summa 56€. Vaja läheb selle summa tagastamiseks kolme rahatähte: 50€, 5€, 1€ (funktsioon tagastab 3).

# Liida murdarvud

Defineeri funktsioon, mille parameetriteks on neli täisarvu. Esimesed 2 argumendina saadud arvu a ja b tähistavad esimest murdu, a/b. Teised 2 argumendina saadud arvu c ja d tähistavad teist murdu, c/d.

Funktsioon peab sõnena murru formaadis tagastama nende kahe murru summa: a/b + c/d

Vastus ei pea olema taandatud murd. (Võib näiteks "1/3" asemel tagastada ka "2/6")
Vastuses ei tohi olla komasid. (Näiteks "1.5/3" ei ole korrektne. "3/6" on võrdväärne, aga korrektne)
Isegi kui vastus on täisarv, peaks selle esitama murruna (Näiteks "1/1", mitte "1")
Kirjuta lahendus kasutades matemaatilisi operaatoreid, millega selle ülesande varasemates osades tutvusid

Näiteid:
```
add_fractions(1, 2, 1, 2) # => 1/2 + 1/2 => Võimalikud vastused "1/1", "4/4", "2/2", jne
add_fractions(3, 1, 1, 1) # => 3/1 + 1/1 => Võimalikud vastused "4/1", "16/4", "8/2", jne
add_fractions(1, 6, 3, 5) # => 1/6 + 3/5 => Võimalikud vastused "23/30", "46/60", jne
```
