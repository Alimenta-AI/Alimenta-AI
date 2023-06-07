import React, { useState, useEffect } from "react";
import axios from "axios";

function MeuPerfil() {
  const [nome, setNome] = useState("");
  const [email, setEmail] = useState("");
  const [senha, setSenha] = useState("");
  const [celular, setCelular] = useState("");
  const [endereco, setEndereco] = useState("");
  const [cpf, setCPF] = useState("");
  const [nascimento, setNascimento] = useState("");
  const [doador, setDoador] = useState(false);
  const [website, setWebsite] = useState("");
  const [tipo, setTipo] = useState("");
  const [cnpj, setCnpj] = useState("");

  useEffect(() => {
    getUsuario();
  }, []);

  const usuarioJson = sessionStorage.getItem("usuario");
  const usuario = JSON.parse(usuarioJson);

  const getUsuario = async () => {
    try {
      if (!usuario) {
        console.error("Usuário não encontrado na sessão.");
        return;
      }

      const response = await axios.get(
        `http://localhost:8080/AlimentaAI/cliente/${usuario.clienteId}`
      );
      const usuarioData = response.data;

      const { nome, email, senha, celular, endereco, tipoCliente } =
        usuarioData.cliente;

      setNome(nome);
      setEmail(email);
      setSenha(senha);
      setCelular(celular);
      setEndereco(endereco);

      if (tipoCliente === 0) {
        const { cpf, nascimento, doador } = usuarioData.usuario;
        setCPF(cpf);
        setNascimento(nascimento);
        setDoador(doador === "sim");
      } else if (tipoCliente === 1) {
        const { website, tipo, cnpj } = usuarioData.usuario;
        setWebsite(website);
        setTipo(tipo);
        setCnpj(cnpj);
      }
    } catch (error) {
      console.error("Erro ao obter usuário:", error);
    }
  };

  const handleEditarPerfil = async () => {
    const perfilData = {
      nome: nome,
      email: email,
      senha: senha,
      celular: celular,
      endereco: endereco,
    };
    axios
      .put("http://localhost:8080/AlimentaAI/usuario", perfilData)
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
      const clienteId = sessionStorage.getItem("clienteId");
      const tipoCliente = sessionStorage.getItem("tipoCliente");

      if (!clienteId) {
        console.error("clienteId não encontrado na sessão.");
        return;
      }

      const deleteData = {
        clienteId: clienteId,
        tipoCliente: tipoCliente,
      };

      const response = await axios.delete(
        "http://localhost:8080/AlimentaAI/cliente/",
        { data: deleteData }
      );
      console.log("Perfil excluído com sucesso:", response.data);
    } catch (error) {
      console.error("Erro ao excluir perfil:", error);
    }
  };

  return (
    <div>
      <h1>Meu Perfil</h1>
      <div className="input-container">
        <label htmlFor="nome">Nome:</label>
        <input
          type="text"
          id="nome"
          value={nome}
          onChange={(e) => setNome(e.target.value)}
        />
      </div>
      <div className="input-container">
        <label htmlFor="email">Email:</label>
        <input
          type="email"
          id="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
      </div>
      <div className="input-container">
        <label htmlFor="celular">Celular:</label>
        <input
          type="text"
          id="celular"
          value={celular}
          onChange={(e) => setCelular(e.target.value)}
        />
      </div>
      <div className="input-container">
        <label htmlFor="endereco">Endereço:</label>
        <input
          type="text"
          id="endereco"
          value={endereco}
          onChange={(e) => setEndereco(e.target.value)}
        />
      </div>

      {usuario.tipoCliente === "0" && (
        <div>
          <div className="input-container">
            <label htmlFor="cpf">CPF:</label>
            <input
              type="text"
              id="cpf"
              value={cpf}
              onChange={(e) => setCPF(e.target.value)}
            />
          </div>
          <div className="input-container">
            <label htmlFor="nascimento">Data de Nascimento:</label>
            <input
              type="text"
              id="nascimento"
              value={nascimento}
              onChange={(e) => setNascimento(e.target.value)}
            />
          </div>
          <div className="input-container">
            <label htmlFor="doador">Doador:</label>
            <input
              type="checkbox"
              id="doador"
              checked={doador}
              onChange={(e) => setDoador(e.target.checked)}
            />
          </div>
        </div>
      )}

      {usuario.tipoCliente === "1" && (
        <div>
          <div className="input-container">
            <label htmlFor="website">Website:</label>
            <input
              type="text"
              id="website"
              value={website}
              onChange={(e) => setWebsite(e.target.value)}
            />
          </div>
          <div className="input-container">
            <label htmlFor="tipo">Tipo:</label>
            <input
              type="text"
              id="tipo"
              value={tipo}
              onChange={(e) => setTipo(e.target.value)}
            />
          </div>
          <div className="input-container">
            <label htmlFor="cnpj">CNPJ:</label>
            <input
              type="text"
              id="cnpj"
              value={cnpj}
              onChange={(e) => setCnpj(e.target.value)}
            />
          </div>
        </div>
      )}

      <div className="button-container">
        <div className="btn-wrapper">
          <button className="btn-editar" onClick={handleEditarPerfil}>
            Editar
          </button>
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
