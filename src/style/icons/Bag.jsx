export const Bag = ({ count, onClick, stylesIcon, stylesIconCount }) => {
  const onClickBag = () => {
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
    <div className={stylesIcon} onClick={onClickBag} onKeyDown={handleKeyDown} role="button" tabIndex="0">
      <svg viewBox="0 0 33 32" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path
          d="M26.8433 27H5.63524C5.37993 27 5.13341 26.9049 4.9421 26.7326C4.75079 26.5602 4.62788 26.3225 4.59652 26.0643L2.7463 10.1819C2.72919 10.0329 2.74334 9.88188 2.78782 9.73885C2.8323 9.59583 2.9061 9.46407 3.00431 9.35231C3.10253 9.24056 3.22292 9.15136 3.35752 9.09062C3.49211 9.02989 3.63783 8.99901 3.78502 9.00002H28.6935C28.8407 8.99901 28.9864 9.02989 29.121 9.09062C29.2556 9.15136 29.376 9.24056 29.4742 9.35231C29.5724 9.46407 29.6462 9.59583 29.6907 9.73885C29.7352 9.88188 29.7493 10.0329 29.7322 10.1819L27.882 26.0643C27.8506 26.3225 27.7277 26.5602 27.5364 26.7326C27.3451 26.9049 27.0986 27 26.8433 27Z"
          strokeWidth="1.5"
          strokeLinecap="round"
          strokeLinejoin="round"
        />
        <path
          d="M11.7393 14V8.5C11.7393 7.04131 12.2134 5.64236 13.0573 4.61091C13.9012 3.57946 15.0458 3 16.2393 3C17.4327 3 18.5773 3.57946 19.4212 4.61091C20.2652 5.64236 20.7393 7.04131 20.7393 8.5V14"
          strokeWidth="1.5"
          strokeLinecap="round"
          strokeLinejoin="round"
        />
      </svg>
      {count && <div className={stylesIconCount}>{count}</div>}
    </div>
  );
};
