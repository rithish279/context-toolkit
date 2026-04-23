
function StrategyResults({ results }) {

    return (
        <div className="result-grid">
            {Object.entries(results).map(([key, strategy]) => (
                <div key={key} className="strategy-card">
                    <h3>{strategy.name}</h3>
                    <div className="metrics">
                        <div className="metric">
                            <span className="label">Tokens:</span>
                            <span className="value">{strategy.tokensUsed}</span>
                        </div>
                        <div className="metric">
                            <span className="label">Messages:</span>
                            <span className="value">{strategy.keptCount}/{strategy.totalCount}</span>
                        </div>
                    </div>
                    <div className="kept-messages">
                        <h4>Context Sent:</h4>
                        {strategy.keptMessages.map((msg, i) => (
                            <div key={i} className="message">{msg}</div>
                        ))}
                    </div>
                    <div className="ai-response">
                        <h4>AI Response:</h4>
                        <p>{strategy.response}</p>
                    </div>
                </div>
            ))}
        </div>
    )
}

export default StrategyResults