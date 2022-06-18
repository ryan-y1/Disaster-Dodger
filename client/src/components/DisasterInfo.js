import React from 'react'
import { Typography } from '@mui/material';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia'
import Tabs from '@mui/material/Tabs'
import Tab from '@mui/material/Tab'
import { useState } from 'react'

function TabPanel(props) {
  const { items, value, index } = props
  return (
    <div
      role="tabpanel"
      hidden={value !== index}
      id={index}
      className="itemList"
    >
      {
        value === index &&
        (items.map(e => {
          return <Card
            sx={{
              width: 350,
              height: 450,
              borderRadius: 5,
              textAlign: "center",
              margin: "1rem",
              marginBottom: 15,
              backgroundColor: "#D2E4C4",
            }}
            key={e.name}
          >
            <CardMedia
              component='img'
              height='194'
              image={e.image}
              alt='picture'
            />
            <CardContent>
              <Typography variant='h5'>{e.name}</Typography>
              <Typography variant='body2'>{e.text}</Typography>
            </CardContent>
          </Card>
        }))}
    </div>
  )
}

function DisasterInfo(props) {
  const [tabVal, setTabVal] = useState(0)
  return props.trigger ? (
    <div className='infoDiv'>
      <Typography variant="h1">{props.info.state}</Typography>
      <Typography variant='h2'>Recommended Items to Prepare</Typography>

      <Tabs textColor="black" value={tabVal} onChange={(e, val) => setTabVal(val)}>
        {
          props.info.disasterList.map(e => {
            return <Tab sx={{ backgroundColor: "#9ac6e3" }} label={e.disasterType} key={e.disasterType} />
          })
        }
      </Tabs>
      {
        props.info.disasterList.map((e, i) => {
          return <TabPanel items={e.items} value={tabVal} index={i} key={i} />
        })
      }
    </div>
  ) : (
    <div className='preInfoDiv'>
      <Typography variant="h2" sx={{ textAlign: "center" }}>Pick a region to start Preparing!</Typography>
    </div>
  )
}

export default DisasterInfo