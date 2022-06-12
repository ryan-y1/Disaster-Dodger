import React, { useState, useEffect } from 'react'
import { Parallax, ParallaxLayer } from '@react-spring/parallax'
import './App.css';

import SubmitRegion from './components/SubmitRegion';
import DisasterInfo from './components/DisasterInfo';

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
  const [infoActivate, setInfoActivate] = useState(false)

  return (
    <ThemeProvider theme={theme}>
      <Parallax pages={2}>
        <div className='app'>
          <ParallaxLayer
            speed={1.3}
          >
            <section className='main'>
              <Typography variant='h1'>Disaster Dodger</Typography>
              <SubmitRegion setTrigger={setInfoActivate}/>
            </section>
          </ParallaxLayer>
          <ParallaxLayer 
            offset={0.7}
            speed={2}
            factor={1}
          >
            <DisasterInfo trigger={infoActivate}/>
          </ParallaxLayer>
        </div>
      </Parallax>
    </ThemeProvider>
  );
}

export default App;
