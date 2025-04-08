#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <string>
#include <iostream>

using namespace std;

/*
Escreva um programa que contenha duas variaveis inteiras. Leia essas variaveis
do teclado. Em seguida, compare seus endere�os e exiba o conteudo do maior endereco.
*/

int main(){
    setlocale(LC_ALL, "");

    //C�DIGO EM C
    //Declarando as vari�veis e seus ponteiros.
    int a, b, *pontA, *pontB;

    //Lendo os valores de A e B.
    printf("\nDigite o valor de A: ");
    scanf("%d", &a);
    printf("\nDigite o valor de B: ");
    scanf("%d", &b);

    //Declarando os valores dos ponteiros.
    pontA = &a;
    pontB = &b;

    //Imprimindo os dois endere�os.
    printf("\nO endere�o de A � %d", pontA);
    printf("\nO endere�o de B � %d", pontB);

    //Condicional para verificar qual o maior endere�o e qual o conte�do dentro desse endere�o.
    if (&a > &b){
        printf("\nO maior endere�o � o de A, e o conte�do dentro dele � %d", a);
    }
    else{
        printf("\nO maior endere�o � o de B, e o conte�do dentro dele � %d", b);
    }

    printf("\n ------------ \n");

    //C�DIGO EM C++
    int c, d, *pontC, *pontD;

    cout << "\nDigite um valor para C: ";
    cin >> c;
    cout << "\nDigite um valor para D: ";
    cin >> d;

    pontC = &c;
    pontD = &d;

    cout << "\nO endere�o de C � " << &c;
    cout << "\nO endere�o de D � " << &d;

    if (pontC > pontD){
        cout << "\nO maior endere�o � o de C, e o conte�do dentro dele � " << c;
    }
    else{
        cout << "\nO maior endere�o � o de D, e o conte�do dentro dele � " << d;
    }

    return 0;
}
