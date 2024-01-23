import React from 'react';
import Routes from '../../routes/Routers';
import ScrollToTop from "react-scroll-to-top";
import Scrollup from "../../assets/images/scrollup.svg"



const Layout = () => {
    return (
        <div className=' font-norms min-h-screen flex flex-col text-primary'>
            <div className=' flex-auto'>
                <Routes />
                <ScrollToTop smooth
                component={<img src={Scrollup} alt='scrollup'></img>}
                />
            </div>
        </div>
    )
}

export default Layout