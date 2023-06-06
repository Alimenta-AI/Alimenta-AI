package br.com.alimentaai.dao;

import br.com.alimentaai.model.Cliente;
import com.google.gson.Gson;
import oracle.jdbc.internal.OraclePreparedStatement;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

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

    public Cliente buscarTipoClientePeloClienteId(String clienteId) {
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

    public List<Cliente> buscarClientesPeloTipo(int tipoCliente) {
        if(tipoCliente == 0){
            tipoCliente = 1;
        }
        else{
            tipoCliente = 0;
        }
        String sql = "SELECT * FROM cliente WHERE tipoCliente = ?";
        ArrayList<Cliente> clientes = new ArrayList<>();
        try {
            PreparedStatement stmt = con.prepareStatement(sql);
            stmt.setInt(1, tipoCliente);
            ResultSet rs = stmt.executeQuery();
            if (rs != null) {
                while (rs.next()) {
                    Cliente cliente = new Cliente();
                    cliente.setNome(rs.getString(2));
                    cliente.setEmail(rs.getString(3));
                    cliente.setSenha(rs.getString(4));
                    cliente.setCelular(rs.getString(5));
                    cliente.setEndereco(rs.getString(6));
                    cliente.setClienteId(rs.getString(1));
                    cliente.setTipoCliente(rs.getInt(7));
                    clientes.add(cliente);
                }
                return clientes;
            } else {
                return null;
            }
        } catch (SQLException e) {
            return null;
        }
    }

    public Cliente buscarEmail(String email) {
        String sql = "SELECT * FROM cliente WHERE email = ?";
        try {
            PreparedStatement stmt = con.prepareStatement(sql);
            stmt.setString(1, email);
            ResultSet rs = stmt.executeQuery();
            if (rs.next()) {
                Cliente cliente = new Cliente();
                cliente.setClienteId(rs.getString("clienteId"));
                cliente.setNome(rs.getString("nome"));
                cliente.setEmail(rs.getString("email"));
                cliente.setSenha(rs.getString("senha"));
                cliente.setCelular(rs.getString("celular"));
                cliente.setEndereco(rs.getString("endereco"));
                cliente.setTipoCliente(rs.getInt("tipoCliente"));
                return cliente;
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return null;
    }

    public JsonDataLoggedIn login(String json) {
        Gson gson = new Gson();
        return gson.fromJson(json, JsonDataLoggedIn.class);
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
