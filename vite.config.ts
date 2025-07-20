import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  optimizeDeps: {
    exclude: ['lucide-react'],
  },
  server: {
    port: parseInt(process.env.PORT) || 5173, // Use Render's assigned port
    host: true, // Allow external access (required for cloud hosting)
  },
});
