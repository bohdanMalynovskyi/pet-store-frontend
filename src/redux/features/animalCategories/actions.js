import { BASE_URL } from '../../../constants';

const actions = {
  FETCH_ANIMAL_CATEGORIES_REQUEST: 'FETCH_ANIMAL_CATEGORIES_REQUEST',
  FETCH_ANIMAL_CATEGORIES_SUCCESS: 'FETCH_ANIMAL_CATEGORIES_SUCCESS',
  FETCH_ANIMAL_CATEGORIES_FAILURE: 'FETCH_ANIMAL_CATEGORIES_FAILURE',
  FETCH_ANIMAL_CATEGORY_ID_REQUEST: 'FETCH_ANIMAL_CATEGORY_ID_REQUEST',
  FETCH_ANIMAL_CATEGORY_ID_SUCCESS: 'FETCH_ANIMAL_CATEGORY_ID_SUCCESS',
  FETCH_ANIMAL_CATEGORY_ID_FAILURE: 'FETCH_ANIMAL_CATEGORY_ID_FAILURE',
};

export default actions;

export const fetchAnimalCategories = () => async (dispatch) => {
  dispatch({ type: actions.FETCH_ANIMAL_CATEGORIES_REQUEST });

  try {
    const response = await fetch(`${BASE_URL}animalcategories`);
    const data = await response.json();

    dispatch({ type: actions.FETCH_ANIMAL_CATEGORIES_SUCCESS, payload: { data } });
  } catch (error) {
    dispatch({ type: actions.FETCH_ANIMAL_CATEGORIES_FAILURE, payload: { error: error.toString() } });
  }
};

export const fetchAnimalCategory = (id) => async (dispatch) => {
  dispatch({ type: actions.FETCH_ANIMAL_CATEGORY_ID_REQUEST });

  try {
    const response = await fetch(`${BASE_URL}animalcategories/${id}`);
    const data = await response.json();
    dispatch({ type: actions.FETCH_ANIMAL_CATEGORY_ID_SUCCESS, payload: { data } });
  } catch (error) {
    dispatch({ type: actions.FETCH_ANIMAL_CATEGORY_ID_FAILURE, payload: { error: error.toString() } });
  }
};
