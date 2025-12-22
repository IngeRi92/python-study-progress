# Parooli valideerimine
Funktsioon includes_uppercase(password: str) kontrollib, kas funktsioonile argumendina antud parool sisaldab vähemalt ühte suurtähte. Siin sobiks kasutada näiteks sõne sisseehitatud meetodit .isupper(). Funktsioon tagastab True kui parool sisaldab vähemalt ühte suurtähte, False kui ei sisalda.
Funktsioon includes_lowercase(password: str) kontrollib, kas funktsioonile argumendina antud parool sisaldab vähemalt ühte väiketähte. Sarnaselt eelmise funktsiooniga on ka selle kontrolli tegemiseks Pythonis sissehitatud meetod olemas - .islower(). Funktsioon tagastab True kui parool sisaldab vähemalt ühte väiketähte, False kui ei sisalda.
Funktsioon includes_number(password: str) kontrollib, kas funktsioonile argumendina antud parool sisaldab vähemalt ühte numbrit. Kontrolli tegemisel on abiks meetod .isdigit(). Funktsioon tagastab True kui parool sisaldab vähemalt ühte numbrit, False kui ei sisalda.

# Leia paaritud arvud
Kirjuta funktsioon, mis tagastab hulga, kus on kõik paaritud arvud, mis on kas hulgas set_a või hulgas set_b, aga mitte mõlemas korraga.

# Poole järjendi summa
Kirjuta funktsioon, mis saab sisendiks täisarvude järjendi. Tagastab summa esimesest poolest paarisarvudest. Kui paarisarve on paaritu arv, siis keskmine arv läheb summas arvesse.

# Sõnastik
unique_dict_items
Funktsioon saab sisendiks kaks sõnastikku. Tuleb leida kahest sõnastikust kõik sellised võti-väärtus paarid, mis on unikaalsed mõlema sõnastiku jaoks (ehk leiduvad ainult ühes või teises sõnastikus).
Võite olla kindlad, et kui mõlemas sõnastikus esineb sama võti, siis nende väärtused on samad ehk sellist olukorda ei saa tekkida: 
dict1 = {"a": 1}, dict2 = {"a": 2}