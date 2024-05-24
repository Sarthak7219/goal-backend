import React,{ useEffect, useState } from "react";
import "./global.css";
import "./style.css";
import { NavLink } from "react-router-dom";
import { scrollSpy } from "./scrollSpy";

import iconImg from "../images/icon.png";
import profileImg from "../images/profile.jpeg"; // Import profile image
import resourceCardBg from "../images/Rectangle 5995.png"; // Import background image for member card
import harshitImg from "../images/harshit.jpeg"; // Import Harshit's image

function Team() {
  const [data, setData] = useState({
    resources: [],
    team_members: [],
    workshops: [],
    case_studies: [],
  });

  useEffect(() => {
    fetch('/api/combined-data/')
      .then(response => response.json())
      .then(data => setData(data))
      .catch(error => console.error('Error fetching data:', error));
  }, []);
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
            <NavLink to="/">Home</NavLink> / <NavLink to="/team">Team</NavLink>
          </p>
        </div>
        <img src={iconImg} alt="Icon" />
      </div>

      <div class="container">
        <div class="quick-link-box" id="team-sidebox">
          <a href="#collaborators" class="quicklink active">
            - Collaborators
          </a>
          <a href="#research_associates" class="quicklink">
            - Research Associates
          </a>
          <a href="#community_trainers" class="quicklink">
            - Community Trainers
          </a>
          <a href="#interns" class="quicklink">
            - Interns
          </a>
          <a href="#students" class="quicklink">
            - Students
          </a>
        </div>

        <div class="right" id="team-right">
          <section class="team" id="collaborators">
            <h2>Collaborators</h2>

            <div class="photo-container">
  {data.team_members
    .filter(team_member => team_member.category === 'collaborator')
    .map(team_member => (
      <div class="member-card" key={team_member.id}>
        <img
          src="/static/images/harshit.jpeg"
          class="member-img"
          alt=""
        />
        <img
          src="/static/images/Rectangle 5995.png"
          class="member-card-bg"
          alt=""
        />
        <div class="member-details">
          <h3>{team_member.name}</h3>
          <div class="member-line"></div>
          <p class="position">{team_member.position}</p>
          <p class="institute">{team_member.organisation}</p>
          <div class="social-icons">
            <i class="fa-regular fa-envelope" style={{ color: "#ec028c" }}></i>
            <i class="fa-brands fa-linkedin" style={{ color: "#ec028c" }}></i>
          </div>
        </div>
      </div>
    ))}
</div>
          </section>
          <section class="team" id="research_associates">
            <h2>Research Associates</h2>

            <div class="photo-container">
              <div class="member-card">
                <img
                  src="/static/images/harshit.jpeg"
                  class="member-img"
                  alt=""
                />
                <img
                  src="/static/images/Rectangle 5995.png"
                  class="member-card-bg
                        "
                  alt=""
                />
                <div class="member-details">
                  <h3>Dr. Harshit Sosan Lakra</h3>

                  <div class="member-line"></div>

                  <p class="position">Assistant Professor</p>
                  <p class="institute">
                    Indian Institute of Technology Roorkee, India
                  </p>

                  <div class="social-icons">
                    <i
                      class="fa-regular fa-envelope"
                      style={{ color: "#ec028c" }}
                    ></i>
                    <i
                      class="fa-brands fa-linkedin"
                      style={{ color: "#ec028c" }}
                    ></i>
                  </div>
                </div>
              </div>
              <div class="member-card">
                <img
                  src="/static/images/profile.jpeg"
                  class="member-img"
                  alt=""
                />
                <img
                  src="/static/images/Rectangle 5995.png"
                  class="member-card-bg
                        "
                  alt=""
                />
                <div class="member-details">
                  <h3>Name</h3>

                  <div class="member-line"></div>

                  <p class="position">Position</p>
                  <p class="institute">Institute</p>

                  <div class="social-icons">
                    <i
                      class="fa-regular fa-envelope"
                      style={{ color: "#ec028c" }}
                    ></i>
                    <i
                      class="fa-brands fa-linkedin"
                      style={{ color: "#ec028c" }}
                    ></i>
                  </div>
                </div>
              </div>
              <div class="member-card">
                <img
                  src="/static/images/profile.jpeg"
                  class="member-img"
                  alt=""
                />
                <img
                  src="/static/images/Rectangle 5995.png"
                  class="member-card-bg
                        "
                  alt=""
                />
                <div class="member-details">
                  <h3>Name</h3>

                  <div class="member-line"></div>

                  <p class="position">Position</p>
                  <p class="institute">Institute</p>

                  <div class="social-icons">
                    <i
                      class="fa-regular fa-envelope"
                      style={{ color: "#ec028c" }}
                    ></i>
                    <i
                      class="fa-brands fa-linkedin"
                      style={{ color: "#ec028c" }}
                    ></i>
                  </div>
                </div>
              </div>
            </div>
          </section>
          <section class="team" id="community_trainers">
            <h2>Community Trainers</h2>

            <div class="photo-container">
              <div class="member-card">
                <img
                  src="/static/images/harshit.jpeg"
                  class="member-img"
                  alt=""
                />
                <img
                  src="/static/images/Rectangle 5995.png"
                  class="member-card-bg
                        "
                  alt=""
                />
                <div class="member-details">
                  <h3>Dr. Harshit Sosan Lakra</h3>

                  <div class="member-line"></div>

                  <p class="position">Assistant Professor</p>
                  <p class="institute">
                    Indian Institute of Technology Roorkee, India
                  </p>

                  <div class="social-icons">
                    <a href="#">
                      <i
                        className="fa-regular fa-envelope"
                        style={{ color: "#ec028c" }}
                      ></i>
                    </a>
                    <a href="#">
                      <i
                        className="fa-brands fa-linkedin"
                        style={{ color: "#ec028c" }}
                      ></i>
                    </a>
                  </div>
                </div>
              </div>
              <div class="member-card">
                <img
                  src="/static/images/profile.jpeg"
                  class="member-img"
                  alt=""
                />
                <img
                  src="/static/images/Rectangle 5995.png"
                  class="member-card-bg
                        "
                  alt=""
                />
                <div class="member-details">
                  <h3>Name</h3>

                  <div class="member-line"></div>

                  <p class="position">Position</p>
                  <p class="institute">Institute</p>

                  <div class="social-icons">
                    <i
                      class="fa-regular fa-envelope"
                      style={{ color: "#ec028c" }}
                    ></i>
                    <i
                      class="fa-brands fa-linkedin"
                      style={{ color: "ec028c" }}
                    ></i>
                  </div>
                </div>
              </div>
              <div class="member-card">
                <img
                  src="/static/images/profile.jpeg"
                  class="member-img"
                  alt=""
                />
                <img
                  src="/static/images/Rectangle 5995.png"
                  class="member-card-bg
                        "
                  alt=""
                />
                <div class="member-details">
                  <h3>Name</h3>

                  <div class="member-line"></div>

                  <p class="position">Position</p>
                  <p class="institute">Institute</p>

                  <div class="social-icons">
                    <i
                      class="fa-regular fa-envelope"
                      style={{ color: "#ec028c" }}
                    ></i>
                    <i
                      class="fa-brands fa-linkedin"
                      style={{ color: "#ec028c" }}
                    ></i>
                  </div>
                </div>
              </div>
            </div>
          </section>
          <section class="team" id="interns">
            <h2>Interns</h2>

            <div class="photo-container">
              <div class="member-card">
                <img
                  src="/static/images/harshit.jpeg"
                  class="member-img"
                  alt=""
                />
                <img
                  src="/static/images/Rectangle 5995.png"
                  class="member-card-bg
                        "
                  alt=""
                />
                <div class="member-details">
                  <h3>Dr. Harshit Sosan Lakra</h3>

                  <div class="member-line"></div>

                  <p class="position">Assistant Professor</p>
                  <p class="institute">
                    Indian Institute of Technology Roorkee, India
                  </p>

                  <div class="social-icons">
                    <i
                      class="fa-regular fa-envelope"
                      style={{ color: "#ec028c" }}
                    ></i>
                    <i
                      class="fa-brands fa-linkedin"
                      style={{ color: "#ec028c" }}
                    ></i>
                  </div>
                </div>
              </div>
              <div class="member-card">
                <img
                  src="/static/images/profile.jpeg"
                  class="member-img"
                  alt=""
                />
                <img
                  src="/static/images/Rectangle 5995.png"
                  class="member-card-bg
                        "
                  alt=""
                />
                <div class="member-details">
                  <h3>Name</h3>

                  <div class="member-line"></div>

                  <p class="position">Position</p>
                  <p class="institute">Institute</p>

                  <div class="social-icons">
                    <i
                      class="fa-regular fa-envelope"
                      style={{ color: "#ec028c" }}
                    ></i>
                    <i
                      class="fa-brands fa-linkedin"
                      style={{ color: "#ec028c" }}
                    ></i>
                  </div>
                </div>
              </div>
              <div class="member-card">
                <img
                  src="/static/images/profile.jpeg"
                  class="member-img"
                  alt=""
                />
                <img
                  src="/static/images/Rectangle 5995.png"
                  class="member-card-bg
                        "
                  alt=""
                />
                <div class="member-details">
                  <h3>Name</h3>

                  <div class="member-line"></div>

                  <p class="position">Position</p>
                  <p class="institute">Institute</p>

                  <div class="social-icons">
                    <i
                      class="fa-regular fa-envelope"
                      style={{ color: "#ec028c" }}
                    ></i>
                    <i
                      class="fa-brands fa-linkedin"
                      style={{ color: "#ec028c" }}
                    ></i>
                  </div>
                </div>
              </div>
            </div>
          </section>
          <section class="team" id="students">
            <h2>Students</h2>

            <div class="photo-container">
              <div class="member-card">
                <img
                  src="/static/images/harshit.jpeg"
                  class="member-img"
                  alt=""
                />
                <img
                  src="/static/images/Rectangle 5995.png"
                  class="member-card-bg
                        "
                  alt=""
                />
                <div class="member-details">
                  <h3>Dr. Harshit Sosan Lakra</h3>

                  <div class="member-line"></div>

                  <p class="position">Assistant Professor</p>
                  <p class="institute">
                    Indian Institute of Technology Roorkee, India
                  </p>

                  <div class="social-icons">
                    <i
                      class="fa-regular fa-envelope"
                      style={{ color: "#ec028c" }}
                    ></i>
                    <i
                      class="fa-brands fa-linkedin"
                      style={{ color: "#ec028c" }}
                    ></i>
                  </div>
                </div>
              </div>
              <div class="member-card">
                <img
                  src="/static/images/profile.jpeg"
                  class="member-img"
                  alt=""
                />
                <img
                  src="/static/images/Rectangle 5995.png"
                  class="member-card-bg
                        "
                  alt=""
                />
                <div class="member-details">
                  <h3>Name</h3>

                  <div class="member-line"></div>

                  <p class="position">Position</p>
                  <p class="institute">Institute</p>

                  <div class="social-icons">
                    <i
                      class="fa-regular fa-envelope"
                      style={{ color: "#ec028c" }}
                    ></i>
                    <i
                      class="fa-brands fa-linkedin"
                      style={{ color: "#ec028c" }}
                    ></i>
                  </div>
                </div>
              </div>
              <div class="member-card">
                <img
                  src="/static/images/profile.jpeg"
                  class="member-img"
                  alt=""
                />
                <img
                  src="/static/images/Rectangle 5995.png"
                  class="member-card-bg
                        "
                  alt=""
                />
                <div class="member-details">
                  <h3>Name</h3>

                  <div class="member-line"></div>

                  <p class="position">Position</p>
                  <p class="institute">Institute</p>

                  <div class="social-icons">
                    <i
                      class="fa-regular fa-envelope"
                      style={{ color: "#ec028c" }}
                    ></i>
                    <i
                      class="fa-brands fa-linkedin"
                      style={{ color: "#ec028c" }}
                    ></i>
                  </div>
                </div>
              </div>
            </div>
          </section>
        </div>
      </div>
    </div>
  );
}

export default Team;
