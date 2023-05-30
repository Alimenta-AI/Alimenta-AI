package br.com.alimentaai.apiresource;

import br.com.alimentaai.bo.InstituicaoBO;
import br.com.alimentaai.bo.UsuarioBO;
import br.com.alimentaai.model.Instituicao;
import br.com.alimentaai.model.Usuario;

import javax.ws.rs.Consumes;
import javax.ws.rs.POST;
import javax.ws.rs.Path;
import javax.ws.rs.core.*;

@Path("/instituicao")
public class CompanyResource {
    private InstituicaoBO instituicaoBO = new InstituicaoBO();

    @POST
    @Consumes(MediaType.APPLICATION_JSON)
    public Response cadastraInstituicao(String json, @Context UriInfo uriInfo) {
        System.out.println(json);
        Instituicao cadastrando = instituicaoBO.cadastrarInstituicaoBo(json);
        UriBuilder builder = uriInfo.getAbsolutePathBuilder();
        builder.path((cadastrando.getNome()));
        return Response.created(builder.build()).build();
    }
}
