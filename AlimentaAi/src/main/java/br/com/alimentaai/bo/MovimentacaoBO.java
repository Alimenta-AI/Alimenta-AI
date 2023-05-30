package br.com.alimentaai.bo;

import br.com.alimentaai.controller.MovimentacaoController;
import br.com.alimentaai.model.Movimentacao;

public class MovimentacaoBO {
    private MovimentacaoController mc;
    public Movimentacao cadastrarMovimentacaoBo(String json) {
        mc = new MovimentacaoController();
        Movimentacao dadosMovimentacao = mc.cadastro(json);
        return mc.cadastrarMovimentacao(dadosMovimentacao);
    }
}
