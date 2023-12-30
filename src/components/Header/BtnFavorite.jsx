import React from 'react';
import heart from '../../assets/images/heart-primary.svg';
import heartHover from '../../assets/images/heart-hover.svg';
import heartClicked from '../../assets/images/heart-fill.svg';

const BtnFavorite = () => {
    const [isHovered, setIsHovered] = React.useState(false);
    const [isClicked, setIsClicked] = React.useState(false);
    const [heartSrc, setHeartSrc] = React.useState(heart);

    const handleMouseEnter = () => {
        if (!isClicked) {
            setIsHovered(true);
            setHeartSrc(heartHover);
        }
    };

    const handleMouseLeave = () => {
        if (!isClicked) {
            setIsHovered(false);
            setHeartSrc(heart);
        }
    };

    const handleMouseDown = () => {
        setIsClicked(true);
        setHeartSrc(heartClicked);
    };

    const handleMouseUp = () => {
        setIsClicked(false);
        if (!isHovered) {
            setHeartSrc(heart);
        } else {
            setHeartSrc(heartHover);
        }
    };

    return (
        <div className='md:ml-[120px]'>
            <button
                onMouseEnter={handleMouseEnter}
                onMouseLeave={handleMouseLeave}
                onMouseDown={handleMouseDown}
                onMouseUp={handleMouseUp}
                style={{ border: 'none', background: 'none', padding: 0, cursor: 'pointer' }}
            >
                <img src={heartSrc} alt="" />
            </button>
        </div>
    );
};

export default BtnFavorite;
