import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

function ComparisonChart({ results }) {
  const data = Object.entries(results).map(([key, strategy]) => ({
    name: strategy.name.replace(' (Semantic + Recent)', ''),
    tokens: strategy.tokensUsed,
    messages: strategy.keptCount,
    efficiency: Math.round(((strategy.totalCount - strategy.keptCount) / strategy.totalCount) * 100)
  }));

  return (
    <div className="comparison-section">
      <h2>Strategy Comparison</h2>
      
      <div className="chart-container">
        <h3>Token Usage</h3>
        <ResponsiveContainer width="100%" height={300}>
          <BarChart data={data}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="name" angle={-45} textAnchor="end" height={100} />
            <YAxis label={{ value: 'Tokens Used', angle: -90, position: 'insideLeft' }} />
            <Tooltip />
            <Bar dataKey="tokens" fill="#8884d8" />
          </BarChart>
        </ResponsiveContainer>
      </div>

      <div className="chart-container">
        <h3>Context Reduction</h3>
        <ResponsiveContainer width="100%" height={300}>
          <BarChart data={data}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="name" angle={-45} textAnchor="end" height={100} />
            <YAxis label={{ value: 'Reduction %', angle: -90, position: 'insideLeft' }} />
            <Tooltip />
            <Bar dataKey="efficiency" fill="#82ca9d" />
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}

export default ComparisonChart;