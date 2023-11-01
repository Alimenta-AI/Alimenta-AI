package br.com.alimentaai.dao;

import br.com.alimentaai.model.Instituicao;
import br.com.alimentaai.model.Usuario;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class InstituicaoDAO {
    private Connection con;
    public final Connection getCon() {
        return con;
    }
    public final void setCon(Connection con) {
        this.con = con;
    }
    public InstituicaoDAO(Connection con) {
        setCon(con);
    }

    public String inserir(Instituicao instituicao) {

        String sqlCliente = "insert into cliente(nome, email, senha, celular, endereco, clienteId, tipoCliente) values (?,?,?,?,?,?,?)";
        String sqlInstituicao = "insert into instituicao(clienteId, website, tipo, cnpj) values (?,?,?,?)";

        try {
            PreparedStatement ps = getCon().prepareStatement(sqlCliente);
            ps.setString(1, instituicao.getNome());
            ps.setString(2, instituicao.getEmail());
            ps.setString(3, instituicao.getSenha());
            ps.setString(4, instituicao.getCelular());
            ps.setString(5, instituicao.getEndereco());
            ps.setString(6, instituicao.getClienteId());
            ps.setInt(7, instituicao.getTipoCliente());
            if (ps.executeUpdate() > 0) {
                System.out.println("Inserido com sucesso.");
            } else {
                System.out.println("Erro ao inserir.");
            }
        } catch (SQLException e) {
            return e.getMessage();
        }
        try {
            PreparedStatement ps = getCon().prepareStatement(sqlInstituicao);
            ps.setString(1, instituicao.getClienteId());
            ps.setString(2, instituicao.getWebsite());
            ps.setString(3, instituicao.getTipo());
            ps.setString(4, instituicao.getCnpj());
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

    public Instituicao buscarInstituicaoPeloClienteId(String clienteId) {
        String sql = "SELECT * FROM instituicao WHERE clienteid = ?";
        try {
            PreparedStatement stmt = con.prepareStatement(sql);
            stmt.setString(1, clienteId);
            ResultSet rs = stmt.executeQuery();
            if (rs.next()) {
                Instituicao instituicao = new Instituicao();
                instituicao.setCnpj(rs.getString("cnpj"));
                instituicao.setWebsite(rs.getString("website"));
                instituicao.setTipo(rs.getString("tipo"));
                return instituicao;
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return null;
    }

    public String atualizar(Instituicao instituicao) {
        String sqlCliente = "UPDATE cliente SET nome = ?, email = ?, senha = ?, celular = ?, endereco = ?, tipoCliente = ? WHERE clienteId = ?";
        String sqlInstituicao = "UPDATE instituicao SET cnpj = ?, website = ?, tipo = ? WHERE clienteId = ?";

        try {
            PreparedStatement ps = getCon().prepareStatement(sqlCliente);
            ps.setString(1, instituicao.getNome());
            ps.setString(2, instituicao.getEmail());
            ps.setString(3, instituicao.getSenha());
            ps.setString(4, instituicao.getCelular());
            ps.setString(5, instituicao.getEndereco());
            ps.setInt(6, instituicao.getTipoCliente());
            ps.setString(7, instituicao.getClienteId());
            if (ps.executeUpdate() > 0) {
                System.out.println("Dados do cliente atualizados com sucesso.");
            } else {
                System.out.println("Erro ao atualizar os dados do cliente.");
            }
        } catch (SQLException e) {
            return e.getMessage();
        }
        try {
            PreparedStatement ps = getCon().prepareStatement(sqlInstituicao);
            ps.setString(1, instituicao.getCnpj());
            ps.setString(2, instituicao.getWebsite());
            ps.setString(3, instituicao.getTipo());
            ps.setString(4, instituicao.getClienteId());
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
        String sqlInstituicao = "DELETE FROM instituicao WHERE clienteId = ?";
        String sqlCliente = "DELETE FROM cliente WHERE clienteId = ?";
        try {
            PreparedStatement psUsuario = getCon().prepareStatement(sqlInstituicao);
            psUsuario.setString(1, clienteId);
            if (psUsuario.executeUpdate() > 0) {
                System.out.println("Instituição deletado com sucesso.");
            } else {
                System.out.println("Erro ao deletar o Instituição.");
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
