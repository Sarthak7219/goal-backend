import React from 'react';
import './global.css';
import './style.css';
import iconImg from '../images/icon.png';
import profileImg from '../images/profile.jpeg'; // Import profile image
import resourceCardBg from '../images/Rectangle 5995.png'; // Import background image for member card
import harshitImg from '../images/harshit.jpeg'; // Import Harshit's image

function Team() {
  return (
    <div className="team-page">
      <div className="page-hero" id="team-bg">
        <div className="page-head">
          <h1>Our Team</h1>
          <p><a href="{% url 'home' %}">Home</a> / <a href="">Team</a></p>
        </div>
        <img src={iconImg} alt="Icon" />
      </div>

      <div className="container">
        <div className="quick-link-box" id="team-sidebox">
          <a href="#collaborators" className="quicklink active">- Collaborators</a>
          <a href="#research_associates" className="quicklink">- Research Associates</a>
          <a href="#community_trainers" className="quicklink">- Community Trainers</a>
          <a href="#interns" className="quicklink">- Interns</a>
          <a href="#students" className="quicklink">- Students</a>
        </div>

        <div className="right" id="team-right">
          <section className="team" id="collaborators">
            <h2>Collaborators</h2>

            <div className="photo-container">
              <div className="member-card">
                <img src={harshitImg} className="member-img" alt="" />
                <img src={resourceCardBg} className="member-card-bg" alt="" />
                <div className="member-details">
                  <h3>Dr. Harshit Sosan Lakra</h3>
                  <div className="member-line"></div>
                  <p className="position">Assistant Professor</p>
                  <p className="institute">Indian Institute of Technology Roorkee, India</p>
                  <div className="social-icons">
                    <a href="#"><i className="fa-regular fa-envelope" style={{ color: '#ec028c' }}></i></a>
                    <a href="#"><i className="fa-brands fa-linkedin" style={{ color: '#ec028c' }}></i></a>
                  </div>
                </div>
              </div>
              {/* Repeat the same structure for other members */}
            </div>
          </section>

          {/* Repeat similar sections for Research Associates, Community Trainers, Interns, and Students */}
        </div>
      </div>
    </div>
  );
}

export default Team;
