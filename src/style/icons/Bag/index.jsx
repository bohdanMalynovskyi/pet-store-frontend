import { BagDesktop } from './BagDesktop';
import { BagMobile } from './BagMobile';

export const BagOld = ({ size, itemСount, onClick }) => {
  /*    Props:
    size(string): "desktop", "mobile"
    itemСount(number)
     onClick(function)
  */
  if (size === 'desktop') {
    return <BagDesktop itemСount={itemСount} onClick={onClick} />;
  }
  if (size === 'mobile') {
    return <BagMobile itemСount={itemСount} onClick={onClick} />;
  }
};
