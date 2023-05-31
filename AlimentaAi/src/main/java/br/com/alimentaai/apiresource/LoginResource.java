package br.com.alimentaai.apiresource;

import br.com.alimentaai.bo.ClienteBO;
import br.com.alimentaai.bo.LoginBO;
import br.com.alimentaai.model.Cliente;

import javax.ws.rs.Consumes;
import javax.ws.rs.POST;
import javax.ws.rs.Path;
import javax.ws.rs.core.*;


@Path("/login")
public class LoginResource {
    private LoginBO loginBO = new LoginBO();

    @POST
    @Consumes(MediaType.APPLICATION_JSON)
    public Response logar(String json, @Context UriInfo uriInfo) {
//        String jsonTeste = "{\"email\": \"matpierro570@gmail.com\", \"senha\":\"matheus9\"}";
        System.out.println(json);
        Cliente logando = loginBO.loginBo(json);
        UriBuilder builder = uriInfo.getAbsolutePathBuilder();
        builder.path((logando.getEmail()));

        return Response.created(builder.build()).build();
    }
}
