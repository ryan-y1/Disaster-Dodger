import React from 'react'
import Button from '@mui/material/Button'
import Select from '@mui/material/Select'
import { MenuItem } from '@mui/material'

function SubmitRegion(props) {
    const [region, setRegion] = React.useState('')

    const USStateList = [
        "Alabama",
        "Alaska",
        "Arizona",
        "Arkansas",
        "California",
        "Colorado",
        "Connecticut",
        "Delaware",
        "Florida",
        "Georgia",
        "Hawaii",
        "Idaho",
        "Illinois",
        "Indiana",
        "Iowa",
        "Kansas",
        "Kentucky",
        "Louisiana",
        "Maine",
        "Maryland",
        "Massachusetts",
        "Michigan",
        "Minnesota",
        "Mississippi",
        "Missouri",
        "Montana",
        "Nebraska",
        "Nevada",
        "New Hampshire",
        "New Jersey",
        "New Mexico",
        "New York",
        "North Carolina",
        "North Dakota",
        "Ohio",
        "Oklahoma",
        "Oregon",
        "Pennsylvania",
        "Rhode Island",
        "South Carolina",
        "South Dakota",
        "Tennessee",
        "Texas",
        "Utah",
        "Vermont",
        "Virginia",
        "Washington",
        "West Virginia",
        "Wisconsin",
        "Wyoming"
    ]

    const handleChange = (event) => {
        setRegion(event.target.value)
    }

    return (
        <div className='form'>
            <Select 
                value={region}
                onChange={handleChange}
                color="primary"
                sx={{
                    width: "300px"
                }}
            >
            {USStateList.map(e => {
                return <MenuItem 
                            value={e}
                            key={e}
                        >{e}</MenuItem>
            })}
            </Select>
            <Button 
                variant='contained'
                onClick={ region !== '' ? async () => {
                    const rawResponse = await fetch('/searchRegion', {
                        method: 'POST',
                        headers: {
                            'Accept': 'application/json',
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({ region: region })
                    }).catch(error => console.log(error))
                    const response = await rawResponse.json();
                    console.log(response)
                    props.setTrigger(true)
                } : {}}
                >Search</Button>
        </div>
    )
    
}

export default SubmitRegion