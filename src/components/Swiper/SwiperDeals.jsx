import React, { useRef, } from 'react';
import { Swiper, SwiperSlide } from 'swiper/react';
import SwiperCore, { Pagination, } from "swiper"
import "swiper/swiper-bundle.min.css";
import "swiper/components/pagination/pagination.scss";
import data from "../../db/data";
import Item from '../Item/Item';

SwiperCore.use([Pagination])
export default function SwiperDeals() {
  const SlideRef = useRef();

  const handleNext = () => {
    SlideRef.current.swiper.slideNext();
  };
  const handlePrev = () => {
    SlideRef.current.swiper.slidePrev();
  };
  return (
    <div className=' relative'>
      <div className='hidden sm:absolute -top-8 right-0 sm:flex justify-end gap-5'>
        <button onClick={handlePrev}>
          <svg  width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <g clipPath="url(#clip0_4_3869)">
              <rect className="arrow hover:fill-hover" width="24" height="24" rx="4" fill="#011240" />
              <path d="M16 19L8.5 11.5L16 4" stroke="white" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round" />
            </g>
            <defs>
              <clipPath id="clip0_4_3869">
                <rect width="24" height="24" rx="4" fill="white" />
              </clipPath>
            </defs>
          </svg>

        </button>
        <button onClick={handleNext}>
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <g clipPath="url(#clip0_4_3881)">
              <rect className="arrow hover:fill-hover" width="24" height="24" rx="4" fill="#011240" />
              <path d="M8 19L15.5 11.5L8 4" stroke="white" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round" />
            </g>
            <defs>
              <clipPath id="clip0_4_3869">
                <rect width="24" height="24" rx="4" fill="white" />
              </clipPath>
            </defs>
          </svg>
        </button>
      </div>
      <Swiper
        slidesPerView={1}
        breakpoints={{
          0: {
            slidesPerView: 1,
            spaceBetween: 10,
          },
          539: {
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
        {data.map((item) =>
          <SwiperSlide key={item.id} >
            <Item
              title={item.title}
              image={item.img}
              description={item.description}
              new_price={item.new_price}
              old_price={item.old_price} />
          </SwiperSlide>
        )}
      </Swiper>
    </div>
  );
}



