#include <stdio.h>
#include <stdlib.h>

//Limpa a tela
void limpaTela(){
    system("CLS");
}

int main(){

    //Definindo Variáveis
    int a;

    //Imprimindo alguma coisa
    printf("Digite um valor para 'a':");

    //Lendo o valor
    scanf("%d", &a);

    //Chama a função que limpa a tela
    limpaTela();

    printf("O valor digitado foi %d \nFim do Programa!", a);

    //Retorno da Função
    return 0;
}
