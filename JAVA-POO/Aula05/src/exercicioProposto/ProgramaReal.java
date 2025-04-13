public class ProgramaReal {
    public static void main(String[] args) {

        // Criando uma conta corrente (CC)
        ContaBanco c1 = new ContaBanco(1111, "CC", "Arthur");
        c1.abrirConta();          // Abrindo a conta
        c1.depositar(100);        // Depositando
        c1.sacar(30);             // Sacando
        c1.pagarMensal();         // Pagando mensalidade
        c1.mostrarConta();        // Mostrando status
        c1.fecharConta();         // Tentando fechar (ainda tem saldo)
        c1.sacar(108);            // Zerando conta
        c1.fecharConta();         // Agora sim pode fechar

        System.out.println("\n----------------------------\n");

        // Criando uma conta poupança (CP)
        ContaBanco c2 = new ContaBanco(2222, "CP", "Joana");
        c2.abrirConta();
        c2.pagarMensal();
        c2.sacar(100);
        c2.mostrarConta();
    }
}    

