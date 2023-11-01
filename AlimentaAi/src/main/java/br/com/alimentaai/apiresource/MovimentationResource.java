package br.com.alimentaai.apiresource;

import br.com.alimentaai.bo.ClienteBO;
import br.com.alimentaai.bo.MovimentacaoBO;
import br.com.alimentaai.model.Cliente;
import br.com.alimentaai.model.Movimentacao;

import javax.ws.rs.*;
import javax.ws.rs.core.*;

@Path("/movimentacao")
public class MovimentationResource {

//    MovimentacaoBO movimentacaoBO = new MovimentacaoBO();
//
//    @POST
//    @Consumes(MediaType.APPLICATION_JSON)
//    public Response cadastraMovimentacao(String json, @Context UriInfo uriInfo) {
//        System.out.println(json);
//        Movimentacao cadastrando = movimentacaoBO.cadastrarMovimentacaoBo(json);
//        UriBuilder builder = uriInfo.getAbsolutePathBuilder();
//        builder.path((cadastrando.getNum_solicitacao()));
//        return Response.created(builder.build()).build();
//    }
}

