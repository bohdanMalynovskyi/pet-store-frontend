import React from 'react';
import { NavLink } from 'react-router-dom';
import navLinks from "../../db/menu";

const Navbar = () => {
    return (
        <nav className='hidden md:block max-w-[1200px] px-5 '>
            <ul className='flex items-center justify-center'>
                {navLinks.map((item, index) => (
                    <li key={index} className='group relative'>
                        <NavLink
                            className='relative mx-5 text-lg font-ttnorms font-bold block transition hover:text-hover'
                            to={item.path}
                        >
                            {item.display}
                        </NavLink>
                        {item.dropdown && (
                            <div className='absolute z-50 hidden group-hover:block inline-block whitespace-nowrap bg-[#fff] drop-shadow-md p-[40px]'>
                                <ul>
                                    {item.dropdown.map((subItem) => (
                                        <li key={subItem.id}>
                                            <NavLink
                                                className='block py-2 px-4 transition hover:text-hover'
                                                to={subItem.path}
                                            >
                                                {subItem.display}
                                            </NavLink>
                                        </li>
                                    ))}
                                </ul>
                            </div>
                        )}
                    </li>
                ))}
            </ul>
        </nav>
    );
};

export default Navbar;












