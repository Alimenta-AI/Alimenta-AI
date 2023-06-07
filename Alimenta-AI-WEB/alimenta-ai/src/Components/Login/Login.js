import React, { useState, useContext } from "react";
import { Link, useHistory } from "react-router-dom";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import "./Login.css";
import { AuthContext } from "../AuthContext";

const Login = () => {
  const [email, setEmail] = useState("");
  const [senha, setSenha] = useState("");
  const [loading, setLoading] = useState(false);
  const history = useHistory();
  const { handleLogin } = useContext(AuthContext);

  const handleSubmit = (event) => {
    event.preventDefault();

    setLoading(true);

    const formData = {
      email: email,
      senha: senha,
    };

    fetch("http://localhost:8080/AlimentaAI/login", {
      method: "post",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formData),
    })
      .then((response) => {
        if (response.ok) {
          return response.json();
        } else {
          throw new Error("Senha incorreta!");
        }
      })
      .then((userData) => {
        handleLogin(email);

        // Armazene a sessão no sessionStorage
        sessionStorage.setItem("usuario", JSON.stringify(userData));

        history.push("/meuperfil");
        toast.success("Login realizado com sucesso", {
          position: toast.POSITION.TOP_CENTER,
          autoClose: 3000,
        });
      })
      .catch((error) => {
        toast.error(error.message, {
          position: toast.POSITION.TOP_CENTER,
          autoClose: 3000,
        });
      })
      .finally(() => {
        setLoading(false);
      });
  };

  const handleLogout = () => {
    sessionStorage.removeItem("usuario");
    history.push("/login");
  };

  const sessionSessao = sessionStorage.getItem("usuario");

  if (sessionSessao) {
    history.push("/");
  }

  return (
    <div className="login-container background-image">
      <ToastContainer />
      {loading && <div className="loading-overlay">Carregando...</div>}
      <form className="login-form" onSubmit={handleSubmit}>
        <h2 className="text-form">Login</h2>

        <div className="email-input-group">
          <label htmlFor="email">Username</label>
          <input
            type="text"
            id="email"
            placeholder="Digite seu e-mail"
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
};

export default Login;
