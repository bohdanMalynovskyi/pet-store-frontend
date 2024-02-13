import styles from "./index.module.css";

import { Heart } from "../../style/icons";

const SliderItem = ({ item }) => {
  return (
    <div className={styles.swiper__item}>
      <div className={styles.swiper__image_wrapper}>
        <img src={item.img} alt={item.title} className={styles.swiper__image} />
        <Heart count={null} stylesIcon={styles.swiper__icon} />
      </div>
      <div className={styles.swiper__info_wrapper}>
        <ul className={styles.swiper__weight_list}>
          <li className={styles.swiper__weight_item}>
            <p
              className={`${styles.swiper__weight_text} ${styles.swiper__weight_able}`}
            >
              3kg
            </p>
          </li>
          <li className={styles.swiper__weight_item}>
            <p className={`${styles.swiper__weight_text}`}>6kg</p>
          </li>
          <li className={styles.swiper__weight_item}>
            <p className={`${styles.swiper__weight_text}`}>12kg</p>
          </li>
        </ul>
        <div className={styles.swiper__descr_wrapper}>
          <h3 className={styles.swiper__title}>{item.title}</h3>
          <p className={styles.swipper__description}>{item.description}</p>
          <div className={styles.swiper__price_wrapper}>
            <p className={styles.swiper__new_price}>{item.new_price} грн.</p>
            <p className={styles.swiper__old_price}>{item.old_price} грн.</p>
          </div>
        </div>
      </div>
      <button className={styles.button__add}>Додати в кошик</button>
    </div>
  );
};

export default SliderItem;
