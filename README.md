# Änderungsschneiderei Altun Website

Offizielle Website der Änderungsschneiderei Altun in Düsseldorf-Oberkassel — statische Site, gebaut mit [Astro](https://astro.build).

## Entwicklung

```bash
npm install
npm run dev      # http://localhost:4321
npm run build    # Ausgabe nach dist/
npm run preview  # gebaute Site lokal servieren
npm run check    # Typ- und Template-Prüfung
```

Node 20+ empfohlen.

## Aufbau

```text
src/
  pages/        index, impressum, datenschutz, ueber-uns
  layouts/      Base.astro — <head>, Meta-Tags, Header/Footer
  components/   Wiederverwendbare Komponenten (Header, Footer)
  styles/       fonts.css (@font-face) + global.css (Zentrale Styles & Farben)
  assets/       Bilder (Storefront, Innenaufnahmen, Logo) und Fonts
  site.ts       Geschäftsdaten und Navigation — zentrale Konfiguration
```

## Besonderheiten

- **Design:** Ein individuelles, klassisches Layout mit einer burgunderroten Leitfarbe (`#6e3c4d`), passend zur realen Außenwerbung der Schneiderei.
- **Bilder:** Die Bilddateien im Ordner `src/assets/images` wurden aus realen Aufnahmen (z.B. Google Maps) aufbereitet.
- **Rechtstexte:** Aktuell sind Platzhaltertexte eingefügt. Diese müssen vor Livegang noch einmal rechtlich geprüft und mit den tatsächlichen Inhaberdaten versehen werden. (Siehe `src/site.ts`).
