import React, {useEffect, useState} from 'react'
import { Link } from 'react-router-dom'
import axios from 'axios'

const HomePage = () => {

  const[advocates, setAdvocates] = useState([])
  const [total, setTotal] = useState(0)
  const [pagination, setPagination] = useState(null)

  useEffect(() => {
    getData()
  }, [])

  let getData = async (query='') => {
    let response = await axios.get(`https://cados.up.railway.app/advocates?query=${query}`)
    console.log('RESPONSE', response)
    setAdvocates(response.data.advocates)
    setTotal(response.data.total)
    setPagination(response.data.pagination)
  }

  let searchData = (e) => {
    e.preventDefault()
    let query = e.target.query.value
    getData(query)
  }

  return (
    <div className='main--container'>
      <h2>Search {total} developer advocates found by @leo's webscraper and the TwitterAPI.</h2>
        <p>{pagination?.results_found} developers found</p>
        <div className='form--wrapper'>
          <form onSubmit={searchData} id='search form'>
            <input type="text" name="query" placeholder="Search advocates..."/>
            <input type="submit" value="Search" className='btn--primary' />
          </form>
        </div>

      <div className='advocate_list'>
        {advocates.map((advocate, index) => (
          <div className='advocate__preview__wrapper' key={index}>

            <div className='advocate__preview__header'>
              <Link to={`/advocate/${advocate.username}`}>
                  <img className='advocate__preview__image' src={advocate.profile_pic}/>
              </Link>
              <div>
                <strong>{advocate.name} </strong>
                <br/>
                <a href={advocate.twitter}>@{advocate.username}</a>
              </div>
            </div>
            <small className='bio--preview'>{advocate.bio} </small>

          </div>
        ))}
      </div>
    </div>
  )
}

export default HomePage
