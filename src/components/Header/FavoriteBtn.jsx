import React, { useState, useEffect } from 'react';

const Favorite = () => {
  const [isMobile, setIsMobile] = useState(false);

  useEffect(() => {

    const checkScreenSize = () => {
      setIsMobile(window.innerWidth < 720);
    };
    checkScreenSize();

    window.addEventListener('resize', checkScreenSize);

    return () => {
      window.removeEventListener('resize', checkScreenSize);
    };
  }, []);
  const navbarClasses = isMobile ? 'text-[#fff] w-6 h-6' : 'text-primary w-8 h-8';

  return (
    <div className={` hover:text-hover ${navbarClasses}`}>
      <svg
        viewBox="0 0 32 32"
        fill="none"
        xmlns="http://www.w3.org/2000/svg">
        <g transform="translate(0, 2)"
        clipPath="url(#clip0_35_333)"
          filter="url(#filter0_d_35_333)">
          <path d="M18.2393 27C18.2393 27 5.23926 20 5.23926 11.75C5.23926 9.95979 5.95042 8.2429 7.21629 6.97703C8.48216 5.71116 10.199 5 11.9893 5C14.813 5 17.2318 6.53875 18.2393 9C19.2468 6.53875 21.6655 5 24.4893 5C26.2795 5 27.9964 5.71116 29.2622 6.97703C30.5281 8.2429 31.2393 9.95979 31.2393 11.75C31.2393 20 18.2393 27 18.2393 27Z"
            stroke="currentColor"
            strokeWidth="1.5"
            strokeLinecap="round"
            strokeLinejoin="round" />
        </g>
      </svg>
    </div>
  );
};
export default Favorite

