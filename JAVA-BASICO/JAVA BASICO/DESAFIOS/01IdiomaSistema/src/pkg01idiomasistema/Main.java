/*  Crie um programa que imprima o idioma do sistema atual   */
package pkg01idiomasistema;

import java.util.Locale;

public class Main {
    public static void main(String[] args) {
        Locale idiomaSistema = Locale.getDefault();
        System.out.println("Idioma do sistema: " + idiomaSistema.getDisplayLanguage());
        System.out.println("País: " + idiomaSistema.getDisplayCountry());
    }
    
}
