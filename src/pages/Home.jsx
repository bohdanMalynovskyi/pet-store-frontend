import React from 'react';
import Hero from '../components/Hero/Hero';
import Deals from '../components/Deals/Deals';
import New from '../components/New/New';


const Home = () => {
  return (
    <div className=' flex flex-col'>
      <Hero />
      <div className=' container flex flex-col mx-auto max-w-[1260px] px-4'>
        <Deals />
        <New />
      </div>
    </div>
  )
}

export default Home