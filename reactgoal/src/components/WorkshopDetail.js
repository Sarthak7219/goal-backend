import React, { useEffect, useState } from "react";

import "./global.css";
import "./style.css";
import { NavLink, useParams } from "react-router-dom";

import workshopImage from "../images/workhopimage.png";
import workshopDetailImage1 from "../images/workshops/workshopdetail1.png";
import iconImg from "../images/icon.png";

function WorkshopDetail({ workshops }) {
  const { id } = useParams();
  const [workshop, setWorkshop] = useState(null);

  useEffect(() => {
    const selectedWorkshop = workshops.find(
      (workshop) => workshop.id === parseInt(id)
    );
    setWorkshop(selectedWorkshop);
  }, [id, workshops]);

  if (!workshop) {
    return <div>Workshop not found</div>;
  }

  return (
    <div className="workshop-detail-page">
      <div className="page-hero" id="gallery-bg">
        <div className="page-head">
          <h1>Workshop</h1>
          <p>
            {" "}
            <NavLink to="/" className="hero-link">
              Home
            </NavLink>{" "}
            /{" "}
            <NavLink to="/workshops" className="hero-link">
              Workshops
            </NavLink>{" "}
            /{" "}
            <NavLink
              to={`/workshops/workshop-detail/${workshop.id}`}
              className="hero-link"
            >
              {workshop.title.slice(0, 40)}
            </NavLink>
          </p>
        </div>
        <img src={iconImg} alt="" />
      </div>

      <div className="workshop-content">
        <div className="section-head">
          <div>
            <p>Workshop #1</p>
            <div className="line"></div>
          </div>
          <h1>{workshop.title}</h1>
        </div>
        <div className="workshop-container">
          <div className="left-container">
            <img src={workshopImage} alt="" />

            <div className="about-workshop">
              <h2>About the workshop</h2>
              <p>{workshop.description}</p>
            </div>
            <div className="registration-detail">
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
            <div className="accomodation">
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
          <div className="right-container">
            <div className="workshop-detail">
              <h2>Workshop Details</h2>
              <div>
                <h4>Date:</h4>
                <p>{workshop.date}</p>
              </div>
              <div>
                <h4>Coordinator:</h4>
                <p>Sarthak Rangari</p>
              </div>
              <div>
                <h4>Venue:</h4>
                <p>{workshop.venue}</p>
              </div>
            </div>
            <div className="recent-workshops">
              <h2>Recent Workshops</h2>
              <div className="workshop-cards">
                <div className="card">
                  <img src={workshopDetailImage1} alt="" />

                  <div className="desc">
                    <h5>Charity, Expectati ons vs. Reality</h5>
                    <p>Homeless</p>
                  </div>
                </div>
                <div className="card">
                  <img src={workshopDetailImage1} alt="" />

                  <div className="desc">
                    <h5>Charity, Expectati ons vs. Reality</h5>
                    <p>Homeless</p>
                  </div>
                </div>
                <div className="card">
                  <img src={workshopDetailImage1} alt="" />

                  <div className="desc">
                    <h5>Charity, Expectati ons vs. Reality</h5>
                    <p>Homeless</p>
                  </div>
                </div>
              </div>
            </div>
            {/* <!-- <div className="popular-tags">
                <h2>Popular tags</h2>
                <div className="tags">
                    <div className="btn">Food</div>
                    <div className="btn">Food</div>
                    <div className="btn">Food</div>
                    <div className="btn">Food</div>
                    <div className="btn">Food</div>
                    <div className="btn">Food</div>
                    <div className="btn">Food</div>
                </div>
            </div> --> */}
          </div>
        </div>
      </div>
    </div>
  );
}

export default WorkshopDetail;
