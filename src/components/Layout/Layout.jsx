import React, { useEffect } from 'react';
import Routes from '../../routes/Routers';
import { useLocation } from 'react-router-dom';
import Header from '../Header/Header';
import Footer from '../Footer';
import { useDispatch, useSelector } from 'react-redux';
import { fetchAnimalCategories } from '../../redux/features/animalCategories/actions';
import { selectAnimalCategories } from '../../redux/features/animalCategories/selectors';

const Layout = () => {
  const location = useLocation();
  const isHomePage = location.pathname === '/home';

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
      <Header isHomePage={isHomePage} />
      <div className=" flex-auto">
        <Routes />
      </div>
      <Footer />
    </div>
  );
};

export default Layout;
