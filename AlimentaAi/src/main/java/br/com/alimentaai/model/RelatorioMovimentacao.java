package br.com.alimentaai.model;

import java.time.LocalDate;
import java.util.List;

public class RelatorioMovimentacao extends Movimentacao{
    private Instituicao instituicao;
    private LocalDate dataInicio;
    private LocalDate dataTermino;
    private List<MovimentacaoEstoque> movimentacoes;

    public RelatorioMovimentacao() {
    }

    public RelatorioMovimentacao(String num_solicitacao, String data_movimentacao, String descricao, String categoria, Instituicao instituicao, LocalDate dataInicio, LocalDate dataTermino, List<MovimentacaoEstoque> movimentacoes) {
        super(num_solicitacao, data_movimentacao, descricao, categoria);
        this.instituicao = instituicao;
        this.dataInicio = dataInicio;
        this.dataTermino = dataTermino;
        this.movimentacoes = movimentacoes;
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
}

