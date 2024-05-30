import React, { useEffect } from "react";
import "./global.css";
import "./style.css";
import searchImg from "../images/search_icon.svg";
import { NavLink } from "react-router-dom";
import { scrollSpy } from "./scrollSpy";

function SearchPage({}) {
  useEffect(() => {
    const cleanup = scrollSpy();

    return () => {
      cleanup();
    };
  }, []);

  return (
    <div className="search-page">
      <div>
        <div className="search-box">
          <input
            type="text"
            placeholder="Search workshops, case studies"
          ></input>

          <div className="search-btn">
            <img src={searchImg} alt="" />
          </div>
        </div>

        <h3>Search Result For “Climate”</h3>

        <div className="search-container">
          <div>
            <div className="search-item">
              <h3>Workshop</h3>
              <p>
                Flyingfish Kafue pike cow shark climate smoothtongue golden
                loach temperate ocean-bass gulper Sailbearer kanyu porcupinefish
                Kafue pike opah sunfish gudgeon boga Asiatic glassfish tadpole
                fish!{" "}
              </p>
            </div>
            <div className="line"></div>
          </div>
          <div>
            <div className="search-item">
              <h3>Workshop</h3>
              <p>
                Flyingfish Kafue pike cow shark climate smoothtongue golden
                loach temperate ocean-bass gulper Sailbearer kanyu porcupinefish
                Kafue pike opah sunfish gudgeon boga Asiatic glassfish tadpole
                fish!{" "}
              </p>
            </div>
            <div className="line"></div>
          </div>
          <div>
            <div className="search-item">
              <h3>Workshop</h3>
              <p>
                Flyingfish Kafue pike cow shark climate smoothtongue golden
                loach temperate ocean-bass gulper Sailbearer kanyu porcupinefish
                Kafue pike opah sunfish gudgeon boga Asiatic glassfish tadpole
                fish!{" "}
              </p>
            </div>
            <div className="line"></div>
          </div>
        </div>

        <NavLink to="/">
          <div className="back-to-home-btn">
            <p>Back To Home Page</p>
          </div>
        </NavLink>
      </div>
    </div>
  );
}

export default SearchPage;
