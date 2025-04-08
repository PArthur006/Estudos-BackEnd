#include <stdio.h>
#include <stdlib.h>

void mostraSoma(int primeiroValor, int segundoValor){
    printf("\n A soma entre %d e %d eh %d", primeiroValor,segundoValor,primeiroValor + segundoValor);
}

int retornaSoma(int primeiroValor, int segundoValor){
    return primeiroValor + segundoValor;
}

int main(){

    //Definindo Variáveis
    int a = 5, b = 7;

    //Função que mostra a soma
    mostraSoma(a,b);

    //Exibe o resultado da soma retornado pela função
    printf("\n A soma entre %d e %d eh %d", a,b,retornaSoma(a,b));

    //Retorno da Função
    return 0;
}
