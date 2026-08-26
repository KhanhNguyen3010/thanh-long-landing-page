import { defineConfig } from 'vite';
import handlebars from 'vite-plugin-handlebars';
import { resolve } from 'path';

export default defineConfig({
  base: '/thanh-long-landing-page/',
  server: {
    allowedHosts: true
  },
  plugins: [
    handlebars({
      partialDirectory: resolve(__dirname, 'src/components'),
    }),
  ],
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        about: resolve(__dirname, 'about.html'),
        camon: resolve(__dirname, 'cam-on.html'),
        contact: resolve(__dirname, 'contact.html'),
        programs: resolve(__dirname, 'programs.html'),
        testimonials: resolve(__dirname, 'testimonials.html')
      }
    }
  }
});
