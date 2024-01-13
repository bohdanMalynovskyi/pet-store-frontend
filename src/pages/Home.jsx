import React from 'react';
import Hero from '../components/Hero/Hero';
import Deals from '../components/Deals/Deals';
import New from '../components/New/New';


const Home = () => {
  return (
    <div className=' flex flex-col'>
      <Hero/>
      <Deals/>
      <New/>

      </div>
  )
}

export default Home