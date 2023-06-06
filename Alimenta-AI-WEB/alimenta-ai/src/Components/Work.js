import React from "react";
import PickMeals from "../Assets/pick-meals-image.png";
import ChooseMeals from "../Assets/choose-image.png";
import DeliveryMeals from "../Assets/delivery-image.png";

const Work = () => {
  const workInfoData = [
    {
      image: PickMeals,
      title: "Escolha Refeições Saudáveis",
      text: "Uma seleção de refeições saudáveis e nutritivas está à sua disposição. Escolha dentre nosso diversificado menu para apoiar o seu bem-estar.",
    },
    {
      image: ChooseMeals,
      title: "Personalize seu Plano de Refeições",
      text: "Adapte o seu plano de refeições de acordo com suas necessidades e preferências. Aproveite a flexibilidade de escolher suas refeições e a frequência de recebê-las.",
    },
    {
      image: DeliveryMeals,
      title: "Entregas Rápidas e Confiáveis",
      text: "Você pode contar conosco para entregas pontuais e confiáveis. Nos empenhamos para garantir que suas refeições sejam entregues frescas e no horário certo, proporcionando conveniência e tranquilidade.",
    },
  ];
  return (
    <div className="work-section-wrapper">
      <div className="work-section-top">
        <p className="primary-subheading">Alimente-se</p>
        <h1 className="primary-heading">Como nós trabalhamos?</h1>
        <p className="primary-text">
          Fornecemos suporte efetivo aos moradores de rua por meio de uma plataforma digital interativa, alimentada pela inteligência artificial. Nosso foco é garantir acesso a alimentos adequados e programas de assistência, além de facilitar a conexão entre doadores e aqueles em necessidade. Com uma equipe dedicada, estamos comprometidos em fazer a diferença e construir um futuro melhor para os mais vulneráveis
        </p>
      </div>
      <div className="work-section-bottom">
        {workInfoData.map((data) => (
          <div className="work-section-info" key={data.title}>
            <div className="info-boxes-img-container">
              <img src={data.image} alt="" />
            </div>
            <h2>{data.title}</h2>
            <p>{data.text}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Work;
