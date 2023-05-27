package br.com.alimentaai.apiresource;

import javax.ws.rs.*;
import javax.ws.rs.core.*;

import br.com.alimentaai.bo.UsuarioBO;
import br.com.alimentaai.model.Usuario;

@Path("/usuario")
public class UserResource {
    private UsuarioBO usuarioBO = new UsuarioBO();

    @POST
    @Consumes(MediaType.APPLICATION_JSON)
    public Response cadastraUsuario(String json, @Context UriInfo uriInfo) {
        System.out.println(json);
        Usuario cadastrando = usuarioBO.cadastrarUsuarioBo(json);
        UriBuilder builder = uriInfo.getAbsolutePathBuilder();
        builder.path((cadastrando.getNome()));
        return Response.created(builder.build()).build();
    }
}
