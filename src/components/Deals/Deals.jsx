import React from 'react';
import SwiperDeals from '../Swiper/SwiperDeals';

const Deals = () => {
  return (
    <section className='container mx-auto max-w-[1260px] px-4 mb-10'>
        <h3 className=' text-lg font-bold mb-2'>Акції та знижки</h3>
        <SwiperDeals/>
    </section>
  )
}

export default Deals