package br.com.alimentaai.model;

public class Cliente {
    private String nome;
    private String email;
    private String senha;
    private String celular;
    private String endereco;

    public Cliente(String nome, String email, String senha, String celular, String endereco) {
        this.nome = nome;
        this.email = email;
        this.senha = senha;
        this.celular = celular;
        this.endereco = endereco;
    }

    public Cliente() {
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getSenha() {
        return senha;
    }

    public void setSenha(String senha) {
        this.senha = senha;
    }

    public String getCelular() {
        return celular;
    }

    public void setCelular(String celular) {
        this.celular = celular;
    }

    public String getEndereco() {
        return endereco;
    }

    public void setEndereco(String endereco) {
        this.endereco = endereco;
    }

    @Override
    public String toString() {
        return "Cliente{" +
                "nome='" + nome + '\'' +
                ", email='" + email + '\'' +
                ", senha='" + senha + '\'' +
                ", celular='" + celular + '\'' +
                ", endereco='" + endereco + '\'' +
                '}';
    }
}
