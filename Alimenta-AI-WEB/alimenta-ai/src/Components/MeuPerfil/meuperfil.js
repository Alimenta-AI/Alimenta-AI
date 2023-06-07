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
    getUsuario(); // Chama a função getUsuario ao montar o componente
  }, []);

  const getUsuario = async () => {
    try {
      // Obter o clienteId da sessão atual do sessionStorage
      const usuarioJson = sessionStorage.getItem("usuario");
      const usuario = JSON.parse(usuarioJson);

      // Verificar se o usuário existe na sessão
      if (!usuario) {
        console.error("Usuário não encontrado na sessão.");
        return;
      }

      const {
        nome,
        email,
        senha,
        celular,
        endereco,
        cpf,
        nascimento,
        doador,
        website,
        tipo,
        cnpj,
      } = usuario;

      setNome(nome);
      setEmail(email);
      setSenha(senha);
      setCelular(celular);
      setEndereco(endereco);

      // Configurar os campos adicionais com base no tipoCliente
      if (usuario.tipoCliente === 0) {
        setCPF(cpf);
        setNascimento(nascimento);
        setDoador(doador);
      } else if (usuario.tipoCliente === 1) {
        setWebsite(website);
        setTipo(tipo);
        setCnpj(cnpj);
      }
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
    <div>
      <h1>Meu Perfil</h1>
      <div className="input-container">
        <label htmlFor="nome">Nome:</label>
        <input type="text" id="nome" value={nome} />
      </div>
      <div className="input-container">
        <label htmlFor="email">Email:</label>
        <input type="email" id="email" value={email} />
      </div>
      <div className="input-container">
        <label htmlFor="celular">Celular:</label>
        <input type="text" id="celular" value={celular} />
      </div>
      <div className="input-container">
        <label htmlFor="endereco">Endereço:</label>
        <input type="text" id="endereco" value={endereco} />
      </div>

      {/* Renderizar campos adicionais com base no tipoCliente */}
      {sessionStorage.getItem("tipoCliente") === 0 && (
        <div>
          <div className="input-container">
            <label htmlFor="cpf">CPF:</label>
            <input type="text" id="cpf" value={cpf} />
          </div>
          <div className="input-container">
            <label htmlFor="nascimento">Data de Nascimento:</label>
            <input type="text" id="nascimento" value={nascimento} />
          </div>
          <div className="input-container">
            <label htmlFor="doador">Doador:</label>
            <input type="checkbox" id="doador" checked={doador} />
          </div>
        </div>
      )}

      {sessionStorage.getItem("tipoCliente") === 1 && (
        <div>
          <div className="input-container">
            <label htmlFor="website">Website:</label>
            <input type="text" id="website" value={website} />
          </div>
          <div className="input-container">
            <label htmlFor="tipo">Tipo:</label>
            <input type="text" id="tipo" value={tipo} />
          </div>
          <div className="input-container">
            <label htmlFor="cnpj">CNPJ:</label>
            <input type="text" id="cnpj" value={cnpj} />
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
