package br.com.alimentaai.service;

public class MovimentacaoService {
    public boolean validarDadosMovimentacao(String clienteIdUsuario, String clienteIdInstituicao, String num_solicitacao, String data_movimentacao, String descricao, String categoria) {

        boolean dadosValidos = true;

        // Validar o clienteIdUsuario
        if (clienteIdUsuario == null || clienteIdUsuario.trim().equals("")) {
            dadosValidos = false;//validaclienteIdUsuario(clienteIdUsuario);
        }

        // Validar o clienteIdInstituicao
        if (clienteIdInstituicao == null || clienteIdInstituicao.trim().equals("")) {
            dadosValidos = false;//validaclienteIdInstituicao(clienteIdInstituicao);
        }

        // Validar o num_solicitacao
        if (num_solicitacao == null || num_solicitacao.trim().equals("")) {
            dadosValidos = false;//validarnum_solicitacao(num_solicitacao);
        }
        // Validar a data_movimentacao
        if (data_movimentacao == null || data_movimentacao.trim().equals("")) {
            dadosValidos = false;//validardata_movimentacao(data_movimentacao);
        }
        // Validar a descricao
        if (descricao == null || descricao.trim().equals("")) {
            dadosValidos = false;//validardescricao(descricao);
        }
        //Validar a categoria
        if (categoria == null || categoria.trim().equals("")) {
            dadosValidos = false;//validarcategoria(categoria);
        }
        return dadosValidos;
    }
}