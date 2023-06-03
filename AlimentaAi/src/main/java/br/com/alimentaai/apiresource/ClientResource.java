package br.com.alimentaai.apiresource;

import br.com.alimentaai.bo.ClienteBO;
import br.com.alimentaai.bo.MovimentacaoBO;
import br.com.alimentaai.model.Cliente;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;
import java.util.List;

@Path("/cliente")
public class ClientResource {
        private ClienteBO clienteBO = new ClienteBO();

        @GET
        @Path("/{clienteId}")
        @Produces(MediaType.APPLICATION_JSON)
        public String buscarOpçõesMovimentacoes(@PathParam("clienteId") String clienteId) {
                System.out.println(clienteId);
                return clienteBO.listar(clienteId);
        }
}
