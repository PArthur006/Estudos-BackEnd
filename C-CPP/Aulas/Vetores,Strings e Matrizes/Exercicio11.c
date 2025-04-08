#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

void main(){
    setlocale(LC_ALL, "");

    //Deifinindo a matriz 2X2 e as variáveis.
    int matriz[2][2], i, j, aux1, aux2;
    //Lendo vetor por vetor da matriz, digitado pelo usuário.
    for(i = 0; i < 2; i++){
        for (j= 0; j< 2; j++){
            printf("Digite um valor: ");
            scanf("%d", &matriz[i][j]);
        }
    }
    //Definindo os valores das variáveis auxiliares.
    aux1 = matriz[0][0];
    aux2 = matriz[0][1];

    //Substituindo os vetores dentro da matriz.
    matriz[0][0] = matriz[1][0];
    matriz[0][1] = matriz[1][1];
    matriz[1][0] = aux1;
    matriz[1][1] = aux2;

    //Imprimindo a matriz, número por número, inversamente.
    for(i = 0; i < 2; i++){
        for (j= 0; j< 2; j++){
            printf("%d ", matriz[i][j]);
        }
        printf("\n");
    }
    system("pause");
}
