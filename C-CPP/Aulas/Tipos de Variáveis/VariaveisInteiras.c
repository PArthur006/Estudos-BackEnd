#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

void main(){
    setlocale(LC_ALL,"");
    //Definindo uma vari�vel.
    int a = 5, b;
    //Imprimindo a vari�vel 'a'.
    printf("%d", a);
    //Concatenando.
    printf("\nO valor da vari�vel A �: %d", a);
    //Mudando o valor de 'a'.
    a = 15;
    //concatenando.
    printf("\nO valor de A agora �: %d", a);
    //Lendo valores.
    printf("\nEscolha o valor de B: ");
    scanf("%d", &b);
    //Concatenado.
    printf("\nO valor de B �: %d", b);
    //Pula linha.
    printf("\n");
    //Imprimindo.
    printf("Fim!");
    //Pausando.
    system("pause");
}
