package br.com.alimentaai.service;

import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.HttpClientBuilder;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class UsuarioService {

    public boolean  validarDadosUsuario(String nome, String email, String senha, String celular, String cpf, String nascimento, String endereco) throws IOException {
        // Validar o nome vazio
        if (nome == null || nome.trim().equals("")) {
            return false;
        }
        // Validar o e-mail vazio
        if (email == null || email.trim().equals("")) {
            return false;
        }
        // Validar a senha vazio
        if (senha == null || senha.trim().equals("")) {
            return false;
        }
        // Validar o celular vazio
        if (celular == null || celular.trim().equals("")) {
            return false;
        }
        // Validar o CPF vazio
        if (cpf == null || cpf.trim().equals("")) {
            return false;
        }
        // Validar o Nascimento vazio
        if (nascimento == null) {
            return false;
        }
        //Validar o endereco vazio
        if (endereco == null || endereco.trim().equals("")) {
            return false;
        }

        //Validações criadas
//        if(!validarNascimento(nascimento)){
//            return false;
//        }
//        if(!validarSenha(senha)){
//            return false;
//        }
//        if(!validarNome(nome)){
//            return false;
//        }

        //Validações por API:
//        if (!validaCPF(cpf)) {
//            return false;
//        }
//        if (!validaEmail(email)) {
//            return false;
//        }
//        if (!validaPhone(celular)) {
//            return false;
//        }

        //Se todas as validações derem certo ele retorna true e faz o insert no Banco, caso contrário retorna dados inválidos
        return true;
    }

    private static final String API_URL_CPF = "https://api.apicep.com/validar-cpf/";

    public static boolean validaCPF(String cpf) throws IOException {
        HttpClient httpClient = HttpClientBuilder.create().build();
        HttpGet request = new HttpGet(API_URL_CPF + cpf);
        HttpResponse response = httpClient.execute(request);
        BufferedReader reader = new BufferedReader(new InputStreamReader(response.getEntity().getContent()));
        String jsonResponse = reader.readLine();
        System.out.println("Validação cpf");
        return jsonResponse.contains("\"status\": true");
    }

    private static final String API_URL_EMAIL = "https://apilayer.net/api/check?access_key=YOUR_ACCESS_KEY&email=";

    public static boolean validaEmail(String email) throws IOException {
        HttpClient httpClient = HttpClientBuilder.create().build();
        HttpGet request = new HttpGet(API_URL_EMAIL + email);
        HttpResponse response = httpClient.execute(request);
        BufferedReader reader = new BufferedReader(new InputStreamReader(response.getEntity().getContent()));
        String jsonResponse = reader.readLine();
        System.out.println("Validação email");
        return jsonResponse.contains("\"format_valid\": true");
    }

    private static final String API_URL_CELULAR = "https://apilayer.net/api/validate?access_key=YOUR_ACCESS_KEY&number=";

    public static boolean validaPhone(String phoneNumber) throws IOException {
        HttpClient httpClient = HttpClientBuilder.create().build();
        HttpGet request = new HttpGet(API_URL_CELULAR + phoneNumber);
        HttpResponse response = httpClient.execute(request);
        BufferedReader reader = new BufferedReader(new InputStreamReader(response.getEntity().getContent()));
        String jsonResponse = reader.readLine();
        System.out.println("Validação celular");
        return jsonResponse.contains("\"valid\": true");
    }

    private boolean validarNascimento(String nascimento) {
        if (nascimento.length() != 8) {
            return false;
        }

        for (char c : nascimento.toCharArray()) {
            if (!Character.isDigit(c)) {
                return false;
            }
        }

        int dia = Integer.parseInt(nascimento.substring(0, 2));
        int mes = Integer.parseInt(nascimento.substring(2, 4));
        int ano = Integer.parseInt(nascimento.substring(4, 8));
        if (dia < 1 || dia > 31 || mes < 1 || mes > 12 || ano < 1900 || ano > 2100) {
            return false;
        }
        if ((mes == 4 || mes == 6 || mes == 9 || mes == 11) && dia > 30) {
            return false;
        }
        if (mes == 2) {
            boolean bissexto = (ano % 4 == 0 && ano % 100 != 0) || ano % 400 == 0;
            if (bissexto && dia > 29) {
                return false;
            } else if (!bissexto && dia > 28) {
                return false;
            }
        }
        return true;
    }

    private boolean validarSenha(String senha) {
        if (senha.length() < 8) {
            return false;
        }
        if (!senha.matches(".*[A-Z].*")) {
            return false;
        }
        if (!senha.matches(".*[a-z].*")) {
            return false;
        }
        if (!senha.matches(".*[0-9].*")) {
            return false;
        }
        if (!senha.matches(".*[@#$%^&+=].*")) {
            return false;
        }
        return true;
    }

    private boolean validarNome(String nome) {
        if (!nome.matches("[a-zA-Z]+")) {
            return false;
        }
        int minimoCaracteres = 3;
        if (nome.length() < minimoCaracteres) {
            return false;
        }
        if (!nome.matches("[A-Z][a-z]+ [A-Z][a-z]+")) {
            return false;
        }
        return true;
    }
}
