# Ülesanne 9: Lauluvõistlus

### class Song

`__init__(self, name: str, genre: str, duration: float, difficulty: int)`: Konstruktor, mis määrab laulu nime, žanri, pikkuse ja raskuse. Kasuta samanimelisi objekti muutujaid (self.name, self.genre jne). Juhul kui laulu nimi algab väikse tähega, muuda see suureks. Kui laulu raskus on suurem kui 10, siis määra see 10 peale. Kui see on väiksem kui 1, siis määra see 1-ks.

`__repr__(self)`: Tuleb tagastada laulu kujul "laulu nimi, style: laulu žanr".

### class Contestant

`__init__(self, first_name: str, last_name: str, age: int, vocals: float)`: Konstruktor, mis määrab võistleja nime, vanuse ja vokaalseid võimeid. Loo objekti muutuja self.name, mis koosneb nii ees- kui ka perekonnanimest ning kõik nimed algavad suure algustähega.

`__repr__(self)`: Tuleb tagastada võisteja kujul "täisnimi" (self.name).

`choose_song(self, song_list: list)`: Meetod choose_song valib võistlejale sobiva laulu. Eelistatud on see laul, mille nimes on kõige rohkem sarnaseid tähti võistleja täisnimega. Valitud laul lisatakse võistleja lauluks. Võistlejal on vaid üks laul. Ehk siis ülesande raames ei kutsuta choose_song meetodit rohkem kui üks kord välja. Kui laulu nimes ei esine ühtegi võistleja nime tähte, siis seda lugu ei valita. Kui ühtegi sobivat lugu valikus ei ole, siis laulu ei valita ja meetod tagastab None.

### class Judge

`__init__(self, name: str, preferences: list)`: Konstruktor, mis määrab kohtuniku nime ja muusikalise eelistusi (žanrid). Nimi peab olema läbiva suure algustähega (.title()).

`__repr__(self)`: Tuleb tagastada kohtuniku kujul "täisnimi".

### class Competition

`__init__(self, minimum_age: int, maximum_age: int, suitable_genres: list)`: Konstruktor, mis määrab võistluse minimaalset- ja maksimaalset vanus ning sobivaid muusikalisi žanre. Loo vastavate nimedega objekti muutujad (self.minimum_age jne).

`add_contestant(self, contestant: Contestant)`: Võistlejate registreerimine võistlusele. Võistleja saab osa võtta ainult juhul, kui ta on Contestant tüüpi, tema laulu žanr sisaldub võistlusel aktsipteeritavates žanrites ning võistleja on vanuselt sobiv. Tagastab True, kui lisamine õnnestub. Muul juhul False.

`add_judge(self, judge: Judge)`: Kohtuniku lisamine. Kohtunikuks saab lisada ainult siis, kui ta on Judge ja tema kõik eelistused klapivad kokku võistluse muusikaliste žanritega.

`create_order_of_performances(self)`: Loo esinemisjärjekord. Esimestena esinevad kõige nooremad, kui vanus on sama, asetatakse võistejaid järjekorda laulu nime järgi (tähestiku järjekord a-z). Tagastab sorteeritud järjendi võistlejatest.

`perform_song_rankings(self)`: Loo sõnastik, mille võti on laulu objekt ja väärtus sellele laulule väljapandud punktid.

Punktisumma arvutamine:

Esineja vokaalseid võimed korrutatakse läbi laulu raskusega. Juhul kui kohtunikule meeldib selle laulu žanr, lisa 10 punkti.

`get_suitable_genres(self)`: Tagasta võistusel lubatuid muusikažanrid tähestiku järjekorras.

`get_contestants(self)`: Tagasta nime järgi tähestiku järjekorras sorteerituid võistlejad.

`get_judges(self)`: Tagasta nime järgi tähestiku järjekorras sorteerituid kohtunikud.

`get_judges_rankings_in_order(self)`: Tagasta laulude pingerida alustades parimast. Vt perform_song_rankings. Tagastada järjend sorteeritud laulu objekidest.

`get_winner(self)`: Tagastab võistluse võitja (laul) vastavalt punktidele.
