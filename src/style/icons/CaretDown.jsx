export const CaretDown = ({ color, onClick }) => {
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
      <g clipPath="url(#clip0_4_3657)">
        <path
          d="M19.2393 8L11.7393 15.5L4.23926 8"
          stroke={color === 'txtSecondary' ? 'white' : '#011240'}
          strokeWidth="1.5"
          strokeLinecap="round"
          strokeLinejoin="round"
        />
      </g>
      <defs>
        <clipPath id="clip0_4_3657">
          <rect
            width="24"
            height="24"
            fill={color === 'txtSecondary' ? 'white' : '#011240'}
            transform="translate(0.239258)"
          />
        </clipPath>
      </defs>
    </svg>
  );
};
