package br.com.alimentaai.controller;

import br.com.alimentaai.connection.Conexao;
import br.com.alimentaai.dao.InstituicaoDAO;
import br.com.alimentaai.dao.UsuarioDAO;
import br.com.alimentaai.model.Instituicao;
import br.com.alimentaai.model.Usuario;
import br.com.alimentaai.service.InstituicaoService;
import br.com.alimentaai.service.UsuarioService;
import com.google.gson.Gson;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.sql.Connection;

public class InstituicaoController {

    public Instituicao cadastrarInstituicao(Instituicao instituicao){
        Connection con = Conexao.abrirConexao();
        InstituicaoDAO instituicaoDAO = new InstituicaoDAO(con);
        InstituicaoService instituicaoService = new InstituicaoService();
        ClienteController clienteController = new ClienteController();

        String clienteId = clienteController.generateUniqueId();

        String nome = instituicao.getNome();
        String email = instituicao.getEmail();
        String senha = instituicao.getSenha();
        String celular = instituicao.getCelular();
        String endereco = instituicao.getEndereco();
        String cnpj = instituicao.getCnpj();
        String website = instituicao.getWebsite();
        String tipo = instituicao.getTipo();
        String clienteIdFixo = clienteId;
        int tipoCliente = 1;

        // Cria um objeto MessageDigest para calcular o hash SHA-256 da senha
        MessageDigest digest;
        try {
            digest = MessageDigest.getInstance("SHA-256");
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
            return null;
        }

        // Encripta a senha usando o hash SHA-256
        byte[] hashSenha = digest.digest(senha.getBytes());

        // Converte o hash da senha para uma string hexadecimal de 20 caracteres
        StringBuilder hexString = new StringBuilder();
        for (int i = 0; i < hashSenha.length && i < 10; i++) {
            String hex = Integer.toHexString(0xff & hashSenha[i]);
            hexString.append(hex);
        }
        String senhaEncriptada = hexString.toString();

        if (instituicaoService.validarDadosInstituicao()) {
            instituicao.setNome(nome);
            instituicao.setEmail(email);
            instituicao.setSenha(senhaEncriptada);
            instituicao.setCelular(celular);
            instituicao.setEndereco(endereco);
            instituicao.setCnpj(cnpj);
            instituicao.setWebsite(website);
            instituicao.setTipo(tipo);
            instituicao.setClienteId(clienteIdFixo);
            instituicao.setTipoCliente(tipoCliente);

            System.out.println(instituicaoDAO.inserir(instituicao));

        } else {
            System.out.println("Os dados do usuário não são válidos.");
            return null;
        }
        Conexao.fecharConexao(con);
        return instituicao;
    }

    public Instituicao cadastro(String json) {
        Gson gson = new Gson();
        return gson.fromJson(json, Instituicao.class);
    }

}
