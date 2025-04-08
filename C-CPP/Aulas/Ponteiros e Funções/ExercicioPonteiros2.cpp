#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <string>
#include <iostream>

using namespace std;

    /*Escreva um programa que contenha duas variáveis inteiras.
    Compare seus endereços e exiba o maior endereço.*/

int main(){

    setlocale(LC_ALL, "");

    //Declarando as variáveis e os ponteiros.
    int a = 10, b = 20, *pontA, *pontB;

    //Atribuindo os endereços das variáveis aos ponteiros.
    pontA = &a;
    pontB = &b;

    //Imprimindo os endereços na tela.
    printf("\nO endereço de A é = %d", &a);
    printf("\nO endereço de B é = %d", &b);

    printf("\n");

    //Condicional que verifica qual dos dois endereços é maior e imprime na tela.
    if (&a > &b){
        printf("\nO maior endereço é o de A, que vale %d", pontA);
    }
    else{
        printf("\nO maior endereço é o de B, que vale %d", pontB);
    }
    printf("\n");

    //Código em C++.

    //Declarando as variáveis e os ponteiros.
    int c = 30, d = 40, *pontC, *pontD;

    //Imprimindo os endereços na tela.
    cout << "\nO endereço de C é = " << &c;
    cout << "\nO endereço de D é = " << &d;

    //Condicional que verifica qual dos dois endereços é maior e imprime na tela.
    if (pontC < pontD){
        cout << "\nO maior endereço é o de D, que vale " << &d;
    }
    else{
        cout << "\nO maior endereço é o de C, que vale " << &c;
    }

    return 0;
}
