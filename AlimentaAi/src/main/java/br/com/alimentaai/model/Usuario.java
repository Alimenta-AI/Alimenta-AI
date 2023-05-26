package br.com.alimentaai.model;

import java.sql.Date;

public class Usuario extends Cliente{
    private String nascimento;
    private String cpf;

    public Usuario(String nome, String email, String senha, String celular, String endereco, String clienteId, int tipoCliente, String nascimento, String cpf) {
        super(nome, email, senha, celular, endereco, clienteId, tipoCliente);
        this.nascimento = nascimento;
        this.cpf = cpf;
    }

    public Usuario() {
    }

    public String getNascimento() {
        return nascimento;
    }

    public void setNascimento(String nascimento) {
        this.nascimento = nascimento;
    }

    public String getCpf() {
        return cpf;
    }

    public void setCpf(String cpf) {
        this.cpf = cpf;
    }

    @Override
    public String toString() {
        return "Usuario{" +
                "nascimento=" + nascimento +
                ", cpf='" + cpf + '\'' +
                '}';
    }
}
