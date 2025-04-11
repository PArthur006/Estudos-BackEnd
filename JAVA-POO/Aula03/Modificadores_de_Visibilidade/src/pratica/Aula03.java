public class Aula03 {
    public static void main(String[] args) {
        Caneta c1 = new Caneta();
        
        c1.modelo = "Bic cristal";
        c1.cor = "Azul";
        // c1.ponta = 0.5f;  --> private
        c1.carga = 80;
        // c1.tampada = true;  --> private
        
        c1.destampar();
        c1.status();
        c1.rabiscar();
    }
}
