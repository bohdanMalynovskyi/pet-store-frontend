export const Search = ({ color, onClick }) => {
  /*    Props:
  color(string): "primary", "txtSecondary"
  onClick(function)
*/
  return (
    <svg
      onClick={onClick}
      className="cursor-pointer"
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 25 24"
      fill="none"
    >
      <g clipPath="url(#clip0_4_259)">
        <path
          d="M10.7393 18C14.8814 18 18.2393 14.6421 18.2393 10.5C18.2393 6.35786 14.8814 3 10.7393 3C6.59712 3 3.23926 6.35786 3.23926 10.5C3.23926 14.6421 6.59712 18 10.7393 18Z"
          stroke={color === 'txtSecondary' ? 'white' : '#011240'}
          strokeWidth="1.5"
          strokeLinecap="round"
          strokeLinejoin="round"
        />
        <path
          d="M16.0427 15.8035L21.2393 21"
          stroke={color === 'txtSecondary' ? 'white' : '#011240'}
          strokeWidth="1.5"
          strokeLinecap="round"
          strokeLinejoin="round"
        />
      </g>
      <defs>
        <clipPath id="clip0_4_259">
          <rect width="24" height="24" fill="white" transform="translate(0.239258)" />
        </clipPath>
      </defs>
    </svg>
  );
};
