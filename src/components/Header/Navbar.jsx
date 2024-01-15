import React from 'react';
import { NavLink } from 'react-router-dom';

const nav__links = [
    {
        display: "Собакам",
        path: "/dogs"
    },
    {
        display: "Котам",
        path: "/cats"
    },
    {
        display: "Гризунам",
        path: "/smallpets"
    },
    {
        display: "Птахам",
        path: "/birds"
    },
    {
        display: "Рибам",
        path: "/fish"
    },
    {
        display: "Рептиліям",
        path: "/reptiles"
    },
]

const Navbar = () => {
    return (
        <nav className=' hidden md:block max-w-[1200px] px-5'>

            <div className='flex items-center justify-center'>
                {nav__links.map((item, index) => (
                    <div key={index} className=' border-r-2 last:border-r-0'>
                        <NavLink
                            className=' mx-5 font-bold block transition hover:text-cyan '
                            to={item.path}
                        >{item.display}
                        </NavLink>
                    </div>
                ))}
            </div>

        </nav>
    )
}

export default Navbar