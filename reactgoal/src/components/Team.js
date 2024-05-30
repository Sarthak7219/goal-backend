import React, { useEffect } from "react";
import "./global.css";
import "./style.css";
import { NavLink } from "react-router-dom";
import { scrollSpy } from "./scrollSpy";

import iconImg from "../images/icon.png";
import profileImg from "../images/profile.jpeg"; // Import profile image
import resourceCardBg from "../images/Rectangle 5995.png"; // Import background image for member card

function Team({ team_members }) {
  useEffect(() => {
    const cleanup = scrollSpy();

    return () => {
      cleanup();
    };
  }, []);

  return (
    <div className="team-page">
      <div className="page-hero" id="team-bg">
        <div className="page-head">
          <h1>Our Team</h1>
          <p>
            <NavLink to="/" className="hero-link">
              Home
            </NavLink>{" "}
            /{" "}
            <NavLink to="/team" className="hero-link">
              Team
            </NavLink>
          </p>
        </div>
        <img src={iconImg} alt="Icon" />
      </div>

      <div className="container">
        <div className="quick-link-box" id="team-sidebox">
          <a href="#collaborators" className="quicklink active">
            - Collaborators
          </a>
          <a href="#research_associates" className="quicklink">
            - Research Associates
          </a>
          <a href="#community_trainers" className="quicklink">
            - Community Trainers
          </a>
          <a href="#interns" className="quicklink">
            - Interns
          </a>
          <a href="#students" className="quicklink">
            - Students
          </a>
        </div>

        <div className="right" id="team-right">
          <section className="team" id="collaborators">
            <h2>Collaborators</h2>

            <div className="photo-container">
              {team_members
                .filter(
                  (team_member) => team_member.category === "collaborator"
                )
                .map((team_member) => (
                  <NavLink
                    to={`/team-member-detail/${team_member.id}`}
                    key={team_member.id}
                  >
                    <div className="member-card">
                      <img
                        src={team_member.image}
                        className="member-img"
                        alt=""
                      />
                      <img
                        src={resourceCardBg}
                        className="member-card-bg"
                        alt=""
                      />
                      <div className="member-details">
                        <h3>{team_member.name}</h3>
                        <div className="member-line"></div>
                        <p className="position">{team_member.position}</p>
                        <p className="institute">{team_member.organisation}</p>
                        <div className="social-icons">
                          <i
                            className="fa-regular fa-envelope"
                            style={{ color: "#ec028c" }}
                          ></i>
                          <i
                            className="fa-brands fa-linkedin"
                            style={{ color: "#ec028c" }}
                          ></i>
                        </div>
                      </div>
                    </div>
                  </NavLink>
                ))}
            </div>
          </section>
          <section className="team" id="research_associates">
            <h2>Research Associates</h2>

            <div className="photo-container">
              {team_members
                .filter(
                  (team_member) =>
                    team_member.category === "research_associates"
                )
                .map((team_member) => (
                  <NavLink
                    to={`/team-member-detail/${team_member.id}`}
                    key={team_member.id}
                  >
                    <div className="member-card">
                      <img
                        src={team_member.image}
                        className="member-img"
                        alt=""
                      />
                      <img
                        src={resourceCardBg}
                        className="member-card-bg"
                        alt=""
                      />
                      <div className="member-details">
                        <h3>{team_member.name}</h3>
                        <div className="member-line"></div>
                        <p className="position">{team_member.position}</p>
                        <p className="institute">{team_member.organisation}</p>
                        <div className="social-icons">
                          <i
                            className="fa-regular fa-envelope"
                            style={{ color: "#ec028c" }}
                          ></i>
                          <i
                            className="fa-brands fa-linkedin"
                            style={{ color: "#ec028c" }}
                          ></i>
                        </div>
                      </div>
                    </div>
                  </NavLink>
                ))}
            </div>
          </section>
          <section className="team" id="community_trainers">
            <h2>Community Trainers</h2>

            <div className="photo-container">
              {team_members
                .filter(
                  (team_member) => team_member.category === "community_trainers"
                )
                .map((team_member) => (
                  <NavLink
                    to={`/team-member-detail/${team_member.id}`}
                    key={team_member.id}
                  >
                    <div className="member-card">
                      <img
                        src={team_member.image}
                        className="member-img"
                        alt=""
                      />
                      <img
                        src={resourceCardBg}
                        className="member-card-bg"
                        alt=""
                      />
                      <div className="member-details">
                        <h3>{team_member.name}</h3>
                        <div className="member-line"></div>
                        <p className="position">{team_member.position}</p>
                        <p className="institute">{team_member.organisation}</p>
                        <div className="social-icons">
                          <i
                            className="fa-regular fa-envelope"
                            style={{ color: "#ec028c" }}
                          ></i>
                          <i
                            className="fa-brands fa-linkedin"
                            style={{ color: "#ec028c" }}
                          ></i>
                        </div>
                      </div>
                    </div>
                  </NavLink>
                ))}
            </div>
          </section>
          <section className="team" id="interns">
            <h2>Interns</h2>

            <div className="photo-container">
              {team_members
                .filter((team_member) => team_member.category === "interns")
                .map((team_member) => (
                  <NavLink
                    to={`/team-member-detail/${team_member.id}`}
                    key={team_member.id}
                  >
                    <div className="member-card">
                      <img
                        src={team_member.image}
                        className="member-img"
                        alt=""
                      />
                      <img
                        src={resourceCardBg}
                        className="member-card-bg"
                        alt=""
                      />
                      <div className="member-details">
                        <h3>{team_member.name}</h3>
                        <div className="member-line"></div>
                        <p className="position">{team_member.position}</p>
                        <p className="institute">{team_member.organisation}</p>
                        <div className="social-icons">
                          <i
                            className="fa-regular fa-envelope"
                            style={{ color: "#ec028c" }}
                          ></i>
                          <i
                            className="fa-brands fa-linkedin"
                            style={{ color: "#ec028c" }}
                          ></i>
                        </div>
                      </div>
                    </div>
                  </NavLink>
                ))}
            </div>
          </section>
          <section className="team" id="students">
            <h2>Students</h2>

            <div className="photo-container">
              {team_members
                .filter((team_member) => team_member.category === "students")
                .map((team_member) => (
                  <NavLink
                    to={`/team-member-detail/${team_member.id}`}
                    key={team_member.id}
                  >
                    <div className="member-card">
                      <img
                        src={team_member.image}
                        className="member-img"
                        alt=""
                      />
                      <img
                        src={resourceCardBg}
                        className="member-card-bg"
                        alt=""
                      />
                      <div className="member-details">
                        <h3>{team_member.name}</h3>
                        <div className="member-line"></div>
                        <p className="position">{team_member.position}</p>
                        <p className="institute">{team_member.organisation}</p>
                        <div className="social-icons">
                          <i
                            className="fa-regular fa-envelope"
                            style={{ color: "#ec028c" }}
                          ></i>
                          <i
                            className="fa-brands fa-linkedin"
                            style={{ color: "#ec028c" }}
                          ></i>
                        </div>
                      </div>
                    </div>
                  </NavLink>
                ))}
            </div>
          </section>
        </div>
      </div>
    </div>
  );
}

export default Team;
