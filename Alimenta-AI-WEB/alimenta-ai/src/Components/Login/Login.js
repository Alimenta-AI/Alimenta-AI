import React, { useState } from "react";
import { Link, useHistory } from "react-router-dom";
import './Login.css';

function Login () {
  const history = useHistory();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = (event) => {
    event.preventDefault();

    setLoading(true); // Inicia o carregamento

    // Aqui você pode fazer a chamada à API ou implementar a lógica de autenticação

    // Exemplo de lógica de autenticação fictícia
    if (email === "admin" && password === "admin123") {
      // Login bem-sucedido
      history.push("/MeuPerfil");
    } else {
      // Login inválido
      alert("Nome de usuário ou senha incorretos");
    }

    setLoading(false); // Finaliza o carregamento
  };

  return (
    <div className="login-container background-image">
      <form className="login-form" onSubmit={handleSubmit}>
        <h2 className="text-form">Login</h2>

        <div className="email-input-group">
          <label htmlFor="email">Username</label>
          <input
            type="text"
            id="email"
            placeholder="Digite seu e-mail ou username"
            value={email}
            onChange={(event) => setEmail(event.target.value)}
          />
        </div>

        <div className="password-input-group">
          <label htmlFor="password">Senha</label>
          <input
            type="password"
            id="password"
            placeholder="Digite sua senha"
            value={password}
            onChange={(event) => setPassword(event.target.value)}
          />
        </div>
        
        <Link to="/esqueci-minha-senha" className="forgot-password-link">
          Esqueci minha senha
        </Link>
        
        <button className="button-ai" type="submit">
            <span className="span-ai"></span>
            <span className="span-ai"></span>
            <span className="span-ai"></span>
            <span className="span-ai"></span> Login
        </button>
        <p className="text-signin">
          Se não possui uma conta,{" "}
          <Link to="/cadastro">
            <span id="signup-link"> Cadastre-se </span>
          </Link>
        </p>
      </form>
    </div>
  );
};

export default Login;
