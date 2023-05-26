package br.com.alimentaai.dao;

import br.com.alimentaai.model.Usuario;
import com.google.gson.Gson;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;


public class UsuarioDAO {
    private Connection con;
    public final Connection getCon() {
        return con;
    }
    public final void setCon(Connection con) {
        this.con = con;
    }
    public UsuarioDAO(Connection con) {
        setCon(con);
    }

    public String inserir(Usuario usuario) {

        String sqlCliente = "insert into cliente(nome, email, senha, celular, endereco, clienteId, tipoCliente) values (?,?,?,?,?,?,?)";
        String sqlUsuario = "insert into usuario(clienteId, cpf, nascimento) values (?,?,?)";

        try {
            PreparedStatement ps = getCon().prepareStatement(sqlCliente);
            ps.setString(1, usuario.getNome());
            ps.setString(2, usuario.getEmail());
            ps.setString(3, usuario.getSenha());
            ps.setString(4, usuario.getCelular());
            ps.setString(5, usuario.getEndereco());
            ps.setString(6, usuario.getClienteId());
            ps.setInt(7, usuario.getTipoCliente());
            if (ps.executeUpdate() > 0) {
                System.out.println("Inserido com sucesso.");
            } else {
                System.out.println("Erro ao inserir.");
            }
        } catch (SQLException e) {
            return e.getMessage();
        }
        try {
            PreparedStatement ps = getCon().prepareStatement(sqlUsuario);
            ps.setString(1, usuario.getClienteId());
            ps.setString(2, usuario.getCpf());
            ps.setString(3, usuario.getNascimento());
            if (ps.executeUpdate() > 0) {
                System.out.println("Inserido com sucesso.");
            } else {
                System.out.println("Erro ao inserir.");
            }
        } catch (SQLException e) {
            return e.getMessage();
        }

        return "Success";
    }
}