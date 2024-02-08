import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Main from '../pages/Main';

import Wishlist from '../pages/Wishlist';
import Product from '../pages/Product';
import AnimalCategory from '../pages/AnimalCategory';

const Routers = () => {
  return (
    <Routes>
      <Route path="/" element={<Main />} />
      <Route path="/:animalCategory" element={<AnimalCategory />} />
      <Route path="product" element={<Product />} />
      <Route path="wishlist" element={<Wishlist />} />
    </Routes>
  );
};
export default Routers;
