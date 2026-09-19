# nyveo-website

Offizielle Website der nyveo GbR — statische Site, gebaut mit [Astro](https://astro.build).

## Entwicklung

```bash
npm install
npm run dev      # http://localhost:4321
npm run build    # Ausgabe nach dist/
npm run preview  # gebaute Site lokal servieren
npm run check    # Typ- und Template-Prüfung
```

Node 20+ erforderlich (entwickelt mit Node 24).

## Aufbau

```
src/
  pages/        eine Datei je Route (index, impressum, datenschutz, agb, 404)
  layouts/      Base.astro — <head>, Meta-Tags, Header/Footer
  components/   Seitenabschnitte (Hero, Compare, Features, Offer, Steps, ...)
  styles/       fonts.css (@font-face) + global.css (Design aus dem Entwurf)
  assets/       Bilder und Webfonts, werden beim Build optimiert
  site.ts       Firmen- und Kontaktdaten — zentrale Quelle
scripts/        einmalige Migrationsskripte aus dem HTML-Entwurf
```

Das ursprüngliche `nyveo_html_entwurf_Sep-15.html` liegt unverändert im Repo als
Referenz für das Design.

## Offene Punkte vor dem Livegang

- [ ] **Schriften klären.** `Roc Grotesk` und `Maax` sind kommerziell und wurden im
      Entwurf erfolglos von Google Fonts geladen (HTTP 400). Aktuell stehen Archivo
      und Inter als selbst gehostete Platzhalter drin — siehe `src/styles/fonts.css`.
- [ ] **Formular-Endpunkt setzen.** `PUBLIC_FORM_ENDPOINT` in `.env` (siehe
      `.env.example`). Ohne ihn zeigt das Formular den Telefon-Fallback.
- [ ] **Rechtstexte füllen und prüfen lassen.** Impressum, Datenschutz und AGB
      enthalten Platzhalter und eine rote Entwurfs-Warnung. Echte Daten in
      `src/site.ts` eintragen, Texte anwaltlich prüfen, dann
      `<LegalDraftWarning />` aus den Seiten entfernen.
- [ ] **Bildmaterial.** Die sieben Bilder des Entwurfs sind Ausschnitte aus nur zwei
      Fotos (Motorenwerkstatt, Blumenladen). Für die Bildleiste mehr Motive besorgen
      und Lizenzen klären.
- [ ] **Deployment.** Netlify oder Cloudflare Pages; beide bieten einen
      Formular-Endpunkt ohne eigenes Backend.
