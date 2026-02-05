**Vilka kolumner behöver tvättas?**
Alla kolumner är str förutom betyg som redan är en float och det stämmer, så datum behöver göras till datetime, pris och gram till float eller int osv.

**Order_id, orderrad_id, produkt_id och kund_id** - ser bra ut och behöver inte tvättas.
**Orderdatum, önskat_leveransdatum, faktiskt_leveransdatum och recensionsdatum** - Fixa så alla datum är i sammaformat och att datatypen är datetime.
**Produktnamn, säsong och kategori** - Kolla stavning, mellanrum och göra en 'mapping' om det behövs.
**Antal, pris och vikt_gram** - Ta bort alla tillägg och endast ha kvar siffror och ändra datatyp till int eller float.
**Leveranszon** - Kolla så att det är rätt datatyp och om det behövs en mapping.
**Recension_text** - se hur jag ska lägga upp så det är lätt att läsa och få med positiv, neutral eller negativ.

Recensionsdatum verkar stämma och behöver inte tvättas men ändras till datetime.
Kategori ser bra ut och behöver inte tvättas.