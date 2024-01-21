import React from 'react';
import { Facebook, Instagram, Tiktok } from '../../style/icons';

const Contacts = ({ classColumn, classTitle, classItem, classIcons }) => {
  return (
    <div className={classColumn}>
      <div className={classTitle}>Контакти:</div>
      <div className={classItem}>{'+38(000)-000-00-00'}</div>
      <div className={classItem}>pettopiateamchallenge@gmail.com</div>
      <div className={classItem}>
        <div className={classIcons}>
          <a href="https://www.instagram.com/" target="_blank" rel="noopener noreferrer">
            <Instagram color={'txtSecondary'} />
          </a>
          <a href="https://www.facebook.com/" target="_blank" rel="noopener noreferrer">
            <Facebook color={'txtSecondary'} />
          </a>
          <a href="https://www.tiktok.com/" target="_blank" rel="noopener noreferrer">
            <Tiktok color={'txtSecondary'} />
          </a>
        </div>
      </div>
    </div>
  );
};

export default Contacts;
