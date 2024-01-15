export const selectResponsiveStyle = (className, style, isMobile) => {
  if (!style[className]) {
    console.error(`Class ${className} is not defined in style object.`);
    return '';
  }

  if (!style[className].mobile || !style[className].desktop) {
    console.error(`Mobile or desktop style is not defined for class ${className}.`);
    return '';
  }

  return isMobile ? style[className].mobile : style[className].desktop;
};
