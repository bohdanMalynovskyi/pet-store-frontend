export const Close = ({ color, onClick }) => {
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
      <g clipPath="url(#clip0_4_256)">
        <path
          d="M18.9893 5.25L5.48926 18.75"
          stroke={color === 'txtSecondary' ? 'white' : '#011240'}
          strokeWidth="1.5"
          strokeLinecap="round"
          strokeLinejoin="round"
        />
        <path
          d="M18.9893 18.75L5.48926 5.25"
          stroke={color === 'txtSecondary' ? 'white' : '#011240'}
          strokeWidth="1.5"
          strokeLinecap="round"
          strokeLinejoin="round"
        />
      </g>
      <defs>
        <clipPath id="clip0_4_256">
          <rect width="24" height="24" fill="white" transform="translate(0.239258)" />
        </clipPath>
      </defs>
    </svg>
  );
};
