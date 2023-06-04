import React from "react";
import { Link } from "react-router-dom";
import BannerImage from "../assets/BannerImage1.png";
import "../styles/Home.css";

function Home() {
  return (
    <div className="home" style={{ backgroundImage: `url(${BannerImage})` }}>
      <div className="headerContainer">
        <h1> Alimenta Ai!</h1>
        <p>Juntos, alimentamos o mundo com tecnologia e esperança, combatendo a fome com inovação.</p>
        <Link to="/menu">
          <button className="button-home"> Venha Doar! </button>
        </Link>
        <Link to="/reserva">
          <button className="button-home2"> Faça sua reserva! </button>
        </Link>
      </div>
    </div>
  );
}

export default Home;
