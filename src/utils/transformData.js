export function transformDataAnimalCategories(data) {
  const nameToDisplay = {
    Dogs: { display: 'Собакам' },
    Cats: { display: 'Котам' },
    Parrots: { display: 'Гризунам' },
    Birds: { display: 'Птахам' },
    Fish: { display: 'Рибам' },
    Reptiles: { display: 'Рептиліям' },
  };
  // Recheck categories
  return data.map((item) => {
    const display = nameToDisplay[item.name];
    return {
      ...item,
      display: display ? display.display : '',
      path: item.name.toLowerCase(),
    };
  });
}
