package pkg03.indentacao;

// A indentação não altera o funcionamento do código por si só,
// porém, visualmente, ela se faz muito necessária, pois facilita
// a compreensão do código e da lógica utilizada.

public class Aula03_BoletimEstudantil {
    
    public static void main(String[] args) {
        // Exemplo de código SEM indentação
/*        
        int mediaFinal = 6;
        if(mediaFinal<6)
        System.out.println("REPROVADO");
        else if(mediaFinal==6)
        System.out.println("PROVA MINERVA");
        else
        System.out.println("APROVADO");
*/
        // Exemplo de código COM indentação
        int mediaFinal = 6;
        if(mediaFinal<6)
            System.out.println("REPROVADO");
        else if(mediaFinal==6)
            System.out.println("PROVA MINERVA");
        else
            System.out.println("APROVADO");
    }
}
