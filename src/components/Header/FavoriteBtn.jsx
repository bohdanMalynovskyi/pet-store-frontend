import React, { useState, useEffect } from 'react';
import { HeartIcon } from '@heroicons/react/24/outline';

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
  const navbarClasses = isMobile ? 'text-[#fff]' : 'text-primary';

  return (
    <div className={` ml-[120px] hover:text-cyan ${navbarClasses}`}>
      <HeartIcon/>
    </div>
  );
};

export default Favorite