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

  phone: '0211 46841229',
  phoneHref: 'tel:021146841229',
  email: 'info@altun-schneiderei.de',

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

export const nav = [
  { label: 'Leistungen', href: '/#leistungen' },
  { label: 'Kontakt', href: '/#kontakt' },
] as const;
