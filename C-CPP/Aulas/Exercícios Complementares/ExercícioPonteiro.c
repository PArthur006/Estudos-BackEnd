#include <stdio.h>
#include <stdlib.h>
#include <locale.h>


/*
Elaborar um programa que leia dois valores inteiros(A e B).Em seguida fa�a uma fun��o
que retorne a soma do dobro dos dois n�umeros lidos.A fun��o dever� armazenar o dobro
de A na pr�pria vari�vel A e o dobro de B na pr�pria vari�vel B.
*/

//Declarando que a fun��o 'SomaDobro' existe.
int SomaDobro(n1, n2);

void main(){
    setlocale(LC_ALL, "");

    //Declarando as vari�veis.
    int a, b, *pA, *pB;

    //Pedindo valores ao usu�rio.
    printf("Digite o primeiro valor: ");
    scanf("%d", &a);
    printf("Digite o segundo valor: ");
    scanf("%d", &b);

    //Definindo os ponteiros.
    pA = &a;
    pB = &b;

    printf("A soma do dobro dos dois n�meros lidos � = %d", SomaDobro(*pA, *pB)/*Chamando a fun��o*/);
}

int SomaDobro(n1, n2){

    //Dobrando os valores recebidos.
    n1 *= 2;
    n2 *= 2;

    //Retornando a soma.
    return n1 + n2;
}
