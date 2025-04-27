import React, { useState } from 'react';
import './App.css';

function App() {
  const [features, setFeatures] = useState('');
  const [prediction, setPrediction] = useState(null);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const featureArray = features.split(',').map(Number);

    try {
      const response = await fetch('http://localhost:5000/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ features: featureArray }),
      });

      const data = await response.json();
      setPrediction(data.prediction);
      setError('');
    } catch (err) {
      console.error('Error:', err);
      setError('⚠️ Failed to fetch prediction from the server.');
      setPrediction(null);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        🌐 <span>Network Traffic Predictor</span>
      </header>

      <div className="dashboard">
        <div className="card">
          <h2>📋 Enter Traffic Features</h2>
          <form onSubmit={handleSubmit}>
            <input
              type="text"
              value={features}
              onChange={(e) => setFeatures(e.target.value)}
              placeholder="e.g., 1.5,6,1,2,123,456"
            />
            <button type="submit">Predict</button>
          </form>
        </div>

        <div className="card">
          <h2>📊 Prediction Output</h2>
          {error && <p className="error">{error}</p>}
          {!prediction && !error && <p>Awaiting input...</p>}
          {prediction && (
            <div className={`result ${prediction === 'BENIGN' ? 'benign' : 'malicious'}`}>
              <p>{prediction}</p>
              {prediction === 'BENIGN' ? (
                <p className="status good">✅ Normal Traffic</p>
              ) : (
                <p className="status threat">⚠️ Detected Threat: {prediction}</p> )/* Improved message */
                }
              )
            </div>
          )}
        </div>

        <div className="card">
          <h2>📈 Future: Visualization</h2>
          <p>Charts will be integrated here using real-time traffic data.</p>
        </div>
      </div>

      <footer>Made with 🧠 by Network AI</footer>
    </div>
  );
}

export default App;
