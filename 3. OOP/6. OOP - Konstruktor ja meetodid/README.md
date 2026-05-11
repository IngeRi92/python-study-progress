# Ülesanne 6.1: Konstruktor

Ülesandes on vaja luua kolm klassi:

1. `Empty` - siin konstruktorit pole. Kui jätame konstruktori kirjutamata, siis tegelikult kasutatakse vaikimisi konstruktorit, mis midagi erilist ei tee. Päriselt kasutatakse seda väga harva.
2. `Person` - siin on konstruktor, mis ei võta ühtegi argumenti sisse. Konstruktoris tuleb luua objektile väljad: `firstname`, `lastname` ja `age`. Vastavalt vaikeväärtustega: `""`, `""` ja `0`.
3. `Student` - siin konstruktor võtab vastu 3 argumenti: `firstname`, `lastname` ja `age`. Need salvestatakse objekti juurde samanimelistesse muutujatesse.

Kirjuta "main" (`if __name__ == '__main__'` osasse) järgmine kood:

1. Loo `Empty` objekt
2. Loo 3 `Person` objekti ja määra igale objektile eesnimi, perenimi ja vanus (kõigile erinevad väärtused)
3. Loo 3 `Student` objekti ja määra igale objektile eesnimi, perenimi ja vanus (kõigile erinevad väärtused)

Kui paned tähele, siis `Person` objekti puhul peame väärtused eraldi määrama (kuna konstruktoris pole parameetreid). Student puhul aga saame mugavalt väärtused kaasa anda ja objektide täitmine andmetega on oluliselt mugavam.

# Ülesanne 6.2: Raamatukogu

Loo kaks klassi: Book ja Library.

### Klass `Book`

Atribuudid: `title`, `author`, `year`.

Spetsiaalsed meetodid:

- `__init__` – seab atribuudi väärtused.
- `__str__` – tagastab kasutajasõbraliku stringi `"Pealkiri" by Autor (Aasta)`.
- `__repr__` – tagastab arendajasõbraliku stringi `Book(title='...', author='...', year=...)`.
- `__eq__` – võrdsed, kui pealkiri ja autor on samad.
- `__hash__` – arvutab hash’i väärtuse (pealkiri, autor).
- `__lt__` – võimaldab raamatuid sorteerida aasta järgi.
- `__len__` – tagastab pealkirja pikkuse.

### Klass `Library`

Atribuudid: `name`, `books` (list).

Spetsiaalsed meetodid:

- `__init__` – seab nime ja loob tühja listi.
- `__str__` – tagastab `Library "Nimi" has X books`.
- `__len__` – tagastab raamatute arvu.
- `__contains__` – kontrollib, kas raamat on raamatukogus.
- `__getitem__` – lubab ligipääsu nagu listis (`library[0]`).
- `__add__` – liidab kaks raamatukogu uueks.

Tavalised meetodid:

- add_book(book) – lisab raamatu, kui seda pole.
- remove_book(book) – eemaldab raamatu.
- find_books_by_author(author) – tagastab listi kõigist antud autori raamatutest.

# Ülesanne 6.3: Joonistus

### Drawing

Selle ülesande eesmärk on tutvuda OOP-ga ehk Objekt Orienteeritud Programmeerimisega.

### Taust

Kujutage ette, et Te tahate kunstnikuks saada, kuid kahjuks puudub Teil joonistamise oskus, kuna koolis lasite kunsti tunde üle. Õnneks olete väga hea programmeerija. Otsustasite kirjutada klassi, mis kirjeldaks joonistusi, kus saaks erinevaid kujundeid joonistada ja vajadusel neid sealt ära kustutada. Just nagu päris joonistusel!

### Sisu

- `__init__(self, max_figures: int, author: str)` - konstruktor, millel on kaks parameetrit:
  - `max_figures` - tähistab maksimaalset kujundite arvu joonistusel.
  - `author` - tähistab joonistuse autorit.
    Lisaks looge kolmas isendimuutuja figures. Siia hakkate salvestama lisatud kujundeid, seega tüübiks võiks olla mingisugune andmestruktuur, mis võimaldaks elemente lisada ja eemaldada.

  Ehk kokku peaks teil tulema kolm isendimuutujat. Te võite luua ka rohkem, kuid meie testid vajavad ainult kolme. Jälgige, et nimed oleksid samad nagu nõutud, sest muidu me ei saa teie lahendusi testida.

- `draw_figure(self, figure: str) -> str or None`- meetod kujundi joonistamiseks. Saab sisendiks kujundu, mida on vaja joonistusele lisada. Tagastab lisatud kujundi. Joonistusel ei saa olla mitu samasugust kujundit, seega kui selline kujund on juba olemas, siis meetod ei tee midagi ja tagastab None. Juhul, kui kujundite arv on võrdne maksimaalse lubatud arvuga, tõstatab erindi DrawingFullError sõnumiga The drawing is full.

- `erase_figure(self, figure: str) -> str` - meetod kujundi kustutamiseks. Saab sisendiks kujundi, mida on vaja kustutada. Tagastab kustutatud kujundi. Kui sellist kujundit ei ole olemas, tõstatab erindi FigureDoesNotExistError sõnumiga There is no such figure on the drawing.

- `is_empty(self) -> bool` - meetod, mis ütleb, kas joonistus on tühi või mitte. Tagastab True, kui on tühi, ja False, kui joonistuse peal on olemas vähemalt üks kujund.

- `size(self) -> int` - meetod, mis näitab ära, kui palju kujundeid on joonistusel. Suurus peab muutuma iga draw ja erase operatsiooniga.

- `__str__(self)` - spetsiaalne meetod objekti stringina näitamiseks. Tagastab sõne kujul: "The drawing painted by {autori nimi}. Contains {kujundite arv} figure(s)"

Mainitud erindid peate ise looma.
