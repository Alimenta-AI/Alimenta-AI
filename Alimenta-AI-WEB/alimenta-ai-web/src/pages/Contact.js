import React from "react";
import "../styles/Contact.css";
import twitter from '../assets/twiter.png';
import facebook from '../assets/fecebook.png';
import instagram from '../assets/instagram.png';

function Contact() {
  return (
    <div className="contact">
      <div className="leftSide">
        <div className="socialMedia">
          <div className="socialMediaItem">
            <img src={facebook} alt="Facebook" />
            <span>@facebook</span>
          </div>
          <div className="socialMediaItem">
            <img src={instagram} alt="Instagram" />
            <span>@instagram</span>
          </div>
          <div className="socialMediaItem">
            <img className="twitter" src={twitter} alt="Twitter" />
            <span>@twitter</span>
          </div>
        </div>
      </div>
      <div className="rightSide">
        <h1> Contact Us</h1>
        <form id="contact-form" method="POST">
          <label htmlFor="name">Full Name</label>
          <input name="name" placeholder="Enter full name..." type="text" />
          <label htmlFor="email">Email</label>
          <input name="email" placeholder="Enter email..." type="email" />
          <label htmlFor="message">Message</label>
          <textarea rows="6" placeholder="Enter message..." name="message" required></textarea>
          <button type="submit"> Send Message</button>
        </form>
      </div>
    </div>
  );
}

export default Contact;
