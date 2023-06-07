import React, { useState, useEffect } from "react";
import axios from "axios";
import "../MeuPerfil/MeuPerfil.css";

function MeuPerfil() {
  const [nome, setNome] = useState("");
  const [email, setEmail] = useState("");
  const [senha, setSenha] = useState("");
  const [celular, setCelular] = useState("");
  const [endereco, setEndereco] = useState("");

  useEffect(() => {
    getUsuario(); // Chama a função getUsuario ao montar o componente
  }, []);

  const getUsuario = async () => {
    try {
      const response = await axios.get(
        `http://localhost:8080/AlimentaAI/cliente/`
      );
      const { nome, email, senha, celular, endereco } = response.data;
      setNome(nome);
      setEmail(email);
      setSenha(senha);
      setCelular(celular);
      setEndereco(endereco);
    } catch (error) {
      console.error("Erro ao obter usuário:", error);
    }
  };

  const handleEditarPerfil = async () => {
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
        if (response.status === 200) {
          console.log(response.data);
          alert("Perfil atualizado com sucesso!");
        } else {
          alert("Ocorreu um erro ao atualizar o perfil.");
        }
      })
      .catch((error) => {
        console.error(error);
        alert("Ocorreu um erro ao atualizar o perfil.");
      });
  };

  const handleExcluirPerfil = async () => {
    try {
      // Obter o clienteId da sessão atual do sessionStorage
      const clienteId = sessionStorage.getItem("clienteId");
      const tipoCliente = sessionStorage.getItem("tipoCliente");

      // Verificar se o clienteId existe na sessão
      if (!clienteId) {
        console.error("clienteId não encontrado na sessão.");
        return;
      }

      // Montar o objeto de dados para a requisição DELETE
      const data = {
        clienteId: clienteId,
        tipoCliente: tipoCliente,
      };

      const response = await axios.delete(
        "http://localhost:8080/AlimentaAI/cliente/",
        { data }
      );
      console.log("Perfil excluído com sucesso:", response.data);
    } catch (error) {
      console.error("Erro ao excluir perfil:", error);
    }
  };

  return (
    <div className="container">
      <h1>Meu Perfil</h1>
      <div className="input-container">
        <label htmlFor="nome">Nome:</label>
        <input type="text" id="nome" value={nome} />
      </div>
      <br />
      <div className="input-container">
        <label htmlFor="email">Email:</label>
        <input type="email" id="email" value={email} />
      </div>
      <br />
      <div className="input-container">
        <label htmlFor="senha">Senha:</label>
        <input type="password" id="senha" value={senha} />
      </div>
      <br />
      <div className="input-container">
        <label htmlFor="celular">Celular:</label>
        <input type="text" id="celular" value={celular} />
      </div>
      <br />
      <div className="input-container">
        <label htmlFor="endereco">Endereço:</label>
        <input type="text" id="endereco" value={endereco} />
      </div>
      <br />
      <div className="button-container">
        <div className="btn-wrapper">
          <button className="btn-editar" onClick={handleEditarPerfil}>
            Editar
          </button>
        </div>
        <div className="btn-wrapper">
          <input type="file" id="foto" accept=".png,.jpg" />
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
