package br.com.alimentaai.dao;

import br.com.alimentaai.model.Alimento;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class AlimentoDAO {
        private Connection con;
        public final Connection getCon() {
            return con;
        }
        public final void setCon(Connection con) {
            this.con = con;
        }
        public AlimentoDAO(Connection con) {
            setCon(con);
        }

    public String inserir(Alimento alimento) {
        String sqlAlimento = "insert into alimento(alimentoId, nome, descricao, validade, quantidade) values (?,?,?,?,?)";

        try (PreparedStatement ps = getCon().prepareStatement(sqlAlimento)) {
            ps.setString(1, alimento.getAlimentoId());
            ps.setString(2, alimento.getNome());
            ps.setString(3, alimento.getDescricao());
            ps.setString(4, alimento.getValidade());
            ps.setInt(5, alimento.getQuantidade());
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



