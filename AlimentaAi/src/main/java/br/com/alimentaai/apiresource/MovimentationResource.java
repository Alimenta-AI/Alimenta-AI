package br.com.alimentaai.apiresource;

import br.com.alimentaai.bo.ClienteBO;
import br.com.alimentaai.bo.MovimentacaoBO;
import br.com.alimentaai.model.Cliente;
import br.com.alimentaai.model.Movimentacao;

import javax.ws.rs.*;
import javax.ws.rs.core.*;

@Path("/movimentacao")
public class MovimentationResource {
    private MovimentacaoBO movimentacaoBO = new MovimentacaoBO();
    ClienteBO clienteBO;

//    @GET
//    @Path("/{clienteId}")
//    @Produces(MediaType.APPLICATION_JSON)
//    public String buscarOpçõesMovimentacoes(@PathParam("clienteId") int clienteId) {
//        clienteBO = new ClienteBO();
//        if (clienteBO.dadosClienteLogado(String.valueOf(clienteId)) == 0) {
////            mostra as instituicoes pro usuario
//        }
////            mostrar os usuarios pra instituicao
//    }


    @POST
    @Consumes(MediaType.APPLICATION_JSON)
    public Response cadastraMovimentacao(String json, @Context UriInfo uriInfo) {
        System.out.println(json);
        Movimentacao cadastrando = movimentacaoBO.cadastrarMovimentacaoBo(json);
        UriBuilder builder = uriInfo.getAbsolutePathBuilder();
        builder.path((cadastrando.getNum_solicitacao()));
        return Response.created(builder.build()).build();
    }
}

