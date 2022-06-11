import React from 'react'
import Select from '@mui/material/Select'
import { MenuItem } from '@mui/material'

function RegionDropdown() {
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
        <Select 
            value={region}
            onChange={handleChange}
            color="primary"
            sx={{
                width: "300px"
            }}
        >
            {USStateList.map(e => {
                return <MenuItem value={e}>{e}</MenuItem>
            })}
        </Select>
    )
}

export default RegionDropdown