import { useState } from 'react';

export const Heart = ({ count, onClick, stylesIcon, stylesIconCount, type = 'header' }) => {
  const [clicked, setClicked] = useState(false);

  const onClickHeart = () => {
    if (onClick) {
      if (type === 'card') {
        setClicked(!clicked);
      }
      onClick();
    }
  };

  const handleKeyDown = (event) => {
    if (event.key === 'Enter') {
      onClickHeart();
    }
  };

  return (
    <div className={stylesIcon} onClick={onClickHeart} onKeyDown={handleKeyDown} role="button" tabIndex="0">
      <svg viewBox="0 0 33 32" fill="none" xmlns="http://www.w3.org/2000/svg">
        <g clipPath="url(#clip0_37_4548)">
          <path
            fill={clicked ? 'var(--secondary)' : 'none'}
            d="M16.2393 27C16.2393 27 3.23926 20 3.23926 11.75C3.23926 9.95979 3.95042 8.2429 5.21629 6.97703C6.48216 5.71116 8.19905 5 9.98926 5C12.813 5 15.2318 6.53875 16.2393 9C17.2468 6.53875 19.6655 5 22.4893 5C24.2795 5 25.9964 5.71116 27.2622 6.97703C28.5281 8.2429 29.2393 9.95979 29.2393 11.75C29.2393 20 16.2393 27 16.2393 27Z"
            strokeWidth="1.5"
            strokeLinecap="round"
            strokeLinejoin="round"
          />
        </g>
        <defs>
          <clipPath id="clip0_37_4548">
            <rect width="32" height="32" fill="white" transform="translate(0.239258)" />
          </clipPath>
        </defs>
      </svg>
      {count && <div className={stylesIconCount}>{count}</div>}
    </div>
  );
};
