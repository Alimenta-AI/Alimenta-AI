package br.com.alimentaai.bo;

import br.com.alimentaai.controller.InstituicaoController;
import br.com.alimentaai.controller.UsuarioController;
import br.com.alimentaai.model.Instituicao;
import br.com.alimentaai.model.Usuario;

import java.io.IOException;

public class InstituicaoBO {
    private InstituicaoController ic;
    public Instituicao cadastrarInstituicaoBo(String json) {
        ic = new InstituicaoController();
        Instituicao dadosInstituicao = ic.instituicaoJsonToClass(json);
        return ic.cadastrarInstituicao(dadosInstituicao);
    }

    public Instituicao dadosInstituicao(String clienteId){
        ic = new InstituicaoController();
        return ic.recebeDadosInstituicao(clienteId);
    }

    public Instituicao atualizarInstituicaoBo(String json) throws IOException {
        ic = new InstituicaoController();
        Instituicao dadosInstituicao = ic.instituicaoJsonToClass(json);
        System.out.println(dadosInstituicao);
        return ic.atualizarInstituicao(dadosInstituicao);
    }

    public Instituicao excluiInstituicaoBo(String json) {
        ic = new InstituicaoController();
        Instituicao dadosInstituicao = ic.instituicaoJsonToClass(json);
        System.out.println(dadosInstituicao);
        return ic.excluirInstituicao(dadosInstituicao);
    }
}
