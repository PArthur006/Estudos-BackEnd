/*class ContaBanco
 * 
 * ATRIBUTOS ( necessário getters e setter para cada um)
 * + numConta
 * # tipo } só aceita 2 tipos: CC(corrente) ou CP(poupança)
 * - dono
 * - saldo
 * - status
 * MÉTODOS (Todos são public)
 * - abrirConta() } muda o status para true e tenho que definir qual o tipo de conta CC ou CP
 * -- CC abre a conta com 50 reais de crédito / CP abre a conta com 150 reais de crédito
 * - fecharConta() } não pode ter dinheiro nem dívida na conta
 * - depositar() } o status precisa estar true
 * - sacar() } o status precisa estar true e eu preciso ter dinheiro na conta
 * - pagarMensal() } sempre que chamado, será descontado um valor da conta do usuário.
 * -- CC paga 12 reais de mensalidade / CP paga 20 reais de mensalidade
 * 
 * MÉTODO CONSTRUTOR
 * - O saldo precisa ser definido como 0 e o status tem que estar false
 */

 public class ContaBanco {

    // ATRIBUTOS
    public int numConta;
    protected String tipo;
    private String dono;
    private double saldo;
    private boolean status;

    // MÉTODO CONSTRUTOR
    public ContaBanco(int numConta, String tipo, String dono) {
        setNumConta(numConta);
        setTipo(tipo);
        setDono(dono);
        setSaldo(0);
        setStatus(false);
    }

    // MÉTODOS
    public void abrirConta() {
        if (!getTipo().equals("CC") && !getTipo().equals("CP")) {
            System.out.println("Tipo de conta inválido.");
            return;
        }

        if (isStatus()) {
            System.out.println("A conta já está aberta.");
            return;
        }

        setStatus(true);

        if (getTipo().equals("CP")) {
            setSaldo(getSaldo() + 150);
        } else {
            setSaldo(getSaldo() + 50);
        }

        System.out.println("Conta aberta com sucesso!");
    }

    public void fecharConta() {
        if (getSaldo() != 0) {
            System.out.println("Não é possível fechar a conta com saldo ou dívida.");
        } else {
            setStatus(false);
            System.out.println("Conta encerrada com sucesso.");
        }
    }

    public void depositar(double valor) {
        if (isStatus()) {
            setSaldo(getSaldo() + valor);
            System.out.println("Depósito de R$" + valor + " realizado com sucesso.");
        } else {
            System.out.println("Não é possível depositar: conta está fechada.");
        }
    }

    public void sacar(double valor) {
        if (!isStatus()) {
            System.out.println("Conta está fechada. Impossível sacar.");
            return;
        }

        if (getSaldo() >= valor) {
            setSaldo(getSaldo() - valor);
            System.out.println("Saque de R$" + valor + " realizado com sucesso.");
        } else {
            System.out.println("Saldo insuficiente para saque.");
        }
    }

    public void pagarMensal() {
        if (!isStatus()) {
            System.out.println("Conta está fechada. Não é possível pagar mensalidade.");
            return;
        }

        double valorMensal = getTipo().equals("CC") ? 12 : 20;

        if (getSaldo() >= valorMensal) {
            setSaldo(getSaldo() - valorMensal);
            System.out.println("Mensalidade de R$" + valorMensal + " debitada.");
        } else {
            System.out.println("Saldo insuficiente para pagar mensalidade.");
        }
    }

    public void mostrarConta() {
        System.out.println("========= DADOS DA CONTA =========");
        System.out.println("Número: " + getNumConta());
        System.out.println("Tipo: " + getTipo());
        System.out.println("Dono: " + getDono());
        System.out.println("Saldo: R$" + getSaldo());
        System.out.println("Status: " + (isStatus() ? "Aberta" : "Fechada"));
        System.out.println("==================================");
    }

    // GETTERS E SETTERS
    public int getNumConta() {
        return numConta;
    }

    public void setNumConta(int numConta) {
        this.numConta = numConta;
    }

    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }

    public String getDono() {
        return dono;
    }

    public void setDono(String dono) {
        this.dono = dono;
    }

    public double getSaldo() {
        return saldo;
    }

    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }

    public boolean isStatus() {
        return status;
    }

    public void setStatus(boolean status) {
        this.status = status;
    }
}
