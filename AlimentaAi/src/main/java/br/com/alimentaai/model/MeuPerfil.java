package br.com.alimentaai.model;

public class MeuPerfil {
    private Cliente cliente;
    private Usuario usuario;

    public MeuPerfil() {}

    public MeuPerfil(Cliente cliente, Usuario usuario) {
        this.cliente = cliente;
        this.usuario = usuario;
    }

    public Cliente getCliente() {
        return cliente;
    }

    public void setCliente(Cliente cliente) {
        this.cliente = cliente;
    }

    public Usuario getUsuario() {
        return usuario;
    }

    public void setUsuario(Usuario usuario) {
        this.usuario = usuario;
    }

    @Override
    public String toString() {
        return "MeuPerfil{" +
                "cliente=" + cliente +
                ", usuario=" + usuario +
                '}';
    }
}
