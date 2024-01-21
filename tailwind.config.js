/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        primary: '#011240' /*active*/,
        secondary: '#3786A5' /*hover*/,
        third: '#317B98' /*press*/,
        disabled: '#B2B2B2',
        background: '#F2CC85',
        accent: '#F2CC85',
        txtPrimary: '#161616',
        txtSecondary: '#FFFFFF' /*txtWhite*/,
      },
      fontFamily: {
        norms: ['TT Norms', 'sans-serif'],
      },
    },
  },
  primary: '#011240',
  plugins: [],
};
