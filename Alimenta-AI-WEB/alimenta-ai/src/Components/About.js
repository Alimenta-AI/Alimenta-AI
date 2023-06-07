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
        <h1 className="primary-heading-about">
          Tecnologias inovadoras e distribuição de alimentos: combatendo a fome e promovendo a sustentabilidade
        </h1>
        <p className="primary-text-about">
          As tecnologias inovadoras, como as IAs generativas, têm o potencial de ajudar no combate à fome mundial e à escassez de alimentos. Essas IAs podem ser aplicadas na otimização da produção agrícola, auxiliando os agricultores na tomada de decisões informadas sobre plantio, uso de fertilizantes e manejo de pragas. Além disso, podem ser usadas na criação de novas variedades de cultivos, identificando características desejáveis e desenvolvendo plantas mais resistentes e produtivas. As IAs generativas também podem reduzir o desperdício de alimentos ao prever a demanda, otimizar a logística de distribuição e identificar alimentos próximos do vencimento. 
        </p>
        <p className="primary-text-about">
          No entanto, é importante reconhecer que as IAs generativas não são uma solução completa. É necessário abordar questões fundamentais, como desigualdade, acesso a recursos básicos, políticas agrícolas e sistemas de distribuição equitativos. Além disso, as tecnologias devem ser acessíveis e adaptadas às necessidades específicas de cada região. O combate à fome e à escassez de alimentos requer um esforço conjunto envolvendo governos, organizações internacionais, setor privado e sociedade civil.
        </p>
        <p className="primary-text-about">
          As tecnologias inovadoras, como a agricultura vertical, a aquaponia e a hidroponia, desempenham um papel importante na promoção da agricultura sustentável. Essas abordagens oferecem soluções eficientes e sustentáveis para a produção de alimentos em áreas urbanas e com recursos limitados. A agricultura vertical envolve o cultivo de plantas em camadas verticais, utilizando sistemas fechados para maximizar a eficiência do espaço. A aquaponia combina a criação de peixes com o cultivo de plantas em um sistema integrado, permitindo um ciclo sustentável de nutrientes. A hidroponia é o cultivo de plantas sem solo, utilizando uma solução nutritiva em vez disso. Essas tecnologias reduzem a necessidade de terra, água e pesticidas, além de permitir o cultivo o ano todo, independentemente das condições climáticas externas. Elas contribuem para a agricultura sustentável ao reduzir o uso de recursos, minimizar as emissões de gases de efeito estufa e preservar áreas naturais. No entanto, é importante considerar fatores socioeconômicos, ambientais e culturais, além de garantir a acessibilidade dessas tecnologias para promover a inclusão e o desenvolvimento sustentável.
        </p>
        <p className="primary-text-about">
          As IAs generativas podem melhorar a distribuição de alimentos por meio da previsão de demanda, otimização logística, monitoramento de estoque, sistemas inteligentes de embalagem e rotulagem, e redução do desperdício de alimentos. Essas tecnologias analisam grandes volumes de dados para prever a demanda futura, otimizar rotas de transporte, monitorar estoques em tempo real, fornecer informações de segurança alimentar e identificar produtos próximos do vencimento. No entanto, é necessário garantir que essas tecnologias sejam acessíveis e adaptadas às necessidades específicas das comunidades e regiões.
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
