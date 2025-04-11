public class Caneta {
    public String modelo;
    public String cor;
    protected int carga;
    private float ponta;
    private boolean tampada;

    public void status() {
        System.out.println("Modelo: " + this.modelo);
        System.out.println("Cor: " + this.cor);
        System.out.println("Carga: " + this.carga);
        System.out.println("Ponta: " + this.ponta);
        System.out.println("Está tampada? " + this.tampada);
    }

    public void tampar() {
        this.tampada = true;
    }

    public void destampar() {
        this.tampada = false;
    }

    protected void rabiscar() {
        if (this.tampada) {
            System.out.println("A caneta está tampada! Não posso rabiscar.");
        } else {
            System.out.println("Estou rabiscando!");
        }
    }
}
