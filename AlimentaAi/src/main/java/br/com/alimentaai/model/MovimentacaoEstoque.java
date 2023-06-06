package br.com.alimentaai.model;

public class MovimentacaoEstoque  extends Movimentacao{
    private Estoque estoque;
    private int qtdeMovimentada;
    private boolean entrada; // Indica se é uma entrada (true) ou saída (false) no estoque

    public MovimentacaoEstoque() {
    }

    public MovimentacaoEstoque(String num_solicitacao, String data_movimentacao, String descricao, String categoria, Estoque estoque, int qtdeMovimentada, boolean entrada) {
        super(num_solicitacao, data_movimentacao, descricao, categoria);
        this.estoque = estoque;
        this.qtdeMovimentada = qtdeMovimentada;
        this.entrada = entrada;
    }

    public Estoque getEstoque() {
        return estoque;
    }

    public void setEstoque(Estoque estoque) {
        this.estoque = estoque;
    }

    public int getQtdeMovimentada() {
        return qtdeMovimentada;
    }

    public void setQtdeMovimentada(int qtdeMovimentada) {
        this.qtdeMovimentada = qtdeMovimentada;
    }

    public boolean isEntrada() {
        return entrada;
    }

    public void setEntrada(boolean entrada) {
        this.entrada = entrada;
    }

    @Override
    public String toString() {
        return "MovimentacaoEstoque{" +
                "estoque=" + estoque +
                ", qtdeMovimentada=" + qtdeMovimentada +
                ", entrada=" + entrada +
                '}';
    }
}

