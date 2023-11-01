import React from "react";
import BannerBackground from "../Assets/home-banner-background.png";
import BannerImage from "../Assets/home-banner-image.png";
import { FiArrowRight } from "react-icons/fi";

const Home = () => {
  return (
    <div className="home-container">
      <div className="home-banner-container">
        <div className="home-bannerImage-container">
          <img src={BannerBackground} alt="" />
        </div>
        <div className="home-text-section">
          <h1 className="primary-heading">
            Alimenta Ai!
          </h1>
          <p className="primary-text">
            Juntos, alimentamos o mundo com tecnologia e esperança, combatendo a fome com inovação.
          </p>
          <button className="secondary-button">
            Adquira Já! <FiArrowRight />{" "}
          </button>
          <br/>
          <button className="secondary-button">
            Doe! <FiArrowRight />{" "}
          </button>
        </div>
        <div className="home-image-section">
          <img src={BannerImage} alt="" />
        </div>
      </div>
    </div>
  );
};

export default Home;
