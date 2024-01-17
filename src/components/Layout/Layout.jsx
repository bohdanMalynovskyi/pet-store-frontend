import React from 'react';
import Routes from '../../routes/Routers';
import Footer from '../Footer/Footer';

const Layout = () => {
  return (
    <div className=" min-h-screen flex flex-col text-primary">
      <div className=" flex-auto">
        <Routes />
      </div>
      <Footer />
    </div>
  );
};

export default Layout;
