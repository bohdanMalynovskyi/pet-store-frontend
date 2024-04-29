import React, { useState } from 'react';
import phone from '../../assets/images/phone.svg';
import email from '../../assets/images/google.svg';
import { ChevronDownIcon } from '@heroicons/react/24/outline';

const Contacts = () => {
  const [showContacts, setShowContacts] = useState(false);

  return (
    <div className="hidden md:block items-center bg-[#fff] text-lg group">
      <button onClick={() => setShowContacts((prev) => !prev)} className=" flex items-center gap-1 hover:text-hover">
        <span className="hover:drop-shadow-lg cursor-pointer  text-lg hover:text-hover">Контакти</span>
        <ChevronDownIcon className={`h-6 w-6 transition-transform lg:block ${showContacts ? 'rotate-180 ' : ''}`} />
      </button>
      {showContacts && (
        <div className=" flex flex-col absolute bg-white">
          <div className="flex gap-1 items-center mt-5 mb-[11px] ">
            <img src={phone} alt="phone" />
            <div className={``}>+38(097)-122-41-54</div>
          </div>
          <div className="flex gap-1 items-center ">
            <img src={email} alt="email" />
            <div className={``}>felinecanine@gmail.com</div>
          </div>
        </div>
      )}
    </div>
  );
};

export default Contacts;
