/**
 * Single source of truth for company and contact details.
 */
export const site = {
  name: 'Altun',
  legalName: 'Änderungsschneiderei Altun',
  tagline: 'Maßgeschneiderte Qualität für Ihre Kleidung',
  description:
    'Ihre zuverlässige Änderungsschneiderei in Düsseldorf-Oberkassel. Anpassungen, Reparaturen und Maßanfertigungen von Damen- und Herrenbekleidung.',
  url: 'https://altun-schneiderei.de', // Platzhalter URL

  phone: '0163 8219282',
  phoneHref: 'tel:01638219282',
  email: 'info@altun-schneiderei.de',

  // Google Business Profile (Öffnungszeiten, Feiertage, Anfahrt).
  mapsUrl: 'https://maps.app.goo.gl/aRWsfjSnJb85uXTXA',

  // Required by § 5 DDG (formerly § 5 TMG).
  address: {
    street: 'Belsenstraße 25',
    postalCode: '40545',
    city: 'Düsseldorf',
    country: 'Deutschland',
  },

  partners: ['Herr Altun'], // Inhaber

  vatId: '',

  socials: {
    instagram: '',
    linkedin: '',
  }
} as const;
