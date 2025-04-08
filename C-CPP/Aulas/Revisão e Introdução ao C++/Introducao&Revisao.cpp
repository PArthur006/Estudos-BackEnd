#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <iostream>
#include <string>

using namespace std;

int main(){

    //Definindo Variáveis
    int a;
    float b;
    char c;
    bool d;

    //Passando Valores
    a = 10;
    b = 2.8;
    c = 'w';
    d = true;

    //Escrevendo variáveis na tela
    printf("Valor : %d \n", a);
    printf("Valor : %.2f \n", b);
    printf("Valor : %c \n", c);
    printf("Valor : %d \n", d);

    //Imprimindo com C++
    cout << "Valor :" << a << "! \n";

    //Lendo Valores
    scanf("%d", &a);
    scanf("%f", &b);
    scanf("%c", &c);
    scanf("%d", &d);

    //Lendo valores com C++
    cin >> a;

    //Imprimindo novo valor
    cout << "Valor :" << a;

    return 0;
}
