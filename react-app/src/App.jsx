import React from 'react';
import Sidebar from './components/sidebar/Sidebar.jsx';
import Navbar from './components/navbar/Navbar.jsx';
import './App.css';
function App() {
  return (
    <div className="app">
      <Sidebar />
      <div className="main-content">
        <Navbar />
        <div className="content">
          {/* Your other content goes here */}
        </div>
      </div>
    </div>
  );
}

export default App;

