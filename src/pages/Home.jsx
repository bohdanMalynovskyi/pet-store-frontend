import React from 'react';

import Hero from '../components/Hero/Hero';
import Deals from '../components/Deals';



const Home = () => {
  return (
    <div className=' flex flex-col'>
      <Hero/>
      <Deals/>
    </div>
  )
}

export default Home