import React from "react";
import "./style.css";
import "./global.css";
import { NavLink } from "react-router-dom";

import logoImg from "../images/logo (2).png";
import downArrowImg from "../images/down_arrow.svg";
import searchImg from "../images/search_icon.svg";
import cancelIcon from "../images/cancel_icon.svg";
import { useState } from "react";
function Base() {
  const [isActive, setIsActive] = useState(false);

  const handleSearchClick = () => {
    if (!isActive) {
      setIsActive(true);
    }
  };

  const toggleActiveClass = () => {
    setIsActive(!isActive);
  };

  return (
    <div class="navbar">
      <NavLink to="/">
        <img src={logoImg} alt="image" />
      </NavLink>
      <ul class="navlist">
        <li>
          <NavLink to="/about">About</NavLink>
        </li>
        <li>
          <NavLink to="/workshops">Workshops</NavLink>
        </li>

        <li class="dropdown-menu">
          <NavLink to="/resources" class="Resources">
            Resources
            <img src={downArrowImg} />
          </NavLink>
          <ul class="dropdown">
            <li>
              <a href="{% url 'resources' %}#publications">Publications</a>
            </li>
            <li>
              <a href="{% url 'resources' %}#training_manuals">
                Training manuals
              </a>
            </li>
          </ul>
        </li>
        <li class="dropdown-menu">
          <NavLink to="/team" class="/team">
            Team
            <img src={downArrowImg} />
          </NavLink>
          <ul class="dropdown">
            <li>
              <a href="{% url 'team' %}#collabarotors">Collabarotors</a>
            </li>
            <li>
              <a href="{% url 'team' %}#research_associates">
                Research associates
              </a>
            </li>
            <li>
              <a href="{% url 'team' %}#community_trainers">
                Community Trainers
              </a>
            </li>
            <li>
              <a href="{% url 'team' %}#intern">Intern</a>
            </li>
            <li>
              <a href="{% url 'team' %}#students">Students</a>
            </li>
          </ul>
        </li>
        <li>
          <NavLink to="/gallery">Gallery</NavLink>
        </li>
        <li class="dropdown-menu">
          <NavLink to="/casestudy">
            Case Studies
            <img src={downArrowImg} />
          </NavLink>
          <ul class="dropdown">
            <li>
              <a href="{% url 'case_studies' %}#case_study1">Case Study1</a>
            </li>
            <li>
              <a href="{% url 'case_studies' %}#case_study2">Case Study2</a>
            </li>
            <li>
              <a href="{% url 'case_studies' %}#case_study3">Case Study3</a>
            </li>
            <li>
              <a href="{% url 'case_studies' %}#case_study4">Case Study4</a>
            </li>
            <li>
              <a href="{% url 'case_studies' %}#case_study5">Case Study5</a>
            </li>
          </ul>
        </li>
      </ul>
      <div class="nav-right">
        <div class="dropdown-menu">
          <NavLink to="#" class="language">
            English
            <img src={downArrowImg} />
          </NavLink>
          <ul class="dropdown">
            <li class="case1">
              <a href="#">Hindi</a>
            </li>
            <li class="case2">
              <a href="#">Sinhali</a>
            </li>
            <li class="case2">
              <a href="#">Nepali</a>
            </li>
            <li class="case2">
              <a href="#">Japanese</a>
            </li>
          </ul>
        </div>
        <div
          className={`searchbar ${isActive ? "active" : ""}`}
          onClick={handleSearchClick}
        >
          <img src={searchImg} alt="search_icon" />
          <form>
            <input type="text" placeholder="Search" />
            <img src={cancelIcon} onClick={toggleActiveClass} />
          </form>
        </div>
      </div>
    </div>
  );
}

export default Base;
