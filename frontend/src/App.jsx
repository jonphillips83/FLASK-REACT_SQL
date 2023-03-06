import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import './App.css'

function App() {
  const [articles, setArticles] = useState([])

  useEffect(() => {
    fetch('http://127.0.0.1:5000/api/get/articles', {
      'methods':'GET',
      headers: {
        'Content-Type':'applications/json'
      }
    })
    .then(resp => resp.json())
    .then(resp => setArticles(resp))
    .catch(error => console.log(error))

  },[])

  return (
    <div className="App">
      <h1>Flask</h1>

      {articles.map(articles => {
        return (
          <div key = {articles.article_id}>

            <h2>{articles.title}</h2>
            <p>{articles.body}</p>
            <p>{articles.date}</p>

            </div>
        )
      })}
    </div>
  );

}

export default App
