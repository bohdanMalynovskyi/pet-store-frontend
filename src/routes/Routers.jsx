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
      <Route path="/dogs" element={<CategoryPage category="dogs" />}>
        <Route path='/dogs/korm-dlya-sobak' element={<CategoryPage/>} />
        <Route path='/dogs/odyag-dlya-sobak' element={<CategoryPage/>} />
        <Route path='/dogs/igrashki-dlya-sobak' element={<CategoryPage/>} />
        <Route path='/dogs/lasoshhi-dlya-sobak' element={<CategoryPage/>} />
        <Route path='/dogs/vitamini-dlya-sobak' element={<CategoryPage/>} />
      </Route>
      <Route path="/cats" element={<CategoryPage category="cats" />}></Route>
      <Route path="/birds" element={<CategoryPage category="birds" />}></Route>
      <Route path="/fish" element={<CategoryPage category="fish" />} ></Route>
      <Route path="/smallpets" element={<CategoryPage category="smallpets" />} ></Route>
      <Route path="/reptiles" element={<CategoryPage category="reptiles" />}></Route>
      <Route path="/my-account" element={<Login />} />
      <Route path="/wishlist" element={<Wishlist />} />
      <Route path="/cart" element={<Cart/>} />
    </Routes>
  );
};

export default Routers;

