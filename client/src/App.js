import logo from './logo.svg';
import React, { useState, useEffect } from 'react'
import './App.css';

import SubmitRegion from './components/SubmitRegion';

import { createTheme, ThemeProvider } from '@mui/material/styles'
import { Typography } from '@mui/material';

const theme = createTheme({
  palette: {
    primary: {
      main: "#b89986"
    },
    secondary: {
      main: "#ffffff"
    }
  },
  typograpghy: {
    fontFamily: [
      'Roboto'
    ]
  }
})

function App() {
  return (
    <ThemeProvider theme={theme}>
      <div className='app'>
      <section className='main'>
        <Typography variant='h1'>Disaster Buddy</Typography>
        <SubmitRegion/>
      </section>
      <div className='sub'>

      </div>
    </div>
    </ThemeProvider>
  );
}

export default App;
