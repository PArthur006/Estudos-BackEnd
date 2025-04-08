#include <stdio.h>
#include <stdlib.h>

char retornaLetra(){
    return 'x';
}

int main(){

    //Definindo variáveis
    char letra;

    //Char recebendo valor de uma função
    letra = retornaLetra();

    //Imprimindo novo valor
    printf("%c", letra);

    return 0;
}
