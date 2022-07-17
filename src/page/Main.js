import axios from "axios";
import React, { useEffect, useState } from "react";
import { SERVER_PATH } from "../genenrel/Config";

const Main = () => {

    const [serverData, setServerData] = useState({})

    useEffect(() => {
        axios.get(SERVER_PATH + '/items').then((result) => {
            console.log(result)
            setServerData(result.data[0])
        })
    }, [])
    

    return(
        <div className="flex flex-1 justify-center items-start">
            <p>main</p>
        </div>
    )
}

export default Main