package pkg04.javabeans;

public class Aula04_JavaBeans {
    public static void javabeans(String[] args) {
        // ==========================
        // 📌 REGRAS DE NOMENCLATURA DE VARIÁVEIS
        // ==========================

        // 1. O nome da variável deve ser claro e descritivo, evitando abreviações ou nomes sem sentido.
        // ❌ int vlr  →  ✅ int valorProduto;

        // 2. As variáveis devem ser sempre no SINGULAR, exceto se representarem um array ou coleção.
        // ❌ String nomesClientes → ✅ String nomeCliente;
        // ❌ int numeroPedido[]  → ✅ int numerosPedidos[];  (Plural permitido para arrays ou coleções)

        // 3. Defina um único idioma para as variáveis no projeto (português ou inglês).
        // ❌ String nomeCliente e String customerName (Mistura de idiomas)  
        // ✅ String nomeCliente ou ✅ String customerName (Escolher um padrão único)


        // ==========================
        // 📌 NOMENCLATURA PARA MÉTODOS
        // ==========================

        // 1. O nome de um método deve SEMPRE começar com um VERBO, indicando a ação que ele executa.
        // ❌ int cliente()  →  ✅ int obterCliente();
        // ❌ void dados()   →  ✅ void salvarDados();

        // 2. Utilizar a convenção CAMELCASE, ou seja, a primeira palavra em minúsculas e as seguintes com a primeira letra maiúscula.
        // ❌ void salvar_dados_cliente()  →  ✅ void salvarDadosCliente();
        // ❌ void GetUser()  →  ✅ void getUser();
    }

// ✅ Exemplos corretos:
    public void calcularDesconto() { /* código aqui */ }
    public String obterNomeCliente() { /* código aqui */ return "";}
    public boolean validarPagamento() { /* código aqui */ return true;}
        
}