package br.com.alimentaai.model;
public class Alimento {
    private String alimentoId;
    private String nome;
    private String descricao;
    private String validade;
    private int quantidade;
    public String getAlimentoId() {
        return alimentoId;
    }
    public Alimento(String alimentoId, String nome, String descricao, String validade, int quantidade) {
        this.alimentoId = alimentoId;
        this.nome = nome;
        this.descricao = descricao;
        this.validade = validade;
        this.quantidade = quantidade;
    }
    public Alimento() {
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

    public String getDescricao() {
        return descricao;
    }

    public void setDescricao(String descricao) {
        this.descricao = descricao;
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
                ", descricao='" + descricao + '\'' +
                ", validade='" + validade + '\'' +
                ", quantidade=" + quantidade +
                '}';
    }
}
