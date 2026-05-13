# Ülesanne 8.1: Autoremont

Realiseerida väga lihtsustatud autoremondi infosüsteemi.

### Klass Car

- `__init__(self, color: str, make: str, engine_size: int)` - klassi konstruktor, mille sisendparameetriks on auto värv, mark ja mootori suurus.

### Klass Service

- `__init__(self, name: str, max_car_num: int)` - klassi konstruktor, mille sisendparameetriks on auto remonti nimi ja maksimaalne autode arv, mida töökoda suudab samal ajal teenindada. Lisaks hoiab konstruktor infot sellest, millised autod on praegu remodis.

- `can_add_to_service_queue(self, car: Car) -> bool` - meetod kontrollib, kas autot saab lisada järjekorda. Autot saab lisada, kui:
  1. lisades uue auto ei läheb remondis olevate autode arv suuremaks kui max_car_num
  2. sama mudeli ja värviga autot ei ole veel selles töökojas
     Tagastab True, kui autot saab järjekorda lisada, False muul juhul.

- `add_car_to_service_queue(self, car: Car)` - meetod lisab auto järjekorda, kui see on võimalik (vt eelmist meetodit).

- `get_service_cars(self)` - meetod, mis tagastab listi autodest, mis on hetkel remodis (järjekorras).

- `repair(self)` - meetod, mis parandab remondis olevat autot. Tavaliselt võetakse järjekorrast esimese auto ning tehakse sellele remonti, AGA kui antud aja hetkel on järjekorras auto, mille värvi ja margi pikkus kokku (sõnede pikkus) on täpselt 13 -> valitakse see auto (kui leitakse mitu, siis ükskõik milline neist) ja remonditakse seda. Peale remonti auto ei ole enam selle töökoja remondi järjekorras. Meetod peab tagastama valitud ja parandatud auto. Siin ülesandes alati leidub mingi auto, mida remontida.

- `get_the_car_with_the_biggest_engine(self)` - meetod, mis tagastab listi autodega (autoga), millel on suurim mootori suurus.

# Ülesann 8.2: Raamatud

Võimalusel taaskasuta meetodeid.

### Klass Book

- `__init__(self, title: str, author: str, sales: int, genres: list[str], publication_year: int)`
  Konstruktor, mis loob raamatu objekti antud parameetritega. Igal raamatul on pealkiri, autor, müüdud eksemplaride arv, žanrid ning ilmumisaasta. Siit midagi eemaldada ei tohi, kuid soovi korral juurde võib panna.

- `__eq__(self, other) -> bool`
  See meetod aitab objektide võrdlemisega. Ära seda muuda.

- `__hash__(self) -> int`
  See meetod võimaldab objekti panna hulka ning sõnastikku (võtmena). Ära seda muuda.

- `__repr__(self) -> str`
  See meetod võimaldab objekti kuvada loetaval kujul (näiteks kasutades print()). Seda pole vaja muuta.

### Funktsioonid

- `author_book_count(library: list[Book], author: str) -> int`
  Leia, mitu raamatut on antud autor kirjutanud.

- `most_popular_book(library: list[Book]) -> Book`
  Leia raamat, mis on kõige populaarsem (kõige suurem müüdud eksemplaride arv).

- `most_popular_author(library: list[Book]) -> str`
  Leia autor, kelle raamatuid on kõige rohkem müüdud. Kui mitmel autoril on sama palju müüdud raamatuid, siis pole oluline, millise neist tagastad.

- `find_best_selling_genre(library: list[Book]) -> str`
  Leia kõige populaarsem žanr. Kui mitu žanrit on sama populaarsed, siis pole oluline, millise neist tagastad.

- `find_books_by_genre_and_year(library: list[Book], genre: str, year: int) -> list[Book]`
  Leia raamatud, mis on antud žanrist ja ilmusid antud aastal. Tagasta need raamatud listis, mis on sorteeritud müüdud eksemplaride arvu järgi (kahanevalt) ning kui mitmel raamatul on sama palju müüdud eksemplare, siis sorteeri need pealkirja järgi (tähestiku järjekorras).

- `most_popular_author_per_century(library: list[Book]) -> dict[int, str]`
  Leia iga sajandi populaarseim autor ehk autor, kes on müünud kõige rohkem vastaval sajandil avaldatud raamatuid. Tagasta tulemus sõnastikuna, kus võtmeteks on sajandite numbrid ja väärtusteks on autorite nimed. Kui mitmel autoril on sama palju müüke, siis pole vahet, milline sõnastikku satub.

Sajandite arvestus:

- 1801-1900 on 19. sajand
- 1901-2000 on 20. sajand
- ....

Sõnastik peaks välja nägema umbes selline:

```
{
    19: "Jane Austen",
    20: "Stephen King",
    21: "J. K. Rowling"
}
```

NB! Collections teegi Counter klass tuleks siin ülesandes kasuks, kuid sellest hoolimata pole selle kasutamine kahjuks lubatud.
