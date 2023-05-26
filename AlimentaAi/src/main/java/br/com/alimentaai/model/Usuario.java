package br.com.alimentaai.model;

import java.sql.Date;

public class Usuario extends Cliente{
    private String nascimento;
    private String cpf;

    public Usuario(String nascimento, String cpf) {
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
