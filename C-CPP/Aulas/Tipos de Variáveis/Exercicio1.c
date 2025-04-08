//Crie um programa que leia duas notas e imprima a média entre elas.
#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

void main(){
    setlocale(LC_ALL, "");
    float n1, n2, media; //Definindo variáveis
    printf("Digite a primeira nota: ");
    scanf("%f", &n1); //Escaneia a primeira nota.
    printf("\nDigite a segunda nota: ");
    scanf("%f", &n2); //Escaneia a segunda aula.
    media = (n1 + n2) / 2; //Gera a média
    printf("\nA média entre %.2f e %.2f é %.2f", n1, n2, media); //Imprime a média.
    system("pause");
}
