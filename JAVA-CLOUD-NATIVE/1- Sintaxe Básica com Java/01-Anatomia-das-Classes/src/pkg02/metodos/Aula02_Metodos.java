/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package pkg02.metodos;

public class Aula02_Metodos {
    // Um método em Java é um bloco de código que executa uma tarefa específica.
    // Ele pode receber parâmetros e retornar um valor ou apenas executar uma ação.

    // Estrutura básica de um método:
    // TIPO_DE_RETORNO nomeDoMetodo(TIPO parametro1, TIPO parametro2, ...) {
    //     // Corpo do método
    //     return valor; // (se aplicável)
    // }

    // Exemplos:

    // Método sem retorno (void) e sem parâmetros
    public void exibirMensagem() {
        System.out.println("Olá, este é um método!");
    }

    // Método com retorno e sem parâmetros
    public int obterNumero() {
        return 42;
    }

    // Método com parâmetros e retorno
    public int somar(int a, int b) {
        return a + b;
    }

    // Regras para criar métodos:
    // - O nome do método deve começar com letra e seguir o padrão camelCase (ex: calcularSoma).
    // - Se um método retornar um valor, deve ser declarado com o tipo correspondente (ex: int, double, String).
    // - Se não retornar nada, usa-se "void".
    // - Métodos podem receber parâmetros para processar dados dinamicamente.
    // - O uso da palavra-chave "return" é obrigatório em métodos que não sejam "void".

    public static void main(String[] args) {
        String primeiroNome = "Pedro Arthur";
        String segundoNome = "Rodrigues";
        
        String nomeCompleto = nomeCompleto(primeiroNome, segundoNome);
        
        System.out.println(nomeCompleto);
    }
    
    public static String nomeCompleto(String primeiroNome, String segundoNome){
        return primeiroNome.concat(" ").concat(segundoNome);
    }
}

