import React from 'react';
import { NavLink } from 'react-router-dom';
import { ChevronDownIcon } from '@heroicons/react/24/outline';

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

const NavMobile = () => {
    const [click, setClick] = React.useState(false);
    const toggleMenu = () => {
        setClick(!click);
    };
    return (
        <nav className=' absolute w-full h-[100vh] bg-[#fff] px-5'>

            <div className=' my-5 ul '>
                {nav__links.map((item, index) => (
                    <div key={index} className=' flex justify-between border-b-2 py-3 '>
                        <NavLink
                            className='  font-bold block '
                            onClick={toggleMenu}
                            to={item.path}
                        >
                            {item.display}
                        </NavLink>
                        <ChevronDownIcon
                            strokeWidth={2.5}
                            className={` h-6 w-6 transition-transform lg:block  ${click ? "rotate-90" : ""
                                }`}
                        />
                    </div>
                ))}
            </div>

        </nav>
    )
}

export default NavMobile