import { Provider } from 'react-redux';
import ThemeProvider from '@mui/material/styles/ThemeProvider';
import store from './redux';
import theme from './style/theme';
import Layout from './components/Layout/Layout';

function App() {
  return (
    <Provider store={store}>
      <ThemeProvider theme={theme}>
        <Layout />
      </ThemeProvider>
    </Provider>
  );
}

export default App;
