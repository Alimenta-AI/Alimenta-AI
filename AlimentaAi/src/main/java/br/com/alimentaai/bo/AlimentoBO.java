package br.com.alimentaai.bo;

import br.com.alimentaai.controller.AlimentoController;
import br.com.alimentaai.controller.ClienteController;
import br.com.alimentaai.model.Alimento;
import br.com.alimentaai.model.Cliente;

public class AlimentoBO {
    private AlimentoController ac;
    private ClienteController cc;
    public Alimento cadastrarAlimentoBo(String json) {
        ac = new AlimentoController();
        cc = new ClienteController();
        Alimento dadosAlimento = ac.cadastro(json);
        String dadoClienteId = cc.cadastro(json);
        return ac.cadastrarAlimento(dadosAlimento, dadoClienteId);
    }
}
