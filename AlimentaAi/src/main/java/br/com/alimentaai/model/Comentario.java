package br.com.alimentaai.model;

import java.time.LocalDate;

public class Comentario extends Avaliacao{
    private Usuario usuario;
    private Instituicao instituicao;
    private String texto;
    private LocalDate dataComentario;
    private String comentarioId;

    public Comentario() {
    }

    public Comentario(Alimento alimento, Instituicao instituicao, Cliente cliente, int nota, LocalDate dataAvaliacao, String avaliacaoId, Usuario usuario, Instituicao instituicao1, String texto, LocalDate dataComentario, String comentarioId) {
        super(alimento, instituicao, cliente, nota, dataAvaliacao, avaliacaoId);
        this.usuario = usuario;
        this.instituicao = instituicao1;
        this.texto = texto;
        this.dataComentario = dataComentario;
        this.comentarioId = comentarioId;
    }

    public Usuario getUsuario() {
        return usuario;
    }

    public void setUsuario(Usuario usuario) {
        this.usuario = usuario;
    }

    @Override
    public Instituicao getInstituicao() {
        return instituicao;
    }

    @Override
    public void setInstituicao(Instituicao instituicao) {
        this.instituicao = instituicao;
    }

    public String getTexto() {
        return texto;
    }

    public void setTexto(String texto) {
        this.texto = texto;
    }

    public LocalDate getDataComentario() {
        return dataComentario;
    }

    public void setDataComentario(LocalDate dataComentario) {
        this.dataComentario = dataComentario;
    }

    public String getComentarioId() {
        return comentarioId;
    }

    public void setComentarioId(String comentarioId) {
        this.comentarioId = comentarioId;
    }

    @Override
    public String toString() {
        return "Comentario{" +
                "usuario=" + usuario +
                ", instituicao=" + instituicao +
                ", texto='" + texto + '\'' +
                ", dataComentario=" + dataComentario +
                ", comentarioId='" + comentarioId + '\'' +
                '}';
    }
}
