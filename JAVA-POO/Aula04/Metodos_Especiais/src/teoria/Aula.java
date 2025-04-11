public class Aula {
    public static void main(String[] args) {
        Caneta c1 = new Caneta("BIC Cristal", 0.7f);

        c1.status(); // Mostra os valores definidos no construtor

        // Usando os setters para alterar os valores
        c1.setModelo("Faber-Castell");
        c1.setPonta(1.0f);

        // Mostrando valores atualizados
        c1.status();
    }
}
