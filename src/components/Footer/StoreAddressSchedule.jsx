import React from 'react';

const StoreAddressSchedule = ({ classColumn, classItem }) => {
  return (
    <div className={classColumn}>
      <div className={classItem}>Графік роботи: Пн-Нд: 9:00-18:00</div>
      <div className={classItem}>Адреса: Харків, вул. Героїв Праці, 9 ТРЦ «Дафі»</div>
    </div>
  );
};

export default StoreAddressSchedule;
