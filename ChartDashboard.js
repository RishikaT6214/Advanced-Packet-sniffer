// ChartDashboard.js
import React from 'react';
import { Cell, Legend, Pie, PieChart, Tooltip } from 'recharts';

const COLORS = ['#0088FE', '#FF8042']; // Normal, Malicious colors

function ChartDashboard({ stats }) {
  const data = [
    { name: 'Normal', value: stats.normal },
    { name: 'Malicious', value: stats.malicious },
  ];

  return (
    <div>
      <h2>Traffic Prediction Summary</h2>
      <PieChart width={400} height={300}>
        <Pie
          data={data}
          dataKey="value"
          cx="50%"
          cy="50%"
          outerRadius={100}
          fill="#8884d8"
          label
        >
          {data.map((entry, index) => (
            <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
          ))}
        </Pie>
        <Tooltip />
        <Legend />
      </PieChart>
    </div>
  );
}

export default ChartDashboard;
