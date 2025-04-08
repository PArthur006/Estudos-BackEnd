public class TiposDeVariaveis {
    public static void main(String[] args) {
        
        // Tipos primitivos numéricos inteiros
        byte idadeByte = 30;          // Ocupa 1 byte (-128 a 127)
        short populacaoPequena = 1000; // Ocupa 2 bytes
        int populacao = 100000;        // Ocupa 4 bytes (mais usado para inteiros)
        long populacaoMundial = 8000000000L; // Ocupa 8 bytes, precisa do L no final

        // Tipos primitivos numéricos com ponto flutuante
        float altura = 1.75f;          // Ocupa 4 bytes, precisa do f no final
        double peso = 70.5;            // Ocupa 8 bytes (mais usado para decimais)

        // Tipo caractere
        char inicial = 'A';            // Guarda um único caractere

        // Tipo lógico (booleano)
        boolean ligado = true;         // Pode ser true ou false

        // Exibindo os valores
        System.out.println("Idade (byte): " + idadeByte);
        System.out.println("População pequena (short): " + populacaoPequena);
        System.out.println("População (int): " + populacao);
        System.out.println("População mundial (long): " + populacaoMundial);
        System.out.println("Altura (float): " + altura);
        System.out.println("Peso (double): " + peso);
        System.out.println("Inicial do nome (char): " + inicial);
        System.out.println("Ligado (boolean): " + ligado);
    }
}
