#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

//Crie um algoritmo que imprima os números de 10 até 0
    //de forma regressiva. (usando While, Do While ou For)
    //While
void main(){
    setlocale(LC_ALL, "");

    //WHILE
    int cont = 10;
    while(cont >= 0){
        printf("%d ", cont);
        cont--;
    }
    printf("\n");

    //DO WHILE
    cont = 10;
    do{
        printf("%d ", cont);
        cont--;
    }
    while(cont >= 0);

    printf("\n");
    //FOR
    for(cont = 10; cont >= 0; cont--){
        printf("%d ", cont);
    }
}
