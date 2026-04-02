# Puuviljade tellimus
Iga suure koosoleku või ürituse jaoks tellib firma teatud koguse puuvilju. Tellimus esitatakse tavaliselt kilodes. Kui tellimus jõuab kullerini, peab ta andma laotöötajatele teada, kui palju väiksemaid ja suuremaid puuviljukorve läheb tellimuse jaoks vaja. Väike puuviljakorv on 1 kg, suur puuviljakorv on 5 kg. Tellimuse edukaks täitmiseks peab saama panna lao poolt pakutud väiksed ja suured puuviljakorvid kokku, et lõpuks saada tellitud summa kilodes.

Kui tellitud puuviljade kaalu ei ole võimalik moodustada antud korvidest, siis tellimust täita ei saa ning funktsioon peab tagastama -1

Tellimus tuleb täita täpselt soovitud mahus. Kui tellitakse 9kg, siis seda ei saa katta kahe suure korviga (10kg). Vaja on kas ühte suurt ja 4 väikest või 9 väikest korvi.

Suured korvid lähevad alati esimesena arvesse. Kui on vaja täita tellimus 11 kg ning meil on 20 suurt ja 20 väikest korvi, siis kõigepealt kasutame kaks suurt korvi, seejärel 1 väikese korvi.

Kui tellimus õnnestub täita, siis tuleb tagastada laost võetud väikeste korvide arvu

small_basket - int: väikeste puuviljakorvide arv

big_baskets - int: suurte puuviljakorvide arv

ordered_amount - int: tellitud kogus kilodes

sisendid on alati mittenegatiivsed täisarvud.
