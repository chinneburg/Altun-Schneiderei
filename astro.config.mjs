// @ts-check
import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://nyveo.de',
  image: {
    // Astro's sharp pipeline handles the resizing/AVIF+WebP encoding that the
    // base64 draft could not do.
    responsiveStyles: true,
  },
});
