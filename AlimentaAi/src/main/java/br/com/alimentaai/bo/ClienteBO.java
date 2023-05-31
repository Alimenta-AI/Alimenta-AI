package br.com.alimentaai.bo;

import br.com.alimentaai.controller.ClienteController;

import java.sql.Connection;

public class ClienteBO {
    private ClienteController cc;

    public int dadosClienteLogado(String clienteId) {
        cc = new ClienteController();
        return cc.recebeDadosCliente(clienteId);
    }

}
