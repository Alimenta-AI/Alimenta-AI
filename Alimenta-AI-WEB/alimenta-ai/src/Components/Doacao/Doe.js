import { useState, useEffect } from 'react';
import './Doe.css';

function Menu() {
  const [data, setData] = useState([
    { codigo: '', descricao: '', unidade: '', quantidade: '', validade: '' },
    { codigo: '', descricao: '', unidade: '', quantidade: '', validade: '' },
    { codigo: '', descricao: '', unidade: '', quantidade: '', validade: '' }
  ]);

  const unitsOfMeasure = ['kg', 'g', 'L', 'mL', 'un'];

  const hashCode = (str) => {
    let hash = 0;
    if (str.length === 0) {
      return hash;
    }
    for (let i = 0; i < str.length; i++) {
      const char = str.charCodeAt(i);
      hash = (hash << 5) - hash + char;
      hash = hash & hash; // Convert to 32-bit integer
    }
    return hash;
  };

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

  const handleDeleteRow = (index) => {
    const newData = [...data];
    newData.splice(index, 1);
    setData(newData);
  };

  const handleAddRow = () => {
    const newData = [...data];
    const newRow = {
      codigo: hashCode(JSON.stringify(newData)),
      descricao: '',
      unidade: '',
      quantidade: '',
      validade: ''
    };
    newData.push(newRow);
    setData(newData);
  };

  const handleClearAll = () => {
    const clearedData = data.map((row) => ({
      ...row,
      descricao: '',
      unidade: '',
      quantidade: '',
      validade: ''
    }));
    setData(clearedData);
    setErrorMessage('');
  };

  useEffect(() => {
    const handleGenerateHash = () => {
      const newData = [...data];
      newData.forEach((row) => {
        if (!row.codigo) {
          row.codigo = hashCode(JSON.stringify(row));
        }
      });
      setData(newData);
    };

    handleGenerateHash();
  }, [data]);

  const [doacaoRealizada, setDoacaoRealizada] = useState(false);
  const [errorMessage, setErrorMessage] = useState('');

  const handleCadastrarDoacao = () => {
    const validationMessage = validateFields(data);

    if (validationMessage === '') {
      setDoacaoRealizada(true);
      setErrorMessage('');
    } else {
      setErrorMessage(validationMessage);
    }
  };

  function validateFields(data) {
    for (let i = 0; i < data.length; i++) {
      const row = data[i];

      if (row.descricao === '') {
        return 'Por favor, preencha a descrição do alimento.';
      }

      if (row.quantidade === '') {
        return 'Por favor, preencha a quantidade do alimento.';
      } else if (!/^\d{1,3}$/.test(row.quantidade)) {
        return 'A quantidade do alimento deve conter apenas números de até 3 dígitos.';
      }

      if (/\d/.test(row.descricao)) {
        return 'A descrição do alimento não pode conter números.';
      }
    }

    return '';
  }

  return (
      <div className="Menu page">
          <p className="Titulo-tabela">Cadastro para realizar a doação de alimentos</p>
          <table>
            <thead>
              <tr>
                <th>Código</th>
                <th>Descrição alimento</th>
                <th>Unidade</th>
                <th>Qtde Alimento</th>
                <th>Validade</th>
                <th>Ações</th>
              </tr>
            </thead>
            <tbody>
              {data.map((row, index) => (
                <tr key={index}>
                  <td>
                    <input type="text" className="codigo-input" value={row.codigo} readOnly />
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
                    <select
                      className="unidade-select"
                      value={row.unidade}
                      onChange={(event) => handleSelectChange(event, index, 'unidade')}
                    >
                      <option value="">Selecione</option>
                      {unitsOfMeasure.map((unit) => (
                        <option key={unit} value={unit}>
                          {unit}
                        </option>
                      ))}
                    </select>
                  </td>
                  <td>
                    <input
                      type="text"
                      className="quantidade-input"
                      value={row.quantidade}
                      onChange={(event) => handleInputChange(event, index, 'quantidade')}
                    />
                  </td>
                  <td>
                    <input
                      type="date"
                      className="validade-input"
                      value={row.validade}
                      onChange={(event) => handleInputChange(event, index, 'validade')}
                    />
                  </td>
                  <td>
                    {index === data.length - 1 ? (
                      <button className="add-button" onClick={handleAddRow}>
                        <i className="fa fa-plus-circle add-icon" aria-hidden="true">
                          +
                        </i>
                      </button>
                    ) : (
                      <button className="delete-button" onClick={() => handleDeleteRow(index)}>
                        <i className="fa fa-times-circle delete-icon" aria-hidden="true">
                          x
                        </i>
                      </button>
                    )}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
          <div className="botoes">
            <button className="clear-all-button" onClick={handleClearAll}>
              Limpar Tudo
            </button>
            <button className="cadastrar-doacao-button" onClick={handleCadastrarDoacao}>
              Cadastrar Doação
            </button>
          </div>
          {errorMessage && (
            <div className="error-message">
              <p className="error-text">{errorMessage}</p>
            </div>
          )}
          {doacaoRealizada && (
            <div className="popup success-popup">
              <p>Doação realizada com sucesso!</p>
            </div>
          )}
        </div>
  );
}

export default Menu;
