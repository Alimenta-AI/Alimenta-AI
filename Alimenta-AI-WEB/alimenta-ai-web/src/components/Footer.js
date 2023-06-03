import React from "react";
import InstagramIcon from "@material-ui/icons/Instagram";
import TwitterIcon from "@material-ui/icons/Twitter";
import FacebookIcon from "@material-ui/icons/Facebook";
import LinkedInIcon from "@material-ui/icons/LinkedIn";
import "../styles/Footer.css";
import {
Box,
Container,
Row,
Column,
FooterLink,
Heading,
} from "../styles/FooterStyles";

const Footer = () => {
return (
	<Box>
	<h1 style={{ color: "green",
				textAlign: "center",
				marginTop: "-50px" }}>
		Alimenta AI: Tecnologia que nutre, fome que desaparece
	</h1>
	<Container>
		<Row>
		<Column>
			<Heading>Sobre nós</Heading>
			<FooterLink href="#">Publico</FooterLink>
			<FooterLink href="#">Motivo</FooterLink>
			<FooterLink href="#">Como surgiu?</FooterLink>
		</Column>
		<Column>
			<Heading>Serviços</Heading>
			<FooterLink href="#">Doar</FooterLink>
			<FooterLink href="#">Receber</FooterLink>
			<FooterLink href="#">Cadastro</FooterLink>
		</Column>
		<Column>
			<Heading>Contate-nos</Heading>
			<FooterLink href="#">alimentaai@gmail.com</FooterLink>
			<FooterLink href="#">+55 (11) 98370-2045</FooterLink>
			<FooterLink href="#">+55 (11) 4002-8922</FooterLink>
		</Column>
		<Column>
			<Heading>Redes Sociais</Heading>
			<FooterLink href="#">
			<i className="fab fa-facebook-f">
				<span style={{ marginLeft: "10px" }}>
				  {/* <FacebookIcon/> */}Facebook
				</span>
			</i>
			</FooterLink>
			<FooterLink href="#">
			<i className="fab fa-instagram">
				<span style={{ marginLeft: "10px" }}>
          {/* <InstagramIcon/> */}Instagram 
				</span>
			</i>
			</FooterLink>
			<FooterLink href="#">
			<i className="fab fa-twitter">
				<span className="socialMedia" style={{ marginLeft: "10px" }}>
				  <TwitterIcon/>
				</span>
			</i>
			</FooterLink>
      {/* <FooterLink href="#">
			<i className="fab fa-linkedin">
				<span className="socialMedia" style={{ marginLeft: "10px" }}>
				  <LinkedInIcon/>
				</span>
			</i>
			</FooterLink> */}
		</Column>
		</Row>
	</Container>
	</Box>
);
};
export default Footer;
