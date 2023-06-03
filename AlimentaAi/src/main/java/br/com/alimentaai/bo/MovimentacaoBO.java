package br.com.alimentaai.bo;

import br.com.alimentaai.controller.ClienteController;
import br.com.alimentaai.controller.MovimentacaoController;
import br.com.alimentaai.model.Cliente;
import br.com.alimentaai.model.Movimentacao;

public class MovimentacaoBO {
    private MovimentacaoController mc;
    private ClienteController cc;
    public Movimentacao cadastrarMovimentacaoBo(String json) {
        mc = new MovimentacaoController();
        cc = new ClienteController();
        Movimentacao dadosMovimentacao = mc.cadastro(json);
        String dadosClienteUsuario = cc.getIdUsuario(json);
        String dadosClienteInstituicao = cc.getIdInstituicao(json);
        return mc.cadastrarMovimentacao(dadosMovimentacao, dadosClienteUsuario, dadosClienteInstituicao);
    }
}
