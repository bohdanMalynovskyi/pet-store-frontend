import React, {} from 'react';
import { NavLink } from 'react-router-dom';
import nav__links from "../../db/menu"


const Navbar = () => {
    console.log(nav__links);
    return (

        <nav className='hidden md:block max-w-[1200px] px-5'>
            <ul className='flex items-center justify-center'>
                {nav__links.map((item, index) => (
                    <li
                        key={index}
                        className='border-r-2 last:border-r-0'
                    >

                        <NavLink
                                className='relative mx-5 font-bold block transition hover:text-cyan'
                                to={item.path}
                            >
                                {item.display}
                            </NavLink>


                    </li>

                ))}
            </ul>
        </nav >
    )
}

export default Navbar













