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

      <div class="container">

<div class="quick-link-box" id="resources-sidebox">
    <a href="#publications" class="quicklink active">- Publications</a>
    <a href="#training-manuels" class="quicklink">- Training Manuels</a>
</div>

<div class="right" id="resources-right">
    <section class="resources" id="publications">
        <div class="section-head">
            <div>
                <p>Publications</p>
                <div class="line"></div>
            </div>
            <h1>Read Our Publications</h1>
        </div>

        <div class="resources-container">
            <div class="resource-box">
                <img src={resourceImage} alt="here is image"/>
                <div class="detail">
                    <p>Publisher</p>
                    <h3>Lorem ipsum dolor sit amet consectetur.</h3>
                    <p class="date">June27, 2023</p>
                </div>
            </div>
            <div class="resource-box">
                <img src={resourceImage} alt="here is image"/>
                <div class="detail">
                    <p>Publisher</p>
                    <h3>Lorem ipsum dolor sit amet consectetur.</h3>
                    <p class="date">June27, 2023</p>
                </div>
            </div>
            <div class="resource-box">
                <img src={resourceImage} alt="here is image"/>
                <div class="detail">
                    <p>Publisher</p>
                    <h3>Lorem ipsum dolor sit amet consectetur.</h3>
                    <p class="date">June27, 2023</p>
                </div>
            </div>
            <div class="resource-box">
                <img src={resourceImage} alt="here is image"/>
                <div class="detail">
                    <p>Publisher</p>
                    <h3>Lorem ipsum dolor sit amet consectetur.</h3>
                    <p class="date">June27, 2023</p>
                </div>
            </div>
        </div>
    </section>

    <section class="resources" id="training-manuels">
        <div class="section-head">
            <div>
                <p>Training Manuels</p>
                <div class="line"></div>
            </div>

            <h1>Read Our Training Manuels</h1>
        </div>

        <div class="resources-container">
            <div class="resource-box">
                <img src={resourceImage} alt="here is image"/>
                <div class="detail">
                    <p>Publisher</p>
                    <h3>Lorem ipsum dolor sit amet consectetur.</h3>
                    <p class="date">June27, 2023</p>
                </div>
            </div>
            <div class="resource-box">
                <img src={resourceImage} alt="here is image"/>
                <div class="detail">
                    <p>Publisher</p>
                    <h3>Lorem ipsum dolor sit amet consectetur.</h3>
                    <p class="date">June27, 2023</p>
                </div>
            </div>
            <div class="resource-box">
                <img src={resourceImage} alt="here is image"/>
                <div class="detail">
                    <p>Publisher</p>
                    <h3>Lorem ipsum dolor sit amet consectetur.</h3>
                    <p class="date">June27, 2023</p>
                </div>
            </div>
            <div class="resource-box">
                <img src={resourceImage} alt="here is image"/>
                <div class="detail">
                    <p>Publisher</p>
                    <h3>Lorem ipsum dolor sit amet consectetur.</h3>
                    <p class="date">June27, 2023</p>
                </div>
            </div>
        </div>
    </section>
</div>
</div>
    </div>
  );
}

export default Resources;
