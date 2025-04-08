public class VariaveisEConstantes {
    public static void main(String[] args) {

        // VARIÁVEL: pode mudar seu valor durante a execução
        int idade = 20;
        System.out.println("Idade: " + idade);

        idade = 25; // mudamos o valor da variável
        System.out.println("Nova idade: " + idade);

        // CONSTANTE: valor fixo, não pode ser alterado
        final double PI = 3.14159;
        System.out.println("Valor de PI: " + PI);

        // PI = 3.14;  // ERRO! Não é possível alterar o valor de uma constante
    }
}
