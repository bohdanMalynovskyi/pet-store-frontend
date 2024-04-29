export const CaretRight = ({ color, onClick }) => {
  /*    Props:
    color(string): "primary", "txtSecondary"
    onClick(function)
  */

  return (
    <svg
      onClick={onClick}
      style={{ cursor: 'pointer' }}
      xmlns="http://www.w3.org/2000/svg"
      width="25"
      height="24"
      viewBox="0 0 25 24"
      fill="none"
    >
      <g clipPath="url(#clip0_4_3655)">
        <path
          d="M8.23926 19L15.7393 11.5L8.23926 4"
          stroke={color === 'txtSecondary' ? 'white' : '#011240'}
          strokeWidth="1.5"
          strokeLinecap="round"
          strokeLinejoin="round"
        />
      </g>
      <defs>
        <clipPath id="clip0_4_3655">
          <rect x="0.239258" width="24" height="24" fill="white" />
        </clipPath>
      </defs>
    </svg>
  );
};
