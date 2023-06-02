import React from "react";
import { Link } from "react-router-dom";
import BannerImage from "../assets/pizza.jpeg";
import "../styles/Home.css";

function Home() {
  return (
      <div className="headerContainer">
        <h1> Alimenta Ai!</h1>
        <p>Juntos, alimentamos o mundo com tecnologia e esperança, combatendo a fome com inovação.</p>
        <Link to="/menu">
          <button> Venha! </button>
        </Link>
      </div>
  );
}

export default Home;
