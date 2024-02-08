import React from 'react';
import styles from './index.module.css';
import classNames from 'classnames';
import ProductList from './ProductList';
import Contacts from './Contacts';
import StoreAddressSchedule from './StoreAddressSchedule';
import { LogoVertical, Mastercard, Visa } from '../../style/icons';

const Footer = () => {
  return (
    <footer className={styles.wrapper}>
      <div className={styles.storeInfo}>
        <div className={styles.logoLink}>
          <a href="/home">
            <LogoVertical className={styles.logo} color={'txtSecondary'} />
          </a>
        </div>
        <ProductList classColumn={styles.column} classTitle={styles.title} classItem={styles.item} />
        <Contacts
          classColumn={styles.column}
          classTitle={styles.title}
          classItem={styles.item}
          classIcons={styles.icons}
        />
        <StoreAddressSchedule classColumn={styles.column} classItem={styles.item} />
      </div>
      <div className={classNames(styles.column, styles.column_payments)}>
        <div className={styles.icons}>
          <Mastercard />
          <Visa />
        </div>
        <div className={styles.copyright}>Copyright © 2023, Pettopia. All Rights Reserved.</div>
      </div>
    </footer>
  );
};

export default Footer;
