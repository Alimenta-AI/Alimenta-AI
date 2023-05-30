package br.com.alimentaai.dao;

import br.com.alimentaai.model.Instituicao;
import br.com.alimentaai.model.Usuario;

import java.sql.Connection;
import java.sql.PreparedStatement;
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
}
