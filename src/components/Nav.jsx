import React, { useState } from 'react';

const Navbar = () => {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <nav className="bg-gray-800 p-4">
      <div className="max-w-7xl mx-auto flex items-center justify-between">
        <div className="flex items-center">
          <span className="text-white text-xl font-bold">LOGO</span>
      
        </div>
        <div className="hidden md:flex items-center space-x-4">
          <p className="text-white hover:text-gray-300">Menu Item 1</p>
          <p  className="text-white hover:text-gray-300">Menu Item 2</p>
          <p className="text-white hover:text-gray-300">Menu Item 3</p>
          <p  className="text-white hover:text-gray-300">Menu Item 4</p>
        </div>
        <div className="md:hidden flex items-center">
        <button
            onClick={() => setIsOpen(!isOpen)}
            className="text-white focus:outline-none focus:text-white"
          >
            MENU
          </button>
        </div>
      </div>
      {/* Responsive menu */}
      {isOpen && (
        <div className="md:hidden mt-2 flex flex-col items-center space-y-2">
          <p className="text-white hover:text-gray-300">Menu Item 1</p>
          <p  className="text-white hover:text-gray-300">Menu Item 2</p>
          <p  className="text-white hover:text-gray-300">Menu Item 3</p>
          <p  className="text-white hover:text-gray-300">Menu Item 4</p>
        </div>
      )}
    </nav>
  );
};

export default Navbar;
