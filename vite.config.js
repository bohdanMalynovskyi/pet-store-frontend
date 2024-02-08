// eslint-disable-next-line import/namespace
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react-swc';
import eslint from 'vite-plugin-eslint';

// https://vitejs.dev/config/
export default defineConfig({
  // optimizeDeps: { exclude: ["swiper/vue", "swiper/types"], },
  plugins: [react(), eslint()],
});
