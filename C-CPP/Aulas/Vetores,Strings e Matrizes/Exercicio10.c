#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
 //Crie um algoritmo que leia 3 valores para um vetor de 3 posi��es
    //e depois calcule a m�dia dos valores acessando o vetor.

void main(){
    setlocale(LC_ALL, "");

    //Definindo as vari�veis
    int aux, tam;
    printf("Quantos valores ser�o digitados? ");
    scanf("%d", &tam);
    float vetor[tam], media;


    for (aux = 0; aux < tam; aux++){
        printf("Digite o %d� valor: ", aux + 1);
        scanf("%f", &vetor[aux]);
        media = media + vetor[aux];
    }

    printf("A m�dia dos valores � %.2f", (media / tam));
system("pause");
}
