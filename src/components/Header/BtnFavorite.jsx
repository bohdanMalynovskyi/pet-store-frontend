import React from 'react';
import heart from '../../assets/images/heart-primary.svg';
import heartHover from '../../assets/images/heart-hover.svg';
// import heartFill from '../../assets/images/heart-fill.svg';

const BtnFavorite = () => {
    const[isHovered,setIsHovered] = React.useState(false);
    const heartSrc = isHovered ? heartHover : heart;
  return (
    <div className=' ml-[120px]'>
        <img  
        src={heartSrc} 
        alt=""
        onMouseEnter={() => setIsHovered(true)}
        onMouseLeave={() => setIsHovered(false)} />
    </div>
  )
}

export default BtnFavorite