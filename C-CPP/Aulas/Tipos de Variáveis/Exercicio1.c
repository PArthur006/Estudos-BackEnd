//Crie um programa que leia duas notas e imprima a m�dia entre elas.
#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

void main(){
    setlocale(LC_ALL, "");
    float n1, n2, media; //Definindo vari�veis
    printf("Digite a primeira nota: ");
    scanf("%f", &n1); //Escaneia a primeira nota.
    printf("\nDigite a segunda nota: ");
    scanf("%f", &n2); //Escaneia a segunda aula.
    media = (n1 + n2) / 2; //Gera a m�dia
    printf("\nA m�dia entre %.2f e %.2f � %.2f", n1, n2, media); //Imprime a m�dia.
    system("pause");
}
