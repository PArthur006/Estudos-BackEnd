//Crie um algoritmo que leia 2 notas e mostre a diferen�a absoluta entre elas.
#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

void main(){
    setlocale(LC_ALL, "");
    float n1, n2, resultado; //Cria as tr�s vari�veis.
    printf("Digite um n�mero: ");
    scanf("%f", &n1);
    printf("\nDIgite outro n�mero: ");
    scanf("%f", &n2);
    resultado = abs(n1 - n2); //Utiliza o comando 'abs' para mostrar a diferen�a absoluita entre os n�meros.
    printf("\nA diferen�a absoluta entre %.2f e %.2f � %.2f", n1, n2, resultado);
    system("pause");
}
