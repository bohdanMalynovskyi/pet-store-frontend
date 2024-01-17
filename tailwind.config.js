/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        primary: '#011240',
        hover: '#3786A5',
        zinc: '#B2B2B2',
        txtWhite: '#FFFFFF',
      },
      fontFamily: {
        norms: ['TT Norms', 'sans-serif'],
      },
    },
  },
  primary: '#011240',
  plugins: [],
};
