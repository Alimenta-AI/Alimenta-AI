package br.com.alimentaai.model;

public class Movimentacao {
    private String num_solicitacao;
    private String data_movimentacao;
    private String descricao;
    private String categoria;

    public Movimentacao() {
    }

    public Movimentacao(String num_solicitacao, String data_movimentacao, String descricao, String categoria) {
        this.num_solicitacao = num_solicitacao;
        this.data_movimentacao = data_movimentacao;
        this.descricao = descricao;
        this.categoria = categoria;
    }

    public String getNum_solicitacao() {
        return num_solicitacao;
    }

    public void setNum_solicitacao(String num_solicitacao) {
        this.num_solicitacao = num_solicitacao;
    }

    public String getData_movimentacao() {
        return data_movimentacao;
    }

    public void setData_movimentacao(String data_movimentacao) {
        this.data_movimentacao = data_movimentacao;
    }

    public String getDescricao() {
        return descricao;
    }

    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }

    public String getCategoria() {
        return categoria;
    }

    public void setCategoria(String categoria) {
        this.categoria = categoria;
    }

    @Override
    public String toString() {
        return "Movimentacao{" +
                "num_solicitacao='" + num_solicitacao + '\'' +
                ", data_movimentacao='" + data_movimentacao + '\'' +
                ", descricao='" + descricao + '\'' +
                ", categoria='" + categoria + '\'' +
                '}';
    }
}
