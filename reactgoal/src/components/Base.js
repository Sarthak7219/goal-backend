import React from 'react'
import "./style.css";
import "./global.css";


import logoImg from "../images/logo (2).png";
import downArrowImg from "../images/down.png";
import searchImg from "../images/search.png";
function Base() {
  return (
    <div class="navbar">
    <div class="goal-logo"><a href="/"><img src={logoImg} alt="image" /></a></div>
    <div class="navlist">
      <ul class="lists">
        <li class="about"><a href="/about">About</a></li>
        <li class="worshops"><a href="/workshop">Workshops</a></li>

        <li class="dropdown-menu">
          <a href="/resources" class="Resources"
            >Resources<img src={downArrowImg}
          /></a>
          <ul class="dropdown">
            <li class="case1"><a href="#">Publications</a></li>
            <li class="case2"><a href="#">Training manuals</a></li>
          </ul>
        </li>
        <li class="dropdown-menu">
          <a href="/team" class="/team">Team<img src={downArrowImg} /></a>
          <ul class="dropdown">
            <li class="case1"><a href="#">Collabarotors</a></li>
            <li class="case2"><a href="#">Research associates</a></li>
            <li class="case2"><a href="#">Community Trainers</a></li>
            <li class="case2"><a href="#">Intern</a></li>
            <li class="case2"><a href="#">Students</a></li>
          </ul>
        </li>
        <li class="Gallery"><a href="/gallery">Gallery</a></li>
        <li class="dropdown-menu">
          <a href="/casestudy">Case Studies<img src={downArrowImg} /></a>
          <ul class="dropdown">
            <li class="case1"><a href="#">Case Study1</a></li>
            <li class="case2"><a href="#">Case Study2</a></li>
            <li class="case3"><a href="#">Case Study3</a></li>
            <li class="case4"><a href="#">Case Study4</a></li>
            <li class="case5"><a href="#">Case Study5</a></li>
          </ul>
        </li>
      </ul>
    </div>
    <div class="lang">
      <li class="dropdown-menu">
        <a href="#" class="language"
          >English<img src={downArrowImg}
        /></a>
        <ul class="dropdown">
          <li class="case1"><a href="#">Hindi</a></li>
          <li class="case2"><a href="#">Sinhali</a></li>
          <li class="case2"><a href="#">Nepali</a></li>
          <li class="case2"><a href="#">Japanese</a></li>
        </ul>
      </li>
      <img src={searchImg} alt="" />
    </div>
  </div>
  )
}

export default Base