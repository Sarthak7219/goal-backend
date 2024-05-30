import React, { useEffect, useState } from "react";

import "./global.css";
import "./style.css";
import { useParams } from "react-router-dom";

function ProfileDetail({ team_members }) {
  const { id } = useParams();
  const [profile, setProfile] = useState(null);

  useEffect(() => {
    const selectedProfile = team_members.find(
      (profile) => profile.id === parseInt(id)
    );
    setProfile(selectedProfile);
  }, [id, team_members]);

  if (!profile) {
    return <div>Profile not found</div>;
  }

  return (
    <div className="profile-detail-container">
      <div className="page-hero" id="profile-bg">
        <img src="/static/images/icon.svg" alt="" />
      </div>
      <div className="name-section">
        <img src={profile.image} alt="" />
        <div className="profile-heading">
          <h2>{profile.name}</h2>
          <h5>{profile.organisation}</h5>
          <p>{profile.position}</p>
        </div>
      </div>
      <div className="detail-section">
        <div className="imp-detail">
          <ul>
            <li>
              <h4>Country</h4>
              <p>{profile.country}</p>
            </li>
            <li>
              <h4>Organisation</h4>
              <p>{profile.organisation}</p>
            </li>
            <li>
              <h4>Email</h4>
              <p>{profile.email}</p>
            </li>
            <li>
              <h4>Contact</h4>
              <p>{profile.contact}</p>
            </li>
          </ul>
        </div>
        <div className="detail-desc">{profile.description}</div>
      </div>
    </div>
  );
}

export default ProfileDetail;
