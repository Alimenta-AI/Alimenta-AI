package br.com.alimentaai.model;

public class Estoque {
    private Alimento alimento;
    private int tamanho;
    private String estoqueId;

    public Estoque() {
    }

    public Estoque(Alimento alimento, int tamanho, String estoqueId) {
        this.alimento = alimento;
        this.tamanho = tamanho;
        this.estoqueId = estoqueId;
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

    public String getEstoqueId() {
        return estoqueId;
    }

    public void setEstoqueId(String estoqueId) {
        this.estoqueId = estoqueId;
    }

    @Override
    public String toString() {
        return "Estoque{" +
                "alimento=" + alimento +
                ", tamanho=" + tamanho +
                ", estoqueId='" + estoqueId + '\'' +
                '}';
    }
}
