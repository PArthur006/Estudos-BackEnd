public class Caneta {
    String modelo;
    String cor;
    int carga;
    float ponta;
    boolean tampada;

    void status() {
        System.out.println("Modelo: " + this.modelo);
        System.out.println("Cor: " + this.cor);
        System.out.println("Carga: " + this.carga);
        System.out.println("Ponta: " + this.ponta);
        System.out.println("Está tampada? " + this.tampada);
    }

    void tampar() {
        this.tampada = true;
    }

    void destampar() {
        this.tampada = false;
    }

    void rabiscar() {
        if (this.tampada) {
            System.out.println("A caneta está tampada! Não posso rabiscar.");
        } else {
            System.out.println("Estou rabiscando!");
        }
    }
}
