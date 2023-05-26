package br.com.alimentaai.model;

import java.util.Date;

public class Usuario extends Cliente{
    private Date nascimento;
    private String cpf;

    public Usuario(Date nascimento, String cpf) {
        this.nascimento = nascimento;
        this.cpf = cpf;
    }

    public Usuario() {
    }

    public Date getNascimento() {
        return nascimento;
    }

    public void setNascimento(Date nascimento) {
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
