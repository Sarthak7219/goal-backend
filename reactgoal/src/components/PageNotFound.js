import React from "react";
import "./global.css";
import "./style.css";
import NotFoundImg from "../images/404.png";
import { NavLink } from "react-router-dom";

function PageNotFound() {
  return (
    <div class="page_404">
      <img src={NotFoundImg} alt="" />

      <NavLink to="/">
        <h3>Back To Home</h3>
      </NavLink>
    </div>
  );
}

export default PageNotFound;
