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
    private LocalDateTime inicioSessao;
    private LocalDateTime fimSessao;
    // Autentica um usuário com o nome ou email e a senha encriptada
    public boolean autenticarUsuario(String email, String senha) {
        try (Connection con = Conexao.abrirConexao()) {
            ClienteDAO clienteDAO = new ClienteDAO(con);

            Cliente cliente = clienteDAO.buscarEmail(email);
            if (cliente != null) {
                // Cria um objeto MessageDigest para calcular o hash SHA-256 da senha fornecida pelo usuário
                MessageDigest digest;
                try {
                    digest = MessageDigest.getInstance("SHA-256");
                } catch (NoSuchAlgorithmException e) {
                    e.printStackTrace();
                    return false;
                }

                // Encripta a senha fornecida pelo usuário usando o hash SHA-256
                byte[] hashSenha = digest.digest(senha.getBytes());

                // Converte o hash da senha para uma string hexadecimal
                StringBuilder hexString = new StringBuilder();
                for (int i = 0; i < hashSenha.length && i < 10; i++) {
                    String hex = Integer.toHexString(0xff & hashSenha[i]);
                    hexString.append(hex);
                }
                String senhaEncriptada = hexString.toString();

                // Compara a senha encriptada fornecida pelo usuário com a senha encriptada armazenada no banco de dados
                if (senhaEncriptada.equals(clienteDAO.buscarSenha(senhaEncriptada))) {
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
