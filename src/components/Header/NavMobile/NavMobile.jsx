import styles from './index.module.css';
import { useState } from 'react';
import { NavLink } from 'react-router-dom';
import { CaretRight } from '../../../style/icons';
import nav__links from '../../../db/menu';

const NavMobile = () => {
  const [click, setClick] = useState(false);
  const toggleMenu = () => {
    console.log('click');
    setClick(!click);
  };
  return (
    <nav className={styles.nav}>
      <div className={styles.list}>
        {nav__links.map((item, index) => (
          <NavLink onClick={toggleMenu} className={styles.item} to={item.path} key={index}>
            {item.display}
            <CaretRight className={styles.caret} />
          </NavLink>
        ))}
      </div>
    </nav>
  );
};

export default NavMobile;
