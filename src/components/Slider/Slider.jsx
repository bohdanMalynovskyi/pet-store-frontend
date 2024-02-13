import { useRef, useState } from 'react';

import SliderItem from './SliderItem';
import SliderButtons from './SliderButtons';

import { Swiper, SwiperSlide } from 'swiper/react';
import { Navigation, Pagination } from 'swiper/modules';

import 'swiper/css';
import './index.css';
import 'swiper/css/pagination';
import styles from './index.module.css';

const Slider = ({ title, data }) => {
  const [isStartBtnActive, setStartBtnActive] = useState(true);
  const [isEndBtnActive, setIsEndBtnActive] = useState(false);

  const swiperRef = useRef();

  function isButtonActive(e) {
    e.isBeginning ? setStartBtnActive(true) : setStartBtnActive(false);
    e.isEnd ? setIsEndBtnActive(true) : setIsEndBtnActive(false);
  }

  return (
    <div className={styles.container}>
      <div className={styles.slider__header}>
        <h2 className={styles.slider__header_title}>{title}</h2>
        <SliderButtons isStartBtnActive={isStartBtnActive} isEndBtnActive={isEndBtnActive} swiperRef={swiperRef} />
      </div>
      <Swiper
        slidesPerView={'auto'}
        spaceBetween={40}
        pagination={{
          clickable: true,
        }}
        onSlideChange={isButtonActive}
        modules={[Pagination, Navigation]}
        className="mySwiper"
        onSwiper={(swiper) => {
          swiperRef.current = swiper;
        }}
      >
        {data.map((item) => (
          <SwiperSlide key={item.id}>
            <SliderItem item={item} />
          </SwiperSlide>
        ))}
      </Swiper>
    </div>
  );
};

export default Slider;
