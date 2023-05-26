package br.com.alimentaai.controller;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.UUID;

public class ClienteController {
        public String generateUniqueId() {
            try {
                UUID uuid = UUID.randomUUID();
                MessageDigest sha1 = MessageDigest.getInstance("SHA-1");
                byte[] hashBytes = sha1.digest(uuid.toString().getBytes());
                StringBuilder hexString = new StringBuilder();
                for (byte b : hashBytes) {
                    String hex = Integer.toHexString(0xFF & b);
                    if (hex.length() == 1) {
                        hexString.append('0');
                    }
                    hexString.append(hex);
                }
                return hexString.toString().substring(0, 20);
            } catch (NoSuchAlgorithmException e) {
                e.printStackTrace();
            }
            return null;
        }
}
