package br.com.alimentaai.model;

import java.time.LocalDate;

public class Avaliacao {
    private Alimento alimento;
    private Instituicao instituicao;
    private Cliente cliente;
    private int nota;

    private LocalDate dataAvaliacao;

    public Avaliacao(Alimento alimento, Instituicao instituicao, Cliente cliente, int nota, String comentario, LocalDate dataAvaliacao) {
        this.alimento = alimento;
        this.instituicao = instituicao;
        this.cliente = cliente;
        this.nota = nota;
        this.comentario = comentario;
        this.dataAvaliacao = dataAvaliacao;
    }

    public Avaliacao() {
    }

    public Alimento getAlimento() {
        return alimento;
    }

    public void setAlimento(Alimento alimento) {
        this.alimento = alimento;
    }

    public Instituicao getInstituicao() {
        return instituicao;
    }

    public void setInstituicao(Instituicao instituicao) {
        this.instituicao = instituicao;
    }

    public Cliente getCliente() {
        return cliente;
    }

    public void setCliente(Cliente cliente) {
        this.cliente = cliente;
    }

    public int getNota() {
        return nota;
    }

    public void setNota(int nota) {
        this.nota = nota;
    }

    public String getComentario() {
        return comentario;
    }

    public void setComentario(String comentario) {
        this.comentario = comentario;
    }

    public LocalDate getDataAvaliacao() {
        return dataAvaliacao;
    }

    public void setDataAvaliacao(LocalDate dataAvaliacao) {
        this.dataAvaliacao = dataAvaliacao;
    }

    @Override
    public String toString() {
        return "Avaliacao{" +
                "alimento=" + alimento +
                ", instituicao=" + instituicao +
                ", cliente=" + cliente +
                ", nota=" + nota +
                ", comentario='" + comentario + '\'' +
                ", dataAvaliacao=" + dataAvaliacao +
                '}';
    }
}