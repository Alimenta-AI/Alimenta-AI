package br.com.alimentaai.controller;

import br.com.alimentaai.connection.Conexao;
import br.com.alimentaai.dao.AlimentoDAO;
import br.com.alimentaai.model.Alimento;
import br.com.alimentaai.service.AlimentoService;
import com.google.gson.Gson;

import java.sql.Connection;

public class AlimentoController {
    public Alimento cadastrarAlimento(Alimento alimento){
        Connection con = Conexao.abrirConexao();
        AlimentoDAO alimentoDAO = new AlimentoDAO(con);
        AlimentoService alimentoService = new AlimentoService();

        String alimentoId = alimento.getAlimentoId();
        String nome = alimento.getNome();
        String descricao = alimento.getDescricao();
        String validade = alimento.getValidade();
        int quantidade = alimento.getQuantidade();



        if (alimentoService.validarDadosAlimento(alimentoId, nome, descricao, validade, quantidade)) {
            alimento.setAlimentoId(alimentoId);
            alimento.setNome(nome);
            alimento.setDescricao(descricao);
            alimento.setValidade(validade);
            alimento.setQuantidade(quantidade);

            System.out.println(alimentoDAO.inserir(alimento));

        } else {
            System.out.println("Os dados do alimento não são válidos.");
            return null;
        }
        Conexao.fecharConexao(con);
        return alimento;
    }
    public Alimento cadastro(String json) {
        Gson gson = new Gson();
        return gson.fromJson(json, Alimento.class);
    }
}