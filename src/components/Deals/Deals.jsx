import React from 'react';
// import data from "../../db/data"
// import Item from '../Item/Item';
import SwiperDeals from '../Swiper/SwiperDeals';

const Deals = () => {
  return (
    <section className='container mx-auto max-w-[1260px] px-4 mb-10'>
        <h3 className=' text-lg font-bold mb-2'>Акції та знижки</h3>
        {/* <div>
            {data.map((item)=>{
                return <Item  
                key={item.id} 
                title={item.title} 
                image={item.img}
                description={item.description}
                new_price={item.new_price}
                old_price={item.old_price} />
            })}
        </div> */}
        <SwiperDeals/>
    </section>
  )
}

export default Deals