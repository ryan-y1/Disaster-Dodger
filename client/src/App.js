import logo from './logo.svg';
import React, { useState, useEffect } from 'react'
import './App.css';

import RegionDropdown from './components/RegionDropdown';
import ConfirmRegionButton from './components/ConfirmRegionButton';

import { createTheme, ThemeProvider } from '@mui/material/styles'

const theme = createTheme({
  palette: {
    primary: {
      main: "#ffffff"
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
        <h1>Disaster Buddy</h1>
        <div className='form'>
          <RegionDropdown />
          <ConfirmRegionButton />
        </div>
      </section>
      <div className='sub'>

      </div>
    </div>
    </ThemeProvider>
  );
}

export default App;
