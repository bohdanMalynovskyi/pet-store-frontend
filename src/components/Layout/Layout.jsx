import React from 'react';
import Header from "../Header/Header";
import Footer from "../Footer/Footer";
import Routes from '../../routes/Routers';
import { useLocation } from 'react-router-dom';


const Layout = () => {
    const location = useLocation();
    const isHomePage = location.pathname === '/home';
    return (
        <div className=' min-h-screen flex flex-col text-primary'>
            <Header isHomePage={isHomePage}/>
            <div className=' flex-auto'>
                <Routes />
            </div>
            <Footer />
        </div>

    )
}

export default Layout
