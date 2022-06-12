import React, { useState } from 'react'
import { Parallax, ParallaxLayer } from '@react-spring/parallax'
import './App.css';

import SubmitRegion from './components/SubmitRegion';
import DisasterInfo from './components/DisasterInfo';
import logo from './images/Logo_transparent.png'

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
              <div style={{
                display: "inline-flex",
                alignItems: "center"
              }}>
                <img
                  src={logo}
                  alt=''
                  className='logo'
                />
                <Typography variant='h1'>Disaster Dodger</Typography>
              </div>
              <SubmitRegion setTrigger={setInfoActivate} />
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
      <div className='about'>
        <div>
          <div>
            <Typography variant='h2'>About</Typography>
            <Typography variant='p'>
              Disaster Dodger is a website built to assist in safer evacuation in the case of a potential natural disaster. Due to changes in climate conditions, there has been an overall increase in natural disasters around the world. As of now, Disaster Dodger has been programmed to assist in the United States. Simply select your state using the drop down menu on the home page, then you will find the most common natural disasters in your area, and items you can purchase to prepare for them (if one were to happen).
            </Typography>
          </div>
          <div>
            <Typography variant='h2'>Future Endeavors</Typography>
            <Typography variant='p'>
              In order to provide a more personalized system for our users, we wish to implement a profile system where each user with an account can access a dashboard and receive information about their target area. Another idea we had in mind was to directly connect Disaster Dodger with an interactive Amazon store via Google Cloud Product. Lastly, we hope to expand the service to other countries, even other continents, as well. This is just the beginning of an impactful service curated to protect its customers.
            </Typography>
          </div>
        </div>
      </div>
    </ThemeProvider>
  );
}

export default App;
