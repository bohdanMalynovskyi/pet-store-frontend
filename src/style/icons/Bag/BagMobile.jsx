import { useState } from 'react';

export const BagMobile = ({ itemСount, onClick }) => {
  const [hovered, setHovered] = useState(false);

  const style = {
    wrapper: 'relative inline-block w-[24px] h-[24px] select-none',
    circle:
      'rounded-[50%] bg-secondary flex items-center justify-center absolute bottom-0 right-0 text-secondary font-normal leading-normal text-txtSecondary text-[13px] min-w-[14px] h-[14px] p-[2px]',
  };

  const onClickHeart = () => {
    // add navigate page bag
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
      <svg xmlns="http://www.w3.org/2000/svg" width="25" height="24" viewBox="0 0 25 24" fill="none">
        <path
          d="M20.1923 21H4.28624C4.09476 21 3.90987 20.9287 3.76639 20.7994C3.6229 20.6702 3.53073 20.4919 3.50721 20.2982L2.11954 8.38645C2.10671 8.27468 2.11732 8.16141 2.15068 8.05414C2.18404 7.94687 2.23939 7.84805 2.31305 7.76424C2.38671 7.68042 2.47701 7.61352 2.57795 7.56797C2.6789 7.52242 2.78819 7.49926 2.89858 7.50002H21.5799C21.6903 7.49926 21.7996 7.52242 21.9006 7.56797C22.0015 7.61352 22.0918 7.68042 22.1655 7.76424C22.2391 7.84805 22.2945 7.94687 22.3278 8.05414C22.3612 8.16141 22.3718 8.27468 22.359 8.38645L20.9713 20.2982C20.9478 20.4919 20.8556 20.6702 20.7121 20.7994C20.5686 20.9287 20.3838 21 20.1923 21Z"
          stroke={hovered ? '#3786A5' : 'var(--txtSecondary)'}
          strokeWidth="1.5"
          strokeLinecap="round"
          strokeLinejoin="round"
        />
        <path
          d="M7.73926 11.25V7.125C7.73926 6.03098 8.21336 4.98177 9.05728 4.20818C9.90119 3.4346 11.0458 3 12.2393 3C13.4327 3 14.5773 3.4346 15.4212 4.20818C16.2652 4.98177 16.7393 6.03098 16.7393 7.125V11.25"
          stroke={hovered ? '#3786A5' : 'var(--txtSecondary)'}
          strokeWidth="1.5"
          strokeLinecap="round"
          strokeLinejoin="round"
        />
      </svg>
      {itemСount && <div className={style.circle}>{itemСount}</div>}
    </div>
  );
};
