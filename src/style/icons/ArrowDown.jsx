export const ArrowDown = ({ onClick }) => {
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
      <g clipPath="url(#clip0_4_3640)">
        <path
          d="M12.2393 3.75L12.2393 20.25"
          stroke="#011240"
          strokeWidth="1.5"
          strokeLinecap="round"
          strokeLinejoin="round"
        />
        <path
          d="M18.9893 13.5L12.2393 20.25L5.48926 13.5"
          stroke="#011240"
          strokeWidth="1.5"
          strokeLinecap="round"
          strokeLinejoin="round"
        />
      </g>
      <defs>
        <clipPath id="clip0_4_3640">
          <rect width="24" height="24" fill="white" transform="translate(0.239258)" />
        </clipPath>
      </defs>
    </svg>
  );
};
