package br.com.alimentaai.model;

import com.fasterxml.jackson.annotation.JsonInclude;

@JsonInclude(JsonInclude.Include.NON_NULL)
public class Usuario extends Cliente{
    private String nascimento;
    private String cpf;
    private String doador;

    public Usuario() {
    }

    public Usuario(String nome, String email, String senha, String celular, String endereco, String clienteId, int tipoCliente, String nascimento, String cpf, String doador) {
        super(nome, email, senha, celular, endereco, clienteId, tipoCliente);
        this.nascimento = nascimento;
        this.cpf = cpf;
        this.doador = doador;
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

    public String getDoador() {
        return doador;
    }

    public void setDoador(String doador) {
        this.doador = doador;
    }

    @Override
    public String toString() {
        return "Usuario{" +
                "nascimento='" + nascimento + '\'' +
                ", cpf='" + cpf + '\'' +
                ", doador='" + doador + '\'' +
                '}';
    }
}
