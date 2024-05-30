import React, { useEffect, useState } from "react";
import "./App.css";
import Home from "./components/Home";
import Base from "./components/Base";
import Footer from "./components/Footer";
import WorkshopDetail from "./components/WorkshopDetail";
import WorkshopList from "./components/WorkshopList";
import Gallery from "./components/Gallery";
import Team from "./components/Team";
import ProfileDetail from "./components/ProfileDetail";
import Resources from "./components/Resources";
import Casestudy from "./components/Casestudy";
import About from "./components/About";
import SearchPage from "./components/SearchPage";
import PageNotFound from "./components/PageNotFound";
import { Routes, Route } from "react-router-dom";

function App() {
  const [data, setData] = useState({
    resources: [],
    team_members: [],
    workshops: [],
    case_studies: [],
  });

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/combined-data/")
      .then((response) => response.json())
      .then((data) => setData(data))
      .catch((error) => console.error("Error fetching data:", error));
  }, []);

  return (
    <div className="App">
      <Base />

      <Routes>
        <Route path="/" element={<Home data={data} />} />

        <Route path="/about" element={<About />} />

        <Route
          path="/workshops"
          element={<WorkshopList workshops={data.workshops} />}
        />

        <Route
          path="/workshops/workshop-detail/:id"
          element={<WorkshopDetail workshops={data.workshops} />}
        />

        <Route path="/gallery" element={<Gallery />} />

        <Route
          path="/resources"
          element={<Resources resources={data.resources} />} // Pass props here
        />

        <Route
          path="/casestudy"
          element={<Casestudy case_studies={data.case_studies} />}
        />

        <Route
          path="/team"
          element={<Team team_members={data.team_members} />}
        />

        <Route
          path="/team-member-detail/:id"
          element={<ProfileDetail team_members={data.team_members} />}
        />

        <Route path="/search" element={<SearchPage />} />

        <Route path="*" element={<PageNotFound />} />
      </Routes>

      <Footer />
    </div>
  );
}

export default App;
