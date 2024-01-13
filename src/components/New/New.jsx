import React from 'react';
// import data from "../../db/data"
// import Item from '../Item/Item';
import SwiperDeals from '../Swiper/SwiperDeals';

const New= () => {
  return (
    <section className='container mx-auto max-w-[1260px] px-4 mb-10'>
        <h3 className=' text-lg font-bold mb-2'>Новинки</h3>
        <SwiperDeals/>
    </section>
  )
}

export default New