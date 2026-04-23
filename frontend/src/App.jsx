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
    // TODO: Call backend/API
    // For now, use mock data
    setTimeout(() => {
      setResults({
        recentOnly: {
          name: "Recent Only",
          tokensUsed: 17,
          keptCount: 2,
          totalCount: 6,
          response: "Generic suggestions...",
          keptMessages: conversation.slice(-2)
        },
        importantOnly: {
          name: "Important Only",
          tokensUsed: 23,
          keptCount: 3,
          totalCount: 6,
          response: "Pepperoni pizza recommended...",
          keptMessages: [conversation[1], conversation[2], conversation[5]]
        },
        summarize: {
          name: "Summarize",
          tokensUsed: 32,
          keptCount: 4,
          totalCount: 6,
          response: "Generic Suggestions (forgot the allergy)...",
          keptMessages: [
            "User: Hi, I'm Alex",
            "[... 3 messages omitted ...]",
            "User: What movie should I watch?",
            "User: What Should I order for dinner"
          ]
        }
      })
      setLoading(false)
    }, 1000)
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