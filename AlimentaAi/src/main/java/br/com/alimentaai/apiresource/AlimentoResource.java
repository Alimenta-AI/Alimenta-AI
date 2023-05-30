package br.com.alimentaai.apiresource;

import br.com.alimentaai.bo.AlimentoBO;
import br.com.alimentaai.model.Alimento;
import javax.ws.rs.Consumes;
import javax.ws.rs.POST;
import javax.ws.rs.Path;
import javax.ws.rs.core.*;

@Path("/alimento")
public class AlimentoResource {
    private AlimentoBO alimentoBO = new AlimentoBO();
    @POST
    @Consumes(MediaType.APPLICATION_JSON)
    public Response cadastraAlimento(String json, @Context UriInfo uriInfo) {
        System.out.println(json);
        Alimento cadastrando = alimentoBO.cadastrarAlimentoBo(json);
        UriBuilder builder = uriInfo.getAbsolutePathBuilder();
        builder.path((cadastrando.getNome()));
        return Response.created(builder.build()).build();
    }
}


