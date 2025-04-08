//Crie um algoritmo que leia 2 notas e mostre a diferença absoluta entre elas.
#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

void main(){
    setlocale(LC_ALL, "");
    float n1, n2, resultado; //Cria as três variáveis.
    printf("Digite um número: ");
    scanf("%f", &n1);
    printf("\nDIgite outro número: ");
    scanf("%f", &n2);
    resultado = abs(n1 - n2); //Utiliza o comando 'abs' para mostrar a diferença absoluita entre os números.
    printf("\nA diferença absoluta entre %.2f e %.2f é %.2f", n1, n2, resultado);
    system("pause");
}
