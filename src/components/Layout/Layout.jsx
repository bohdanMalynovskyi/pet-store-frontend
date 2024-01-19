import React from 'react';
import Header from "../Header/Header";
import Footer from "../Footer/Footer";
import Routes from '../../routes/Routers';
import { useLocation } from 'react-router-dom';
import ScrollToTop from "react-scroll-to-top";
import Scrollup from "../../assets/images/scrollup.svg"



const Layout = () => {
    const location = useLocation();
    const isHomePage = location.pathname === '/home';
    return (
        <div className=' font-ttnorms min-h-screen flex flex-col text-primary'>
            <Header isHomePage={isHomePage} />
            <div className=' flex-auto'>
                <Routes />
                <ScrollToTop smooth
                component={<img src={Scrollup} alt='scrollup'></img>}
                />
            </div>
            <Footer />
        </div>

    )
}

export default Layout