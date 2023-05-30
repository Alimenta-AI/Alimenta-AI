package br.com.alimentaai.dao;

import br.com.alimentaai.model.Movimentacao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class MovimentacaoDAO {
    private Connection con;
    public final Connection getCon() {
        return con;
    }
    public final void setCon(Connection con) {
        this.con = con;
    }
    public MovimentacaoDAO(Connection con) {
        setCon(con);
    }

    public String inserir(Movimentacao movimentacao) {

        String sqlMovimentacao = "insert into movimentacao(clienteIdUsuario, clienteIdInstituicao, num_solicitacao, data_movimentacao, descricao, categoria) values (?,?,?,?,?,?)";

        try {
            PreparedStatement ps = getCon().prepareStatement(sqlMovimentacao);
            ps.setString(1, movimentacao.getClienteIdUsuario());
            ps.setString(2, movimentacao.getClienteIdInstituicao());
            ps.setString(3, movimentacao.getNum_solicitacao());
            ps.setString(4, movimentacao.getData_movimentacao());
            ps.setString(5, movimentacao.getDescricao());
            ps.setString(6, movimentacao.getCategoria());
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