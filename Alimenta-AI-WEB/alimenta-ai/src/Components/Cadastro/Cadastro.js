import React, { useState } from "react";
import { Link } from "react-router-dom";
import "./Cadastro.css";

function Cadastro() {
  const [nome, setNome] = useState("");
  const [email, setEmail] = useState("");
  const [senha, setSenha] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [celular, setCelular] = useState("");
  const [endereco, setEndereco] = useState("");
  const [clientType, setClientType] = useState("person");
  const [cpf, setCPF] = useState("");
  const [nascimento, setNascimento] = useState("");
  const [doador, setDoador] = useState("");
  const [website, setWebsite] = useState("");
  const [tipo, setTipo] = useState("");
  const [cnpj, setCNPJ] = useState("");
  const [termsChecked, setTermsChecked] = useState(false);

  const handleClientTypeChange = (event) => {
    setClientType(event.target.value);
  };

  const handleTermsChange = (event) => {
    setTermsChecked(event.target.checked);
  };

  const handleSubmit = (event) => {
    event.preventDefault();

    if (!termsChecked) {
      alert("Por favor, aceite os termos e condições.");
      return;
    }

    let formData;

    if (clientType === "person") {
      // Cria o objeto JSON para pessoa física
      formData = {
        nome: nome,
        email: email,
        senha: senha,
        celular: celular,
        endereco: endereco,
        tipoCliente: 0,
        cpf: cpf,
        nascimento: nascimento,
        doador: doador,
      };
    } else if (clientType === "company") {
      // Cria o objeto JSON para pessoa jurídica
      formData = {
        nome: nome,
        email: email,
        senha: senha,
        celular: celular,
        endereco: endereco,
        tipoCliente: 1,
        website: website,
        tipo: tipo,
        cnpj: cnpj,
      };
    }

    fetch("https://seuservidor.com/cadastro", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formData),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        setNome("");
        setEmail("");
        setSenha("");
        setCelular("");
        setEndereco("");
        setCPF("");
        setNascimento("");
        setDoador("");
        setWebsite("");
        setTipo("");
        setCNPJ("");
        setTermsChecked(false);
        alert("Cadastro feito com sucesso!");
        setTimeout(() => {
          window.location = "/login";
        }, 2000);
      })
      .catch((error) => {
        console.error(error);
      });
  };

  return (
    <div className="signup-container background-image">
      <div className="form-wrapper">
        <form className="signup-form" onSubmit={handleSubmit}>
          <h1>Cadastre-se</h1>

          <div className="name-inputgroup">
            <label htmlFor="name">Nome completo</label>
            <input
              type="text"
              id="name"
              placeholder="Digite seu nome"
              value={nome}
              onChange={(event) => setNome(event.target.value)}
            />
          </div>

          <div className="email-inputgroup">
            <label htmlFor="email">Email</label>
            <input
              type="email"
              id="email"
              placeholder="Digite seu e-mail"
              value={email}
              onChange={(event) => setEmail(event.target.value)}
            />
          </div>

          <div className="password-inputgroup">
            <label htmlFor="password">Senha</label>
            <input
              type="password"
              id="password"
              placeholder="Digite sua senha"
              value={senha}
              onChange={(event) => setSenha(event.target.value)}
            />
          </div>

          <div className="confirm-password-inputgroup">
            <label htmlFor="confirmPassword">Confirme sua senha</label>
            <input
              type="password"
              id="confirmpassword"
              placeholder="Confirme sua senha"
              value={confirmPassword}
              onChange={(event) => setConfirmPassword(event.target.value)}
            />
          </div>

          <div className="phone-inputgroup">
            <label htmlFor="phone">Telefone</label>
            <input
              type="tel"
              id="phone"
              placeholder="Digite seu telefone"
              value={celular}
              onChange={(event) => setCelular(event.target.value)}
            />
          </div>

          <div className="address-inputgroup">
            <label htmlFor="address">Endereço</label>
            <input
              type="text"
              id="address"
              placeholder="Digite seu endereço"
              value={endereco}
              onChange={(event) => setEndereco(event.target.value)}
            />
          </div>

          <div className="client-type-inputgroup">
            <label htmlFor="clientType">Tipo de Cliente</label>
            <select
              id="clientType"
              value={clientType}
              onChange={handleClientTypeChange}
            >
              <option value="person">Pessoa Física</option>
              <option value="company">Pessoa Jurídica</option>
            </select>
          </div>

          {clientType === "person" && (
            <div>
              <div className="cpf-inputgroup">
                <label htmlFor="cpf">CPF</label>
                <input
                  type="text"
                  id="CPF"
                  placeholder="Digite seu CPF"
                  value={cpf}
                  onChange={(event) => setCPF(event.target.value)}
                />
              </div>

              <div className="birthdate-inputgroup">
                <label htmlFor="birthdate">Data de Nascimento</label>
                <input
                  type="date"
                  id="birthdate"
                  placeholder="Digite sua data de nascimento"
                  value={nascimento}
                  onChange={(event) => setNascimento(event.target.value)}
                />
              </div>

              <div className="donor-inputgroup">
                <label htmlFor="isDonor">
                  Doador
                  <input
                    type="checkbox"
                    id="isDonor"
                    checked={doador}
                    onChange={(event) => setDoador(event.target.checked)}
                  />
                </label>
              </div>
            </div>
          )}

          {clientType === "company" && (
            <div>
              <div className="website-inputgroup">
                <label htmlFor="website">Website</label>
                <input
                  type="text"
                  id="website"
                  placeholder="Digite o website da empresa"
                  value={website}
                  onChange={(event) => setWebsite(event.target.value)}
                />
              </div>

              <div className="company-type-inputgroup">
                <label htmlFor="companyType">Tipo de Empresa</label>
                <input
                  type="text"
                  id="companyType"
                  placeholder="Digite o tipo de empresa"
                  value={tipo}
                  onChange={(event) => setTipo(event.target.value)}
                />
              </div>

              <div className="cnpj-inputgroup">
                <label htmlFor="cnpj">CNPJ</label>
                <input
                  type="text"
                  id="cnpj"
                  placeholder="Digite o CNPJ da empresa"
                  value={cnpj}
                  onChange={(event) => setCNPJ(event.target.value)}
                />
              </div>
            </div>
          )}

          <div className="termos-inputgroup">
            <input
              type="checkbox"
              id="terms"
              checked={termsChecked}
              onChange={handleTermsChange}
            />
            <label htmlFor="terms">Eu concordo com os termos e condições</label>
          </div>

          <button className="button-cadastro" type="submit">
            Cadastre-se
          </button>

          <p className="text-sign">
            Já possui uma conta, faça o{" "}
            <Link to="/login">
              <span id="signup-link">Login</span>
            </Link>
          </p>
        </form>
      </div>
    </div>
  );
}

export default Cadastro;
