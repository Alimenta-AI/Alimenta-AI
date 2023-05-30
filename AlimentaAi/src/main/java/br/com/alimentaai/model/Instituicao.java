package br.com.alimentaai.model;

public class Instituicao extends Cliente{
    private String cnpj;
    private String website;
    private String tipo;

    public Instituicao(String nome, String email, String senha, String celular, String endereco, String clienteId, int tipoCliente, String cnpj, String website, String tipo) {
        super(nome, email, senha, celular, endereco, clienteId, tipoCliente);
        this.cnpj = cnpj;
        this.website = website;
        this.tipo = tipo;
    }
    public Instituicao() {
    }

    public String getCnpj() {
        return cnpj;
    }

    public void setCnpj(String cnpj) {
        this.cnpj = cnpj;
    }

    public String getWebsite() {
        return website;
    }

    public void setWebsite(String website) {
        this.website = website;
    }

    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }

    @Override
    public String toString() {
        return "Instituicao{" +
                "cnpj='" + cnpj + '\'' +
                ", website='" + website + '\'' +
                ", tipo='" + tipo + '\'' +
                '}';
    }
}
