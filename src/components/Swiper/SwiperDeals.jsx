import React, {useRef, } from 'react';
import { Swiper, SwiperSlide } from 'swiper/react';
import SwiperCore, {Pagination, } from "swiper"
import "swiper/swiper-bundle.min.css";
import "swiper/components/pagination/pagination.scss";
import data from "../../db/data";
import Item from '../Item/Item';

SwiperCore.use([Pagination])
export default function SwiperDeals() {
  const SlideRef = useRef();
 
  const handleNext =() => {
    SlideRef.current.swiper.slideNext();
  };
  const handlePrev=() => {
    SlideRef.current.swiper.slidePrev();
  };
  return (
    <div className=' container mx-auto'>
       <div>
        <button onClick={handlePrev}>Prev</button>
        <button onClick={handleNext}>Next</button>
    </div>
      <Swiper 
      slidesPerView={1}
      breakpoints={{
        0: {
          slidesPerView:1,
          spaceBetween: 10,
        },
        480:{
          slidesPerView: 2,
          spaceBetween: 10,
        },
        768: {
          slidesPerView: 3,
          spaceBetween: 20,
        },
        1024: {
          slidesPerView: 4,
          spaceBetween: 30,
        },
      }}
      spaceBetween={40}
      pagination={{
        dynamicBullets: true,
      }}
      ref={SlideRef}
      modules={[Pagination]}
      className="mySwiper flex justify-center">
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