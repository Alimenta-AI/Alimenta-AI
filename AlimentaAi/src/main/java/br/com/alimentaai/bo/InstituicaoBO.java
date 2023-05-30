package br.com.alimentaai.bo;

import br.com.alimentaai.controller.InstituicaoController;
import br.com.alimentaai.model.Instituicao;

public class InstituicaoBO {
    private InstituicaoController ic;
    public Instituicao cadastrarInstituicaoBo(String json) {
        ic = new InstituicaoController();
        Instituicao dadosInstituicao = ic.cadastro(json);
        return ic.cadastrarInstituicao(dadosInstituicao);
    }
}
