#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <string>
#include <iostream>

using namespace std;

/*
Escreva um programa que contenha duas variaveis inteiras. Leia essas variaveis
do teclado. Em seguida, compare seus endereços e exiba o conteudo do maior endereco.
*/

int main(){
    setlocale(LC_ALL, "");

    //CÓDIGO EM C
    //Declarando as variáveis e seus ponteiros.
    int a, b, *pontA, *pontB;

    //Lendo os valores de A e B.
    printf("\nDigite o valor de A: ");
    scanf("%d", &a);
    printf("\nDigite o valor de B: ");
    scanf("%d", &b);

    //Declarando os valores dos ponteiros.
    pontA = &a;
    pontB = &b;

    //Imprimindo os dois endereços.
    printf("\nO endereço de A é %d", pontA);
    printf("\nO endereço de B é %d", pontB);

    //Condicional para verificar qual o maior endereço e qual o conteúdo dentro desse endereço.
    if (&a > &b){
        printf("\nO maior endereço é o de A, e o conteúdo dentro dele é %d", a);
    }
    else{
        printf("\nO maior endereço é o de B, e o conteúdo dentro dele é %d", b);
    }

    printf("\n ------------ \n");

    //CÓDIGO EM C++
    int c, d, *pontC, *pontD;

    cout << "\nDigite um valor para C: ";
    cin >> c;
    cout << "\nDigite um valor para D: ";
    cin >> d;

    pontC = &c;
    pontD = &d;

    cout << "\nO endereço de C é " << &c;
    cout << "\nO endereço de D é " << &d;

    if (pontC > pontD){
        cout << "\nO maior endereço é o de C, e o conteúdo dentro dele é " << c;
    }
    else{
        cout << "\nO maior endereço é o de D, e o conteúdo dentro dele é " << d;
    }

    return 0;
}
