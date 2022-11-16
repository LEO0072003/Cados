import React, {useEffect, useState} from 'react'
import { useParams } from 'react-router-dom'
import axios from 'axios'
import { Link } from 'react-router-dom'

const AdvocatePage = () => {
    const params = useParams()
    const username = params.username

    const [advocate, setAdvocate] = useState(null)

    useEffect(() => {
      getData()
    }, [username])

    let getData = async () => {
      let response = await axios.get(`https://cados.up.railway.app/advocates/${username}`)
      console.log('RESPONSE', response)
      setAdvocate(response.data.advocate)
    }

  return (
    <>
      {advocate && (
      <div className='advocate__preview__wrapper'>

        <img className='advocate__preview__image' src={advocate.profile_pic}/>

        <strong>{advocate.name} </strong>
        <br/>
        <a href={advocate.twitter}>@{advocate.username}</a>
        <p>{advocate.bio} </p>

      </div>
                    )}


    </>
  )
}

export default AdvocatePage
