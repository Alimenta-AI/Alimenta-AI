package br.com.alimentaai.service;

import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.HttpClientBuilder;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

import java.io.IOException;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class UsuarioService {

    public boolean validarDadosUsuario(String nome, String email, String senha, String celular, String endereco, String cpf, String nascimento, String doador) throws IOException {
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
        //Validar o endereco vazio
        if (endereco == null || endereco.trim().equals("")) {
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
        // Validar o Nascimento vazio
        if (doador == null) {
            return false;
        }

        //Validações criadas
        if(!validarNascimento(nascimento)){
            return false;
        }
        if(!validarSenha(senha)){
            return false;
        }
        if(!validarNome(nome)){
            return false;
        }
        if(!validateCPF(cpf)){
            return false;
        }

        //Validações por API:
        if (!validateEmail(email)) {
            return false;
        }

        return validatePhoneNumber("55" + celular);

        //Se todas as validações derem certo ele retorna true e faz o insert no Banco, caso contrário retorna dados inválidos
    }

    public boolean validarDadosUsuarioAtualizar(String nome, String email, String senha, String celular, String endereco, String cpf, String nascimento, String doador) throws IOException {
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
        //Validar o endereco vazio
        if (endereco == null || endereco.trim().equals("")) {
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
        // Validar o Nascimento vazio
        if (doador == null) {
            return false;
        }

        //Validações criadas
        if(!validarNascimento(nascimento)){
            return false;
        }
        if(!validarNome(nome)){
            return false;
        }
        if(!validateCPF(cpf)){
            return false;
        }

        //Validações por API:
        if (!validateEmail(email)) {
            return false;
        }

        return validatePhoneNumber("55" + celular);

        //Se todas as validações derem certo ele retorna true e faz o insert no Banco, caso contrário retorna dados inválidos
    }

    private static final String API_URL_EMAIL = "https://api.apilayer.com/email_verification/check?email=";

    public static boolean validateEmail(String email) throws IOException {
        OkHttpClient client = new OkHttpClient();

        Request request = new Request.Builder()
                .url(API_URL_EMAIL + email)
                .addHeader("apikey", "1uPle8VvEycnMrIHR4F1gZxLyHWs4O68")
                .build();

        try (Response response = client.newCall(request).execute()) {
            if (response.isSuccessful()) {
                assert response.body() != null;
                String jsonResponse = response.body().string();
                System.out.println(jsonResponse);
                return true;
            } else {
                throw new IOException("Unexpected response code: " + response);
            }
        }
    }

    private static final String API_URL_PHONE = "https://api.apilayer.com/number_verification/validate";
    private static final String API_KEY = "1uPle8VvEycnMrIHR4F1gZxLyHWs4O68";

    public static boolean validatePhoneNumber(String phoneNumber) throws IOException {
        OkHttpClient client = new OkHttpClient();

        String url = API_URL_PHONE + "?number=" + phoneNumber;

        Request request = new Request.Builder()
                .url(url)
                .addHeader("apikey", API_KEY)
                .build();

        try (Response response = client.newCall(request).execute()) {
            if (response.isSuccessful()) {
                assert response.body() != null;
                String jsonResponse = response.body().string();
                System.out.println(jsonResponse);
                JSONParser parser = new JSONParser();
                JSONObject jsonObject = (JSONObject) parser.parse(jsonResponse);

                return (boolean) jsonObject.get("valid");
            } else {
                throw new IOException("Unexpected response code: " + response);
            }
        } catch (ParseException e) {
            throw new RuntimeException(e);
        }
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
        int minimoCaracteres = 3;
        if (nome.length() < minimoCaracteres) {
            return false;
        }
        if (!nome.matches("[A-Z][a-z]+ [A-Z][a-z]+")) {
            return false;
        }
        return true;
    }

    public static boolean validateCPF(String cpf) {
        // Remova caracteres não numéricos
        cpf = cpf.replaceAll("[^0-9]", "");

        // Verifique se o CPF possui 11 dígitos
        if (cpf.length() != 11) {
            return false;
        }

        // Verifique se todos os dígitos são iguais (caso inválido)
        if (cpf.matches("(\\d)\\1{10}")) {
            return false;
        }

        // Calcula o primeiro dígito verificador
        int sum = 0;
        for (int i = 0; i < 9; i++) {
            sum += Character.getNumericValue(cpf.charAt(i)) * (10 - i);
        }
        int firstDigit = (sum * 10) % 11;
        if (firstDigit == 10) {
            firstDigit = 0;
        }

        // Verifica o primeiro dígito verificador
        if (Character.getNumericValue(cpf.charAt(9)) != firstDigit) {
            return false;
        }

        // Calcula o segundo dígito verificador
        sum = 0;
        for (int i = 0; i < 10; i++) {
            sum += Character.getNumericValue(cpf.charAt(i)) * (11 - i);
        }
        int secondDigit = (sum * 10) % 11;
        if (secondDigit == 10) {
            secondDigit = 0;
        }

        // Verifica o segundo dígito verificador
        if (Character.getNumericValue(cpf.charAt(10)) != secondDigit) {
            return false;
        }

        return true;
    }

//    VIA CEP para caso fosse adequado utilizar em nosso projeto
    public static boolean validateEndereco(String endereco) throws IOException {
        String url = "https://viacep.com.br/ws/" + endereco + "/json/";

        OkHttpClient client = new OkHttpClient();
        Request request = new Request.Builder()
                .url(url)
                .build();

        try (Response response = client.newCall(request).execute()) {
            if (response.isSuccessful()) {
                String jsonResponse = response.body().string();
                JSONObject jsonObject = new JSONObject();
                System.out.println(jsonResponse);
                return true;
            } else {
                throw new IOException("Unexpected response code: " + response);
            }
        }
    }
}
