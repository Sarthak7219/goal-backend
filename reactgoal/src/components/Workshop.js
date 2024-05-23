import React from 'react'

import './global.css'
import './style.css'

import workshopImage from '../images/workhopimage.png';
import workshopDetailImage1 from '../images/workshops/workshopdetail1.png';
import iconImg from '../images/icon.png';
import underlineImg from '../images/underlineimg.png';
function workshop() {
  return (
    <div class="workshop-page">
       <div class="page-hero" id="gallery-bg">
        <div class="page-head">
            <h1>Workshop</h1>
            <p>Home / Workshop</p>
        </div>
        <img src={iconImg} alt=""/>
    </div>
    <div class="workshop-content">
      <h1>
        Adaptive Transformations for Climate Change and Disaster Risk
        Reduction Workshop
      </h1>
      <div class="workshop-container">
        <div class="left-container">
          <div class="image">
            <img src={workshopImage} alt="" />
          </div>
          <div class="about-workshop">
            <h2>About the workshop</h2>
            <p>
              Flyingfish Kafue pike cow shark California smoothtongue golden
              loach temperate ocean-bass gulper Sailbearer kanyu porcupinefish
              Kafue pike opah sunfish gudgeon boga Asiatic glassfish tadpole
              fish! Alewife, poacher airbreathing catfish; zebra tilapia
              northern pearleye naked-back knifefish pupfish dojo loach,
              “snake mackerel bonytail chub arapaima horsefish weasel shark.”
              Flyingfish Kafue pike cow shark California smoothtongue golden
              loach temperate ocean-bass gulper Sailbearer kanyu porcupinefish
              Kafue pike opah sunfish gudgeon boga Asiatic glassfish tadpole
              fish! Alewife, poacher airbreathing catfish; zebra tilapia
              northern pearleye naked-back knifefish pupfish dojo loach,
              “snake mackerel bonytail chub arapaima horsefish weasel shark.”
            </p>
          </div>
          <div class="registration-detail">
            <h2>Registration</h2>
            <h4>Target Audience</h4>
            <p>
              The workshop is designed for Masters and PhD students,
              researchers and working professionals in the fields of
              freshwater ecology, hydrology, climate change, water management,
              environmental science, etc.
            </p>
            <h4>How to register?</h4>
            <p>
              Registration page (for workshop and poster presentations): LINK
              Last Day to register: 25th May 2023 
            </p>
          </div>
          <div class="accomodation">
            <h2>Accomodation</h2>
            <p>
              Accommodation is available for external participants (those from
              outside IIT Roorkee) at IIT Roorkee. Please note that the
              availability of accommodation is limited and will be provided on
              a first-come, first-served basis. If you have any questions or
              concerns regarding accommodation, please contact us at the
              provided email address.
            </p>
          </div>
        </div>
        <div class="right-container">
          <div class="workshop-detail">
            <h2>Workshop Details</h2>
            <h4>Date:</h4>
            <p>12 sep 2021</p>
            <h4>Coordinator:</h4>
            <p>Sarthak Rangari</p>
            <h4>Venue:</h4>
            <p>Department of Architecture and Planning, IIT Roorkee</p>
          </div>
          <div class="recent-workshops">
            <h2>Recent Workshops</h2>
            <div class="workshop-cards">
              <div class="card">
                <div class="image">
                  <img src={workshopDetailImage1} alt="" />
                </div>
                <div class="desc">
                  <h5>Charity, Expectati ons vs. Reality</h5>
                  <p>Homeless</p>
                </div>
              </div>
              <div class="card">
                <div class="image">
                  <img src={workshopDetailImage1} alt="" />
                </div>
                <div class="desc">
                  <h5>Charity, Expectati ons vs. Reality</h5>
                  <p>Homeless</p>
                </div>
              </div>
              <div class="card">
                <div class="image">
                  <img src={workshopDetailImage1} alt="" />
                </div>
                <div class="desc">
                  <h5>Charity, Expectati ons vs. Reality</h5>
                  <p>Homeless</p>
                </div>
              </div>
            </div>
          </div>
          <div class="popular-tags">
            <h2>Popular tags</h2>
            <div class="button-tags">
              <div class="btn"><a>Food</a></div>
              <div class="btn"><a>Food</a></div>
              <div class="btn"><a>Food</a></div>
              <div class="btn"><a>Food</a></div>
              <div class="btn"><a>Food</a></div>
              <div class="btn"><a>Food</a></div>
              <div class="btn"><a>Food</a></div>
              
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  )
}

export default workshop