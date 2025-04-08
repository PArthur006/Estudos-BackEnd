#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <iostream>

/*
    1. Escreva um programa que declare um inteiro, um real e um char, e ponteiros para inteiro,
    real, e char. Associe as variaveis aos ponteiros (use &). Modifique os valores de �
    cada variavel usando os ponteiros. Imprima os valores das vari � aveis antes e ap � os a �
    modificac�ao.
*/

using namespace std;

//C�digo em C
int main(){
    setlocale(LC_ALL, "");

    //Declarando vari�veis e ponteiros.
    int a = 10, *pontA;
    float b = 2.5, *pontB;
    char c = 'X', *pontC;

    //Ponteiros armazenando os endere�os das vari�veis.
    pontA = &a;
    pontB = &b;
    pontC = &c;

    //Valores sendo imprimidos na tela.
    printf("Valores antigos:\nO valor de A = %d", a);
    printf("\nO valor de B = %.2f", b);
    printf("\nO valor de C = %c\n", c);

    //Valores dos ponteiros sendo modificados.
    *pontA = 20;
    *pontB = 3.5;
    *pontC = 'Y';

    //Valores novos sendo imprimidos
    printf("\nValores Novos:\nO valor de A = %d", a);
    printf("\nO valor de B = %.2f", b);
    printf("\nO valor de C = %c\n", c);

    //C�digo em C++

    cout << "\n|---------|\n"; //Linha horizontal

    //Valores dos ponteiros sendo modificados.
    *pontA = 30;
    *pontB = 4.5;
    *pontC = 'Z';

    //Valores novos sendo imprimidos em C++.
    printf("\nValores Novos(2.0):\nO valor de A = %d", a);
    printf("\nO valor de B = %.2f", b);
    printf("\nO valor de C = %c\n", c);
    return 0;
}


