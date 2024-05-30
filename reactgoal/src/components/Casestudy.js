import React from "react";
import iconImg from "../images/icon.png";
import "./global.css";
import "./style.css";
import { NavLink } from "react-router-dom";
import { scrollSpy } from "./scrollSpy";
import { useEffect } from "react";

function Casestudy({ case_studies }) {
  useEffect(() => {
    const cleanup = scrollSpy();

    return () => {
      cleanup();
    };
  }, []);

  return (
    <div class="casestudy-page">
      <div class="page-hero" id="case_studies-bg">
        <div class="page-head">
          <h1>Case Studies</h1>
          <p>
            {" "}
            <NavLink to="/" className="hero-link">
              Home
            </NavLink>{" "}
            /{" "}
            <NavLink to="/casestudy" className="hero-link">
              Case Studies
            </NavLink>
          </p>
        </div>
        <img src={iconImg} alt="" />
      </div>

      <div class="container" id="case_studies">
        <div class="quick-link-box" id="case_studies-sidebox">
          <a href="#case-study-1" class="quicklink active">
            - Case-study-1
          </a>
          <a href="#case-study-2" class="quicklink active">
            - Case-study-2
          </a>
          <a href="#case-study-3" class="quicklink active">
            - Case-study-3
          </a>
          <a href="#case-study-4" class="quicklink active">
            - Case-study-4
          </a>
          <a href="#case-study-5" class="quicklink active">
            - Case-study-5
          </a>
        </div>

        <div className="right" id="case_studies-right">
          <section className="case_studies" id="case-study-1">
            <h1>Case Study-1</h1>
            <p>
              Project Goal attempts to tap adaptive transformations
              (collaborative learning) for Climate Change (CC1&amp; Disaster
              Risk Reduction (DRR) &amp; enhance research &amp; communication
              capacities of the men, women, and youths in their context by
              Training the Community Trainers (ToCT) &amp; developing training
              resources &amp; community-friendly tools for comprehensive
              outreach through an innovative approach.
              <br />
              <br />
              The collaborative case studies are based on scientific research
              and will be developed in- 1. India-Udham Singh Nagar District,
              Uttarakhand. Dumka, Aspirant District harkhand and Bishnupur
              District, Manipur
              <br />
              <br />
              2. Nepal-Chitwan District, Bagmati Province
              <br />
              <br />
              3. Sri Lanka- Gampaha District. Western Province
              <br />
              <br />
              4. Japan- literature-based case study and expert, stakeholders,
              and community inputs through hybrid mode
            </p>
          </section>
          <section className="case_studies" id="case-study-2">
            <h1>Case Study-2</h1>
            <p>
              Project Goal attempts to tap adaptive transformations
              (collaborative learning) for Climate Change (CC1&amp; Disaster
              Risk Reduction (DRR) &amp; enhance research &amp; communication
              capacities of the men, women, and youths in their context by
              Training the Community Trainers (ToCT) &amp; developing training
              resources &amp; community-friendly tools for comprehensive
              outreach through an innovative approach.
              <br />
              <br />
              The collaborative case studies are based on scientific research
              and will be developed in- 1. India-Udham Singh Nagar District,
              Uttarakhand. Dumka, Aspirant District harkhand and Bishnupur
              District, Manipur
              <br />
              <br />
              2. Nepal-Chitwan District, Bagmati Province
              <br />
              <br />
              3. Sri Lanka- Gampaha District. Western Province
              <br />
              <br />
              4. Japan- literature-based case study and expert, stakeholders,
              and community inputs through hybrid mode
            </p>
          </section>
          <section className="case_studies" id="case-study-3">
            <h1>Case Study-3</h1>
            <p>
              Project Goal attempts to tap adaptive transformations
              (collaborative learning) for Climate Change (CC1&amp; Disaster
              Risk Reduction (DRR) &amp; enhance research &amp; communication
              capacities of the men, women, and youths in their context by
              Training the Community Trainers (ToCT) &amp; developing training
              resources &amp; community-friendly tools for comprehensive
              outreach through an innovative approach.
              <br />
              <br />
              The collaborative case studies are based on scientific research
              and will be developed in- 1. India-Udham Singh Nagar District,
              Uttarakhand. Dumka, Aspirant District harkhand and Bishnupur
              District, Manipur
              <br />
              <br />
              2. Nepal-Chitwan District, Bagmati Province
              <br />
              <br />
              3. Sri Lanka- Gampaha District. Western Province
              <br />
              <br />
              4. Japan- literature-based case study and expert, stakeholders,
              and community inputs through hybrid mode
            </p>
          </section>
          <section className="case_studies" id="case-study-4">
            <h1>Case Study-4</h1>
            <p>
              Project Goal attempts to tap adaptive transformations
              (collaborative learning) for Climate Change (CC1&amp; Disaster
              Risk Reduction (DRR) &amp; enhance research &amp; communication
              capacities of the men, women, and youths in their context by
              Training the Community Trainers (ToCT) &amp; developing training
              resources &amp; community-friendly tools for comprehensive
              outreach through an innovative approach.
              <br />
              <br />
              The collaborative case studies are based on scientific research
              and will be developed in- 1. India-Udham Singh Nagar District,
              Uttarakhand. Dumka, Aspirant District harkhand and Bishnupur
              District, Manipur
              <br />
              <br />
              2. Nepal-Chitwan District, Bagmati Province
              <br />
              <br />
              3. Sri Lanka- Gampaha District. Western Province
              <br />
              <br />
              4. Japan- literature-based case study and expert, stakeholders,
              and community inputs through hybrid mode
            </p>
          </section>
          <section className="case_studies" id="case-study-5">
            <h1>Case Study-5</h1>
            <p>
              Project Goal attempts to tap adaptive transformations
              (collaborative learning) for Climate Change (CC1&amp; Disaster
              Risk Reduction (DRR) &amp; enhance research &amp; communication
              capacities of the men, women, and youths in their context by
              Training the Community Trainers (ToCT) &amp; developing training
              resources &amp; community-friendly tools for comprehensive
              outreach through an innovative approach.
              <br />
              <br />
              The collaborative case studies are based on scientific research
              and will be developed in- 1. India-Udham Singh Nagar District,
              Uttarakhand. Dumka, Aspirant District harkhand and Bishnupur
              District, Manipur
              <br />
              <br />
              2. Nepal-Chitwan District, Bagmati Province
              <br />
              <br />
              3. Sri Lanka- Gampaha District. Western Province
              <br />
              <br />
              4. Japan- literature-based case study and expert, stakeholders,
              and community inputs through hybrid mode
            </p>
          </section>
        </div>
      </div>
    </div>
  );
}

export default Casestudy;
