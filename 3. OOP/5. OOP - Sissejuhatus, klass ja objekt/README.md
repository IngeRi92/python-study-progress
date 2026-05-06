# Õppija klass

Ülesande eesmärk on luua klass Student. Klassile tuleb luua konstruktor (**init** meetod). Konstruktoris tuleb määrata väljad name ja finished. Konstruktorisse saab ette anda nime väärtuse (mis tuleb omistada väljale name). finished väärtus on vaikimisi False.

Ülesande tulemusena peaks töötama järgmine kood:

```
student = Student("John")
print(student.name)       # John
print(student.finished)   # False
```

Jälgi, et kood oleks korrektselt kommenteeritud:

- faili esimesel real peab olema docstring
- klassi definitsiooni järel peab olema docstring
- meetodi definitsiooni järel peab olema docstring

# Film

Ette on antud klass `Movie`. Selle koodi ei tohiks muuta. Filmil on nimi (sõne), aasta (täisarv) ja žanrid (järjend sõnedest).
Vaja on realiseerida funktsioonid, mis opereerivad filmi objektidega.
Meetodid:

- `create_movie(name_with_year: str, genre1: str, genre2: str)` - Funktsioon saab ette filmi nime koos aastaarvuga kujul nimi (aasta) ning kaks žanrit (kaks sõne). Nimetusest tuleb välja parsida filmi pealkiri ja väljalaske aasta. Siia funktsiooni antud nimetuses on alati olemas sulud ja nende vahel 4-kohaline aastaarv. Kui nimetuses kaasa antud aasta on väiksem kui 1900 või suurem kui 2020, tagastab see funktsioon None. Kui kaasa antud nimetuses puudub filmi nimi (nt (1933)), tagastab see funktsioon None. Kui pealkiri ja aastaarv on korrektsed, tagastab see funktsioon uue Movie objekti, kus on määratud filmi nimi (sõne, lõpus ei ole tühikut), aasta (täisarv) ja kaks žanri. film (1999) sisendist saab filmi nime "film" ja aasta 1999.
- `get_ordered_movies(movies: list) -> list` - Tagastab uue järjendi, kus filmid on järjestatud aasta järgi (kahanevalt, uuemad eespool) ja žanri koguse järgi (kaksvavalt). Kui nii aasta kui ka žanrite kogus on sama, peavad filmid jääma algses järjekorras.
- `add_genres(movies: list, genres: list) -> None` - Funktsioon lisab etteantud filmidele etteantud žanrid. Kui mõni žanr on filmil juba olemas, siis seda teistkordselt ei lisata. Funktsioon tagastab None, muutma peab movies listi.
- `remove_movies_by_genre(movies: list, genre: str)` -> list - Funktsioon tagastab uue järjendis filmidest, kus on algsest järjendist eemaldatud need filmid, millel on žanr genre. Filmide järjest peab jääma samaks, algset listi ei tohi muuta.
