public class Aula04 {
    public static void main(String[] args) {        
        Caneta c1 = new Caneta("NIC", "Amarela", 0.7f);

        c1.status();
        
        Caneta c2 = new Caneta("BIC", "Azul", 1f);

        c2.status();

        Caneta c3 = new Caneta("Compactor", "Vermelha", 0.5f);

        c3.status();
    }
}
