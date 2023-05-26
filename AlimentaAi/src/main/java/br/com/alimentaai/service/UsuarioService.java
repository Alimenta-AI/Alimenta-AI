package br.com.alimentaai.service;

import com.google.gson.Gson;
import com.google.gson.JsonObject;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.sql.Date;


public class UsuarioService {

    public boolean validarDadosUsuario(String nome, String email, String senha, String celular, String cpf, String nascimento, String endereco) {

        boolean dadosValidos = true;

        // Validar o nome
        if (nome == null || nome.trim().equals("")) {
            dadosValidos = validarNome(nome);
        }

        // Validar o e-mail
        if (email == null || email.trim().equals("")) {
            dadosValidos = validaEmail(email);
        }

        // Validar a senha
        if (senha == null || senha.trim().equals("")) {
            dadosValidos = validarSenha(senha);
        }

        // Validar o celular
        if (celular == null || celular.trim().equals("")) {
            dadosValidos = validarCelular(celular);
        }

        // Validar o CPF
        if (cpf == null || cpf.trim().equals("")) {
            dadosValidos = validarCpf(cpf);
        }

        // Validar o Nascimento
        if (nascimento == null) {
            dadosValidos = false;
        }
        //Validar o endereco
        if (endereco == null || endereco.trim().equals("")) {
            dadosValidos = false;
        }

        return dadosValidos;
    }


    private boolean validarNascimento(String nascimento) {
        if (nascimento.length() != 8) {
            return true;
        }

        for (char c : nascimento.toCharArray()) {
            if (!Character.isDigit(c)) {
                return true;
            }
        }

        int dia = Integer.parseInt(nascimento.substring(0, 2));
        int mes = Integer.parseInt(nascimento.substring(2, 4));
        int ano = Integer.parseInt(nascimento.substring(4, 8));
        if (dia < 1 || dia > 31 || mes < 1 || mes > 12 || ano < 1900 || ano > 2100) {
            return true;
        }
        if ((mes == 4 || mes == 6 || mes == 9 || mes == 11) && dia > 30) {
            return true;
        }
        if (mes == 2) {
            boolean bissexto = (ano % 4 == 0 && ano % 100 != 0) || ano % 400 == 0;
            if (bissexto && dia > 29) {
                return true;
            } else if (!bissexto && dia > 28) {
                return true;
            }
        }

        return false;
    }

    private boolean validarCpf(String cpf) {
        if (cpf.length() != 11) {
            return true;
        }

        for (char c : cpf.toCharArray()) {
            if (!Character.isDigit(c)) {
                return true;
            }
        }

        int[] numeros = new int[11];
        for (int i = 0; i < 11; i++) {
            numeros[i] = Character.getNumericValue(cpf.charAt(i));
        }
        int soma = 0;
        for (int i = 0; i < 9; i++) {
            soma += numeros[i] * (10 - i);
        }
        int resto = soma % 11;
        if (resto == 10 || resto == 11) {
            resto = 0;
        }
        if (resto != numeros[9]) {
            return true;
        }
        soma = 0;
        for (int i = 0; i < 10; i++) {
            soma += numeros[i] * (11 - i);
        }
        resto = soma % 11;
        if (resto == 10 || resto == 11) {
            resto = 0;
        }
        if (resto != numeros[10]) {
            return true;
        }

        return false;
    }

    private boolean validarCelular(String celular) {
        if (celular.length() != 11 && celular.length() != 12) {
            return true;
        }

        for (char c : celular.toCharArray()) {
            if (!Character.isDigit(c)) {
                return true;
            }
        }

        return false;
    }
    private boolean validarSenha(String senha) {
        if (senha.length() < 8) {
            return true;
        }

        if (!senha.matches(".*[A-Z].*")) {
            return true;
        }

        if (!senha.matches(".*[a-z].*")) {
            return true;
        }

        if (!senha.matches(".*[0-9].*")) {
            return true;
        }

        if (!senha.matches(".*[@#$%^&+=].*")) {
            return true;
        }

        return false;
    }
    private boolean validarNome(String nome) {
        if (!nome.matches("[a-zA-Z]+")) {
            return true;
        }

        int minimoCaracteres = 3;
        if (nome.length() < minimoCaracteres) {
            return true;
        }

        if (!nome.matches("[A-Z][a-z]+ [A-Z][a-z]+")) {
            return true;
        }

        return false;
    }
    public boolean validaEmail(String email) {

        String apiKey = "92ddd0010a9620726efc46de85fb711291b86214";

        try {
            // Cria a URL de chamada da API do Hunter
            URL url = new URL("https://api.hunter.io/v2/email-verifier?email=" + email + "&api_key=" + apiKey);

            // Abre a conexão com a API do Hunter
            HttpURLConnection con = (HttpURLConnection) url.openConnection();

            // Define o método de requisição para GET
            con.setRequestMethod("GET");

            // Lê a resposta da API do Hunter
            BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()));
            String inputLine;
            StringBuffer response = new StringBuffer();
            while ((inputLine = in.readLine()) != null) {
                response.append(inputLine);
            }
            in.close();

            // Converte a resposta da API do Hunter em um objeto JSON
            Gson gson = new Gson();
            JsonObject jsonObject = gson.fromJson(response.toString(), JsonObject.class);

            // Extrai a informação de validação do e-mail do objeto JSON
            String result = jsonObject.get("data").getAsJsonObject().get("result").getAsString();

            System.out.println(result);

            // Verifica se o e-mail é válido
            return !result.equals("deliverable");

        } catch (IOException e) {
            if (e.getMessage().contains("Server returned HTTP response code: 400")) {
                System.out.println("Erro de digitação: verifique se o endereço de e-mail foi digitado corretamente.");
            } else {
                e.printStackTrace();
            }
        }
        return true;
    }
}
