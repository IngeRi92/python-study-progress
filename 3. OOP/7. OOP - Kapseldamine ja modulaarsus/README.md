# Ülesanne 7.1: Kapseldamine

Tuleb luua klass `Student` ning kasutada "privaatseid" muutujaid. Objekti loomisel (konstruktoris) võetakse vastu kaks väärtust selles järjekorras: nimi (sõne) ja id (täisarv). Seega peab konstruktor aktsepteerima kahte parameetrit. Need väärtused salvestatakse "privaatsetesse" muutujatesse. Lisaks on igal tudengil eraldi info staatuse kohta. Vaikimisi staatus (kui tudeng luuakse) on "Active".

Tudengi objektil on võimalik muuta nime ja staatust. Id väärtust jooksvalt enam muuta ei saa. Staatuse muutmisel on kindlad reeglid.

Tudengi objektil peavad olema järgmised meetodid:

- `get_id(self)` - tagastab algselt tudengile määratud id.
- `set_name(self, name)` - määrab tudengile uue nime
- `get_name(self)` - tagastab tudengi hetke nime
- `set_status(self, status)` - määrab tudengile uue staatuse, aga seda vaid juhul, kui staatuse väärtus on üks järgmistest: `Active, Expelled, Finished, Inactive`. Muul juhul staatust ei muudeta (viga ka ei anta - funktsioon lihtsalt ei tee midagi)
- `get_status(self)` - tagastab tudengi hetke staatuse

Kuigi üldiselt on väga hea kasutada "privaatseid" muutujaid oma klassis, siis Pythonis seda alati ei tehta (teistes keeltes on see rohkem kasutusel). Samas on hea, kui oskad vajadusel oma muutujaid n-ö ära peita välismaailma eest.

