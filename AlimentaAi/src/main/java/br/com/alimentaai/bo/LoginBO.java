package br.com.alimentaai.bo;

import br.com.alimentaai.connection.Conexao;
import br.com.alimentaai.controller.LoginController;
import br.com.alimentaai.dao.ClienteDAO;
import br.com.alimentaai.model.Cliente;

import java.sql.Connection;
public class LoginBO {
    private ClienteDAO cd;
    private LoginController lc;
    public Cliente loginBo(String json) {
        Connection con = Conexao.abrirConexao();
        cd = new ClienteDAO(con);
        lc = new LoginController();
        ClienteDAO.JsonDataLoggedIn dadosAutenticar = cd.login(json);
        Boolean responseAuth = lc.autenticarUsuario(dadosAutenticar.getEmail(), dadosAutenticar.getSenha());
        if(responseAuth){
            Cliente cliente = new Cliente();
            cliente = cd.buscarEmail(dadosAutenticar.getEmail());
            Conexao.fecharConexao(con);
            return cliente;
        }
        return null;
    }
}
