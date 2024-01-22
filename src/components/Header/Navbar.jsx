import React from 'react';
import { NavLink } from 'react-router-dom';
import navLinks from "../../db/menu";

const Navbar = () => {
    return (
        <nav className='relative hidden md:block max-w-[1200px] px-5 '>
            <ul className='flex items-center justify-center'>

                {navLinks.map((item, index) => {
                    return (
                        <li key={index} className='group'>
                            {/* категорія тварин */}
                            <NavLink
                                className='relative mx-5 text-lg font-ttnorms font-bold block transition hover:text-hover'
                                to={item.path}
                            >
                                {item.display}
                            </NavLink>

                            {/* випадаюче меню */}
                            {item.dropdown && (
                                <div className=' dropdown-item  absolute z-50 hidden group-hover:block inline-block whitespace-nowrap bg-[#fff] drop-shadow-md p-[40px] transform -translate-x-1/2 left-1/2'>
                                    <ul className=' flex gap-10'>
                                        {/* категорія товарів */}
                                        {item.dropdown.map((subItem) => {
                                            return (
                                                <li key={`${item.id}-${subItem.id}`}>
                                                    <NavLink
                                                        className='block text-lg font-medium mb-5 transition hover:text-hover'
                                                        to={subItem.path}
                                                    >
                                                        {subItem.display}
                                                    </NavLink>
                                                    {/* підкатегорія товарів */}
                                                    {subItem.children && (
                                                        <div className=' flex flex-col gap-2'>
                                                            {subItem.children.map((el) => {
                                                                return (
                                                                    <li key={el.id}>
                                                                        <NavLink
                                                                        className='transition hover:text-hover'
                                                                        to={el.path}
                                                                        >{el.display}</NavLink>
                                                                    </li>
                                                                )
                                                            })}
                                                        </div>
                                                    )}
                                                </li>
                                            )
                                        })}
                                    </ul>
                                </div>
                            )}
                        </li>
                    )
                }
                )
                }
            </ul>
        </nav>
    );
};

export default Navbar;
