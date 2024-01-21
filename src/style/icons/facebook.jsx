export const Facebook = ({ color, onClick }) => {
  /*    Props:
  color(string): "primary", "txtSecondary"
  onClick(function)
*/
  return (
    <svg
      onClick={onClick}
      className="cursor-pointer"
      xmlns="http://www.w3.org/2000/svg"
      width="25"
      height="24"
      viewBox="0 0 25 24"
      fill="none"
    >
      <g clipPath="url(#clip0_8_415)">
        <path
          d="M12.0796 21C17.0502 21 21.0796 16.9706 21.0796 12C21.0796 7.02944 17.0502 3 12.0796 3C7.10903 3 3.07959 7.02944 3.07959 12C3.07959 16.9706 7.10903 21 12.0796 21Z"
          stroke={color === 'txtSecondary' ? 'white' : '#011240'}
          strokeWidth="1.5"
          strokeLinecap="round"
          strokeLinejoin="round"
        />
        <path
          d="M15.8296 8.25H14.3296C13.7329 8.25 13.1606 8.48705 12.7386 8.90901C12.3166 9.33097 12.0796 9.90326 12.0796 10.5V21"
          stroke={color === 'txtSecondary' ? 'white' : '#011240'}
          strokeWidth="1.5"
          strokeLinecap="round"
          strokeLinejoin="round"
        />
        <path
          d="M9.07959 13.5H15.0796"
          stroke={color === 'txtSecondary' ? 'white' : '#011240'}
          strokeWidth="1.5"
          strokeLinecap="round"
          strokeLinejoin="round"
        />
      </g>
      <defs>
        <clipPath id="clip0_8_415">
          <rect
            width="24"
            height="24"
            fill={color === 'txtSecondary' ? 'white' : '#011240'}
            transform="translate(0.0795898)"
          />
        </clipPath>
      </defs>
    </svg>
  );
};
