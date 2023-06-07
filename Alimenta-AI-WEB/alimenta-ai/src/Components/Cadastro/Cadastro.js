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
  let [doador, setDoador] = useState(false);
  const [website, setWebsite] = useState("");
  const [tipo, setTipo] = useState("");
  const [cnpj, setCNPJ] = useState("");
  const [termsChecked, setTermsChecked] = useState(false);
  const [formErrors, setFormErrors] = useState({});

  const handleClientTypeChange = (event) => {
    setClientType(event.target.value);
  };

  const handleTermsChange = (event) => {
    setTermsChecked(event.target.checked);
  };

  const validateForm = () => {
    const errors = {};

    // Validar nome (campo obrigatório)
    if (nome.trim() === "") {
      errors.nome = "Campo obrigatório.";
    }

    // Validar email (campo obrigatório e formato)
    if (email.trim() === "") {
      errors.email = "Campo obrigatório.";
    } else {
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailRegex.test(email)) {
        errors.email = "Formato de e-mail inválido.";
      }
    }

    // Validar senha (campo obrigatório)
    if (senha.trim() === "") {
      errors.senha = "Campo obrigatório.";
    }

    // Validar confirmação de senha (igual à senha)
    if (confirmPassword.trim() === "") {
      errors.confirmPassword = "Campo obrigatório.";
    } else if (confirmPassword !== senha) {
      errors.confirmPassword = "As senhas não coincidem.";
    }

    // Validar celular (campo obrigatório)
    if (celular.trim() === "") {
      errors.celular = "Campo obrigatório.";
    }

    // Validar endereço (campo obrigatório)
    if (endereco.trim() === "") {
      errors.endereco = "Campo obrigatório.";
    }

    // Validar CPF (campo obrigatório)
    if (clientType === "person" && cpf.trim() === "") {
      errors.cpf = "Campo obrigatório.";
    }

    // Validar data de nascimento (campo obrigatório)
    if (clientType === "person" && nascimento.trim() === "") {
      errors.nascimento = "Campo obrigatório.";
    }

    // Validar website (campo obrigatório)
    if (clientType === "company" && website.trim() === "") {
      errors.website = "Campo obrigatório.";
    }

    // Validar tipo (campo obrigatório)
    if (clientType === "company" && tipo.trim() === "") {
      errors.tipo = "Campo obrigatório.";
    }

    // Validar CNPJ (campo obrigatório)
    if (clientType === "company" && cnpj.trim() === "") {
      errors.cnpj = "Campo obrigatório.";
    }

    // Validar aceite dos termos e condições
    if (!termsChecked) {
      errors.terms = "Por favor, aceite os termos e condições.";
    }

    setFormErrors(errors);

    // Retorna true se não houver erros
    return Object.keys(errors).length === 0;
  };

  const handleSubmit = (event) => {
    event.preventDefault();

    if (!validateForm()) {
      // Se houver erros de validação, não envia o formulário
      return;
    }

    // Cria o objeto de dados a serem enviados para o servidor
    let formData = {};

    function converterData(data) {
      var partes = data.split("-");
      var dataFormatada = partes[2] + partes[1] + partes[0];
      return dataFormatada;
    }

    if (clientType === "person") {
      formData = {
        nome: nome,
        email: email,
        senha: senha,
        celular: celular,
        endereco: endereco,
        tipoCliente: 0,
        cpf: cpf,
        nascimento: converterData(nascimento),
        doador: doador ? "sim" : "nao",
      };
    } else if (clientType === "company") {
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

    // Envia os dados para o servidor
    fetch("http://localhost:8080/AlimentaAI/cliente", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formData),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(data);

        // Limpa os campos após o envio
        setNome("");
        setEmail("");
        setSenha("");
        setConfirmPassword("");
        setCelular("");
        setEndereco("");
        setCPF("");
        setNascimento("");
        setDoador(false);
        setWebsite("");
        setTipo("");
        setCNPJ("");
        setTermsChecked(false);

        // Exibe uma mensagem de sucesso
        alert("Cadastro feito com sucesso!");
        // Redireciona para a página de login após 2 segundos
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

          {/* Campos de formulário e mensagens de erro */}

          {/* Nome */}
          <div className="name-inputgroup">
            <label htmlFor="name">Nome completo</label>
            <input
              type="text"
              id="name"
              placeholder="Digite seu nome"
              value={nome}
              onChange={(event) => setNome(event.target.value)}
            />
            {formErrors.nome && (
              <span className="error-message">{formErrors.nome}</span>
            )}
          </div>

          {/* Email */}
          <div className="email-inputgroup">
            <label htmlFor="email">Email</label>
            <input
              type="email"
              id="email"
              placeholder="Digite seu e-mail"
              value={email}
              onChange={(event) => setEmail(event.target.value)}
            />
            {formErrors.email && (
              <span className="error-message">{formErrors.email}</span>
            )}
          </div>

          {/* Senha */}
          <div className="password-inputgroup">
            <label htmlFor="password">Senha</label>
            <input
              type="password"
              id="password"
              placeholder="Digite sua senha"
              value={senha}
              onChange={(event) => setSenha(event.target.value)}
            />
            {formErrors.senha && (
              <span className="error-message">{formErrors.senha}</span>
            )}
          </div>

          {/* Confirmação de Senha */}
          <div className="confirm-password-inputgroup">
            <label htmlFor="confirmPassword">Confirme sua senha</label>
            <input
              type="password"
              id="confirmPassword"
              placeholder="Digite novamente sua senha"
              value={confirmPassword}
              onChange={(event) => setConfirmPassword(event.target.value)}
            />
            {formErrors.confirmPassword && (
              <span className="error-message">
                {formErrors.confirmPassword}
              </span>
            )}
          </div>

          {/* Outros campos do formulário e mensagens de erro */}

          {/* Tipo de Cliente (Pessoa Física ou Jurídica) */}
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

          {/* Celular */}
          <div className="phone-inputgroup">
            <label htmlFor="phone">Celular</label>
            <input
              type="text"
              id="celular"
              placeholder="Digite seu celular"
              value={celular}
              onChange={(event) => setCelular(event.target.value)}
            />
            {formErrors.celular && (
              <span className="error-message">{formErrors.celular}</span>
            )}
          </div>

          {/* Endereço */}
          <div className="address-inputgroup">
            <label htmlFor="address">Endereço</label>
            <input
              type="text"
              id="endereco"
              placeholder="Digite seu endereço"
              value={endereco}
              onChange={(event) => setEndereco(event.target.value)}
            />
            {formErrors.endereco && (
              <span className="error-message">{formErrors.endereco}</span>
            )}
          </div>

          {/* Outros campos específicos para Pessoa Física */}
          {clientType === "person" && (
            <div className="person-fields">
              {/* CPF */}
              <div className="cpf-inputgroup">
                <label htmlFor="cpf">CPF</label>
                <input
                  type="text"
                  id="cpf"
                  placeholder="Digite seu CPF"
                  value={cpf}
                  onChange={(event) => setCPF(event.target.value)}
                />
                {formErrors.cpf && (
                  <span className="error-message">{formErrors.cpf}</span>
                )}
              </div>

              {/* Data de Nascimento */}
              <div className="birthdate-inputgroup">
                <label htmlFor="birthdate">Data de Nascimento</label>
                <input
                  type="date"
                  id="nascimento"
                  value={nascimento}
                  onChange={(event) => setNascimento(event.target.value)}
                />
                {formErrors.nascimento && (
                  <span className="error-message">{formErrors.nascimento}</span>
                )}
              </div>

              {/* Doador */}
              <div className="doador-inputgroup">
                <label htmlFor="doador">Doador de Alimentos</label>
                <input
                  type="checkbox"
                  id="doador"
                  checked={doador}
                  onChange={(event) => setDoador(event.target.checked)}
                />
              </div>
            </div>
          )}

          {/* Outros campos específicos para Pessoa Jurídica */}
          {clientType === "company" && (
            <div className="company-fields">
              {/* Website */}
              <div className="website-inputgroup">
                <label htmlFor="website">Website</label>
                <input
                  type="text"
                  id="website"
                  placeholder="Digite o website da empresa"
                  value={website}
                  onChange={(event) => setWebsite(event.target.value)}
                />
                {formErrors.website && (
                  <span className="error-message">{formErrors.website}</span>
                )}
              </div>

              {/* Tipo */}
              <div className="tipo-inputgroup">
                <label htmlFor="tipo">Tipo de Empresa</label>
                <input
                  type="text"
                  id="tipo"
                  placeholder="Digite o tipo de empresa"
                  value={tipo}
                  onChange={(event) => setTipo(event.target.value)}
                />
                {formErrors.tipo && (
                  <span className="error-message">{formErrors.tipo}</span>
                )}
              </div>

              {/* CNPJ */}
              <div className="cnpj-inputgroup">
                <label htmlFor="cnpj">CNPJ</label>
                <input
                  type="text"
                  id="cnpj"
                  placeholder="Digite o CNPJ da empresa"
                  value={cnpj}
                  onChange={(event) => setCNPJ(event.target.value)}
                />
                {formErrors.cnpj && (
                  <span className="error-message">{formErrors.cnpj}</span>
                )}
              </div>
            </div>
          )}

          {/* Aceite dos Termos e Condições */}
          <div className="terms-inputgroup">
            <input
              type="checkbox"
              id="terms"
              checked={termsChecked}
              onChange={handleTermsChange}
            />
            <label htmlFor="terms">
              Li e concordo com os <Link to="/termos">termos e condições</Link>
            </label>
            {formErrors.terms && (
              <span className="error-message">{formErrors.terms}</span>
            )}
          </div>

          <button className="button-cadastro" type="submit">
          <span className="span-cadastro"></span>
          <span className="span-cadastro"></span>
          <span className="span-cadastro"></span>
          <span className="span-cadastro"></span> Cadastre-se
          </button>

          {/* Link para a página de login */}
          <div className="login-link">
            <span>Já possui uma conta?</span>{" "}
            <Link to="/login">Faça login aqui</Link>
          </div>
        </form>
      </div>
    </div>
  );
}

export default Cadastro;
