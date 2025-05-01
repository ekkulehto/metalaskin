# Metalaskin

**Metalaskin** on esimerkki Pythonilla toteutetusta metaohjelmointia demonstroivasta sovelluksesta. Tässä ohjelmassa käytetään metaluokkaa, joka muokkaa luokan rakennetta ennen sen luontia. Sovellus rakentaa automaattisesti yksinkertaisen nelilaskimen, joka osaa laskea summan, erotuksen, tulon ja osamäärän.

---

## Mitä ohjelma tekee?

Ohjelma demonstroi Pythonin metaohjelmointia seuraavasti:

- `Metaluokka` muokkaa `Laskin`-luokan rakennetta ennen sen luontia.
- Kaikki laskutoimitukset (`summa`, `erotus`, `tulo`, `osamäärä`) lisätään automaattisesti `Laskin`-luokkaan metaluokan avulla.
- Jokainen laskutoimitus on kääritty **dekoraattorilla**, joka huolehtii laskutoimituksen tulostamisesta käyttäjälle.
- Pääohjelmassa käyttäjä voi valita haluamansa laskutoimituksen, antaa sille luvut ja laskin suorittaa operaation sekä näyttää sen tuloksen.

Esimerkiksi käyttäjän valitessa laskuoperaatio "summa" ja luvut (1, 1) ohjelma tulostaa:

```bash
Valitse laskutoimitus [enter lopettaa]

1: summa
2: erotus
3: tulo
4: osamäärä

Valinta: 1
Anna ensimmäinen luku: 1
Anna toinen luku luku: 1
Lukujen 1 ja 1 summa on 2
```

---

## Miten ohjelmaa ajetaan?

1. **Lataa** tämä repositorio:

2. Suorita Python-tiedosto:

   ```
   python metalaskin.py
   ```

3. Käytä laskinta komentorivillä:

   - Valitse toiminto (1–4)
   - Syötä kaksi kokonaislukua
   - Tulokset tulostuvat automaattisesti

4. Lopeta ohjelma painamalla Enter ilman valintaa.

---

## Riippuvuudet

Ei ulkoisia kirjastoja. Toimii suoraan Pythonin vakiokirjastolla.

---

## Esimerkki metaluokan käytöstä

Metaluokka lisää funktiot suoraan Laskin-luokkaan jo ennen sen luontia:

```python
class Laskin(metaclass=Metaluokka):
    pass
```

Kaikki dekoraattorilla käärityt laskutoimitukset syntyvät automaattisesti ilman että niitä kirjoitetaan Laskin-luokan sisälle manuaalisesti. Tämä on hyvä esimerkki siitä, miten metaohjelmointi voi automatisoida luokkien rakentamista ja/tai laajentamista..
