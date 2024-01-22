import { useState } from 'react';

export const HeartDesktop = ({ itemСount, type, onClick }) => {
  /*    Props:
    itemСount(number)
    type(string): "card", "header"
    onClick(function)
  */
  const [hovered, setHovered] = useState(false);
  const [clicked, setClicked] = useState(false);

  const style = {
    wrapper: 'relative inline-block w-[33px] h-[32px] select-none',
    circle:
      'rounded-[50%] bg-secondary flex items-center justify-center absolute bottom-0 right-0 text-secondary font-normal leading-normal text-txtSecondary text-base min-w-[16px] h-[16px] p-[3.5px]',
  };

  const onClickHeart = () => {
    if (type === 'card') {
      setClicked(!clicked);
    }
    if (type === 'header') {
      // add navigate page favorites
    }
    if (onClick) {
      onClick();
    }
  };

  const handleKeyDown = (event) => {
    if (event.key === 'Enter') {
      onClickHeart();
    }
  };

  return (
    <div
      className={style.wrapper}
      onMouseEnter={() => setHovered(true)}
      onMouseLeave={() => setHovered(false)}
      onClick={onClickHeart}
      onKeyDown={handleKeyDown}
      role="button"
      tabIndex="0"
    >
      <svg xmlns="http://www.w3.org/2000/svg" width="33" height="32" viewBox="0 0 33 32" fill="none">
        <g clipPath="url(#clip0_35_333)">
          <path
            d="M16.2393 27C16.2393 27 3.23926 20 3.23926 11.75C3.23926 9.95979 3.95042 8.2429 5.21629 6.97703C6.48216 5.71116 8.19905 5 9.98926 5C12.813 5 15.2318 6.53875 16.2393 9C17.2468 6.53875 19.6655 5 22.4893 5C24.2795 5 25.9964 5.71116 27.2622 6.97703C28.5281 8.2429 29.2393 9.95979 29.2393 11.75C29.2393 20 16.2393 27 16.2393 27Z"
            fill={clicked ? '#3786A5' : 'none'}
            stroke={hovered ? '#3786A5' : clicked ? '#3786A5' : '#011240'}
            strokeWidth="1.5"
            strokeLinecap="round"
            strokeLinejoin="round"
          />
        </g>
        <defs>
          <clipPath id="clip0_35_333">
            <rect width="32" height="32" fill="white" transform="translate(0.239258)" />
          </clipPath>
        </defs>
      </svg>
      {itemСount && <div className={style.circle}>{itemСount}</div>}
    </div>
  );
};
