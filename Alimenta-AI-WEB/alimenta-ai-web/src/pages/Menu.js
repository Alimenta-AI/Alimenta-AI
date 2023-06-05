  import React, { useState } from 'react';
  import '../styles/Menu.css';

  const estados = [
    { sigla: 'AC', nome: 'Acre' },
    { sigla: 'AL', nome: 'Alagoas' },
    { sigla: 'AP', nome: 'Amapá' },
    { sigla: 'AM', nome: 'Amazonas' },
    { sigla: 'BA', nome: 'Bahia' },
    { sigla: 'CE', nome: 'Ceará' },
    { sigla: 'DF', nome: 'Distrito Federal' },
    { sigla: 'ES', nome: 'Espírito Santo' },
    { sigla: 'GO', nome: 'Goiás' },
    { sigla: 'MA', nome: 'Maranhão' },
    { sigla: 'MT', nome: 'Mato Grosso' },
    { sigla: 'MS', nome: 'Mato Grosso do Sul' },
    { sigla: 'MG', nome: 'Minas Gerais' },
    { sigla: 'PA', nome: 'Pará' },
    { sigla: 'PB', nome: 'Paraíba' },
    { sigla: 'PR', nome: 'Paraná' },
    { sigla: 'PE', nome: 'Pernambuco' },
    { sigla: 'PI', nome: 'Piauí' },
    { sigla: 'RJ', nome: 'Rio de Janeiro' },
    { sigla: 'RN', nome: 'Rio Grande do Norte' },
    { sigla: 'RS', nome: 'Rio Grande do Sul' },
    { sigla: 'RO', nome: 'Rondônia' },
    { sigla: 'RR', nome: 'Roraima' },
    { sigla: 'SC', nome: 'Santa Catarina' },
    { sigla: 'SP', nome: 'São Paulo' },
    { sigla: 'SE', nome: 'Sergipe' },
    { sigla: 'TO', nome: 'Tocantins' }
  ];

  const unidades = [
    'UN', 'KG', 'G', 'MG', 'LB', 'OZ', 'L', 'ML', 'CS', 'CC', 'XC', 'FT', 'PO', 'PC', 'SC', 'LT', 'PT'
  ];

  function Menu() {
    const [data, setData] = useState([
      { codigo: 1, descricao: 'Produto 1', fornecedor: 'Fornecedor A', estado: 'SP', unidade: 'UN', valor: '10,00', quantidade: '' },
      { codigo: 2, descricao: 'Produto 2', fornecedor: 'Fornecedor B', estado: 'RJ', unidade: 'KG', valor: '20,00', quantidade: '' },
      { codigo: 3, descricao: 'Produto 3', fornecedor: 'Fornecedor C', estado: 'MG', unidade: 'UN', valor: '15,00', quantidade: '' }
    ]);

    const handleInputChange = (event, index, field) => {
      const newData = [...data];
      newData[index][field] = event.target.value;
      setData(newData);
    };

    const handleSelectChange = (event, index, field) => {
      const newData = [...data];
      newData[index][field] = event.target.value;
      setData(newData);
    };

    const handleValorUnitarioChange = (event, index) => {
      const newData = [...data];
      newData[index]['valor'] = event.target.value;
      setData(newData);
    };

    const handleValorUnitarioBlur = (event, index) => {
      const newData = [...data];
      const valor = event.target.value;
      if (!isNaN(valor)) {
        const numeroFormatado = parseFloat(valor.replace(',', '.'));
        newData[index]['valor'] = `R$ ${numeroFormatado.toFixed(2).replace('.', ',')}`;
      } else {
        newData[index]['valor'] = valor; // Mantém o valor original se não for um número válido
      }
      setData(newData);
    };

    const handleDeleteRow = (index) => {
      const newData = [...data];
      newData.splice(index, 1);
      setData(newData);
    };

    const handleAddRow = () => {
      const newData = [...data];
      const newRow = {
        codigo: '',
        descricao: '',
        fornecedor: '',
        estado: '',
        unidade: '',
        valor: '',
        quantidade: ''
      };
      newData.push(newRow);
      setData(newData);
    };
    
    const handleClearAll = () => {
      const clearedData = data.map((row) => ({
        ...row,
        codigo: '',
        descricao: '',
        fornecedor: '',
        estado: '',
        unidade: '',
        valor: ''
      }));
      setData(clearedData);
    };

    return (
      <div className="Menu">
        <p className='Titulo-tabela'>Cadastro para realizar a doação de alimentos</p>
        <table>
          <thead>
            <tr>
              <th>Código</th>
              <th>Descrição alimento</th>
              <th>Fornecedor</th>
              <th>Estado</th>
              <th>Unidade</th>
              <th>Val Unit</th>
              <th>Qtde Alimento</th>
              <th>Ações</th>
            </tr>
          </thead>
          <tbody>
            {data.map((row, index) => (
              <tr key={index}>
                <td>
                  <input
                    type="text"
                    className="codigo-input"
                    value={row.codigo}
                    onChange={(event) => handleInputChange(event, index, 'codigo')}
                  />
                </td>
                <td>
                  <input
                    type="text"
                    className="descricao-input"
                    value={row.descricao}
                    onChange={(event) => handleInputChange(event, index, 'descricao')}
                  />
                </td>
                <td>
                  <input
                    type="text"
                    className="fornecedor-input"
                    value={row.fornecedor}
                    onChange={(event) => handleInputChange(event, index, 'fornecedor')}
                  />
                </td>
                <td>
                  <select
                    className="estado-select"
                    value={row.estado}
                    onChange={(event) => handleSelectChange(event, index, 'estado')}
                  >
                    {estados.map((estado) => (
                      <option key={estado.sigla} value={estado.sigla}>
                        {estado.nome}
                      </option>
                    ))}
                  </select>
                </td>
                <td>
                  <select
                    className="unidade-select"
                    value={row.unidade}
                    onChange={(event) => handleSelectChange(event, index, 'unidade')}
                  >
                    {unidades.map((unidade) => (
                      <option key={unidade} value={unidade}>
                        {unidade}
                      </option>
                    ))}
                  </select>
                </td>
                <td>
                  <input
                    type="text"
                    className="valor-input"
                    value={row.valor}
                    onChange={(event) => handleValorUnitarioChange(event, index)}
                    onBlur={(event) => handleValorUnitarioBlur(event, index)}
                  />
                </td>
                <td>
                  <input
                    type="text"
                    className="quantidade-input"
                    value={row.quantidade}
                    onChange={(event) => handleInputChange(event, index, 'quantidade')}
                  />
                </td>
                {index === data.length - 1 ? (
            <td>
              <span className="add-icon" onClick={() => handleAddRow()}>
                +
              </span>
          </td>
        ) : (
          <td>
      <     span className="delete-icon" onClick={() => handleDeleteRow(index)}>
              X
          </span>
      </td>
    )}
              </tr>
            ))}
          </tbody>
        </table>
        <button className="clear-all-button" onClick={handleClearAll}>
          Limpar Tudo
        </button>
        <button className="cadastrar-doacao-button">Cadastrar Doação</button>
        
      </div>
    );
  }
  export default Menu;
