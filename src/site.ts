/**
 * Single source of truth for company and contact details.
 *
 * The legal pages, the footer and the structured data all read from here, so
 * these values are only ever written down once.
 *
 * TODO: fields marked PLACEHOLDER must be filled with the real GbR details
 * before the site goes live — an Impressum with wrong or missing data is the
 * classic Abmahnung trigger.
 */
export const site = {
  name: 'nyveo',
  legalName: 'Hinneburg & Oestmann GbR',
  tagline: 'Ich sehe Neues.',
  description:
    'Moderne Webseiten im Abo für lokale Unternehmen. Design, Hosting, Wartung, Support. Von Anfang an sichtbar.',
  url: 'https://nyveo.de',

  phone: '', // Handynummer auf Wunsch vorerst entfernt
  phoneHref: '',
  email: 'info@nyveo.de',

  // Required by § 5 DDG (formerly § 5 TMG).
  address: {
    street: 'Gärtnerstraße 26a',
    postalCode: '20253',
    city: 'Hamburg',
    country: 'Deutschland',
  },

  // Both partners of a GbR must be named in the Impressum.
  partners: ['Christian Hinneburg', 'Niels Oestmann'],

  vatId: '', // Noch keine USt-IdNr vorhanden

  socials: {
    instagram: 'https://instagram.com/', // PLACEHOLDER
    linkedin: 'https://linkedin.com/', // PLACEHOLDER
  }
} as const;

export const nav = [
  { label: 'Warum nyveo?', href: '/#warum-nyveo' },
  { label: 'Leistungen', href: '/#leistungen' },
  { label: 'Ablauf', href: '/#ablauf' },
  { label: 'Angebot & Kontakt', href: '/#kontakt' },
] as const;
