package br.com.alimentaai.model;

import java.time.LocalDate;

public class Comentario extends Avaliacao{
    private Usuario usuario;
    private Instituicao instituicao;
    private String texto;
    private LocalDate dataComentario;

    public Comentario(Alimento alimento, Instituicao instituicao, Cliente cliente, int nota, String comentario, LocalDate dataAvaliacao, Usuario usuario, Instituicao instituicao1, String texto, LocalDate dataComentario) {
        super(alimento, instituicao, cliente, nota, comentario, dataAvaliacao);
        this.usuario = usuario;
        this.instituicao = instituicao1;
        this.texto = texto;
        this.dataComentario = dataComentario;
    }

    public Comentario() {
    }

    public Usuario getUsuario() {
        return usuario;
    }

    public void setUsuario(Usuario usuario) {
        this.usuario = usuario;
    }

    public Instituicao getInstituicao() {
        return instituicao;
    }

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

    @Override
    public String toString() {
        return "Comentario{" +
                "usuario=" + usuario +
                ", instituicao=" + instituicao +
                ", texto='" + texto + '\'' +
                ", dataComentario=" + dataComentario +
                '}';
    }
}
