import React from 'react';
import './App.css';
import { useRef } from 'react';
import Home from './components/Home';
import Base from './components/Base';
import Footer from './components/Footer';
import Workshop from './components/Workshop';
import Gallery from './components/Gallery';
import Team from './components/Team';
import Resources from './components/Resources';
import Casestudy from './components/Casestudy';
import About from './components/About';
import { Routes, Route } from 'react-router-dom';

function App() {
  return (
    <div className="App">
      <Base />
 
      <Routes>
      
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/workshop" element={<Workshop />} />
        <Route path="/gallery" element={<Gallery />} />
        <Route path="/resources" element={<Resources />} />
        <Route path="/casestudy" element={<Casestudy />} />
        <Route path="/team" element={<Team />} />
      </Routes>
      <Footer />
    </div>
  );
}

export default App;
