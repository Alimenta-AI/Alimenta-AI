package br.com.alimentaai.dao;

import br.com.alimentaai.model.Alimento;
import br.com.alimentaai.model.Cliente;

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

        Cliente cliente = new Cliente();

    public String inserir(Alimento alimento, String clienteId) {

        String sqlAlimento = "insert into alimento(alimentoId, nome, validade, quantidade, clienteId) values (?,?,?,?,?)";

        try (PreparedStatement ps = getCon().prepareStatement(sqlAlimento)) {
            ps.setString(1, alimento.getAlimentoId());
            ps.setString(2, alimento.getNome());
            ps.setString(3, alimento.getValidade());
            ps.setInt(4, alimento.getQuantidade());
            ps.setString(5, clienteId);
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



