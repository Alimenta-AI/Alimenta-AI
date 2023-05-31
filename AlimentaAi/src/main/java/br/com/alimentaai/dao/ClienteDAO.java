package br.com.alimentaai.dao;

import br.com.alimentaai.model.Cliente;
import com.google.gson.Gson;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;

public class ClienteDAO {

    private Connection con;

    public final Connection getCon() {
        return con;
    }

    public final void setCon(Connection con) {
        this.con = con;
    }

    public ClienteDAO(Connection con) {
        setCon(con);
    }

    public Cliente buscarTipoCliente(String clienteId) {
        String sql = "SELECT * FROM cliente WHERE clienteid = ?";
        try {
            PreparedStatement stmt = con.prepareStatement(sql);
            stmt.setString(1, clienteId);
            ResultSet rs = stmt.executeQuery();
            if (rs.next()) {
                Cliente cliente = new Cliente();
                cliente.setNome(rs.getString("nome"));
                cliente.setEmail(rs.getString("email"));
                cliente.setSenha(rs.getString("senha"));
                cliente.setCelular(rs.getString("celular"));
                cliente.setEndereco(rs.getString("endereco"));
                cliente.setClienteId(rs.getString("clienteId"));
                cliente.setTipoCliente(rs.getInt("tipoCliente"));
                return cliente;
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return null;
    }

    public Cliente buscarEmail(String email) {
        String sql = "SELECT * FROM cliente WHERE email = ?";
        try {
            PreparedStatement stmt = con.prepareStatement(sql);
            stmt.setString(1, email);
            ResultSet rs = stmt.executeQuery();
            if (rs.next()) {
                Cliente cliente = new Cliente();
                cliente.setNome(rs.getString("nome"));
                cliente.setEmail(rs.getString("email"));
                cliente.setSenha(rs.getString("senha"));
                cliente.setCelular(rs.getString("celular"));
                cliente.setEndereco(rs.getString("endereco"));
                cliente.setClienteId(rs.getString("clienteId"));
                cliente.setTipoCliente(rs.getInt("tipoCliente"));
                return cliente;
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return null;
    }
    /**
     * Faz o login de um usuário a partir dos dados JSON fornecidos.
     *
     * @param json uma string contendo os dados de login no formato JSON
     * @return um objeto do tipo JsonDataLoggedIn contendo os dados de login convertidos
     */
    public JsonDataLoggedIn login(String json) {
        Gson gson = new Gson();
        return gson.fromJson(json, JsonDataLoggedIn.class);
    }

    public String buscarSenha(String senha) {
        String sql = "SELECT * FROM cliente WHERE senha = ?";
        try {
            PreparedStatement stmt = con.prepareStatement(sql);
            stmt.setString(1, senha);
            ResultSet rs = stmt.executeQuery();
            if (rs.next()) {
                return senha;
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return null;
    }
    public static class JsonDataLoggedIn {
        private String email;
        private String senha;

        public String getEmail() {
            return email;
        }

        public String getSenha() {
            return senha;
        }
    }

}
