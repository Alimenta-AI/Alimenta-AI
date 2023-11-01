package br.com.alimentaai.model;
public class Alimento {
    private String alimentoId;
    private String nome;
    private String validade;
    private int quantidade;

    public Alimento() {
    }

    public Alimento(String alimentoId, String nome, String validade, int quantidade) {
        this.alimentoId = alimentoId;
        this.nome = nome;
        this.validade = validade;
        this.quantidade = quantidade;
    }

    public String getAlimentoId() {
        return alimentoId;
    }

    public void setAlimentoId(String alimentoId) {
        this.alimentoId = alimentoId;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getValidade() {
        return validade;
    }

    public void setValidade(String validade) {
        this.validade = validade;
    }

    public int getQuantidade() {
        return quantidade;
    }

    public void setQuantidade(int quantidade) {
        this.quantidade = quantidade;
    }

    @Override
    public String toString() {
        return "Alimento{" +
                "alimentoId='" + alimentoId + '\'' +
                ", nome='" + nome + '\'' +
                ", validade='" + validade + '\'' +
                ", quantidade=" + quantidade +
                '}';
    }
}
