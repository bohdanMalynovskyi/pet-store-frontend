import { Provider } from 'react-redux';
import { BrowserRouter } from 'react-router-dom';
import ThemeProvider from '@mui/material/styles/ThemeProvider';
import store from './redux';
import routes from './routes';
import theme from './style/theme';

function App() {
  return (
    <Provider store={store}>
      <ThemeProvider theme={theme}>
        <BrowserRouter>{routes}</BrowserRouter>
      </ThemeProvider>
    </Provider>
  );
}

export default App;
