#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

/*
Fa�a um programa que leia 2 valores inteiros e chame uma fun��o que
receba estas 2 vari�veis e troque o seu conte�do, ou seja, esta
fun��o � chamada passando duas vari�veis A e B por exemplo e,ap�s a execu��o
da fun��o, A conter� o valor de B e B ter� o valor de A.
*/

int TrocaValor(int n1, int n2);

int main(){
    setlocale(LC_ALL, "");

    //Declarando as vari�veis.
    int a, b;

    //Lendo os valores a serem invertidos.
    printf("\nDIgite o primeiro valor: ");
    scanf("%d", &a);
    printf("\nDIgite o segundo valor: ");
    scanf("%d", &b);

    //Chamando a fun��o TrocaValor.
    TrocaValor(a, b);

    return 0;
}

int TrocaValor(int n1, int n2){//n1 recebe o valor de 'a', e n2 recebe o valor de 'b'.

    //Declarando vari�vel auxiliar.
    int aux;

    //Realizar a troca de valores entre as vari�veis, utilizando um auxiliar.
    aux = n1;
    n1 = n2;
    n2 = aux;

    //Imprimindo o valores de volta, por�m invertidos.
    printf("\nO primeiro valor agora �: %d", n1);
    printf("\nO segundo valor agora �: %d", n2);

    return 0;
}
