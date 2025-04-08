#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

void main(){
    setlocale(LC_ALL,"");
    //Definindo uma variável.
    int a = 5, b;
    //Imprimindo a variável 'a'.
    printf("%d", a);
    //Concatenando.
    printf("\nO valor da variável A é: %d", a);
    //Mudando o valor de 'a'.
    a = 15;
    //concatenando.
    printf("\nO valor de A agora é: %d", a);
    //Lendo valores.
    printf("\nEscolha o valor de B: ");
    scanf("%d", &b);
    //Concatenado.
    printf("\nO valor de B é: %d", b);
    //Pula linha.
    printf("\n");
    //Imprimindo.
    printf("Fim!");
    //Pausando.
    system("pause");
}
