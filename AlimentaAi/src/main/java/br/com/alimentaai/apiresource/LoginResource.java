package br.com.alimentaai.apiresource;

import br.com.alimentaai.bo.ClienteBO;
import br.com.alimentaai.bo.LoginBO;
import br.com.alimentaai.controller.ClienteController;
import br.com.alimentaai.dao.ClienteDAO;
import br.com.alimentaai.model.Cliente;

import javax.ws.rs.Consumes;
import javax.ws.rs.POST;
import javax.ws.rs.Path;
import javax.ws.rs.core.*;


@Path("/login")
public class LoginResource {
    private LoginBO loginBO = new LoginBO();
    private ClienteController cc = new ClienteController();
    @POST
    @Consumes(MediaType.APPLICATION_JSON)
    public Response logar(String json, @Context UriInfo uriInfo) {
        System.out.println(json);
        Cliente logando = loginBO.loginBo(json);
        String logandoJson = cc.converterParaJson(logando);
        return Response.ok(logandoJson, MediaType.APPLICATION_JSON).build();
    }
}
