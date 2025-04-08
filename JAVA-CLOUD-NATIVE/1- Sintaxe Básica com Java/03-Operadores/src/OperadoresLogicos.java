public class OperadoresLogicos {
    public static void main(String[] args) {
        boolean a = true;
        boolean b = false;

        boolean e = a && b; // AND lógico
        boolean ou = a || b; // OR lógico
        boolean nao = !a;    // NOT lógico (negação)

        System.out.println("a && b: " + e);
        System.out.println("a || b: " + ou);
        System.out.println("!a: " + nao);
    }
}
