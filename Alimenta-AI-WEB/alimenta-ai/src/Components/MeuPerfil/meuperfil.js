import React, { useState } from 'react';

function MeuPerfil() {
  const [foto, setFoto] = useState('');
  const [nome, setNome] = useState('');
  const [email, setEmail] = useState('');
  const [senha, setSenha] = useState('');
  const [celular, setCelular] = useState('');
  const [endereco, setEndereco] = useState('');

  const handleFotoChange = (e) => {
    const file = e.target.files[0];
    setFoto(file);

    const reader = new FileReader();
    reader.onloadend = () => {
      setFoto(reader.result);
    };

    if (file) {
      reader.readAsDataURL(file);
    }
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
    // Lógica para salvar as alterações do perfil no backend
    // Pode-se usar uma API ou um serviço de armazenamento de dados
    console.log('Perfil editado:', {
      foto,
      nome,
      email,
      senha,
      celular,
      endereco
    });
  };

  const handleExcluirPerfil = () => {
    // Lógica para excluir o perfil do usuário
    // Pode-se usar uma API ou um serviço de armazenamento de dados
    console.log('Perfil excluído');
  };

  return (
    <div>
      <h1>Meu Perfil</h1>
      <div>
        <label htmlFor="foto">Foto:</label>
        <input
          type="file"
          id="foto"
          accept=".png,.jpg"
          onChange={handleFotoChange}
        />
        {foto && <img src={foto} alt="Foto do Perfil" />}
      </div>
      <br />
      <div>
        <label htmlFor="nome">Nome:</label>
        <input
          type="text"
          id="nome"
          value={nome}
          onChange={handleNomeChange}
        />
      </div>
      <br />
      <div>
        <label htmlFor="email">Email:</label>
        <input
          type="email"
          id="email"
          value={email}
          onChange={handleEmailChange}
        />
      </div>
      <br />
      <div>
        <label htmlFor="senha">Senha:</label>
        <input
          type="password"
          id="senha"
          value={senha}
          onChange={handleSenhaChange}
        />
      </div>
      <br />
      <div>
        <label htmlFor="celular">Celular:</label>
        <input
          type="text"
          id="celular"
          value={celular}
          onChange={handleCelularChange}
        />
      </div>
      <br />
      <div>
        <label htmlFor="endereco">Endereço:</label>
        <input
          type="text"
          id="endereco"
          value={endereco}
          onChange={handleEnderecoChange}
        />
      </div>
      <br />
      <br />
      <div>
        <button className="btn-editar" onClick={handleEditarPerfil}>
          Editar
        </button>&nbsp;
        <button className="btn-excluir" onClick={handleExcluirPerfil}>
          Excluir
        </button>
      </div>
    </div>
  );
}

export default MeuPerfil;

