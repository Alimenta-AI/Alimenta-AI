package br.com.alimentaai.apiresource;

import javax.ws.rs.*;
import javax.ws.rs.core.*;

import br.com.alimentaai.bo.UsuarioBO;
import br.com.alimentaai.model.Usuario;

import java.io.IOException;

@Path("/usuario")
public class UserResource {
    private UsuarioBO usuarioBO = new UsuarioBO();

    @PUT
    @Consumes(MediaType.APPLICATION_JSON)
    public Response atualizaUsuario(String json, @Context UriInfo uriInfo) throws IOException {
        System.out.println(json);
        Usuario atualizando = usuarioBO.atualizarUsuarioBo(json);
        UriBuilder builder = uriInfo.getAbsolutePathBuilder();
        builder.path((atualizando.getNome()));
        return Response.created(builder.build()).build();
    }

    @DELETE
    @Consumes(MediaType.APPLICATION_JSON)
    public Response excluirUsuario(String json, @Context UriInfo uriInfo) {
        System.out.println(json);
        Usuario excluindo = usuarioBO.excluiUsuarioBo(json);
        UriBuilder builder = uriInfo.getAbsolutePathBuilder();
        builder.path((excluindo.getClienteId()));
        return Response.created(builder.build()).build();
    }
}
