package br.com.alimentaai.bo;


import br.com.alimentaai.controller.UsuarioController;
import br.com.alimentaai.model.Usuario;

public class UsuarioBO {
    private UsuarioController uc;
    public Usuario cadastrarUsuarioBo(String json) {
        uc = new UsuarioController();
        Usuario dadosUsuario = uc.cadastro(json);
        System.out.println(dadosUsuario);
        return uc.cadastrarUsuario(dadosUsuario);
    }
}
