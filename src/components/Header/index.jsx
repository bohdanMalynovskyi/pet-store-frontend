import { useEffect, useState } from 'react';
import styles from './index.module.css';
import Navbar from './Navbar';
import Search from './SearchBtn';
import Contacts from './Contacts';
// import logoBlack from '../../assets/images/logo.svg';
// import logoWhite from '../../assets/images/logo-white.svg';
// import { Link } from 'react-router-dom';
// import Cart from './CartBtn';
// import Favorite from './FavoriteBtn';
import { IconButton, MobileNav } from '@material-tailwind/react';
import { Bars3Icon, XMarkIcon } from '@heroicons/react/24/outline';
import SearchDesktop from './SearchDesktop';

// import { Heart } from '../../style/icons/Heart';
import NavMobile from './NavMobile/NavMobile';
import { Bag, Heart, LogoHorizontal, LogoVertical } from '../../style/icons';

const Header = () => {
  const [isMobile, setIsMobile] = useState(false);
  const [openNav, setOpenNav] = useState(false);
  useEffect(() => {
    const checkScreenSize = () => {
      setIsMobile(window.innerWidth < 720);
    };
    checkScreenSize();

    window.addEventListener('resize', checkScreenSize);

    return () => {
      window.removeEventListener('resize', checkScreenSize);
    };
  }, []);

  const navbarClasses = isMobile ? 'bg-primary' : 'bg-[#ffffff]';
  const logoSrc = isMobile ? <LogoHorizontal color="txtSecondary" /> : <LogoVertical color="primary" />;

  useEffect(() => {
    window.addEventListener('resize', () => window.innerWidth >= 960 && setOpenNav(false));
  }, []);

  return (
    <header className={` w-full relative font-norms ${navbarClasses}`}>
      <div className=" mx-auto flex flex-col max-w-[1200px] px-5 py-[17px] md:py-[40px]  ">
        <div className=" flex items-center justify-between md:mb-8">
          <div className="menu__left flex items-center">
            {/*  кнопка моб.меню */}
            <div className=" burger mr-5">
              <IconButton variant="text" color="white" className="md:hidden" onClick={() => setOpenNav(!openNav)}>
                {openNav ? (
                  <XMarkIcon className="h-6 w-6" strokeWidth={2} />
                ) : (
                  <Bars3Icon className="h-6 w-6" strokeWidth={2} />
                )}
              </IconButton>
            </div>

            {/* logo */}
            {logoSrc}
          </div>

          {/* пошук на десктоп-версії */}
          <SearchDesktop />

          {/*  пошук мобверсія/ контакти / улюблене / кошик */}
          <div className="menu__right flex items-center gap-5 relative">
            <Search />
            <Contacts />
            {/* <Favorite /> */}
            {/* <Heart /> */}
            {/* <Cart /> */}
            <Heart count={null} stylesIcon={styles.icon} stylesIconCount={styles.iconCount} />
            <Bag count={null} stylesIcon={styles.icon} stylesIconCount={styles.iconCount} />
          </div>
        </div>
        <div>
          <Navbar />
        </div>
      </div>
      {/* меню на моб */}
      <MobileNav open={openNav}>
        <NavMobile />
      </MobileNav>
    </header>
  );
};

export default Header;
