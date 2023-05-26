package br.com.alimentaai.model;

public class Instituicao extends Cliente{
    private String cnpj;

    public Instituicao(String nome, String email, String senha, String celular, String endereco, String clienteId, int tipoCliente, String cnpj) {
        super(nome, email, senha, celular, endereco, clienteId, tipoCliente);
        this.cnpj = cnpj;
    }

    public Instituicao() {
    }

    public String getCnpj() {
        return cnpj;
    }

    public void setCnpj(String cnpj) {
        this.cnpj = cnpj;
    }

    @Override
    public String toString() {
        return "Instituicao{" +
                "cnpj='" + cnpj + '\'' +
                '}';
    }
}
