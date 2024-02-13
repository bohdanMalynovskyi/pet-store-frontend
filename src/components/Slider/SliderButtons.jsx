import styles from "./index.module.css";

import { CaretLeft, CaretRight } from "../../style/icons";

const SliderButtons = ({ swiperRef, isStartBtnActive, isEndBtnActive }) => {
  return (
    <div className={styles.slider__buttons_wrapper}>
      <button
        onClick={() => swiperRef.current.slidePrev()}
        disabled={isStartBtnActive}
        className={styles.slider__button}
      >
        <CaretLeft color={"txtSecondary"} />
      </button>
      <button
        onClick={() => swiperRef.current.slideNext()}
        disabled={isEndBtnActive}
        className={styles.slider__button}
      >
        <CaretRight color={"txtSecondary"} />
      </button>
    </div>
  );
};

export default SliderButtons;
