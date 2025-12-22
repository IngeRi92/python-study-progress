# Nämm nämm
Funktsioon print_food_person_eats(foods: list, many_can_eat: int) võtab sisendiks nimekirja (foods), kus on erinevad toidud, ja täisarvu (many_can_eat), mis näitab, mitu toitu inimene jaksab ära süüa.
Funktsioon prindib iga söödava toidu nime kujul Eating [food], alustades nimekirja algusest ja liikudes edasi, kuni lubatud kogus on söödud.
Kui many_can_eat on 0 või väiksem, ei peaks funktsioon midagi printima.
Lahenda kasutades while-loop’i!
Näiteks print_food_person_eats(["banana", "chicken", "cake", "potato"], 3) korral prindib konsool järgmised read
Eating banana
Eating chicken
Eating cake

# Trüki paarisarvud kahest kuni kahekümneni
Kirjuta funktsioon print_even_numbers_to_twenty(), mis trükib konsooli paarisarvud vahemikus 2 kuni 20-ni. Kasuta lahenduses while-tsükklit.

# Summa ühest viieni
Kirjuta funktsioon sum_to_five(), mis tagastab summa 1-st kuni 5-ni. Kasuta selleks while-tsüklit.

# Make hola string
Funktsioon saab sisendiks arvu, mis näitab, mitu korda peab sõne "hola" sisalduma funktsiooni väljundis.
Ülesanne tuleks lahendada while-tsükliga nii, et iga kord, kui väljundsõnele on liidetud "hola", siis count väärtus väheneb ühe võrra.
Tsükkel kestab seni, kuni count väärtus on 0.

# Liida kuni sajani
Funktsioon count_until_sum_hundred(number: int) saab sisendiks ühe suvalise täisarvu number (mis on väiksem kui 100) ning alustab liitmist nullist. Iga kord lisatakse saadud summale sisendiks antud arv, kuni summa jõuab vähemalt 100-ni. Funktsioon tagastab, mitu iteratsiooni ehk lisamistegevust oli vaja, et saavutada või ületada 100.
Lahenda kasutades while-tsüklit!