#include <stdio.h>
#include <stdlib.h>
#include <locale.h>


/*
Elaborar um programa que leia dois valores inteiros(A e B).Em seguida faça uma função
que retorne a soma do dobro dos dois núumeros lidos.A função deverá armazenar o dobro
de A na própria variável A e o dobro de B na própria variável B.
*/

//Declarando que a função 'SomaDobro' existe.
int SomaDobro(n1, n2);

void main(){
    setlocale(LC_ALL, "");

    //Declarando as variáveis.
    int a, b, *pA, *pB;

    //Pedindo valores ao usuário.
    printf("Digite o primeiro valor: ");
    scanf("%d", &a);
    printf("Digite o segundo valor: ");
    scanf("%d", &b);

    //Definindo os ponteiros.
    pA = &a;
    pB = &b;

    printf("A soma do dobro dos dois números lidos é = %d", SomaDobro(*pA, *pB)/*Chamando a função*/);
}

int SomaDobro(n1, n2){

    //Dobrando os valores recebidos.
    n1 *= 2;
    n2 *= 2;

    //Retornando a soma.
    return n1 + n2;
}
