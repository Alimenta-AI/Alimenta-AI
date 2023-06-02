import React from "react";
import "./Footer.css";

function Footer() {
  return (
    <div className="main-footer">
      <div className="container">
        <div className="row">
          <div className="col">
            <h4>THICC MEMES INC</h4>
            <h1 className="contact-info">
              <li>342-420-6969</li>
              <li>Moscow, Russia</li>
              <li>123 Streeet South North</li>
            </h1>
          </div>
          <div className="col">
            <h4>Stuff</h4>
            <ul className="list-unstyled"> {/* Corrigido de 'ui' para 'ul' */}
              <li>DANK MEMES</li>
              <li>OTHER STUFF</li>
              <li>GUD STUFF</li>
            </ul>
          </div>
          <div className="col">
            <h4>WELL ANOTHER COLUMN</h4>
            <ul className="list-unstyled"> {/* Corrigido de 'ui' para 'ul' */}
              <li>DANK MEMES</li>
              <li>OTHER STUFF</li>
              <li>GUD STUFF</li>
            </ul>
          </div>
        </div>
      </div>
      <hr />
      <div className="container">
        <div className="row">
          <p className="col-sm">
            &copy;{new Date().getFullYear()} THICC MEMES | All rights reserved |
            Terms Of Service | Privacy
          </p>
        </div>
      </div>
    </div>
  );
}

export default Footer;
