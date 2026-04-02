# Sõne alustõed 
Sõne-tüüpi muutujate deklareerimine
Loo muutujad first_name väärtusega "James" ja last_name väärtusega "Bond". Muutuja kohta saad vajadusel samuti lugeda PyDocist.
Sõnede konkatenatsioon (liitmine)
Loo muutuja full_name, mille väärtuseks on sõne järgmisel kujul: "first_name last_name", kus first_name ja last_name on eelmises ülesandes loodud muutujate väärtused. Kasuta selleks sõnede liitmist.
Loo muutuja self_description_sentence, mille väärtus on sõne järgmisel kujul: "My name is last_name, first_name last_name.", kus first_name ja last_name on eelmises ülesandes loodud muutujate väärtused. Sõne kujundamiseks kasuta f-stringi.
Ära unusta, et nimede vahele peaks jääma ka tühik!
Sõnede tükeldamine
Harjutame sõnede tükeldamist ehk slice notation'i kasutamist.
Loo muutuja original_string = "Programming is fun!". Seda sõne hakkame edaspidi tükeldama slice notatsiooni abil.
Loo muutuja backwards, mille väärtus on esialgne sõne tagurpidi (ehk "!nuf si gnimmargorP").
Loo muutuja every_other, mille väärtus on esialgsest sõnest iga järgmine täht ehk esimene, kolmas, viies jne. (ehk "Pormigi u!").
Loo muutuja first_word_reversed, mille väärtus on esialgse sõne esimene sõna tagurpidi ("Programming" -> "gnimmargorP").
Mitmerealised sõned
Loo muutuja cake = "toppingfillingbase".
See on meie kook, mille kihid on vaja printida ülevalt alla kindlas järjekorras: vahukoor, marjad, täidis, põhi. Kasuta selleks muutujat cake, vaid ühte print() funktsiooni ning sõne tükeldamist.
Tulemus peaks välja nägema selline:
topping
filling
base
Vihje: \n kasutamisel prinditakse sõne järgmisele reale.

# Join two strings together
Funktsioon saab parameetritena kaks sõne. Need sõned tuleb kokku kleepida (kõigepealt esimene sõne, siis teine sõne).
Näide: join_strings("ac", "b") peaks tagastama "acb".

# Get first n symbols of a string
On antud sõne ja täisarv n, kirjuta funktsiooni sisu nii, et funktsioon tagastaks sõne esimesed n tähte.
Näide: get_first_n_symbols("hello world", 5) peaks tagastama "hello".

# Longer string first
On antud kaks sõne, pikem sõne läheb esimeseks ja lühem järgneb sellele.
Kui sõned on sama pikkusega, siis first_string on sõne alguses.
Näide: longer_first("abc", "defg") peaks tagastama "defgabc".

# Slice of string
Ette on antud sõne ja kaks indeksit, funktsioon tagastab nende indeksite vahelise alamsõne (kaasa arvatud).
Näide: slice_of_string("hello", 1, 3) peaks tagastama "ell".
