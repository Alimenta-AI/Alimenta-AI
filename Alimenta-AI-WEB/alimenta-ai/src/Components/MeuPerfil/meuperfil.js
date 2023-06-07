import React, { useState } from "react";
import axios from "axios";
import "../MeuPerfil/MeuPerfil.css";

function MeuPerfil() {
  const [foto, setFoto] = useState(null);
  const [nome, setNome] = useState("");
  const [email, setEmail] = useState("");
  const [senha, setSenha] = useState("");
  const [celular, setCelular] = useState("");
  const [endereco, setEndereco] = useState("");

  const handleFotoChange = (event) => {
    const selectedFile = event.target.files[0];
    setFoto(URL.createObjectURL(selectedFile));
  };

  const handleNomeChange = (event) => {
    setNome(event.target.value);
  };

  const handleEmailChange = (event) => {
    setEmail(event.target.value);
  };

  const handleSenhaChange = (event) => {
    setSenha(event.target.value);
  };

  const handleCelularChange = (event) => {
    setCelular(event.target.value);
  };

  const handleEnderecoChange = (event) => {
    setEndereco(event.target.value);
  };

  const handleEditarPerfil = () => {
    const formData = {
      nome: nome,
      email: email,
      senha: senha,
      celular: celular,
      endereco: endereco,
    };

    axios
      .put("http://localhost:8080/AlimentaAI/usuario", formData)
      .then((response) => {
        console.log(response.data);
        alert("Perfil atualizado com sucesso!");
      })
      .catch((error) => {
        console.error(error);
        alert("Ocorreu um erro ao atualizar o perfil.");
      });
  };

  const handleExcluirPerfil = () => {
    axios
      .delete("http://localhost:8080/AlimentaAI/usuario")
      .then((response) => {
        console.log(response.data);
        alert("Perfil excluído com sucesso!");
        // Redirecionar para a página de login ou qualquer outra ação necessária
      })
      .catch((error) => {
        console.error(error);
        alert("Ocorreu um erro ao excluir o perfil.");
      });
  };

  return (
    <div className="container">
      <h1>Meu Perfil</h1>
      <div className="input-container">
        {foto && <img className="Imagem-perfil" src={foto} alt="Foto do Perfil" />}
      </div>
      <br />
      <div className="input-container">
        <label htmlFor="nome">Nome:</label>
        <input
          type="text"
          id="nome"
          value={nome}
          onChange={handleNomeChange}
        />
      </div>
      <br />
      <div className="input-container">
        <label htmlFor="email">Email:</label>
        <input
          type="email"
          id="email"
          value={email}
          onChange={handleEmailChange}
        />
      </div>
      <br />
      <div className="input-container">
        <label htmlFor="senha">Senha:</label>
        <input
          type="password"
          id="senha"
          value={senha}
          onChange={handleSenhaChange}
        />
      </div>
      <br />
      <div className="input-container">
        <label htmlFor="celular">Celular:</label>
        <input
          type="text"
          id="celular"
          value={celular}
          onChange={handleCelularChange}
        />
      </div>
      <br />
      <div className="input-container">
        <label htmlFor="endereco">Endereço:</label>
        <input
          type="text"
          id="endereco"
          value={endereco}
          onChange={handleEnderecoChange}
        />
      </div>
      <br />
      <div className="button-container">
        <div className="btn-wrapper">
          <button className="btn-editar" onClick={handleEditarPerfil}>
            Editar
          </button>
        </div>
        <div className="btn-wrapper">
          <input
            type="file"
            id="foto"
            accept=".png,.jpg"
            onChange={handleFotoChange}
          />
        </div>
        <div className="btn-wrapper">
          <button className="btn-excluir" onClick={handleExcluirPerfil}>
            Excluir
          </button>
        </div>
      </div>
    </div>
  );
}

export default MeuPerfil;
