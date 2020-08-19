import React from 'react';
import { ThemeProvider } from 'styled-components';
import { Button, themeDefault } from 'aiq-design-system';

function App() {
  return (
    <div className="App">
      <ThemeProvider theme={themeDefault}>
        <Button palette="primary" variant="contained">TESTE</Button>
      </ThemeProvider>
    </div>
  );
}

export default App;
