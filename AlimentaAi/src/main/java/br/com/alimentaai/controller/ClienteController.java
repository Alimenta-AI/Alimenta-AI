package br.com.alimentaai.controller;

import br.com.alimentaai.connection.Conexao;
import br.com.alimentaai.dao.ClienteDAO;
import br.com.alimentaai.model.Cliente;
import com.google.gson.Gson;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.sql.Connection;
import java.util.UUID;

public class ClienteController {

    public Cliente recebeDadosCliente(String clienteId){
        Connection con= Conexao.abrirConexao();
        ClienteDAO clienteDAO = new ClienteDAO(con);
        Cliente cliente = clienteDAO.buscarClientePeloClienteId(clienteId);
        if(cliente != null){
            Conexao.fecharConexao(con);
            return cliente;
        }
        else{
            Conexao.fecharConexao(con);
            System.out.println("Erro ao buscar cliente");
            return null;
        }
    }

    public String generateUniqueId() {
        try {
            UUID uuid = UUID.randomUUID();
            MessageDigest sha1 = MessageDigest.getInstance("SHA-1");
            byte[] hashBytes = sha1.digest(uuid.toString().getBytes());
            StringBuilder hexString = new StringBuilder();
            for (byte b : hashBytes) {
                String hex = Integer.toHexString(0xFF & b);
                if (hex.length() == 1) {
                    hexString.append('0');
                }
                hexString.append(hex);
            }
            return hexString.toString().substring(0, 20);
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
        }
        return null;
    }

    public String cadastro(String json) {
        Gson gson = new Gson();
        JsonElement element = JsonParser.parseString(json);
        if (element.isJsonObject()) {
            JsonObject jsonObject = element.getAsJsonObject();
            String[] fieldNames = gson.fromJson(String.valueOf(jsonObject.keySet()), String[].class);
            if (fieldNames.length > 0) {
                String lastFieldName = fieldNames[fieldNames.length - 1];
                JsonElement lastValue = jsonObject.get(lastFieldName);

                return gson.toJson(lastValue);
            }
        }
        return null;
    }

    public int verificaTipoCliente(String json){
        JsonParser parser = new JsonParser();
        JsonObject jsonObject = parser.parse(json).getAsJsonObject();
        int tipoCliente = jsonObject.get("tipoCliente").getAsInt();
        System.out.println("Tipo de Cliente: " + tipoCliente);
        return tipoCliente;
    }

    public String getIdUsuario(String json) {
        Gson gson = new Gson();
        JsonElement element = JsonParser.parseString(json);
        if (element.isJsonObject()) {
            JsonObject jsonObject = element.getAsJsonObject();
            if (jsonObject.has("clienteIdUsuario")) {
                JsonElement clienteIdUsuario = jsonObject.get("clienteIdUsuario");
                return gson.toJson(clienteIdUsuario);
            }
        }
        return null;
    }

    public String getIdInstituicao(String json) {
        Gson gson = new Gson();
        JsonElement element = JsonParser.parseString(json);
        if (element.isJsonObject()) {
            JsonObject jsonObject = element.getAsJsonObject();
            if (jsonObject.has("clienteIdInstituicao")) {
                JsonElement clienteIdInstituicao = jsonObject.get("clienteIdInstituicao");
                return gson.toJson(clienteIdInstituicao);
            }
        }
        return null;
    }

    public String converterParaJson(Cliente cliente) {
        Gson gson = new Gson();
        String json = gson.toJson(cliente);
        return json;
    }

}
