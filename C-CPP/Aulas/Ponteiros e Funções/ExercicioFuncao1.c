#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

/*
Faça um programa que leia 2 valores inteiros e chame uma função que
receba estas 2 variáveis e troque o seu conteúdo, ou seja, esta
função é chamada passando duas variáveis A e B por exemplo e,após a execução
da função, A conterá o valor de B e B terá o valor de A.
*/

int TrocaValor(int n1, int n2);

int main(){
    setlocale(LC_ALL, "");

    //Declarando as variáveis.
    int a, b;

    //Lendo os valores a serem invertidos.
    printf("\nDIgite o primeiro valor: ");
    scanf("%d", &a);
    printf("\nDIgite o segundo valor: ");
    scanf("%d", &b);

    //Chamando a função TrocaValor.
    TrocaValor(a, b);

    return 0;
}

int TrocaValor(int n1, int n2){//n1 recebe o valor de 'a', e n2 recebe o valor de 'b'.

    //Declarando variável auxiliar.
    int aux;

    //Realizar a troca de valores entre as variáveis, utilizando um auxiliar.
    aux = n1;
    n1 = n2;
    n2 = aux;

    //Imprimindo o valores de volta, porém invertidos.
    printf("\nO primeiro valor agora é: %d", n1);
    printf("\nO segundo valor agora é: %d", n2);

    return 0;
}
