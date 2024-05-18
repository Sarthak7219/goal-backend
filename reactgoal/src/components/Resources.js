import React from 'react';
import './global.css';
import './style.css';
import iconImg from '../images/icon.png';
import resourceImage from '../images/DSC_2080.JPG'; // Import resource image

function Resources() {
  return (
    <div className="resources-page">
      <div className="page-hero" id="resources-bg">
        <div className="page-head">
          <h1>Resources</h1>
          <p><a href="{% url 'home' %}">Home</a> / <a href="">Resources</a></p>
        </div>
        <img src={iconImg} alt="Icon" /> {/* Use imported icon image */}
      </div>

      <div className="container">
        <div className="quick-link-box" id="resources-sidebox">
          <a href="#publications" className="quicklink active">- Publications</a>
          <a href="#training-manuels" className="quicklink">- Training Manuels</a>
        </div>

        <div className="right" id="resources-right">
          <section className="resources" id="publications">
            <div className="section-head">
              <div>
                <p>Publications</p>
                <div className="line"></div>
              </div>
              <h1>Read Our Publications</h1>
            </div>

            <div className="resources-container">
              <div className="resource-box">
                <img src={resourceImage} alt="Resource" /> {/* Use imported resource image */}
                <div className="detail">
                  <p>Publisher</p>
                  <h3>Lorem ipsum dolor sit amet consectetur.</h3>
                  <p className="date">June 27, 2023</p>
                </div>
              </div>
              {/* Repeat the same structure for other resource boxes */}
            </div>
          </section>

          {/* Similar structure for the Training Manuals section */}
        </div>
      </div>
    </div>
  );
}

export default Resources;
