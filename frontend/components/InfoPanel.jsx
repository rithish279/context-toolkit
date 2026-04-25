function InfoPanel() {
  return (
    <div className="info-panel">
      <h3>How It Works</h3>
      <div className="info-grid">
        <div className="info-item">
          <h4>Recent Only</h4>
          <p>Keeps only the last N messages. Fast and simple, but loses historical context.</p>
        </div>
        <div className="info-item">
          <h4>Important Only</h4>
          <p>Filters by keywords (names, allergies, preferences). Works when keywords match domain.</p>
        </div>
        <div className="info-item">
          <h4>Summarize</h4>
          <p>Keeps first and last messages, compresses middle. Balances context and efficiency.</p>
        </div>
        <div className="info-item">
          <h4>Semantic Chunking</h4>
          <p>Uses AI embeddings to find messages most relevant to the question. Smart but may miss keywords.</p>
        </div>
        <div className="info-item">
          <h4>Hybrid</h4>
          <p>Combines semantic relevance with recency. Best of both worlds for most use cases.</p>
        </div>
      </div>
    </div>
  );
}

export default InfoPanel;