package br.com.alimentaai.controller;

import br.com.alimentaai.connection.Conexao;
import br.com.alimentaai.dao.UsuarioDAO;
import br.com.alimentaai.model.Usuario;
import br.com.alimentaai.service.UsuarioService;
import com.google.gson.Gson;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.sql.Connection;
import java.sql.Date;

public class UsuarioController {
    public Usuario cadastrarUsuario(Usuario usuario){
        Connection con = Conexao.abrirConexao();
        UsuarioDAO usuarioDAO = new UsuarioDAO(con);
        UsuarioService usuarioService = new UsuarioService();

        String nome = usuario.getNome();
        String email = usuario.getEmail();
        String senha = usuario.getSenha();
        String celular = usuario.getCelular();
        String endereco = usuario.getEndereco();
        String cpf = usuario.getCpf();
        String nascimento = usuario.getNascimento();

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

        if (usuarioService.validarDadosUsuario(nome, email, senha, celular, cpf, nascimento, endereco)) {
            usuario.setNome(nome);
            usuario.setEmail(email);
            usuario.setSenha(senhaEncriptada);
            usuario.setCelular(celular);
            usuario.setEndereco(endereco);
            usuario.setCpf(cpf);
            usuario.setNascimento(nascimento);

            System.out.println(usuario);
            System.out.println(usuarioDAO.inserir(usuario));

        } else {
            System.out.println("Os dados do usuário não são válidos.");
            return null;
        }
        Conexao.fecharConexao(con);
        return usuario;
    }
    public Usuario cadastro(String json) {
        Gson gson = new Gson();
        return gson.fromJson(json, Usuario.class);
    }
}
