#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

/*Fa�a um programa para receber um n�mero inteiro de segundos do usu�rio
 e imprimir a quantidade correspondente em horas, minutos e segundos.*/

int main(){
    setlocale(LC_ALL, "");

    //Definindo as vari�veis.
    int segundos;
    float horas = 3600, minutos = 60;

    //Lendo os segundos.
    printf("Digite o n�mero em segundos: ");
    scanf("%d", &segundos);

    //Imprimindo na tela os segundos, os minutos e as horas.
    printf("\nO n�mero em segundos � %d", segundos);
    printf("\n%d segundos s�o %.3f minutos", segundos, segundos / minutos);
    printf("\n%d segundos s�o %f horas", segundos, segundos / horas);

    return 0;
}
