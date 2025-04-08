#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <string>
#include <iostream>

using namespace std;

    /*
    Preencha uma matriz 2x2 lendo valores do usu�rio
    e depois troque os valores entre a primeira e a segunda linha.
    */

int main(){
    setlocale(LC_ALL, "");

    //Definindo a matriz 2X2 e as vari�veis de Linha e Coluna.
    int matriz[2][2], l, c;

    //Lendo e armazenando os valores da matriz, digitados pelo usu�rio.
    cout << "Digite os valores da matriz:\n";
    for (l = 0; l < 2; l++){
        for(c = 0; c < 2; c++){
            cout << "   [" << l << "][" << c << "]: ";
            cin >> matriz[l][c];
        }
    }

    /*
    Outra op��o para se inverter as linhas.
    int aux1, aux2;
    aux1 = matriz[0][0];
    aux2 = matriz[0][1];

    matriz[0][0] = matriz[1][0];
    matriz[0][1] = matriz[1][1];
    matriz[1][0] = aux1;
    matriz[1][1] = aux2;
    */

    //Definindo vari�vel auxiliar para armazenar uma linha tempor�riamente.
    int aux;

    //La�o de repeti��o que inverte as linhas.
    for (c = 0; c < 2; c++){
        aux = matriz[0][c];//Auxiliar recebe um valor da coluna.
        matriz[0][c] = matriz[1][c];//Substitui o valor de uma coluna por outro.
        matriz[1][c] = aux;//Substitui o valor de uma coluna pelo valor contido no auxiliar.
}
    //La�o de repeti��o para imprimir a matriz.
    for (l = 0; l < 2; l++){
    for(c = 0; c < 2; c++){
        cout << matriz[l][c] << " ";
    }
    cout << "\n";
}
    return 0;
}
