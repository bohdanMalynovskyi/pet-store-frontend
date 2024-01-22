import { useState } from 'react';

export const BagDesktop = ({ itemСount, onClick }) => {
  /*    Props:
    itemСount(number)
    onClick(function)
  */
  const [hovered, setHovered] = useState(false);

  const style = {
    wrapper: 'relative inline-block w-[33px] h-[32px] select-none',
    circle:
      'rounded-[50%] bg-secondary flex items-center justify-center absolute bottom-0 right-0 text-secondary font-normal leading-normal text-txtSecondary text-base min-w-[16px] h-[16px] p-[3.5px]',
  };

  const onClickBag = () => {
    // add navigate page bag
    if (onClick) {
      onClick();
    }
  };

  const handleKeyDown = (event) => {
    if (event.key === 'Enter') {
      onClickBag();
    }
  };

  return (
    <div
      className={style.wrapper}
      onMouseEnter={() => setHovered(true)}
      onMouseLeave={() => setHovered(false)}
      onClick={onClickBag}
      onKeyDown={handleKeyDown}
      role="button"
      tabIndex="0"
    >
      <svg xmlns="http://www.w3.org/2000/svg" width="33" height="32" viewBox="0 0 30 26" fill="none">
        <path
          d="M25.8433 25H4.63524C4.37993 25 4.13341 24.9049 3.9421 24.7326C3.75079 24.5602 3.62788 24.3225 3.59652 24.0643L1.7463 8.18193C1.72919 8.03291 1.74334 7.88188 1.78782 7.73885C1.8323 7.59583 1.9061 7.46407 2.00431 7.35231C2.10253 7.24056 2.22292 7.15136 2.35752 7.09062C2.49211 7.02989 2.63783 6.99901 2.78502 7.00002H27.6935C27.8407 6.99901 27.9864 7.02989 28.121 7.09062C28.2556 7.15136 28.376 7.24056 28.4742 7.35231C28.5724 7.46407 28.6462 7.59583 28.6907 7.73885C28.7352 7.88188 28.7493 8.03291 28.7322 8.18193L26.882 24.0643C26.8506 24.3225 26.7277 24.5602 26.5364 24.7326C26.3451 24.9049 26.0986 25 25.8433 25Z"
          fill={'none'}
          stroke={hovered ? '#3786A5' : '#011240'}
          strokeWidth="1.5"
          strokeLinecap="round"
          strokeLinejoin="round"
        />
        <path
          d="M10.7393 12V6.5C10.7393 5.04131 11.2134 3.64236 12.0573 2.61091C12.9012 1.57946 14.0458 1 15.2393 1C16.4327 1 17.5773 1.57946 18.4212 2.61091C19.2652 3.64236 19.7393 5.04131 19.7393 6.5V12"
          fill={'none'}
          stroke={hovered ? '#3786A5' : '#011240'}
          strokeWidth="1.5"
          strokeLinecap="round"
          strokeLinejoin="round"
        />
      </svg>
      {itemСount && <div className={style.circle}>{itemСount}</div>}
    </div>
  );
};
