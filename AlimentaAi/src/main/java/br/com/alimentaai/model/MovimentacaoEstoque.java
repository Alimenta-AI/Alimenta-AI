package br.com.alimentaai.model;

public class MovimentacaoEstoque {
    private Estoque estoque;
    private int qtdeMovimentada;
    private boolean entrada; // Indica se é uma entrada (true) ou saída (false) no estoque

    public MovimentacaoEstoque(Estoque estoque, int qtdeMovimentada, boolean entrada) {
        this.estoque = estoque;
        this.qtdeMovimentada = qtdeMovimentada;
        this.entrada = entrada;
    }

    public MovimentacaoEstoque() {
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

