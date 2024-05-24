import React from "react";
import gallery5Img from "../images/gallery/gallery5.png";
import image1Img from "../images/gallery/image1.jpg";
import image2Img from "../images/gallery/image2.jpg";
import image3Img from "../images/gallery/image3.jpg";
import image4Img from "../images/gallery/image4.jpg";
import image5Img from "../images/gallery/image5.jpg";
import image6Img from "../images/gallery/image6.jpg";
import image7Img from "../images/gallery/image7.jpg";
import image8Img from "../images/gallery/image8.jpg";
import iconImg from "../images/icon.png";
import underlineImg from "../images/underlineimg.png";
import "./global.css";
import "./style.css";
import "./main.js";

function Gallery() {
  return (
    <div class="gallery-page">
      <div class="page-hero" id="gallery-bg">
        <div class="page-head">
          <h1>Photo Gallery</h1>
          <p>
            <a href="{% url 'home' %}">Home</a> / <a href="">Gallery</a>
          </p>
        </div>
        <img src={iconImg} alt="" />
      </div>

      <div class="container">
        <div class="quick-link-box" id="gallery-sidebox">
          <a href="#case1-gal" class="quicklink active">
            - Case Study-1
          </a>
          <a href="#case2-gal" class="quicklink">
            - Case Study-2
          </a>
          <a href="#case3-gal" class="quicklink">
            - Case Study-3
          </a>
          <a href="#case4-gal" class="quicklink">
            - Case Study-4
          </a>
          <a href="#case5-gal" class="quicklink">
            - Case Study-5
          </a>
        </div>

        <div class="right" id="gallery-right">
          <section class="gallery">
            <div class="section-head2">
              <h1>Case Study-1</h1>
              <div></div>
            </div>

            <div class="photo-container gallery-container">
              <div
                className="gallery-box"
                style={{ backgroundImage: `url(${gallery5Img})` }}
              ></div>
              <div
                className="gallery-box"
                id="two-col"
                style={{ backgroundImage: `url(${image1Img})` }}
              ></div>
              <div
                className="gallery-box"
                id="onehalf-row"
                style={{ backgroundImage: `url(${image2Img})` }}
              ></div>
              <div
                className="gallery-box"
                style={{ backgroundImage: `url(${image3Img})` }}
              ></div>
              <div
                className="gallery-box"
                style={{ backgroundImage: `url(${image4Img})` }}
              ></div>
              <div
                className="gallery-box"
                style={{ backgroundImage: `url(${image5Img})` }}
              ></div>
              <div
                className="gallery-box"
                id="two-row"
                style={{ backgroundImage: `url(${image6Img})` }}
              ></div>
              <div
                className="gallery-box"
                id="two-col"
                style={{ backgroundImage: `url(${image7Img})` }}
              ></div>
              <div
                className="gallery-box"
                style={{ backgroundImage: `url(${image8Img})` }}
              ></div>
            </div>

            <div class="page-number-wrapper">
              <div>1</div>
              <div>2</div>
              <div>3</div>
              <div>4</div>
            </div>
          </section>
        </div>
      </div>
    </div>
  );
}

export default Gallery;
