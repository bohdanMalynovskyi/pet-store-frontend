import React from 'react';

const Cart = () => {
  const [isMobile, setIsMobile] = React.useState(false);
  React.useEffect(() => {

    const checkScreenSize = () => {
      setIsMobile(window.innerWidth < 720);
    };
    checkScreenSize();

    window.addEventListener('resize', checkScreenSize);

    return () => {
      window.removeEventListener('resize', checkScreenSize);
    };
  }, []);
  const navbarClasses = isMobile ? 'text-[#fff] w-6 h-6' : 'text-primary w-8 h-8';
  return (
    <div className={` hover:text-hover ${navbarClasses}`}>
      <svg
        width="32"
        height="32"
        viewBox="0 0 32 32"
        fill="none"
        xmlns="http://www.w3.org/2000/svg">
        <path d="M26.604 27H5.39598C5.14067 27 4.89415 26.9049 4.70284 26.7326C4.51153 26.5602 4.38862 26.3225 4.35726 26.0643L2.50705 10.1819C2.48993 10.0329 2.50408 9.88188 2.54856 9.73885C2.59304 9.59583 2.66684 9.46407 2.76505 9.35231C2.86327 9.24056 2.98366 9.15136 3.11826 9.09062C3.25285 9.02989 3.39857 8.99901 3.54576 9.00002H28.4542C28.6014 8.99901 28.7471 9.02989 28.8817 9.09062C29.0163 9.15136 29.1367 9.24056 29.2349 9.35231C29.3332 9.46407 29.407 9.59583 29.4514 9.73885C29.4959 9.88188 29.5101 10.0329 29.493 10.1819L27.6427 26.0643C27.6114 26.3225 27.4885 26.5602 27.2972 26.7326C27.1058 26.9049 26.8593 27 26.604 27Z"
          stroke="currentColor"
          strokeWidth="1.5"
          strokeLinecap="round"
          strokeLinejoin="round" />
        <path d="M11.5 14V8.5C11.5 7.04131 11.9741 5.64236 12.818 4.61091C13.6619 3.57946 14.8065 3 16 3C17.1935 3 18.3381 3.57946 19.182 4.61091C20.0259 5.64236 20.5 7.04131 20.5 8.5V14"
          stroke="currentColor"
          strokeWidth="1.5"
          strokeLinecap="round"
          strokeLinejoin="round" />
      </svg>
    </div>
  )
}

export default Cart