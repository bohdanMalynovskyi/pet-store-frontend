const style = {
  wrapper: {
    default: 'flex w-full flex-col items-center overflow-hidden bg-primary text-txtWhite pb-[50px]',
    desktop: 'pt-[50px] gap-[30px]',
    mobile: 'p-[20px] pb-[50px] justify-center items-center flex-col gap-10',
  },
  storeInfo: {
    default: 'flex w-full',
    desktop: 'justify-around',
    mobile: 'justify-center items-center flex-col gap-10',
  },
  logoLink: {
    desktop: 'px-[50px]',
    mobile: 'px-[20px]',
  },
  logo: {
    desktop: 'cursor-pointer w-[85px] h-[50px]',
    mobile: 'cursor-pointer w-[64px] h-[38px]',
  },
  column: {
    default: 'flex flex-col gap-[12px]',
    desktop: 'items-start m-[5px]',
    mobile: 'items-center',
  },
  title: {
    default: 'not-italic font-bold leading-normal',
    desktop: 'text-lg',
    mobile: 'text-base text-center',
  },
  item: {
    default: 'text-base not-italic font-normal leading-normal',
  },
  icons: {
    default: `flex gap-[20px]`,
  },
  copyright: {
    default: 'text-sm not-italic font-normal leading-normal',
  },
};

export default style;
