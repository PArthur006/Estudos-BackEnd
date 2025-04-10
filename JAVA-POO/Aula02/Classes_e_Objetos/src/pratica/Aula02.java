public class Aula02 {
    public static void main(String[] args) {
        Caneta c1 = new Caneta();
        c1.modelo = "Bic";
        c1.cor = "Azul";
        c1.ponta = 0.5f;
        c1.carga = 100;
        c1.tampada = false;

        c1.status();
        c1.rabiscar();

        Caneta c2 = new Caneta();
        c2.modelo = "Compactor";
        c2.cor = "Preta";
        c2.ponta = 1f;
        c2.carga = 80;
        c2.tampada = true;

        c2.status();
        c2.rabiscar();
    }
}
