package br.com.alimentaai.bo;

import br.com.alimentaai.controller.AlimentoController;
import br.com.alimentaai.model.Alimento;

public class AlimentoBO {
    private AlimentoController ac;
    public Alimento cadastrarAlimentoBo(String json) {
        ac = new AlimentoController();
        Alimento dadosAlimento = ac.cadastro(json);
        return ac.cadastrarAlimento(dadosAlimento);
    }
}
