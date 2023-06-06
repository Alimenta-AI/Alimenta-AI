package br.com.alimentaai.apiresource;

import br.com.alimentaai.bo.ClienteBO;
import br.com.alimentaai.bo.InstituicaoBO;
import br.com.alimentaai.bo.MovimentacaoBO;
import br.com.alimentaai.bo.UsuarioBO;
import br.com.alimentaai.model.Cliente;
import br.com.alimentaai.model.Instituicao;
import br.com.alimentaai.model.Usuario;

import javax.ws.rs.*;
import javax.ws.rs.core.*;
import java.io.IOException;
import java.util.List;

@Path("/cliente")
public class ClientResource {
    private ClienteBO clienteBO = new ClienteBO();
    private UsuarioBO usuarioBO = new UsuarioBO();
    private InstituicaoBO instituicaoBO = new InstituicaoBO();

    @POST
    @Consumes(MediaType.APPLICATION_JSON)
    public Response cadastrarCliente(String json, @Context UriInfo uriInfo) throws IOException {
        System.out.println(json);
        if (clienteBO.tipoCliente(json) == 0) {
            Usuario cadastrando = usuarioBO.cadastrarUsuarioBo(json);
            UriBuilder builder = uriInfo.getAbsolutePathBuilder();
            builder.path((cadastrando.getNome()));
            return Response.created(builder.build()).build();
        } else {
            Instituicao cadastrando = instituicaoBO.cadastrarInstituicaoBo(json);
            UriBuilder builder = uriInfo.getAbsolutePathBuilder();
            builder.path((cadastrando.getNome()));
            return Response.created(builder.build()).build();
        }
    }

    @GET
    @Path("/{clienteId}")
    @Produces(MediaType.APPLICATION_JSON)
    public String buscarOpçõesMovimentacoes(@PathParam("clienteId") String clienteId) {
        System.out.println(clienteId);
        return clienteBO.listar(clienteId);
    }
}
