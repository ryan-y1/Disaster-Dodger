import React, { useEffect, useState } from 'react'

function App() {
    const url = 'api.catastrophe.world/states/'
    const [stateData, setStateData] = useState([{}]);

    useEffect(() => {
        fetch(`${url}`), then(
            res => res.json()
        ).then(
            data => {
                setPersonData(data)
                console.log(data)
            }
        )

    }, []);
    return (
        <div>

        </div>
    );
}


export default App;