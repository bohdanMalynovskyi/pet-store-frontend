import React from 'react';
import { ShoppingBagIcon } from '@heroicons/react/24/outline';

const Cart = () => {
  const [isMobile, setIsMobile] = React.useState(false);
  React.useEffect(() => {

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
    <div className={` hover:text-cyan ${navbarClasses}`}><ShoppingBagIcon/></div>
  )
}

export default Cart