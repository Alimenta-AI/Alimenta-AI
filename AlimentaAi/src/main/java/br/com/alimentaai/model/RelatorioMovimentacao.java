package br.com.alimentaai.model;

import java.time.LocalDate;
import java.util.List;

public class RelatorioMovimentacao {
    private Instituicao instituicao;
    private LocalDate dataInicio;
    private LocalDate dataTermino;
    private List<MovimentacaoEstoque> movimentacoes;

    public RelatorioMovimentacao(Instituicao instituicao, LocalDate dataInicio, LocalDate dataTermino, List<MovimentacaoEstoque> movimentacoes) {
        this.instituicao = instituicao;
        this.dataInicio = dataInicio;
        this.dataTermino = dataTermino;
        this.movimentacoes = movimentacoes;
    }

    public RelatorioMovimentacao() {
    }

    public Instituicao getInstituicao() {
        return instituicao;
    }

    public void setInstituicao(Instituicao instituicao) {
        this.instituicao = instituicao;
    }

    public LocalDate getDataInicio() {
        return dataInicio;
    }

    public void setDataInicio(LocalDate dataInicio) {
        this.dataInicio = dataInicio;
    }

    public LocalDate getDataTermino() {
        return dataTermino;
    }

    public void setDataTermino(LocalDate dataTermino) {
        this.dataTermino = dataTermino;
    }

    public List<MovimentacaoEstoque> getMovimentacoes() {
        return movimentacoes;
    }

    public void setMovimentacoes(List<MovimentacaoEstoque> movimentacoes) {
        this.movimentacoes = movimentacoes;
    }

    @Override
    public String toString() {
        return "RelatorioMovimentacao{" +
                "instituicao=" + instituicao +
                ", dataInicio=" + dataInicio +
                ", dataTermino=" + dataTermino +
                ", movimentacoes=" + movimentacoes +
                '}';
    }

    // Métodos para adicionar e remover movimentações
}

