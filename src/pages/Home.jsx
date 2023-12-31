import React from 'react';
import banner from '../assets/images/banner.jpg';
import MegaMenu from '../components/Header/MegaMenu';


const Home = () => {
  return (
    <div className=''>
      <img src={banner} alt="banner" />
      <MegaMenu/>
    </div>
  )
}

export default Home