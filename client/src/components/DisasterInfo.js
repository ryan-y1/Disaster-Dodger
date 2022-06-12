import React from 'react'
import { Typography } from '@mui/material';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia'
import { borderRadius } from '@mui/system';


function DisasterInfo(props) {
  return props.trigger ? (
    <div className='infoDiv'>
        <Typography variant="h2">__insert area__ is prone to these disasters</Typography>
        <p>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque egestas ante et elit porttitor varius. Fusce vel enim leo. Sed iaculis velit id elit pretium, ut placerat ligula malesuada. Vivamus a mattis dolor. Etiam malesuada justo sed justo interdum tempus. Donec tellus risus, accumsan at viverra ut, aliquam quis sapien. Nullam posuere dictum quam, nec sodales felis sodales a. Proin sed commodo enim. Fusce feugiat metus eu nulla ullamcorper, ac suscipit erat viverra. Ut id efficitur massa, non sodales felis. Duis pulvinar magna id ultrices tristique. Sed porttitor lectus ut ex semper, ut ultricies mi imperdiet. Nam dapibus rutrum velit, eget elementum dui ornare sed. Vivamus mattis elit sit amet ultricies sodales.
        </p>
        <Typography variant='h2'>Reccomended Items</Typography>
        <div className='itemList'>
            <Card
              sx={{ width: 400, 
                borderRadius: 5, 
                textAlign: "center", 
                margin: "1rem",
                marginBottom: 15
              }}
            >
              <CardMedia
                component='img'
                height='194'
                image='https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/React-icon.svg/1200px-React-icon.svg.png'
                alt='picture'
              />
              <CardContent>
                <Typography variant='h3'>Item</Typography>
                <Typography variant='body2'>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque egestas ante et elit porttitor varius. Fusce vel enim leo. Sed iaculis velit id elit pretium, ut placerat ligula malesuada. Vivamus a mattis dolor. Etiam malesuada justo sed justo interdum tempus. Donec tellus risus, accumsan at viverra ut, aliquam quis sapien. Nullam posuere dictum quam, nec .</Typography>
              </CardContent>
            </Card>
            <Card
              sx={{ width: 400, 
                borderRadius: 5, 
                textAlign: "center", 
                margin: "1rem",
                marginBottom: 15
              }}
            >
              <CardMedia
                component='img'
                height='194'
                image='https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/React-icon.svg/1200px-React-icon.svg.png'
                alt='picture'
              />
              <CardContent>
                <Typography variant='h3'>Item</Typography>
                <Typography variant='body2'>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque egestas ante et elit porttitor varius. Fusce vel enim leo. Sed iaculis velit id elit pretium, ut placerat ligula malesuada. Vivamus a mattis dolor. Etiam malesuada justo sed justo interdum tempus. Donec tellus risus, accumsan at viverra ut, aliquam quis sapien. Nullam posuere dictum quam, nec .</Typography>
              </CardContent>
            </Card>
            <Card
              sx={{ width: 400, 
                borderRadius: 5, 
                textAlign: "center", 
                margin: "1rem",
                marginBottom: 15
              }}
            >
              <CardMedia
                component='img'
                height='194'
                image='https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/React-icon.svg/1200px-React-icon.svg.png'
                alt='picture'
              />
              <CardContent>
                <Typography variant='h3'>Item</Typography>
                <Typography variant='body2'>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque egestas ante et elit porttitor varius. Fusce vel enim leo. Sed iaculis velit id elit pretium, ut placerat ligula malesuada. Vivamus a mattis dolor. Etiam malesuada justo sed justo interdum tempus. Donec tellus risus, accumsan at viverra ut, aliquam quis sapien. Nullam posuere dictum quam, nec .</Typography>
              </CardContent>
            </Card>
            <Card
              sx={{ width: 400, 
                borderRadius: 5, 
                textAlign: "center", 
                margin: "1rem",
                marginBottom: 15
              }}
            >
              <CardMedia
                component='img'
                height='194'
                image='https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/React-icon.svg/1200px-React-icon.svg.png'
                alt='picture'
              />
              <CardContent>
                <Typography variant='h3'>Item</Typography>
                <Typography variant='body2'>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque egestas ante et elit porttitor varius. Fusce vel enim leo. Sed iaculis velit id elit pretium, ut placerat ligula malesuada. Vivamus a mattis dolor. Etiam malesuada justo sed justo interdum tempus. Donec tellus risus, accumsan at viverra ut, aliquam quis sapien. Nullam posuere dictum quam, nec .</Typography>
              </CardContent>
            </Card>
            <Card
              sx={{ width: 400, 
                borderRadius: 5, 
                textAlign: "center", 
                margin: "1rem",
                marginBottom: 15
              }}
            >
              <CardMedia
                component='img'
                height='194'
                image='https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/React-icon.svg/1200px-React-icon.svg.png'
                alt='picture'
              />
              <CardContent>
                <Typography variant='h3'>Item</Typography>
                <Typography variant='body2'>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque egestas ante et elit porttitor varius. Fusce vel enim leo. Sed iaculis velit id elit pretium, ut placerat ligula malesuada. Vivamus a mattis dolor. Etiam malesuada justo sed justo interdum tempus. Donec tellus risus, accumsan at viverra ut, aliquam quis sapien. Nullam posuere dictum quam, nec .</Typography>
              </CardContent>
            </Card>
            <Card
              sx={{ width: 400, 
                borderRadius: 5, 
                textAlign: "center", 
                margin: "1rem",
                marginBottom: 15
              }}
            >
              <CardMedia
                component='img'
                height='194'
                image='https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/React-icon.svg/1200px-React-icon.svg.png'
                alt='picture'
              />
              <CardContent>
                <Typography variant='h3'>Item</Typography>
                <Typography variant='body2'>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque egestas ante et elit porttitor varius. Fusce vel enim leo. Sed iaculis velit id elit pretium, ut placerat ligula malesuada. Vivamus a mattis dolor. Etiam malesuada justo sed justo interdum tempus. Donec tellus risus, accumsan at viverra ut, aliquam quis sapien. Nullam posuere dictum quam, nec .</Typography>
              </CardContent>
            </Card>
            <Card
              sx={{ width: 400, 
                borderRadius: 5, 
                textAlign: "center", 
                margin: "1rem",
                marginBottom: 15
              }}
            >
              <CardMedia
                component='img'
                height='194'
                image='https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/React-icon.svg/1200px-React-icon.svg.png'
                alt='picture'
              />
              <CardContent>
                <Typography variant='h3'>Item</Typography>
                <Typography variant='body2'>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque egestas ante et elit porttitor varius. Fusce vel enim leo. Sed iaculis velit id elit pretium, ut placerat ligula malesuada. Vivamus a mattis dolor. Etiam malesuada justo sed justo interdum tempus. Donec tellus risus, accumsan at viverra ut, aliquam quis sapien. Nullam posuere dictum quam, nec .</Typography>
              </CardContent>
            </Card>
            
        </div>
    </div>
  ) : (
    <div className='infoDiv'>
        <Typography variant="h2">Pick a region to prepare!</Typography>
    </div>
  )
}

export default DisasterInfo