import React from 'react';
import { Swiper, SwiperSlide } from 'swiper/react';
import SwiperCore, {Pagination} from "swiper"
import "swiper/swiper-bundle.min.css";
import "swiper/components/pagination/pagination.scss";
import data from "../../db/data";
import Item from '../Item/Item';

SwiperCore.use([Pagination])
export default function SwiperDeals() {
  return (
    <div className=' py-4 px-4'>
      <Swiper 
      slidesPerView={1}
      breakpoints={{
        768: {
          slidesPerView: 3,
        },
      }}
      spaceBetween={30}
      pagination={{
        dynamicBullets: true,
      }}
      modules={[Pagination]}
      className="mySwiper">
        {data.map((item)=> 
        <SwiperSlide key={item.id} >
          <Item
          title={item.title} 
          image={item.img}
          description={item.description}
          new_price={item.new_price}
          old_price={item.old_price}/>
        </SwiperSlide>
        )}
        
        
      </Swiper>
    </div>
  );
}