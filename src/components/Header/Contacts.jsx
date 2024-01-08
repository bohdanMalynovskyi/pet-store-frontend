import React, { useState } from 'react';
import { ChevronDownIcon } from '@heroicons/react/24/outline';
import phone from '../../assets/images/phone.svg';
import email from '../../assets/images/google.svg';

const Contacts = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [showContacts, setShowContacts] = useState(false);
  const toggleMenu = () => {
    setIsMenuOpen(!isMenuOpen);
    setShowContacts(!showContacts);
  };
  const handleKeyPress = (event) => {
    if (event.key === 'Enter') {
      toggleMenu();
    }
  };

  const dynamicClass = isMenuOpen ? 'w-full shadow-md px-3 pt-3 pt-[40px]' : '';
  return (
    <div className={` absolute hidden md:block items-center bg-[#fff] text-lg ${dynamicClass}`}>
      <div className=' flex items-center gap-1'>
        <button
          className={`hover:drop-shadow-lg cursor-pointer  text-lg hover:text-cyan `}
          onClick={() => {
            toggleMenu();
          }}
          onKeyPress={handleKeyPress}
          tabIndex={0}
        >Контакти
        </button>
        <ChevronDownIcon
          strokeWidth={2.5}
          className={` h-6 w-6 transition-transform lg:block  ${isMenuOpen ? "rotate-180" : ""
            }`}
        />
      </div>
      {showContacts && (
        <div className=' flex flex-col'>
          <div className='flex gap-1 items-center mt-5 mb-[11px] '>
            <img src={phone} alt="phone" />
            <div className={``}>+38(097)-122-41-54</div>
          </div>
          <div className='flex gap-1 items-center '>
            <img src={email} alt="email" />
            <div className={``}>felinecanine@gmail.com</div>
          </div>
        </div>

      )}
    </div>
  )
}

export default Contacts