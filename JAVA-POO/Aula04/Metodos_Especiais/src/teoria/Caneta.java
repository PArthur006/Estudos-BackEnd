public class Caneta {

    // Atributos privados (encapsulamento)
    private String modelo;
    private float ponta;

    // MÉTODO CONSTRUTOR
    // - Possui o mesmo nome da classe
    // - Não tem tipo de retorno
    // - Usado para definir valores iniciais ao instanciar um objeto
    public Caneta(String m, float p) {
        this.modelo = m;
        this.ponta = p;
    }

    // MÉTODO GET
    // - Usado para acessar um atributo privado
    // - Retorna o valor do atributo
    public String getModelo() {
        return this.modelo;
    }

    public float getPonta() {
        return this.ponta;
    }

    // MÉTODO SET
    // - Usado para modificar um atributo privado
    // - Recebe um parâmetro e altera o valor do atributo
    public void setModelo(String m) {
        this.modelo = m;
    }

    public void setPonta(float p) {
        this.ponta = p;
    }

    // Exibe o status da caneta
    public void status() {
        System.out.println("SOBRE A CANETA:");
        System.out.println("Modelo: " + this.getModelo());
        System.out.println("Ponta: " + this.getPonta());
    }
}
