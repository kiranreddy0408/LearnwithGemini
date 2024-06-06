import React from 'react';
import './dashboard.css';

function Dashboard() {
  return (
    <div className="dashboard">
      <div className="header">
        <h1>Welcome back Anna!</h1>
        <p>You've learned 80% of your goal this week! Keep it up and improve your results!</p>
      </div>
      <div className="content">
        <div className="latest-results">
          <h2>Latest results</h2>
          <ul>
            <li>Unit 5 - Technology <span className="progress">25%</span></li>
            <li>Unit 12 - Ecology <span className="progress">44%</span></li>
            <li>Unit 9 - Real estate <span className="progress">40%</span></li>
            <li>Unit 8 - Education <span className="progress">15%</span></li>
            <li>Unit 16 - Job market <span className="progress">76%</span></li>
          </ul>
        </div>
        <div className="time-spent">
          <h2>Time spent on learning</h2>
          <div className="chart">
            {/* Add a chart here or use a chart library */}
          </div>
        </div>
        <div className="courses">
          <h2>Your courses</h2>
          <div className="course">Business English - Grammar (B2)</div>
          <div className="course">Common English - Phrasal verbs (B2)</div>
          <div className="course">Business Spanish - Vocabulary (C1)</div>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;
