#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

/*
Considere a seguinte declara��o: int A, *B, **C, ***D;
Escreva um programa que leia a vari�vel a e calcule e exiba o dobro,o triplo e
o qu�druplo desse valor utilizando apenas os ponteiros B, C e D.
O ponteiro B deve ser usado para calcular o dobro, C o triplo e D o qu�druplo.
*/

int main(){
    setlocale(LC_ALL, "");

    //Declarando as vari�veis e os ponteiros.
    int a, *Pb, *Pc, *Pd;

    //Lendo o valor informado pelo usu�rio.
    printf("Digite um valor: ");
    scanf("%d", &a);

    //Definindo um endere�o aos ponteiros.
    Pb = &a;
    Pc = &a;
    Pd = &a;

    //Imprimindo na tela o dobro, triplo e qu�druplo do valor informado.
    printf("\n O dobro de %d � = %d", a, *Pb * 2);
    printf("\n O triplo de %d � = %d", a, *Pc * 3);
    printf("\n O qu�druplo de %d � = %d", a,*Pd * 4);

    return 0;
}
