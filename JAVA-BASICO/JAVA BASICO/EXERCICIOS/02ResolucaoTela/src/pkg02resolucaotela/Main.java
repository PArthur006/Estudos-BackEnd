//  Crie um programa que mostre a resolução da tela atual.
package pkg02resolucaotela;

import java.awt.Dimension;
import java.awt.Toolkit;

public class Main {
    public static void main(String[] args) {
        Toolkit resolucaoImagem = Toolkit.getDefaultToolkit();
        Dimension tamanho = resolucaoImagem.getScreenSize();
        
        System.out.println("A tela tem resolucao de " + tamanho.width + " por " + tamanho.height);
    }
    
}
