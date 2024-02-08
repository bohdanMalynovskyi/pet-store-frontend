import { transformDataAnimalCategories } from '../../../utils/transformData';
import actions from './actions';

const INITIAL_STATE = {
  animalCategories: [],
  animalCategoriy: {},
  loading: false,
  error: null,
};

const animalCategoriesReducer = (state = INITIAL_STATE, action) => {
  switch (action.type) {
    case actions.FETCH_ANIMAL_CATEGORIES_REQUEST:
    case actions.FETCH_ANIMAL_CATEGORY_ID_REQUEST: {
      return { ...state, loading: true };
    }
    case actions.FETCH_ANIMAL_CATEGORIES_SUCCESS: {
      const transformedData = transformDataAnimalCategories(action.payload.data);
      return { ...state, loading: false, animalCategories: transformedData };
    }
    case actions.FETCH_ANIMAL_CATEGORY_ID_SUCCESS: {
      return { ...state, loading: false, animalCategory: action.payload.data };
    }
    case actions.FETCH_ANIMAL_CATEGORIES_FAILURE:
    case actions.FETCH_ANIMAL_CATEGORY_ID_FAILURE: {
      return { ...state, loading: false, error: action.payload.error };
    }
    default:
      return state;
  }
};
export default animalCategoriesReducer;
