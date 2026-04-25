import { useState } from 'react'
import ConversationInput from '../components/ConversationInput'
import StrategyResults from '../components/StrategyResults'
import './App.css'
import ComparisonChart from '../components/ComparisonChart'
import InfoPanel from '../components/InfoPanel'

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
  if (conversation.filter(m => m.trim()).length < 2) {
    alert('Please enter at least 2 messages');
    return;
  }
  
  setLoading(true);
  setResults(null);
  
  try {
    const response = await fetch('http://localhost:5000/analyze', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ conversation })
    });
    
    if (!response.ok) {
      throw new Error(`API error: ${response.status} ${response.statusText}`);
    }
    
    const data = await response.json();
    
    if (data.error) {
      throw new Error(data.error);
    }
    
    setResults(data);
  } catch (error) {
    console.error('Error analyzing strategies:', error);

    let errorMessage = 'Analysis failed. ';
    
    if (error.message.includes('Failed to fetch')) {
      errorMessage += 'Make sure the Flask API is running on http://localhost:5000';
    } else {
      errorMessage += error.message;
    }
    
    alert(errorMessage);
  } finally {
    setLoading(false);
  }
};

  return (
    <div className="container">
      <header>
        <h1>Context Strategy Analyzer</h1>
        <p>See how different strategies affect LLM responses</p>
      </header>

      <InfoPanel />

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

      {results && 
        <>
          <ComparisonChart results={results} />
          <StrategyResults results={results} fullConversation={conversation} />
        </>
      }
    </div>
  )
}

export default App