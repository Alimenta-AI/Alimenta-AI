package br.com.alimentaai.bo;

import br.com.alimentaai.connection.Conexao;
import br.com.alimentaai.controller.ClienteController;
import br.com.alimentaai.dao.ClienteDAO;
import br.com.alimentaai.model.Cliente;
import com.google.gson.Gson;

import java.sql.Connection;
import java.util.List;

public class ClienteBO {
    private ClienteController cc;

    public int tipoCliente(String json){
        cc = new ClienteController();
        return cc.verificaTipoCliente(json);
    }

    public Cliente dadosCliente(String clienteId){
        cc = new ClienteController();
        Cliente cliente = cc.recebeDadosCliente(clienteId);
        return cliente;
    }

}
