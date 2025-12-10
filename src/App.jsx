import { useState, useEffect } from 'react'
import axios from 'axios'
import './App.css'

function App() {
  const [currentPage, setCurrentPage] = useState('home')
  const [apiData, setApiData] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  useEffect(() => {
    if (currentPage === 'home') {
      fetchData()
    }
  }, [currentPage])

  const fetchData = async () => {
    setLoading(true)
    setError(null)
    try {
      const response = await axios.get('/api/data')
      setApiData(response.data)
    } catch (err) {
      setError('Failed to fetch data from Flask API')
      console.error(err)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="app">
      <nav className="nav">
        <button 
          onClick={() => setCurrentPage('home')}
          className={currentPage === 'home' ? 'active' : ''}
        >
          Home
        </button>
        <button 
          onClick={() => setCurrentPage('about')}
          className={currentPage === 'about' ? 'active' : ''}
        >
          About
        </button>
      </nav>

      <div className="container">
        {currentPage === 'home' && (
          <div>
            <h1>Welcome to React + Flask</h1>
            <p>This is a full-stack application.</p>
            {loading && <p className="loading">Loading data from API...</p>}
            {error && <p className="error">{error}</p>}
            {apiData && !loading && (
              <div className="api-data">
                <p><strong>Message:</strong> {apiData.message}</p>
                <p><strong>Data:</strong> {apiData.data.join(', ')}</p>
              </div>
            )}
            <button onClick={fetchData} className="fetch-btn">
              Refresh Data
            </button>
          </div>
        )}

        {currentPage === 'about' && (
          <div>
            <h1>About</h1>
            <p>This is a full-stack application built with:</p>
            <ul className="tech-list">
              <li>React (Frontend)</li>
              <li>Flask (Backend API)</li>
              <li>Vite (Build Tool)</li>
            </ul>
          </div>
        )}
      </div>
    </div>
  )
}

export default App

