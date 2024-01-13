import React from 'react';
import { HeartIcon } from '@heroicons/react/24/outline';
import PropTypes from 'prop-types';

const Item = ({image, title, description, new_price, old_price}) => {
  return (
    <div className=' px-4 py-4 max-w-[335px] min-h-[384px] hover:shadow-md'>
        <img className='mx-auto w-[150px] h-[150px] mb-3' src={image} alt="" />
        <h5 className=' text-base font-bold mb-1'>{title}</h5>
        <p className=' text-sm'>{description}</p>
        <div className=' flex gap-2 mb-3'> 
            <div className=' text-cyan text-lg font-bold'>{new_price} грн</div>
            <div className=' text-zinc  text-lg font-bold line-through'>{old_price} грн</div>
        </div>
        <div className=' flex gap-2  items-center'>
            <div className=' w-8 h-8 hover:text-cyan'><HeartIcon/></div>
            <button className=' bg-primary w-[271px] text-[#fff] rounded-[20px]  py-2 justify-center items-center'>Додати в кошик</button>
        
        </div>
    </div>
  )
}
Item.propTypes = {
    image: PropTypes.string.isRequired,
    title: PropTypes.string.isRequired,
    description: PropTypes.string.isRequired,
    new_price: PropTypes.number.isRequired,
    old_price: PropTypes.number.isRequired,
  };

export default Item