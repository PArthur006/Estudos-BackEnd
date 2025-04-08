#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
 //Crie um algoritmo que leia 3 valores para um vetor de 3 posições
    //e depois calcule a média dos valores acessando o vetor.

void main(){
    setlocale(LC_ALL, "");

    //Definindo as variáveis
    int aux, tam;
    printf("Quantos valores serão digitados? ");
    scanf("%d", &tam);
    float vetor[tam], media;


    for (aux = 0; aux < tam; aux++){
        printf("Digite o %dº valor: ", aux + 1);
        scanf("%f", &vetor[aux]);
        media = media + vetor[aux];
    }

    printf("A média dos valores é %.2f", (media / tam));
system("pause");
}
