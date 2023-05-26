package br.com.alimentaai.bo;


import br.com.alimentaai.connection.Conexao;
//import br.com.uinvest.controller.LoginController;
//import br.com.uinvest.controller.UsuarioController;
//import br.com.uinvest.dao.UsuarioDAO;
import br.com.alimentaai.model.Usuario;
import com.google.gson.Gson;

import java.sql.Connection;

public class UsuarioBO {
    private UsuarioDAO ud;
    private UsuarioController uc;
    private LoginController lc;

    public Usuario cadastrarUsuarioBo(String json) {
        Connection con = Conexao.abrirConexao();
        ud = new UsuarioDAO(con);
        uc = new UsuarioController();
        Usuario dadosUsuario = ud.cadastro(json);
        return uc.cadastrarUsuario(dadosUsuario);
    }
}
