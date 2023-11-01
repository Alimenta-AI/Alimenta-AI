package br.com.alimentaai.bo;


import br.com.alimentaai.controller.ClienteController;
import br.com.alimentaai.controller.UsuarioController;
import br.com.alimentaai.model.Cliente;
import br.com.alimentaai.model.Usuario;

import java.io.IOException;

public class UsuarioBO {
    private UsuarioController uc;

    public Usuario dadosUsuario(String clienteId){
        uc = new UsuarioController();
        return uc.recebeDadosUsuario(clienteId);
    }

    public Usuario cadastrarUsuarioBo(String json) throws IOException {
        uc = new UsuarioController();
        Usuario dadosUsuario = uc.usuarioJsonToClass(json);
        return uc.cadastrarUsuario(dadosUsuario);
    }

    public Usuario atualizarUsuarioBo(String json) throws IOException {
        uc = new UsuarioController();
        Usuario dadosUsuario = uc.usuarioJsonToClass(json);
        System.out.println(dadosUsuario);
        return uc.atualizarUsuario(dadosUsuario);
    }

    public Usuario excluiUsuarioBo(String json) {
        uc = new UsuarioController();
        Usuario dadosUsuario = uc.usuarioJsonToClass(json);
        System.out.println(dadosUsuario);
        return uc.excluirUsuario(dadosUsuario);
    }
}
