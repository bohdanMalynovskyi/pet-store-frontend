const withMT = require("@material-tailwind/react/utils/withMT");
module.exports =withMT({
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'primary': '#011240',
        'hover':"#3786A5",
        'zinc':'#B2B2B2'
      }
    },
  },
  plugins: [],
}) 
