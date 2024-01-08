import React, {useState }from 'react';
import cart from '../../assets/images/bag.svg';
import cartHover from '../../assets/images/bag-hover.svg';

const BtnCart = () => {

    const[isHovered, setIsHovered] = useState(false);
    const cartSrc = isHovered? cartHover : cart;
  return (
    <div>
        <img 
        src={cartSrc} 
        alt="cart"
        onMouseEnter={() => setIsHovered(true)}
        onMouseLeave={() => setIsHovered(false)} />
    </div>
  )
}

export default BtnCart