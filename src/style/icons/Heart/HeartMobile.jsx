import { useState } from 'react';

export const HeartMobile = ({ itemСount, type, onClick }) => {
  /*    Props:
    itemСount(number)
    type(string): "card", "header"
    onClick(function)
  */
  const [hovered, setHovered] = useState(false);
  const [clicked, setClicked] = useState(false);

  const style = {
    wrapper: `relative inline-block select-none ${type === 'card' ? 'w-[32px] h-[32px]' : 'w-[24px] h-[24px]'}`,
    circle:
      'rounded-[50%] bg-secondary flex items-center justify-center absolute bottom-0 right-0 text-secondary font-normal leading-normal text-txtSecondary text-[13px] min-w-[14px] h-[14px] p-[2px]',
  };

  const onClickHeart = () => {
    if (type === 'card') {
      setClicked(!clicked);
    }
    if (type === 'header') {
      // add navigate page
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
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width={type === 'card' ? '32' : '24'}
        height={type === 'card' ? '32' : '24'}
        viewBox="0 0 25 24"
        fill="none"
      >
        <g clipPath="url(#clip0_278_1537)">
          <path
            d="M11.9893 20.5C11.9893 20.5 2.23926 15.25 2.23926 9.0625C2.23926 7.71984 2.77263 6.43217 3.72203 5.48277C4.67143 4.53337 5.9591 4 7.30176 4C9.41957 4 11.2336 5.15406 11.9893 7C12.7449 5.15406 14.5589 4 16.6768 4C18.0194 4 19.3071 4.53337 20.2565 5.48277C21.2059 6.43217 21.7393 7.71984 21.7393 9.0625C21.7393 15.25 11.9893 20.5 11.9893 20.5Z"
            fill={clicked ? '#3786A5' : 'none'}
            stroke={hovered ? '#3786A5' : type === 'header' ? 'white' : clicked ? '#3786A5' : '#011240'}
            strokeWidth="1.5"
            strokeLinecap="round"
            strokeLinejoin="round"
          />
        </g>
        <defs>
          <clipPath id="clip0_278_1537">
            <rect width="24" height="24" fill="white" transform="translate(0.239258)" />
          </clipPath>
        </defs>
      </svg>
      {itemСount && <div className={style.circle}>{itemСount}</div>}
    </div>
  );
};
