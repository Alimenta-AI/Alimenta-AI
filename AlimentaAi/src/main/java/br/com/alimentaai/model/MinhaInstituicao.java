package br.com.alimentaai.model;

public class MinhaInstituicao {

    private Cliente cliente;
    private Instituicao instituicao;

    public MinhaInstituicao() {}

    public MinhaInstituicao(Cliente cliente, Instituicao instituicao) {
        this.cliente = cliente;
        this.instituicao = instituicao;
    }

    public Cliente getCliente() {
        return cliente;
    }

    public void setCliente(Cliente cliente) {
        this.cliente = cliente;
    }

    public Instituicao getInstituicao() {
        return instituicao;
    }

    public void setInstituicao(Instituicao instituicao) {
        this.instituicao = instituicao;
    }

    @Override
    public String toString() {
        return "MinhaInstituicao{" +
                "cliente=" + cliente +
                ", instituicao=" + instituicao +
                '}';
    }

}
