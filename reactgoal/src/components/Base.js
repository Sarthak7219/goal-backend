import React from 'react'
import "./style.css";
import "./global.css";
import {NavLink} from "react-router-dom"

import logoImg from "../images/logo (2).png";
import downArrowImg from "../images/down.png";
import searchImg from "../images/search.png";
function Base() {
  return (
    <div class="navbar">
    <div class="goal-logo"><NavLink to="/"><img src={logoImg} alt="image" /></NavLink></div>
    <div class="navlist">
      <ul class="lists">
        <li class="about"><NavLink to="/about">About</NavLink></li>
        <li class="worshops"><NavLink to="/workshop">Workshops</NavLink></li>

        <li class="dropdown-menu">
          <NavLink to="/resources" class="Resources"
            >Resources<img src={downArrowImg}
          /></NavLink>
          <ul class="dropdown">
            <li class="case1"><NavLink to="#">Publications</NavLink></li>
            <li class="case2"><NavLink to="#">Training manuals</NavLink></li>
          </ul>
        </li>
        <li class="dropdown-menu">
          <NavLink to="/team" class="/team">Team<img src={downArrowImg} /></NavLink>
          <ul class="dropdown">
            <li class="case1"><NavLink to="#">Collabarotors</NavLink></li>
            <li class="case2"><NavLink to="#">Research associates</NavLink></li>
            <li class="case2"><NavLink to="#">Community Trainers</NavLink></li>
            <li class="case2"><NavLink to="#">Intern</NavLink></li>
            <li class="case2"><NavLink to="#">Students</NavLink></li>
          </ul>
        </li>
        <li class="Gallery"><NavLink to="/gallery">Gallery</NavLink></li>
        <li class="dropdown-menu">
          <NavLink to="/casestudy">Case Studies<img src={downArrowImg} /></NavLink>
          <ul class="dropdown">
            <li class="case1"><NavLink to="#">Case Study1</NavLink></li>
            <li class="case2"><NavLink to="#">Case Study2</NavLink></li>
            <li class="case3"><NavLink to="#">Case Study3</NavLink></li>
            <li class="case4"><NavLink to="#">Case Study4</NavLink></li>
            <li class="case5"><NavLink to="#">Case Study5</NavLink></li>
          </ul>
        </li>
      </ul>
    </div>
    <div class="lang">
      <li class="dropdown-menu">
        <NavLink to="#" class="language"
          >English<img src={downArrowImg}
        /></NavLink>
        <ul class="dropdown">
          <li class="case1"><NavLink to="#">Hindi</NavLink></li>
          <li class="case2"><NavLink to="#">Sinhali</NavLink></li>
          <li class="case2"><NavLink to="#">Nepali</NavLink></li>
          <li class="case2"><NavLink to="#">Japanese</NavLink></li>
        </ul>
      </li>
      <img src={searchImg} alt="" />
    </div>
  </div>
  )
}

export default Base