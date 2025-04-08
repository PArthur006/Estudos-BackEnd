#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

//Crie um algoritmo que leia 3 valores e informe se eles s�o
    //iguais entre si para formarem os lados de um tri�ngulo equil�tero.
void main(){
    setlocale(LC_ALL, ""); //Habilitando acentua��es.
    //Definindo e lendo os lados informados.
    int ladoA, ladoB, ladoC;
    printf("Informe o comprimento do lado A: ");
    scanf("%d", &ladoA);
    printf("Informe o comprimento do lado B: ");
    scanf("%d", &ladoB);
    printf("Informe o comprimento do lado C: ");
    scanf("%d", &ladoC);
    printf("\n");
    //Condicional para se o tri�ndulo for equil�tero.
    if (ladoA == ladoB && ladoB == ladoC){
        printf("O tri�ngulo � equil�tero");
    }
    //Condicional para se o tri�ndulo for is�sceles.
    else if (ladoA == ladoB || ladoA == ladoC || ladoB == ladoC){
        printf("O tri�ngulo � is�sceles");
    }
    //Condicional para se o tri�ndulo for escaleno.
    else{
        printf("O tri�ngulo � escaleno");
    }
    printf("\n");
system("pause"); //Encerrando o sistema.
}
