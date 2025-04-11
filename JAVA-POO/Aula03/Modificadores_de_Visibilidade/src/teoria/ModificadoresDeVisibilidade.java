// Classe com diferentes modificadores de visibilidade
public class ModificadoresDeVisibilidade {

    // Atributo acessível de qualquer lugar
    public String nomePublico = "Acesso livre";

    // Atributo acessível apenas dentro desta classe
    private int idadePrivada = 30;

    // Atributo acessível no mesmo pacote e por subclasses
    protected boolean ativoProtegido = true;

    // Atributo sem modificador → visível apenas dentro do mesmo pacote
    String enderecoDefault = "Brasília";

    // Método público: pode ser chamado de qualquer lugar
    public void mostrarPublico() {
        System.out.println("Método público");
    }

    // Método privado: só pode ser chamado dentro da própria classe
    private void mostrarPrivado() {
        System.out.println("Método privado");
    }

    // Método protegido: pode ser acessado por classes do mesmo pacote ou herdeiras
    protected void mostrarProtegido() {
        System.out.println("Método protegido");
    }

    // Método default: visível apenas dentro do mesmo pacote
    void mostrarDefault() {
        System.out.println("Método default (package-private)");
    }
}
