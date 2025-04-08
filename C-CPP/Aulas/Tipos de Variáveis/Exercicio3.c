
#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

void main(){
    setlocale(LC_ALL, "");
    int n1, n2, n3, resultado;
    printf("Digite 3 números inteiros separados por um espaço: ");
    scanf("%d %d %d", &n1, &n2, &n3);
    resultado = n1 * n2 * n3;
    printf("O resultado da multiplicação é: %d\n", resultado);
    system("pause");
}
