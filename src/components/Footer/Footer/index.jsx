import React from 'react';
import style from './style';
import useWindowSize from '../../../hooks/useWindowSize';
import { selectResponsiveStyle } from '../../../utils';
import ProductList from '../ProductList';
import Contacts from '../Contacts';
import StoreAddressSchedule from '../StoreAddressSchedule';
import { LogoVertical, Mastercard, Visa } from '../../../style/icons';

const Footer = () => {
  const size = useWindowSize();
  const isMobile = size.width < 720;

  const createClass = (className) => selectResponsiveStyle(className, style, isMobile);

  const classColumn = `${style.column.default} ${createClass('column')}`;
  const classTitle = `${style.title.default} ${createClass('title')}`;
  const classItem = `${style.item.default}`;
  const classIcons = `${style.icons.default}`;

  return (
    <footer className={`${style.wrapper.default} ${createClass('wrapper')}`}>
      <div className={`${style.storeInfo.default} ${createClass('storeInfo')}`}>
        <div className={`${createClass('logoLink')}`}>
          <a href="/home">
            <LogoVertical className={`${createClass('logo')}`} />
          </a>
        </div>
        <ProductList classColumn={classColumn} classTitle={classTitle} classItem={`${classItem} hover:text-hover`} />
        <Contacts classColumn={classColumn} classTitle={classTitle} classItem={classItem} classIcons={classIcons} />
        <StoreAddressSchedule classColumn={classColumn} classItem={classItem} />
      </div>
      <div className={`items-center ${classColumn}`}>
        <div className={classIcons}>
          <Mastercard />
          <Visa />
        </div>
        <div className={style.copyright.default}>Copyright © 2023, Pettopia. All Rights Reserved.</div>
      </div>
    </footer>
  );
};

export default Footer;
