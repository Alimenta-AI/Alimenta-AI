package br.com.alimentaai.controller;

import br.com.alimentaai.connection.Conexao;
import br.com.alimentaai.dao.AlimentoDAO;
import br.com.alimentaai.model.Alimento;
import br.com.alimentaai.model.Cliente;
import br.com.alimentaai.model.Usuario;
import br.com.alimentaai.service.AlimentoService;
import com.google.gson.*;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.sql.Connection;
import java.util.UUID;

public class AlimentoController {
    public Alimento cadastrarAlimento(Alimento alimento, String dadoClienteId){
        Connection con = Conexao.abrirConexao();
        AlimentoDAO alimentoDAO = new AlimentoDAO(con);
        AlimentoService alimentoService = new AlimentoService();
        AlimentoController alimentoController = new AlimentoController();

        String alimentoId = alimentoController.generateUniqueId();
        String alimentoIdFixo = alimentoId;
        String nome = alimento.getNome();
        String validade = alimento.getValidade();
        int quantidade = alimento.getQuantidade();
        String clienteId = dadoClienteId.replaceAll("\"", "");

        if (alimentoService.validarDadosAlimento(alimentoIdFixo, nome, validade, quantidade)) {
            alimento.setAlimentoId(alimentoIdFixo);
            alimento.setNome(nome);
            alimento.setValidade(validade);
            alimento.setQuantidade(quantidade);

            System.out.println(alimentoDAO.inserir(alimento, clienteId));

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

    public String generateUniqueId() {
        try {
            UUID uuid = UUID.randomUUID();
            MessageDigest sha1 = MessageDigest.getInstance("SHA-1");
            byte[] hashBytes = sha1.digest(uuid.toString().getBytes());
            StringBuilder hexString = new StringBuilder();
            for (byte b : hashBytes) {
                String hex = Integer.toHexString(0xFF & b);
                if (hex.length() == 1) {
                    hexString.append('0');
                }
                hexString.append(hex);
            }
            return hexString.toString().substring(0, 20);
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
        }
        return null;
    }
}