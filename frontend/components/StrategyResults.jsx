import { analyzeSafety, calculateEfficiency } from '../utils/safetyAnalyzer';

function StrategyResults({ results, fullConversation }) {
  return (
    <div className="results-grid">
      {Object.entries(results).map(([key, strategy]) => {
        const safety = analyzeSafety(fullConversation, strategy.keptMessages);
        const efficiency = calculateEfficiency(
          strategy.tokensUsed, 
          strategy.totalCount, 
          strategy.keptCount
        );
        
        return (
          <div 
            key={key} 
            className={`strategy-card ${safety.isDangerous ? 'danger-card' : ''}`}
            style={{ borderColor: strategy.color }}
          >
            <div className="card-header">
              <h3>{strategy.name}</h3>
              {safety.isDangerous && (
                <div className="danger-badge">
                  {safety.warning}
                </div>
              )}
            </div>
            
            <p className="description">{strategy.description}</p>
            
            <div className="metrics">
              <div className="metric">
                <span className="label">Tokens:</span>
                <span className="value">{strategy.tokensUsed}</span>
              </div>
              <div className="metric">
                <span className="label">Messages:</span>
                <span className="value">{strategy.keptCount}/{strategy.totalCount}</span>
              </div>
              <div className="metric">
                <span className="label">Efficiency:</span>
                <span className="value">{efficiency}%</span>
              </div>
            </div>
            
            <div className="kept-messages">
              <h4>Context Sent to AI:</h4>
              {strategy.keptMessages.map((msg, i) => (
                <div 
                  key={i} 
                  className="message"
                  style={{ borderLeftColor: strategy.color }}
                >
                  {msg}
                </div>
              ))}
            </div>
            
            <div className="ai-response">
              <h4>AI Response:</h4>
              <p>{strategy.response}</p>
            </div>
          </div>
        );
      })}
    </div>
  );
}

export default StrategyResults;