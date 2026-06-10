/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './index.html',
    './src/**/*.{js,jsx,ts,tsx}'
  ],
  theme: {
    extend: {
      colors: {
        background: '#050505',
        surface: '#111111',
        violet: '#7C3AED',
        violetSoft: '#A855F7',
        gold: '#FFD700',
        text: '#FFFFFF',
        muted: '#D1D5DB'
      },
      boxShadow: {
        glow: '0 30px 90px rgba(124, 58, 237, 0.22)',
        gold: '0 20px 60px rgba(255, 215, 0, 0.18)'
      },
      backgroundImage: {
        'hero-gradient': 'radial-gradient(circle at top left, rgba(124, 58, 237, 0.24), transparent 28%), radial-gradient(circle at 80% 20%, rgba(255, 215, 0, 0.16), transparent 20%)'
      }
    }
  },
  plugins: []
};
