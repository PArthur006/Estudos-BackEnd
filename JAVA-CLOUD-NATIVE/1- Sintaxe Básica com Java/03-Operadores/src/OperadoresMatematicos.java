public class OperadoresMatematicos {
    public static void main(String[] args) {
        int a = 10;
        int b = 3;

        int soma = a + b;          // Adição
        int subtracao = a - b;     // Subtração
        int multiplicacao = a * b; // Multiplicação
        int divisao = a / b;       // Divisão inteira
        int resto = a % b;         // Resto da divisão (módulo)

        System.out.println("Soma: " + soma);
        System.out.println("Subtração: " + subtracao);
        System.out.println("Multiplicação: " + multiplicacao);
        System.out.println("Divisão: " + divisao);
        System.out.println("Resto da divisão: " + resto);

        // ---------------------

        // Operadores de Atribuição
        int x = 5;

        x += 3; // equivale a x = x + 3
        x *= 2; // equivale a x = x * 2

        System.out.println("Resultado final de x: " + x);
    }
}
