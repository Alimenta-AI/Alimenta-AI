import "./App.css";
import Navbar from "./Components/Navbar";
import MainHome from "./Container/MainHome";
import Login from "./Components/Login/Login";
import Cadastro from "./Components/Cadastro/Cadastro";
import Doe from "./Components/Doacao/Doe";
import Footer from "./Components/Footer";
import About from "./Components/About";
import Work from "./Components/Work";
import Testimonial from "./Components/Testimonial";
import Contact from "./Components/Contact";
import Senha from "./Components/Senha/Senha";
import MeuPerfil from "./Components/MeuPerfil/MeuPerfil";
import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

function App() {
  return (
    <div className="App">
      <Router>
        <Navbar />
        <Switch>
          <Route path="/" exact component={MainHome} />
          <Route path="/doe" exact component={Doe} />
          <Route path="/cadastro" exact component={Cadastro} />
          <Route path="/login" exact component={Login} />
          <Route path="/sobre" exact component={About} />
          <Route path="/trabalho" exact component={Work} />
          <Route path="/testemunhos" exact component={Testimonial} />
          <Route path="/contato" exact component={Contact} />
          <Route path="/esqueci-minha-senha" exact component={Senha} />
          <Route path="/MeuPerfil" exact component={MeuPerfil} />
        </Switch>
        <Footer />
      </Router>
    </div>
  );
}

export default App;
