#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

/*
1) Crie um programa que:
    a) Aloque dinamicamente um vetor de 5 números inteiros
    b) Peça para o usuário digitar os 5 números no espaço alocado
    c) Mostre na tela os 5 números
    d) Libere a memória alocada.
*/

int main(){
    setlocale(LC_ALL, "");

//a) Aloque dinamicamente um vetor de 5 números inteiros:

    //Definindo o ponteiro e uma variável contadora.
    int *vetor, i;

    //Alocando memória para o ponteiro.
    vetor = (int *) malloc (5 * sizeof(int));

//b) Peça para o usuário digitar os 5 números no espaço alocado:

    //Laço de repetição para receber os valores inseridos pelo usuário.
    for (i = 0; i < 5; i++){
        printf("\nDigite um valor: ");
        scanf("%d", &vetor[i]);
    }

//c) Mostre na tela os 5 números

    //Laço de repetição para imprimir os valores dentro do vetor.
    for (i = 0; i < 5; i++){
        printf("%d\n", vetor[i]);
    }

//d) Libere a memória alocada.

    //Limpando o vetor.
    free(vetor);
}
