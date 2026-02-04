Alla kolumner är str förutom betyg som redan är en float och det stämmer, så datum behöver göras till datetime, pris och gram till float eller int osv.

Order_id, orderrad_id, produkt_id och kund_id - ser bra ut och behöver inte tvättas.
Orderdatum, önskat_leveransdatum, faktiskt_leveransdatum och recensionsdatum - Fixa så alla datum är i sammaformat och att datatypen är datetime.
Produktnamn, säsong och kategori - Kolla stavning, mellanrum och göra en 'mapping' om det behövs.
Antal, pris och vikt_gram - Ta bort alla tillägg och endast ha kvar siffror och ändra datatyp till int eller float.
Leveranszon - Kolla så att det är rätt datatyp och om det behövs en mapping.
Recension_text - se hur jag ska lägga upp så det är lätt att läsa och få med positiv, neutral eller negativ.

recensionsdatum verkar stämma och behöver inte tvättas.
kategori behöver inte tvättas.

Produktnamn - Här bestämde jag att det blir bäst att försöka göra det till så få produktnamn som möjligt. Därför har jag tagit bort extra tillägg på de produkter som det behövts för att göra färre skillnader. Till exempel har jag valt att göra alla tomatfrön under samma namn och tänkt att typ av tomatfrö blir som ett tillägg att välja senare. Sedan tog jag bort storleken på till exempel terrakottakrukan och tänkte på samma sätt där.



**Vilka kolumner behöver tvättas?**

**1.** Orderdatum - Fixa så alla orderdatum är sammaformat och att datatypen är datetime.
**2.** Önskat_leveransdatum - Fixa så alla orderdatum är sammaformat och att datatypen är datetime.
**3.** Faktiskt_leveransdatum - Göra datatypen till datetime.
**4.** Produktnamn - Kolla stavning, mellanrum och göra en 'mapping' om det behövs.
**5.** Säsong - Kolla stavning, mellanrum och göra en 'mapping' om det behövs.
**6.** Antal - Ta bort alla tillägg och endast ha kvar siffror och ändra datatyp till int eller float.
**7.** Pris - Ta bort alla tillägg och endast ha kvar siffror och ändra datatyp till int eller float.
**8.** Vikt_gram - Ta bort alla tillägg och endast ha kvar siffror och ändra datatyp till int eller float.
**9.** Leveranszon - Kolla så alla har samma datatyp och om det behövs en mapping.
**10.** Recension_text, recensionsdatum, betyg 