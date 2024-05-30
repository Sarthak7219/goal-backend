import React from "react";
import "./global.css";
import "./style.css";

import archdeptImg from "../images/archdept.png";
import footerLogo from "../images/footer-logo.svg";
function Footer() {
  return (
    <div>
      <div class="footer">
        <div class="footer-content">
          <div class="footer-body">
            <div class="project-name">
              <div class="heading">
                <img src={footerLogo} alt="" />
                <p>An initiative by IIT Roorkee</p>
              </div>
              <h3>APN funded project IIT Roorkee</h3>
              <p>APN</p>
              <p>IIT Roorkee</p>
            </div>
            <div class="quicklinks">
              <h4>Quick Link</h4>
              <p>Home</p>
              <p>Workshops</p>
              <p>Team</p>
              <p>gallery</p>
              <p>About</p>
              <p>Case Studies</p>
            </div>
            <div class="get-in-touch">
              <h4>Get In Touch</h4>
              <p>+91-1332-23124</p>
              <p>example@gmail.com</p>
            </div>
            <div class="address">
              <h4>Get In Touch</h4>
              <p>
                Department of Architecture and Planning, Indian Institute of
                Technology (IIT), Roorkee Uttarakhand- 247667, India
              </p>
            </div>
            <div class="dept-img">
              <h2>
                Department Of Architecture and Planning,
                <span>IIT Roorkee</span>
              </h2>
              <img
                src={archdeptImg}
                alt=""
                width="216.21px"
                height="193.21px"
              />
            </div>
          </div>

          <p>Website credits-@Tinky&@Sarthak</p>
        </div>
      </div>
    </div>
  );
}

export default Footer;
