package br.com.alimentaai.controller;

import br.com.alimentaai.connection.Conexao;
import br.com.alimentaai.dao.MovimentacaoDAO;
import br.com.alimentaai.model.Movimentacao;
import br.com.alimentaai.service.MovimentacaoService;
import com.google.gson.Gson;

import java.sql.Connection;

public class MovimentacaoController {
    public Movimentacao cadastrarMovimentacao(Movimentacao movimentacao){
        Connection con = Conexao.abrirConexao();
        MovimentacaoDAO movimentacaoDAO = new MovimentacaoDAO(con);
        MovimentacaoService movimentacaoService = new MovimentacaoService();

        String clienteIdUsuario =  movimentacao.getClienteIdUsuario();
        String clienteIdInstituicao = movimentacao.getClienteIdInstituicao();
        String num_solicitacao = movimentacao.getNum_solicitacao();
        String data_movimentacao = movimentacao.getData_movimentacao();
        String descricao = movimentacao.getDescricao();
        String categoria = movimentacao.getCategoria();



        if (movimentacaoService.validarDadosMovimentacao(clienteIdUsuario, clienteIdInstituicao, num_solicitacao, data_movimentacao, descricao, categoria)) {
            movimentacao.setClienteIdUsuario(clienteIdUsuario);
            movimentacao.setClienteIdInstituicao(clienteIdInstituicao);
            movimentacao.setNum_solicitacao(num_solicitacao);
            movimentacao.setData_movimentacao(data_movimentacao);
            movimentacao.setDescricao(descricao);
            movimentacao.setCategoria(categoria);

            System.out.println(movimentacaoDAO.inserir(movimentacao));

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