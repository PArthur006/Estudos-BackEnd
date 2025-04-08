#include <stdio.h>
#include <stdlib.h>

int retornaComMaisDez(int numero){
    return numero + 10;
}

void aumentaDez(int *numero){
    *numero = *numero + 10;
}

int main(){

    //Definindo Variáveis
    int a = 5;

    //Mostrando o valor
    printf("%d \n", a);

    //Aumenta 10
    a = retornaComMaisDez(a);

    //Mostrando o valor
    printf("%d \n", a);

    //Função que aumenta 10 diretamente
    aumentaDez(&a);

    //Mostrando o valor
    printf("%d \n", a);

    //Retorno da Função
    return 0;
}
