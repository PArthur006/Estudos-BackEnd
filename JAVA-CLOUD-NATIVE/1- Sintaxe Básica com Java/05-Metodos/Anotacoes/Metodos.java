/*
 * Regras e boas práticas para nomear métodos em Java:
 * 
 * 1. Sempre iniciar com letra minúscula.
 *    ✔ correto: calcularSoma()
 *    ✘ errado: CalcularSoma()
 * 
 * 2. Utilizar nomes descritivos que indiquem claramente a ação do método.
 *    ✔ correto: mostrarMensagem(), obterIdade()
 *    ✘ errado: a(), fazerCoisa()
 * 
 * 3. Usar notação camelCase (minúscula + palavras subsequentes com letra maiúscula).
 *    ✔ correto: validarSenha(), imprimirRelatorio()
 * 
 * 4. Evitar usar acentos, caracteres especiais ou espaços.
 *    ✔ correto: enviarEmail()
 *    ✘ errado: enviar-email(), enviar e-mail()
 * 
 * 5. Verbos são preferíveis, pois métodos realizam ações.
 *    ✔ correto: calcularMedia(), buscarUsuario()
 */

 public class Metodos {

    // Método simples sem retorno (void) e sem parâmetros
    public static void dizerOla() {
        System.out.println("Olá, Arthur!");
    }

    // Método com retorno (int) e sem parâmetros
    public static int pegarAnoAtual() {
        return 2025;
    }

    // Método com parâmetros e retorno
    public static int somar(int a, int b) {
        return a + b;
    }

    // Método com parâmetro e sem retorno
    public static void exibirNome(String nome) {
        System.out.println("Seu nome é: " + nome);
    }

    public static void main(String[] args) {
        dizerOla(); // chamada de método sem argumentos

        int ano = pegarAnoAtual(); // recebe valor de retorno
        System.out.println("Ano atual: " + ano);

        int resultado = somar(10, 20); // envia parâmetros
        System.out.println("Soma: " + resultado);

        exibirNome("Arthur");
    }
}
