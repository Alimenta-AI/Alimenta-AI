package br.com.alimentaai.dao;

import br.com.alimentaai.model.Cliente;

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

}
