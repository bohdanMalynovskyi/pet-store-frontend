import { combineReducers } from '@reduxjs/toolkit';
import animalCategoriesReducer from './features/animalCategories/reducer';

const rootReducer = combineReducers({
  animalCategories: animalCategoriesReducer,
  // productCategories: productCategoriesReducer,
  // products: productsReducer,
  // subCategories: subCategoriesReducer,
});

export default rootReducer;
