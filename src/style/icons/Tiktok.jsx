export const Tiktok = ({ color, onClick }) => {
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
      <g clipPath="url(#clip0_8_416)">
        <path
          d="M15.8296 9.5625C17.3586 10.6631 19.1957 11.2536 21.0796 11.25V7.5C19.6872 7.5 18.3518 6.94688 17.3673 5.96231C16.3827 4.97774 15.8296 3.64239 15.8296 2.25H12.0796V14.625C12.0794 15.0947 11.9532 15.5558 11.7141 15.9601C11.475 16.3644 11.1318 16.6971 10.7202 16.9236C10.3087 17.1501 9.84398 17.262 9.37449 17.2477C8.90499 17.2333 8.44793 17.0933 8.051 16.8421C7.65407 16.591 7.3318 16.2379 7.11781 15.8198C6.90382 15.4016 6.80595 14.9337 6.83441 14.4649C6.86287 13.996 7.01661 13.5434 7.2796 13.1542C7.54259 12.765 7.9052 12.4535 8.32959 12.2522V8.25C5.34553 8.78156 3.07959 11.4881 3.07959 14.625C3.07959 16.3158 3.75124 17.9373 4.94678 19.1328C6.14233 20.3284 7.76383 21 9.45459 21C11.1453 21 12.7669 20.3284 13.9624 19.1328C15.1579 17.9373 15.8296 16.3158 15.8296 14.625V9.5625Z"
          stroke={color === 'txtSecondary' ? 'white' : '#011240'}
          strokeWidth="1.5"
          strokeLinecap="round"
          strokeLinejoin="round"
        />
      </g>
      <defs>
        <clipPath id="clip0_8_416">
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
