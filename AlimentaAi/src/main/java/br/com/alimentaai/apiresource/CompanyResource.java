package br.com.alimentaai.apiresource;

import br.com.alimentaai.bo.UsuarioBO;
import br.com.alimentaai.model.Usuario;

import javax.ws.rs.Consumes;
import javax.ws.rs.POST;
import javax.ws.rs.Path;
import javax.ws.rs.core.*;

@Path("/instituicao")
public class CompanyResource {
    private UsuarioBO usuarioBO = new UsuarioBO();

    @POST
    @Consumes(MediaType.APPLICATION_JSON)
    public Response cadastraInstituicao(String json, @Context UriInfo uriInfo) {
        System.out.println(json);
        Usuario cadastrando = usuarioBO.cadastrarUsuarioBo(json);
        UriBuilder builder = uriInfo.getAbsolutePathBuilder();
        builder.path((cadastrando.getNome()));
        return Response.created(builder.build()).build();
    }
}
