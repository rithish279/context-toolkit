import { useState } from 'react'
import ConversationInput from '../components/ConversationInput'
import StrategyResults from '../components/StrategyResults'
import './App.css'

function App() {
  const [conversation, setConversation] = useState([
    "User: Hi, I'm Alex",
    "User: I love pepperoni pizza",
    "User: I'm allergic to peanuts",
    "User: What's the weather?",
    "User: What movie should I watch?",
    "User: What should I order for dinner?"
  ])
  const [results, setResults] = useState(null)
  const [loading, setLoading] = useState(false)

  const analyzeStrategies = async () => {
  setLoading(true)
  const response = await fetch('http://localhost:5000/analyze', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ conversation })
  })
  const data = await response.json()
  setResults(data)
  setLoading(false)
  }

  return (
    <div className="container">
      <header>
        <h1>🧠 Context Strategy Analyzer</h1>
        <p>See how different strategies affect LLM responses</p>
      </header>

      <ConversationInput 
        conversation={conversation}
        setConversation={setConversation}
      />

      <button 
        onClick={analyzeStrategies}
        disabled={loading}
        className="analyze-btn"
      >
        {loading ? 'Analyzing...' : 'Analyze Strategies'}
      </button>

      {results && <StrategyResults results={results} />}
    </div>
  )
}

export default App