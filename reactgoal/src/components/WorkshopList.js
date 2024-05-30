import React, { useEffect } from "react";
import "./global.css";
import "./style.css";
import { NavLink } from "react-router-dom";
import iconImg from "../images/icon.png";

function WorkshopList({ workshops }) {
  return (
    <div className="workshops-page">
      <div className="page-hero" id="team-bg">
        <div className="page-head">
          <h1>Workshops</h1>
          <p>
            <NavLink to="/" className="hero-link">
              Home
            </NavLink>{" "}
            /{" "}
            <NavLink to="/workshops" className="hero-link">
              Workshops
            </NavLink>
          </p>
        </div>
        <img src={iconImg} alt="Icon" />
      </div>

      <div className="workshops-list">
        <h1>Workshops</h1>

        <div className="workshops-list-wrapper">
          {workshops.map((workshop) => (
            <div>
              <div className="line"></div>
              <div className="box">
                <img src={workshop.image} alt="" />
                <div>
                  <div className="flex">
                    <p>Workshop</p>
                    <p className="pink-date">{workshop.date}</p>
                  </div>
                  <NavLink to={`/workshops/workshop-detail/${workshop.id}`}>
                    <h1>{workshop.title}</h1>
                  </NavLink>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default WorkshopList;
