public class Lutador {
    // ATRIBUTOS
    private String nome;
    private String nacionalidade;
    private int idade;
    private double altura;
    private double peso;
    private String categoria;
    private int vitorias, empates, derrotas;

    // MÉTODO CONSTRUTOR
    public Lutador(String nome, String nacionalidade, int idade, double altura, double peso, int vitorias, int derrotas, int empates){
        this.setNome(nome);
        this.setNacionalidade(nacionalidade);
        this.setIdade(idade);
        this.setAltura(altura);
        this.setPeso(peso);
        this.setVitorias(vitorias);
        this.setDerrotas(derrotas);
        this.setEmpates(empates);
    }


    // MÉTODOS
    public void apresentar(){
        System.out.println("-------------------------------------------------");
        System.out.println("CHEGOU A HORA! Apresentando o lutador " + this.getNome());
        System.out.println("Diretamente de " + this.getNacionalidade());
        System.out.print("Com: " + this.getIdade());
        System.out.println(" anos, " + this.getAltura() + " de altura e pesando " + this.getPeso() + "Kg.");
        System.out.println("Vitórias: "+ this.getVitorias());
        System.out.println("Derrotas: " + this.getDerrotas());
        System.out.println("Empates: " + this.getEmpates());
        System.out.println("-------------------------------------------------");
    }
    
    public void status(){
        System.out.println(this.getNome());
        System.out.println("Categoria: Peso " + this.getCategoria());
        System.out.println(this.getVitorias() + " vitórias.");
        System.out.println(this.getDerrotas() + " derrotas.");
        System.out.println(this.getEmpates() + " empates.");
    }
    
    public void ganharLuta(){
        this.setVitorias(this.getVitorias() + 1);
    }

    public void perderLuta(){
        this.setDerrotas(this.getDerrotas() + 1);
    }

    public void empatarLuta(){
        this.setEmpates(this.getEmpates() + 1);
    }

    // MÉTODOS GETTERS & SETTERS

    public String getNome() {
        return nome;
    }


    public void setNome(String nome) {
        this.nome = nome;
    }


    public String getNacionalidade() {
        return nacionalidade;
    }


    public void setNacionalidade(String nacionalidade) {
        this.nacionalidade = nacionalidade;
    }


    public int getIdade() {
        return idade;
    }


    public void setIdade(int idade) {
        this.idade = idade;
    }


    public double getAltura() {
        return altura;
    }


    public void setAltura(double altura) {
        this.altura = altura;
    }


    public double getPeso() {
        return peso;
    }


    public void setPeso(double peso) {
        this.peso = peso;
        setCategoria();
    }


    public String getCategoria() {
        return categoria;
    }


    private void setCategoria() {
        if(this.peso<52.2){
            this.categoria = "Inválido";
        } else if(this.peso<=70.3){
            this.categoria = "Leve";
        } else if(this.peso<=83.9){
            this.categoria = "Médio";
        } else if(this.peso<=120.2){
            this.categoria = "Pesado";
        } else{
            this.categoria = "Inválido";
        }
    }


    public int getVitorias() {
        return vitorias;
    }


    public void setVitorias(int vitorias) {
        this.vitorias = vitorias;
    }


    public int getDerrotas() {
        return derrotas;
    }


    public void setDerrotas(int derrotas) {
        this.derrotas = derrotas;
    }


    public int getEmpates() {
        return empates;
    }


    public void setEmpates(int empates) {
        this.empates = empates;
    }
}
