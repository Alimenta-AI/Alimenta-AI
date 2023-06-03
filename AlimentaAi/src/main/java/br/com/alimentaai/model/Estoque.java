package br.com.alimentaai.model;

public class Estoque {
    private Alimento alimento;
    private int tamanho;

    public Estoque(Alimento alimento, int tamanho) {
        this.alimento = alimento;
        this.tamanho = tamanho;
    }

    public Estoque() {
    }

    public Alimento getAlimento() {
        return alimento;
    }

    public void setAlimento(Alimento alimento) {
        this.alimento = alimento;
    }

    public int getTamanho() {
        return tamanho;
    }

    public void setTamanho(int tamanho) {
        this.tamanho = tamanho;
    }

    @Override
    public String toString() {
        return "Estoque{" +
                "alimento=" + alimento +
                ", tamanho=" + tamanho +
                '}';
    }
}
