import { render, screen } from '@testing-library/react';
import { BrowserRouter as Router } from 'react-router-dom';
import App from './App';

test('renders login title', () => {
  render(<App />);
  const titleElement = screen.getByText(/Войти на сайт/i);
  expect(titleElement).toBeInTheDocument();
});
