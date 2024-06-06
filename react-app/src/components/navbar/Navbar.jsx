import React from 'react';
import './Navbar.css';

const Navbar = () => {
  return (
    <div className="navbar">
      <div className="navbar-center">
        {/* <input type="text" placeholder="Search here..." /> */}
      </div>
      <div className="navbar-right">
        <button className="nav-btn">🌙</button>
        <button className="nav-btn">🔔</button>
        <button className="nav-btn">✉️</button>
        <button className="nav-btn">🗓️</button>
        <img src="./avatar.png" alt="Johndoe" className="profile-pic" />
      </div>
    </div>
  );
};

export default Navbar;
