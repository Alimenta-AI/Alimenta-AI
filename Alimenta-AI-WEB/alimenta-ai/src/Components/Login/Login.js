import './Login.css';
import React, { useState } from 'react';
import { Link } from 'react-router-dom';

function Login() {
  const handleSubmit = (event) => {
  event.preventDefault();

  const formData = {
    email: email,
    senha: senha,
  };

  fetch("http://localhost:8080/AlimentaAI/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(formData),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      setEmail("");
      setSenha("");
      if (data.success) {
        alert("Login realizado com sucesso!");
        setTimeout(() => {
          window.location = "/meuPerfil";
        }, 2000);
      } else {
        alert("Falha no login. Verifique suas credenciais.");
      }
    })
    .catch((error) => {
      console.error(error);
    });
};

const [email, setEmail] = useState("");
const [senha, setSenha] = useState("");

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
            value={senha}
            onChange={(event) => setSenha(event.target.value)}
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
}

export default Login;
