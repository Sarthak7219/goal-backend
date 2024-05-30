import React from "react";
import iconImg from "../images/icon.png";
import "./global.css";
import "./style.css";
import { NavLink } from "react-router-dom";
import { scrollSpy } from "./scrollSpy";
import { useEffect } from "react";

function About() {
  useEffect(() => {
    const cleanup = scrollSpy();

    return () => {
      cleanup();
    };
  }, []);

  return (
    <div className="About-page">
      <div className="page-hero" id="about-bg">
        <div className="page-head">
          <h1>About The Project</h1>
          <p>
            <NavLink to="/" className="hero-link">
              Home
            </NavLink>{" "}
            /{" "}
            <NavLink to="/about" className="hero-link">
              About
            </NavLink>
          </p>
        </div>
        <img src={iconImg} alt="icon" />
      </div>

      <div className="container" id="about">
        <div className="quick-link-box" id="about-sidebox">
          <a href="#abstract" className="quicklink active">
            - Abstract
          </a>
          <a href="#description" className="quicklink">
            - Description
          </a>
        </div>

        <div className="right" id="about-right">
          <section className="about" id="abstract">
            <h1>Abstract</h1>
            <p>
              Project Goal attempts to tap adaptive transformations
              (collaborative learning) for Climate Change (CC1& Disaster Risk
              Reduction (DRR) & enhance research & communication capacities of
              the men, women, and youths in their context by Training the
              Community Trainers (ToCT) & developing training resources &
              community-friendly tools for comprehensive outreach through an
              innovative approach.
              <br></br>
              The collaborative case studies are based on scientific research
              and will be developed in- 1. India-Udham Singh Nagar District,
              Uttarakhand. Dumka, Aspirant District harkhand and Bishnupur
              District, Manipur
              <br></br>
              2. Nepal-Chitwan District, Bagmati Province
              <br></br>
              3. Sri Lanka- Gampaha District. Western Province
              <br></br>
              4. Japan- literature-based case study and expert, stakeholders,
              and community inputs through hybrid mode
            </p>
          </section>
          <section className="about" id="description">
            <h1>Description</h1>
            <p>
              GOAL project creates a focused space for co-designing &
              co-learning of global research from aligned domains from different
              APN countries (India, Nepal. Sn Lanka & Japan) on gender-sensitive
              adaptive transformation (collaborative learning) in CCA & DRR
              Capacity for collaborative learning is fundamental "to environment
              &resource management & sustainability science as it provides a
              foundation for "Joint-action required to respond to
              social-ecological feedback
              <br></br>
              Often capacity to resolve thungs on the ground is fimited due to
              the limited capacity for co-learning at different levels of
              individuals, organizations, &cinstitutions. Moreover there are
              'power differentials & varying "status" which mfluence the
              communities capacity willingness to learn &take action, including
              "className, gender, values, expectations &aspinations &ethimeity
              <br></br>
              Key adaptive transformation, this project focuses, is the capacity
              of individuals, organizations, &societies to collaboratively Icam
              through co-designing, co-research, &co-cross learning, to address
              CCA &DRR Individual men women, &youth's perceptions & behaviour
              can be altered by observation, reflection & critical engagement
              Icading to openness to iudeas, joint action, policy interventions
              <br></br>
              The aim is to enhance communities ability to identify problems
              &solutions, develop strategies, generate meaningful information
              communicate, &participare in decision-making with real-life
              situations in the context of CCA &DRR at a multiscale learning
              platform connecting communities horizontally (local organization
              to local organization) & vertically (local, regional, national)
              <br></br>
              The project creates a multiple-loop learning framework connects
              the groups, fosters know lodge synthesis, Senhances opportunities
              for learning with shortened feedback loops bringing long-term
              transformations The project builds learning by doing case studies
              from diverse contexts through its inbuilt learning structure of
              co-design, co-ersearch, &co-cross learning to strengthen women's
              collaborative learning capacity, wormew leaf. &capacity to act
              along with men &yoth through the Training of Community Trainers
              (ToT), especially wrown risk. Case studies provide evidence-based
              knowledge material for self-ochance. bener undresinfing, &
              improved communication, & create awarenes & dimanation of
              knowledge.
            </p>
          </section>
        </div>
      </div>
    </div>
  );
}

export default About;
