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
  legalName: 'nyveo GbR', // PLACEHOLDER: confirm exact registered name
  tagline: 'Ich sehe Neues.',
  description:
    'Moderne Webseiten im Abo für lokale Unternehmen. Design, Hosting, Wartung, Support. Von Anfang an sichtbar.',
  url: 'https://nyveo.de',

  phone: '0157 388 344 37',
  phoneHref: '+4915738834437',
  email: 'kontakt@nyveo.de', // PLACEHOLDER: confirm public contact address

  // PLACEHOLDER: required by § 5 DDG (formerly § 5 TMG).
  address: {
    street: 'Musterstraße 1',
    postalCode: '00000',
    city: 'Musterstadt',
    country: 'Deutschland',
  },

  // PLACEHOLDER: both partners of a GbR must be named in the Impressum.
  partners: ['Vorname Nachname', 'Vorname Nachname'],

  vatId: '', // PLACEHOLDER: USt-IdNr. per § 27a UStG, if one has been issued.
} as const;

export const nav = [
  { label: 'Leistungen', href: '/#leistungen' },
  { label: 'Angebot', href: '/#pakete' },
  { label: 'Ablauf', href: '/#ablauf' },
  { label: 'Kontakt', href: '/#kontakt' },
] as const;
