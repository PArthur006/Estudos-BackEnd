#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

//Crie um algoritmo que leia 3 valores e informe se eles são
    //iguais entre si para formarem os lados de um triângulo equilátero.
void main(){
    setlocale(LC_ALL, ""); //Habilitando acentuações.
    //Definindo e lendo os lados informados.
    int ladoA, ladoB, ladoC;
    printf("Informe o comprimento do lado A: ");
    scanf("%d", &ladoA);
    printf("Informe o comprimento do lado B: ");
    scanf("%d", &ladoB);
    printf("Informe o comprimento do lado C: ");
    scanf("%d", &ladoC);
    printf("\n");
    //Condicional para se o triândulo for equilátero.
    if (ladoA == ladoB && ladoB == ladoC){
        printf("O triângulo é equilátero");
    }
    //Condicional para se o triândulo for isósceles.
    else if (ladoA == ladoB || ladoA == ladoC || ladoB == ladoC){
        printf("O triângulo é isósceles");
    }
    //Condicional para se o triândulo for escaleno.
    else{
        printf("O triângulo é escaleno");
    }
    printf("\n");
system("pause"); //Encerrando o sistema.
}
