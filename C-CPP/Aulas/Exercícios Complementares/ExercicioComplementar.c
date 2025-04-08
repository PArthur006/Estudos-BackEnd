#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

/*Faça um programa para receber um número inteiro de segundos do usuário
 e imprimir a quantidade correspondente em horas, minutos e segundos.*/

int main(){
    setlocale(LC_ALL, "");

    //Definindo as variáveis.
    int segundos;
    float horas = 3600, minutos = 60;

    //Lendo os segundos.
    printf("Digite o número em segundos: ");
    scanf("%d", &segundos);

    //Imprimindo na tela os segundos, os minutos e as horas.
    printf("\nO número em segundos é %d", segundos);
    printf("\n%d segundos são %.3f minutos", segundos, segundos / minutos);
    printf("\n%d segundos são %f horas", segundos, segundos / horas);

    return 0;
}
