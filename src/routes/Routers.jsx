import React from 'react';
import { Routes, Route, Navigate } from 'react-router-dom';
import Home from '../pages/Home';
import CategoryPage from '../pages/CategoryPage';
import Login from '../pages/Login';
import Wishlist from '../pages/Wishlist';
import Cart from '../pages/Cart';

const Routers = () => {
  return (
    <Routes>
      <Route path="/" element={<Navigate to="/home" />} />
      <Route path="/home" element={<Home />} />
      <Route path="/dogs" element={<CategoryPage category="dogs" />} />
      <Route path="/cats" element={<CategoryPage category="cats" />} />
      <Route path="/birds" element={<CategoryPage category="birds" />} />
      <Route path="/fish" element={<CategoryPage category="fish" />} />
      <Route path="/smallpets" element={<CategoryPage category="smallpets" />} />
      <Route path="/reptiles" element={<CategoryPage category="reptiles" />} />
      <Route path="/my-account" element={<Login />} />
      <Route path="/wishlist" element={<Wishlist />} />
      <Route path="/cart" element={<Cart/>} />
    </Routes>
  );
};

export default Routers;
