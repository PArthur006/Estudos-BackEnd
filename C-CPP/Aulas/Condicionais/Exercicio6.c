#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <math.h>

 /*Crie um algoritmo que leia dois valores e depois crie um menu (Usando Switch Case)
    de 4 opções:1-Somar, 2-Subtrair,3-Dividir,4-Multiplicar.
    Depois que o usuário escolher uma opção, mostre o resultado da operação escolhida
    com os dois valores lidos.*/

void main(){
    setlocale(LC_ALL, ""); //Habilitando acentuações

    int opcao;
    float v1, v2;
    printf(" 1- Adição\n 2-Subtração\n 3-Divisão\n 4-Multiplicação\n 5-Raiz quadrada\n 6-Potenciação");
    printf("\nEscolha sua opção: ");
    scanf("%d", &opcao);
    switch(opcao){
    case 1:
        printf("Insira o primeiro número: ");
        scanf("%f", &v1);
        printf("Insira o segundo número: ");
        scanf("%f", &v2);
        printf("A soma dos valores é: %.2f", v1 + v2);
    case 2:
        printf("Insira o primeiro número: ");
        scanf("%f", &v1);
        printf("Insira o segundo número: ");
        scanf("%f", &v2);
        printf("A diferença entre os valores é: %.2f", v1 - v2);
        break;
    case 3:
        printf("Insira o primeiro número: ");
        scanf("%f", &v1);
        printf("Insira o segundo número: ");
        scanf("%f", &v2);
        printf("O resto entre os valores é: %.2f", v1 / v2);
        break;
    case 4:
        printf("Insira o primeiro número: ");
        scanf("%f", &v1);
        printf("Insira o segundo número: ");
        scanf("%f", &v2);
        printf("O produto entre os valores é: %.2f", v1 * v2);
        break;

    case 5:
        printf("Insira um valor: ");
        scanf("%f", &v1);
        if (v1 >= 0) {
            printf("A raiz quadrada de %.1f é %.1f", v1, sqrt(v1) );
        }
        else{
            printf("O número informado é inválido");
        }
    case 6:
        printf("Insira a base: ");
        scanf("%f", &v1);
        printf("Insira o expoente: ");
        scanf("%f", &v2);
        printf("A potência é: %.1f", pow(v1, v2));
        break;
    }
printf("\n");
system("pause");
}
