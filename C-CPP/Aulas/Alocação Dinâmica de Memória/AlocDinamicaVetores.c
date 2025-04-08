#include <stdio.h>
#include <stdlib.h>

//Aloca um vetor do tamanho pedido
int* alocaVetor (int tam ){

    //É criado um ponteiro
    int *v;

    //A memória é alocada e o ponteiro recebe o endereço de memória dele
    v = (int *) malloc ( tam * sizeof (int) ) ;

    //Esse ponteiro é retornado
    return v;
}

int main(){

    //Ponteiro que vai apontar para o vetor criado
    int *vetor , tam ,i;

    //Lendo o tamanho do vetor
    printf("Digite um tamanho: ");
    scanf ( "%d", &tam ) ;

    //Vetor vai receber um endereço de memória com o vetor que foi alocado
    //ponteiro = ENDERECO_DE_MEMORIA ou PONTEIRO
    //*ponteiro = VALOR
    vetor = alocaVetor(tam) ;

    //Colocando alguns valores no vetor
    vetor[0] = 1;
    vetor[1] = 2;
    vetor[2] = 3;

    //Imprimindo o vetor na tela
    for(i=0;i<tam;i++){
        printf("%d\n", vetor[i]);
    }

    //Libera a memória após usar o vetor
    free ( vetor ) ;

    return 0;
}
