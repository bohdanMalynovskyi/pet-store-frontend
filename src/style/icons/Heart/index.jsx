import { HeartDesktop } from './HeartDesktop';
import { HeartMobile } from './HeartMobile';

export const Heart = ({ size, type, itemСount, onClick }) => {
  /*    Props:
    size(string): "desktop", "mobile"
    type(string): "card", "header"
    itemСount(number)
    onClick(function)
  */
  if (size === 'desktop') {
    if (type === 'header') {
      return <HeartDesktop type={type} itemСount={itemСount} onClick={onClick} />;
    } else return <HeartDesktop type={type} onClick={onClick} />;
  }
  if (size === 'mobile') {
    if (type === 'header') {
      return <HeartMobile type={type} itemСount={itemСount} onClick={onClick} />;
    } else return <HeartMobile type={type} onClick={onClick} />;
  }
};
