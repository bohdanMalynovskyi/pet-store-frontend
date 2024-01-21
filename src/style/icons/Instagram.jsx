export const Instagram = ({ color, onClick }) => {
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
      <g clipPath="url(#clip0_8_414)">
        <path
          d="M12.0796 15.75C14.1507 15.75 15.8296 14.0711 15.8296 12C15.8296 9.92893 14.1507 8.25 12.0796 8.25C10.0085 8.25 8.32959 9.92893 8.32959 12C8.32959 14.0711 10.0085 15.75 12.0796 15.75Z"
          stroke={color === 'txtSecondary' ? 'white' : '#011240'}
          strokeWidth="1.5"
          strokeMiterlimit="10"
        />
        <path
          d="M16.5796 3H7.57959C5.09431 3 3.07959 5.01472 3.07959 7.5V16.5C3.07959 18.9853 5.09431 21 7.57959 21H16.5796C19.0649 21 21.0796 18.9853 21.0796 16.5V7.5C21.0796 5.01472 19.0649 3 16.5796 3Z"
          stroke={color === 'txtSecondary' ? 'white' : '#011240'}
          strokeWidth="1.5"
          strokeLinecap="round"
          strokeLinejoin="round"
        />
        <path
          d="M16.9546 8.25C17.5759 8.25 18.0796 7.74632 18.0796 7.125C18.0796 6.50368 17.5759 6 16.9546 6C16.3333 6 15.8296 6.50368 15.8296 7.125C15.8296 7.74632 16.3333 8.25 16.9546 8.25Z"
          fill={color === 'txtSecondary' ? 'white' : '#011240'}
        />
      </g>
      <defs>
        <clipPath id="clip0_8_414">
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
