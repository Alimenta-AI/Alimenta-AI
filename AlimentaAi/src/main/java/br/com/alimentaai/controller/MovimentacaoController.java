package br.com.alimentaai.controller;

import br.com.alimentaai.connection.Conexao;
import br.com.alimentaai.dao.MovimentacaoDAO;
import br.com.alimentaai.model.Movimentacao;
import br.com.alimentaai.service.MovimentacaoService;
import com.google.gson.Gson;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

import java.sql.Connection;

public class MovimentacaoController {
    public Movimentacao cadastrarMovimentacao(Movimentacao movimentacao, String dadosClienteUsuario, String dadosClienteInstituicao){
        Connection con = Conexao.abrirConexao();
        MovimentacaoDAO movimentacaoDAO = new MovimentacaoDAO(con);
        MovimentacaoService movimentacaoService = new MovimentacaoService();

        LocalDateTime dataAtual = LocalDateTime.now();
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("ddMMyyyyHHmm");
        String dataFormatada = dataAtual.format(formatter);

        String num_solicitacao = movimentacaoDAO.novoNumeroSolicitacao();
        String data_movimentacao = dataFormatada;
        String descricao = movimentacao.getDescricao();
        String categoria = movimentacao.getCategoria();

        if (movimentacaoService.validarDadosMovimentacao(num_solicitacao, data_movimentacao, descricao, categoria)) {
            movimentacao.setNum_solicitacao(num_solicitacao);
            movimentacao.setData_movimentacao(data_movimentacao);
            movimentacao.setDescricao(descricao);
            movimentacao.setCategoria(categoria);

            System.out.println(movimentacaoDAO.inserir(movimentacao, dadosClienteUsuario.replaceAll("\"", ""), dadosClienteInstituicao.replaceAll("\"", "")));

        } else {
            System.out.println("Os dados do movimentação não são válidos.");
            return null;
        }
        Conexao.fecharConexao(con);
        return movimentacao;
    }
    public Movimentacao cadastro(String json) {
        Gson gson = new Gson();
        return gson.fromJson(json, Movimentacao.class);
    }
}