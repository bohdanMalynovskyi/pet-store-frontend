export function transformDataAnimalCategories(data) {
  const nameToDisplayAndPath = {
    Dogs: { display: 'Собакам', path: '/dogs' },
    Cats: { display: 'Котам', path: '/cats' },
    SmallPets: { display: 'Гризунам', path: '/smallpets' },
    Birds: { display: 'Птахам', path: '/birds' },
    Fish: { display: 'Рибам', path: '/fish' },
    Reptiles: { display: 'Рептиліям', path: '/reptiles' },
  };
  // Recheck categories
  return data.map((item) => {
    const displayAndPath = nameToDisplayAndPath[item.name];
    return {
      ...item,
      display: displayAndPath ? displayAndPath.display : '',
      path: displayAndPath ? displayAndPath.path : '',
    };
  });
}
