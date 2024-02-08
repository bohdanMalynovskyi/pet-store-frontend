import React, { useEffect } from 'react';
import Routes from '../../routes/Routers';

import Footer from '../Footer';
import { useDispatch, useSelector } from 'react-redux';
import { fetchAnimalCategories } from '../../redux/features/animalCategories/actions';
import { selectAnimalCategories } from '../../redux/features/animalCategories/selectors';
import Header from '../Header';

const Layout = () => {
  const dispatch = useDispatch();
  const { loading: loadingAnimalCategories } = useSelector(selectAnimalCategories);

  useEffect(() => {
    dispatch(fetchAnimalCategories());
  }, [dispatch]);

  if (loadingAnimalCategories) {
    return <div className="min-h-screen flex flex-col text-primary">Loading...</div>;
  }

  return (
    <div className="font-norms min-h-screen flex flex-col text-primary">
      <Header />
      <div className="flex-auto">
        <Routes />
      </div>
      <Footer />
    </div>
  );
};

export default Layout;
