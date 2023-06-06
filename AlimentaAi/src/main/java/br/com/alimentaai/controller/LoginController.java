package br.com.alimentaai.controller;

import br.com.alimentaai.connection.Conexao;
import br.com.alimentaai.dao.ClienteDAO;
import br.com.alimentaai.model.Cliente;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.sql.Connection;
import java.sql.SQLException;
import java.time.*;
import java.time.format.DateTimeFormatter;
import java.util.UUID;

public class LoginController {

    public boolean autenticarUsuario(String email, String senha) {
        try (Connection con = Conexao.abrirConexao()) {
            ClienteDAO clienteDAO = new ClienteDAO(con);

            Cliente cliente = clienteDAO.buscarEmail(email);
            System.out.println(cliente);
            if (cliente != null) {
                MessageDigest digest;
                try {
                    digest = MessageDigest.getInstance("SHA-256");
                } catch (NoSuchAlgorithmException e) {
                    e.printStackTrace();
                    return false;
                }
                byte[] hashSenha = digest.digest(senha.getBytes());
                StringBuilder hexString = new StringBuilder();
                for (int i = 0; i < hashSenha.length && i < 10; i++) {
                    String hex = Integer.toHexString(0xff & hashSenha[i]);
                    hexString.append(hex);
                }
                String senhaEncriptada = hexString.toString();

                if (senhaEncriptada.equals(cliente.getSenha())) {
                    Conexao.fecharConexao(con);
                    return true;
                } else {
                    Conexao.fecharConexao(con);
                    return false; // Autenticação mal-sucedida
                }
            }
        } catch (SQLException e) {
            e.printStackTrace();
            return false;
        }
        return false;
    }
}
