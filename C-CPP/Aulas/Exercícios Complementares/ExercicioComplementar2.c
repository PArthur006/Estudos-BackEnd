#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

/*
Considere a seguinte declaração: int A, *B, **C, ***D;
Escreva um programa que leia a variável a e calcule e exiba o dobro,o triplo e
o quádruplo desse valor utilizando apenas os ponteiros B, C e D.
O ponteiro B deve ser usado para calcular o dobro, C o triplo e D o quádruplo.
*/

int main(){
    setlocale(LC_ALL, "");

    //Declarando as variáveis e os ponteiros.
    int a, *Pb, *Pc, *Pd;

    //Lendo o valor informado pelo usuário.
    printf("Digite um valor: ");
    scanf("%d", &a);

    //Definindo um endereço aos ponteiros.
    Pb = &a;
    Pc = &a;
    Pd = &a;

    //Imprimindo na tela o dobro, triplo e quádruplo do valor informado.
    printf("\n O dobro de %d é = %d", a, *Pb * 2);
    printf("\n O triplo de %d é = %d", a, *Pc * 3);
    printf("\n O quádruplo de %d é = %d", a,*Pd * 4);

    return 0;
}
