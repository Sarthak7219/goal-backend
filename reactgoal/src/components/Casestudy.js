import React from "react";
import iconImg from "../images/icon.png";
import "./global.css";
import "./style.css";
import { NavLink } from "react-router-dom";
function Casestudy() {
  return (
    <div class="casestudy-page">
      <div class="page-hero" id="case_studies-bg">
        <div class="page-head">
          <h1>Case Studies</h1>
          <p>
            {" "}
            <NavLink to="/">Home</NavLink> /{" "}
            <NavLink to="/casestudy">Case Studies</NavLink>
          </p>
        </div>
        <img src={iconImg} alt="" />
      </div>

      <div class="container" id="case_studies">
        <div class="quick-link-box" id="case_studies-sidebox">
          {/* {% for case_study in case_study_data %}
            <a href="#case-study-{{ forloop.counter }}" class="quicklink active">- Case-study-{{ forloop.counter }}</a>
            {% endfor %} */}
        </div>

        <div class="right" id="case_studies-right">
          {/* {% for case_study in case_study_data %} */}

          <section class="case_studies" id="case-study-{{ forloop.counter }}">
            {/* <h1>Case-study-{{ forloop.counter }}</h1>
                <p>{{case_study.description | safe}}</p> */}
          </section>

          {/* {% empty %} */}
          <h3>No Case sutdies found!</h3>
          {/* {% endfor %} */}
        </div>
      </div>
    </div>
  );
}

export default Casestudy;
