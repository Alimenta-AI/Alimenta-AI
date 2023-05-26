package br.com.alimentaai.model;

public class Instituicao extends Cliente{
    private String cnpj;

    public Instituicao(String cnpj) {
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
