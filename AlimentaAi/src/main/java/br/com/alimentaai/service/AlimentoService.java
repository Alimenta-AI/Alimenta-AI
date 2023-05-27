package br.com.alimentaai.service;

public class AlimentoService {

    public boolean validarDadosAlimento(String alimentoId, String nome, String descricao, String validade, int quantidade) {

        boolean dadosValidos = true;

        // Validar o alimentoId
        if (alimentoId == null || alimentoId.trim().equals("")) {
            dadosValidos = false;//validarAlimentoId(alimentoId);
        }

        // Validar o nome
        if (nome == null || nome.trim().equals("")) {
            dadosValidos = false;//validaNome(nome);
        }

        // Validar a descricao
        if (descricao == null || descricao.trim().equals("")) {
            dadosValidos = false;//validarDescricao(descricao);
        }
        // Validar a validade
        if (validade == null || validade.trim().equals("")) {
            dadosValidos = false;//validarValidade(validade);
        }
        // Validar o quantidade
        if (quantidade == 0) {
            dadosValidos = false;
        }
        return dadosValidos;
    }
}

//Fazer uma validação do nome da empresa, conferindo se tera no banco de dados
//Fazer uma validação da validade do produto, contendo 7 dias no mínimo de prazo
