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
    private ClienteDAO cd;

    public String listar(String clienteId){
        cc = new ClienteController();
        int tipoCliente = cc.recebeDadosCliente(clienteId);
        Connection con = Conexao.abrirConexao();
        cd = new ClienteDAO(con);
        List<Cliente> clientes = cd.buscarClientesPeloTipo(tipoCliente);
        Conexao.fecharConexao(con);
        Gson gson = new Gson();
        String json = gson.toJson(clientes);
        return json;
    }

}
