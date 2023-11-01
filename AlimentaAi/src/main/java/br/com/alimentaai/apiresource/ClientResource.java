package br.com.alimentaai.apiresource;

import br.com.alimentaai.bo.ClienteBO;
import br.com.alimentaai.bo.InstituicaoBO;
import br.com.alimentaai.bo.MovimentacaoBO;
import br.com.alimentaai.bo.UsuarioBO;
import br.com.alimentaai.model.*;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;

import javax.ws.rs.*;
import javax.ws.rs.core.*;
import java.io.IOException;
import java.util.List;

@Path("/cliente")
public class ClientResource {
    private ClienteBO clienteBO = new ClienteBO();
    private UsuarioBO usuarioBO = new UsuarioBO();
    private InstituicaoBO instituicaoBO = new InstituicaoBO();

    @GET
    @Path("/{clienteId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response dadosCliente(@PathParam("clienteId") String clienteId) {
        Cliente cliente = clienteBO.dadosCliente(clienteId);
        if (cliente != null) {
            if (cliente.getTipoCliente() == 0) {
                Usuario usuario = usuarioBO.dadosUsuario(clienteId);
                if (usuario != null) {
                    MeuPerfil meuPerfil = new MeuPerfil(cliente, usuario);
                    try {
                        ObjectMapper mapper = new ObjectMapper();
                        String json = mapper.writeValueAsString(meuPerfil);
                        return Response.ok(json).build();
                    } catch (JsonProcessingException e) {
                        e.printStackTrace();
                        return Response.serverError().build();
                    }
                } else {
                    return Response.status(Response.Status.NOT_FOUND).build();
                }
            } else if (cliente.getTipoCliente() == 1) {
                Instituicao instituicao = instituicaoBO.dadosInstituicao(clienteId);
                if (instituicao != null) {
                    MinhaInstituicao minhaInstituicao = new MinhaInstituicao(cliente, instituicao);
                    try {
                        ObjectMapper mapper = new ObjectMapper();
                        String json = mapper.writeValueAsString(minhaInstituicao);
                        return Response.ok(json).build();
                    } catch (JsonProcessingException e) {
                        e.printStackTrace();
                        return Response.serverError().build();
                    }
                } else {
                    return Response.status(Response.Status.NOT_FOUND).build();
                }
            } else {
                return Response.status(Response.Status.BAD_REQUEST).build(); // Tipo de cliente inválido
            }
        } else {
            return Response.status(Response.Status.NOT_FOUND).build();
        }
    }

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

    @PUT
    @Consumes(MediaType.APPLICATION_JSON)
    public Response atualizaUsuario(String json, @Context UriInfo uriInfo) throws IOException {
        System.out.println(json);
        if (clienteBO.tipoCliente(json) == 0) {
            Usuario atualizando = usuarioBO.atualizarUsuarioBo(json);
            UriBuilder builder = uriInfo.getAbsolutePathBuilder();
            builder.path((atualizando.getNome()));
            return Response.ok(builder.build()).build();
        }
        else if (clienteBO.tipoCliente(json) == 1) {
            Instituicao atualizando = instituicaoBO.atualizarInstituicaoBo(json);
            UriBuilder builder = uriInfo.getAbsolutePathBuilder();
            builder.path((atualizando.getNome()));
            return Response.ok(builder.build()).build();
        } else {
            return Response.status(Response.Status.NOT_FOUND).build();
        }
    }

    @DELETE
    @Consumes(MediaType.APPLICATION_JSON)
    public Response excluirUsuario(String json, @Context UriInfo uriInfo) {
        System.out.println(json);
        if (clienteBO.tipoCliente(json) == 0) {
            Usuario excluiUsuario = usuarioBO.excluiUsuarioBo(json);
            UriBuilder builder = uriInfo.getAbsolutePathBuilder();
            builder.path((excluiUsuario.getClienteId()));
            return Response.ok(builder.build()).build();
        } else if(clienteBO.tipoCliente(json) == 1){
            Instituicao excluiInstituicao = instituicaoBO.excluiInstituicaoBo(json);
            UriBuilder builder = uriInfo.getAbsolutePathBuilder();
            builder.path((excluiInstituicao.getClienteId()));
            return Response.ok(builder.build()).build();
        }else {
            return Response.status(Response.Status.NOT_FOUND).build();
        }
    }
}
