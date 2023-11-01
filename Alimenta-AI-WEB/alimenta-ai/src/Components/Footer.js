import React from "react";
import Logo from "../Assets/alimentaAi.png";
import { BsTwitter } from "react-icons/bs";
import { SiLinkedin } from "react-icons/si";
import { BsYoutube } from "react-icons/bs";
import { FaFacebookF } from "react-icons/fa";
import { Link } from "react-router-dom";

const Footer = () => {
  return (
    <div className="footer-wrapper">
      <div className="footer-content">
        <div className="footer-section-one">
          <div className="footer-logo-container">
            <img src={Logo} alt="" />
          </div>
          <div className="footer-icons">
            <ul>
              <li>
                <button style={{ background: "none", border: "none" }}>
                  <BsTwitter />
                </button>
              </li>
              <li>
                <button style={{ background: "none", border: "none" }}>
                  <SiLinkedin />
                </button>
              </li>
              <li>
                <button style={{ background: "none", border: "none" }}>
                  <BsYoutube />
                </button>
              </li>
              <li>
                <button style={{ background: "none", border: "none" }}>
                  <FaFacebookF />
                </button>
              </li>
            </ul>
          </div>
        </div>
        <div className="footer-section-two">
          <div className="footer-section-columns">
            <span className="span-footer">
              <Link to="/doe">Quero Ajudar!</Link>
            </span>
            <span className="span-footer">
              <Link to="/sobre">Sobre</Link>
            </span>
            <span className="span-footer">
              <Link to="/testemunhos">Testemunhos</Link>
            </span>
            <span className="span-footer">
              <Link to="/trabalho">Trabalho</Link>
            </span>
            <span className="span-footer">
              <Link to="/contato">Contato</Link>
            </span>
          </div>
          <div className="footer-section-columns">
            <span>+55 (11) 97320-9008</span>
            <span>alimentaai@gmail.com</span>
          </div>
          <div className="footer-section-columns">
            <span>Termos & Condições</span>
            <span>Política de Privacidade</span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Footer;
