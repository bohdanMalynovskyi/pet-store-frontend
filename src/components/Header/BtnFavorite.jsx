import React from 'react';
import heart from '../../assets/images/heart-primary.svg';
import heartHover from '../../assets/images/heart-hover.svg';
import heartClicked from '../../assets/images/heart-fill.svg';

const BtnFavorite = () => {
    const[isHovered,setIsHovered] = React.useState(false);
    const [isClicked, setIsClicked] = React.useState(false);
   
    let heartSrc = heart;
    
    if (isClicked) {
        heartSrc = heartClicked;
    } else if (isHovered) {
        heartSrc = heartHover;
    }
    const handleClick = () => {
        setIsClicked(!isClicked);
    };
  return (
    <div className=' ml-[120px]'>
        <button
        onMouseEnter={() => setIsHovered(true)}
        onMouseLeave={() => setIsHovered(false)}
        onClick={handleClick}
        >
        <img  
        src={heartSrc} 
        alt=""
         />
        </button>
    </div>
  )
}

export default BtnFavorite