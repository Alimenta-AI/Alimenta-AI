import React from "react";
import AboutBackground from "../Assets/about-background.png";
import AboutBackgroundImage from "../Assets/about-background-image.png";
import { BsFillPlayCircleFill } from "react-icons/bs";

const About = () => {
  return (
    <div className="about-section-container">
      <div className="about-background-image-container">
        <img src={AboutBackground} alt="" />
      </div>
      <div className="about-section-image-container">
        <img src={AboutBackgroundImage} alt="" />
      </div>
      <div className="about-section-text-container">
        <p className="primary-subheading">Sobre nós</p>
        <h1 className="primary-heading">
          Tecnologia que alimenta e apoia moradores de rua de forma inovadora.
        </h1>
        <p className="primary-text">
          O Alimenta-AI é um projeto inovador que utiliza inteligência artificial e tecnologia para fornecer suporte e acesso a alimentos adequados para pessoas em situação de rua. Por meio de uma plataforma digital interativa e totens nas ruas, oferecemos cardápios diários, informações nutricionais e programas de assistência, conectando doadores aos necessitados. 
        </p>
        <p className="primary-text">
          Nossa equipe está empenhada em construir uma sociedade mais justa, onde ninguém passe fome e todos tenham oportunidades para reconstruir suas vidas. Junte-se a nós nessa missão de fazer a diferença e inspirar mudanças positivas.
        </p>
        <div className="about-buttons-container">
          <button className="watch-video-button">
            <BsFillPlayCircleFill /> Assista o video!
          </button>
        </div>
      </div>
    </div>
  );
};

export default About;
