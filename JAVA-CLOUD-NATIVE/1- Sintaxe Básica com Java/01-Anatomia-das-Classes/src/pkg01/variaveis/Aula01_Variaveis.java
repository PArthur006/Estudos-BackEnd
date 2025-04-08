package pkg01.variaveis;

public class Aula01_Variaveis {
    public static void variaveis(String[] args) {
        /*
           * A estrutura básica para criar uma variável em Java é:
           *   TIPO nomeDaVariavel = valor;        
        */
        // Exemplos de declarações e atribuições de variáveis:
        int idade = 25;         // Variável do tipo inteiro
        double altura = 1.75;   // Variável do tipo double (número decimal)
        boolean ativo = true;   // Variável do tipo boolean (verdadeiro ou falso)
        String nome = "Arthur"; // Variável do tipo String (texto)
                
        /* Regras para criação de variáveis em Java:        
          1. O nome da variável deve começar com uma letra, '$' ou '_'. Não pode começar com números.
          2. Não pode conter espaços ou caracteres especiais (exceto '$' e '_').
          3. O nome deve ser significativo para facilitar a leitura do código.
          4. Seguir a convenção camelCase: a primeira palavra em minúsculo, e as seguintes iniciando 
            com maiúscula (ex: minhaVariavel).
          5. Variáveis do tipo final (constantes) devem ser escritas em MAIÚSCULAS e separadas por '_'.  
        */

        // Exemplo de variável final (constante)
        final double PI = 3.1415; 
        
    }
    
}
