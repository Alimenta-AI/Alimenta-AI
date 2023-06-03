package br.com.alimentaai.dao;

import br.com.alimentaai.model.Usuario;

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

        System.out.println(usuario.getDoador());

        String sqlCliente = "insert into cliente(nome, email, senha, celular, endereco, clienteId, tipoCliente) values (?,?,?,?,?,?,?)";
        String sqlUsuario = "insert into usuario(clienteId, cpf, nascimento, doador) values (?,?,?,?)";

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
            ps.setString(4, usuario.getDoador());
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

    public String atualizar(Usuario usuario) {
        String sqlCliente = "UPDATE cliente SET nome = ?, email = ?, senha = ?, celular = ?, endereco = ?, tipoCliente = ? WHERE clienteId = ?";
        String sqlUsuario = "UPDATE usuario SET cpf = ?, nascimento = ?, doador = ? WHERE clienteId = ?";

        try {
            PreparedStatement ps = getCon().prepareStatement(sqlCliente);
            ps.setString(1, usuario.getNome());
            ps.setString(2, usuario.getEmail());
            ps.setString(3, usuario.getSenha());
            ps.setString(4, usuario.getCelular());
            ps.setString(5, usuario.getEndereco());
            ps.setInt(6, usuario.getTipoCliente());
            ps.setString(7, usuario.getClienteId());
            if (ps.executeUpdate() > 0) {
                System.out.println("Dados do cliente atualizados com sucesso.");
            } else {
                System.out.println("Erro ao atualizar os dados do cliente.");
            }
        } catch (SQLException e) {
            return e.getMessage();
        }
        try {
            PreparedStatement ps = getCon().prepareStatement(sqlUsuario);
            ps.setString(1, usuario.getCpf());
            ps.setString(2, usuario.getNascimento());
            ps.setString(3, usuario.getDoador());
            ps.setString(4, usuario.getClienteId());
            if (ps.executeUpdate() > 0) {
                System.out.println("Dados do usuário atualizados com sucesso.");
            } else {
                System.out.println("Erro ao atualizar os dados do usuário.");
            }
        } catch (SQLException e) {
            return e.getMessage();
        }
        return "Success";
    }

    public String deletar(String clienteId) {
        String sqlUsuario = "DELETE FROM usuario WHERE clienteId = ?";
        String sqlCliente = "DELETE FROM cliente WHERE clienteId = ?";
        try {
            PreparedStatement psUsuario = getCon().prepareStatement(sqlUsuario);
            psUsuario.setString(1, clienteId);
            if (psUsuario.executeUpdate() > 0) {
                System.out.println("Usuário deletado com sucesso.");
            } else {
                System.out.println("Erro ao deletar o usuário.");
            }
        } catch (SQLException e) {
            return e.getMessage();
        }
        try {
            PreparedStatement psCliente = getCon().prepareStatement(sqlCliente);
            psCliente.setString(1, clienteId);
            if (psCliente.executeUpdate() > 0) {
                System.out.println("Cliente deletado com sucesso.");
            } else {
                System.out.println("Erro ao deletar o cliente.");
            }
        } catch (SQLException e) {
            return e.getMessage();
        }
        return "Success";
    }

}