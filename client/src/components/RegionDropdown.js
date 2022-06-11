import React from 'react'
import Select from '@mui/material/Select'
import { MenuItem } from '@mui/material'

function RegionDropdown() {
    const [region, setRegion] = React.useState('')

    const handleChange = (event) => {
        setRegion(event.target.value)
    }
    
    return (
        <Select 
            value={region}
            onChange={handleChange}
        >
            <MenuItem value={"a"}>a</MenuItem>
            <MenuItem value={"b"}>b</MenuItem>
            <MenuItem value={"c"}>c</MenuItem>
            <MenuItem value={"d"}>d</MenuItem>
        </Select>
    )
}

export default RegionDropdown