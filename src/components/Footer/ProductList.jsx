import React from 'react';
import { NavLink } from 'react-router-dom';
import { useSelector } from 'react-redux';
import { selectAnimalCategories } from '../../redux/features/animalCategories/selectors';

const ProductList = ({ classColumn, classTitle, classItem }) => {
  const { animalCategories } = useSelector(selectAnimalCategories);

  return (
    <div className={classColumn}>
      <div className={classTitle}>Товари</div>
      {animalCategories.map((category) => {
        const { display, path, id } = category;

        return (
          <NavLink className={classItem} to={path} key={id}>
            {display}
          </NavLink>
        );
      })}
    </div>
  );
};

export default ProductList;
