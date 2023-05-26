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

        String sql = "insert into usuario(clienteid, cpf, nome, email, senha, celular, endereco, nascimento) values (?,?,?,?,?,?)";
        try {
            PreparedStatement ps = getCon().prepareStatement(sql);
            ps.setString(1, usuario.getNome());
            ps.setString(2, usuario.getEmail());
            ps.setString(3, usuario.getSenha());
            ps.setString(4, usuario.getCelular());
            ps.setString(5, usuario.getCpf());
            ps.setString(6, usuario.getNascimento());
            if (ps.executeUpdate() > 0) {
                return "Inserido com sucesso.";
            } else {
                return "Erro ao inserir.";
            }
        } catch (SQLException e) {
            return e.getMessage();
        }
    }
}