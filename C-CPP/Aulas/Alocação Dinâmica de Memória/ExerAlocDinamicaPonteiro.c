#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

/*
1) Crie um programa que:
    a) Aloque dinamicamente um vetor de 5 n�meros inteiros
    b) Pe�a para o usu�rio digitar os 5 n�meros no espa�o alocado
    c) Mostre na tela os 5 n�meros
    d) Libere a mem�ria alocada.
*/

int main(){
    setlocale(LC_ALL, "");

//a) Aloque dinamicamente um vetor de 5 n�meros inteiros:

    //Definindo o ponteiro e uma vari�vel contadora.
    int *vetor, i;

    //Alocando mem�ria para o ponteiro.
    vetor = (int *) malloc (5 * sizeof(int));

//b) Pe�a para o usu�rio digitar os 5 n�meros no espa�o alocado:

    //La�o de repeti��o para receber os valores inseridos pelo usu�rio.
    for (i = 0; i < 5; i++){
        printf("\nDigite um valor: ");
        scanf("%d", &vetor[i]);
    }

//c) Mostre na tela os 5 n�meros

    //La�o de repeti��o para imprimir os valores dentro do vetor.
    for (i = 0; i < 5; i++){
        printf("%d\n", vetor[i]);
    }

//d) Libere a mem�ria alocada.

    //Limpando o vetor.
    free(vetor);
}
