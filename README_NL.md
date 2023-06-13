# ! DISCLAIMER !
Zie hieronder de nederlandse versie van het README.md bestand, het kan misschien niet helemaal correct (nederlands) zijn.


# Programmadocumentatie

Deze documentatie geeft een overzicht van de functionaliteit van het programma, inclusief hoe het werkt en het doel van elk bestand. Het bevat ook instructies voor het gebruik van het programma en voorbeeldgebruik.

## Inhoudsopgave
- [Overzicht](#overzicht)
- [Bestanden](#bestanden)
  - [main.py](#mainpy)
  - [dbhandler.py](#dbhandlerpy)
- [Gebruik](#gebruik)
- [Voorbeeldgebruik](#voorbeeldgebruik)

## Overzicht<a name="overzicht"></a>
Het programma is een servertoepassing die functionaliteit met betrekking tot e-mail afhandelt. Het stelt gebruikers in staat om verbinding te maken, e-mails op te halen, nieuwe e-mails toe te voegen en andere gerelateerde bewerkingen uit te voeren. Het programma bestaat uit twee hoofdbestanden: `main.py` en `dbhandler.py`.

## Bestanden<a name="bestanden"></a>

### main.py<a name="mainpy"></a>
`main.py` is het toegangspunt van het programma. Het start de server op en behandelt de communicatie tussen clients en de server. Het bestand bevat de volgende secties:

- **Configuratie**: Deze sectie bevat de configuratievariabelen zoals `projectid`, `username` en `sessionid`. Deze variabelen worden gebruikt om verbinding te maken met de cloud en de sessie tot stand te brengen.

- **Opstartcode**: Deze sectie initialiseert de benodigde componenten voor de server om te functioneren. Het importeert de vereiste modules en maakt een verbinding met het cloudproject met behulp van de opgegeven sessie-ID en gebruikersnaam. Het maakt ook een instantie van de klasse `scratch3.CloudRequests` aan om inkomende verzoeken af te handelen.

- **Verzoeken**: Deze sectie definieert verschillende verzoekhandlers die verschillende soorten verzoeken van clients afhandelen. De verzoeken omvatten het verbinden met een gebruikersnaam, het ophalen van e-mails specifiek voor een gebruiker, het ophalen van e-mails op basis van ID en het toevoegen van nieuwe e-mails. Elke verzoekhandler voert specifieke bewerkingen uit en retourneert de bijbehorende gegevens.

- **Eindcode**: Deze sectie definieert een gebeurtenishandler voor het `on_ready`-gebeurtenis van de server, dat wordt geactiveerd wanneer de server gereed is om verzoeken te ontvangen. Het start ook de server door de methode `run` aan te roepen.

### dbhandler.py<a name="dbhandlerpy"></a>
`dbhandler.py` is een module die functies biedt voor toegang tot en manipulatie van e-mailgegevens in de database. Het bevat de volgende functies:

- **getmail**: Deze functie haalt een e-mail op uit de database op basis van het opgegeven ID. Het leest het databasebestand `db.json` en haalt de relevante informatie op voor de gespecificeerde e-mail-ID. De functie retourneert de gegevens van de e-mail in een lijst.

- **add_email**: Deze functie voegt een nieuwe e-mail toe aan de database. Het neemt e-mailinformatie als invoer, splitst deze in titel, inhoud, auteur en ontvanger velden en maakt een nieuw e-mailobject aan. De functie werkt vervolgens het `db.json`-bestand bij door het nieuwe e-mailobject aan de database toe te voegen.

## Gebruik<a name="gebruik"></a>
Om het programma te gebruiken, volg je deze stappen:

1. Zorg ervoor dat je de benodigde afhankelijkheden hebt geïnstalleerd. Het programma vereist de modules `scratchattach` en `json`.

2. Stel de configuratievariabelen in `main.py` in op basis van jouw omgeving. Geef de juiste waarden op voor `projectid`, `username` en `sessionid`.

3. Zorg ervoor dat het bestand `db.json` bestaat en toegankelijk is voor het programma. Dit bestand fungeert als de database voor het opslaan van e-mailgegevens.

4. Voer het programma uit door `main.py` uit te voeren met een Python-interpreter.

5. Zodra de server start, luistert deze naar inkomende verzoeken en reageert daarop.

## Voorbeeldgebruik<a name="voorbeeldgebruik"></a>
Hier is een voorbeeld van hoe je de functie `add_email` in `dbhandler.py` kunt gebruiken om een nieuwe e-mail toe te voegen:

```python
new_email = {
    "title": "Nieuwe e-mailtitel",
    "content": "Dit is de inhoud van de nieuwe e-mail",
    "author": "Jan Jansen",
    "sendto": "janet@example.com"
}
add_email(','.join(new_email.values()))
```
