import React from 'react';
import { NavLink } from 'react-router-dom';
import nav__links from './../../db/menu';

const ProductList = ({ classColumn, classTitle, classItem }) => {
  return (
    <div className={classColumn}>
      <div className={classTitle}>Товари</div>
      {nav__links.map((item, index) => (
        <NavLink key={index} className={classItem} to={item.path}>
          {item.display}
        </NavLink>
      ))}
    </div>
  );
};

export default ProductList;
