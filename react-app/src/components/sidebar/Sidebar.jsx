import React, { useState, useEffect } from 'react';
import './Sidebar.css';

const Sidebar = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [isMobile, setIsMobile] = useState(window.innerWidth <= 768);

  const toggleSidebar = () => {
    setIsOpen(!isOpen);
  };

  useEffect(() => {
    const handleResize = () => {
      setIsMobile(window.innerWidth <= 768);
      if (window.innerWidth > 768) {
        setIsOpen(true);
      }
    };

    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, []);

  return (
    <div className={`sidebar ${isOpen ? 'open' : 'closed'} ${isMobile ? 'mobile' : ''}`}>
      <div className="sidebar-header">
        <img src="./favicon.png" alt="Zenix" className="logo" />
        {isOpen && !isMobile && <h1 className="logo-text">LearnwithGemini</h1>}
        <button className="toggle-btn" onClick={toggleSidebar}>
          {isOpen ? '<' : '>'}
        </button>
      </div>
      {isOpen && (
        <div className="user-info">
          <img src="./avatar.png" alt="Marquez" className="profile-pic" />
          <h2>Hello, Kiran</h2>
          <p>demo@mail.com</p>
        </div>
      )}
      <nav className="menu">
        <ul>
          <li><a href="#dashboard">Dashboard</a></li>
          <li><a href="#cms">My Quizes</a></li>
          <li><a href="#apps">My Learning</a></li>
          <li><a href="#bootstrap">Profile</a></li>
          <li><a href="#plugins">Logout</a></li>
          {/* <li><a href="#widget">Widget</a></li> */}
        </ul>
      </nav>
    </div>
  );
};

export default Sidebar;
