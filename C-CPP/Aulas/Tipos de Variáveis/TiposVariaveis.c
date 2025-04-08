#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

void main(){
    setlocale(LC_ALL, ""); //Permite utilizar acentos em conjunto com o 'include <locale.h>'.

    printf("Olá mundo \n"); //Printa algo na tela. O '\n' é utilizado para pular uma linha

    int a = 50; //Define a variável 'a' como inteira.

    printf("O valor de A é = %d \n", a); //Subtitui o '%d' pelo valor da variável 'a'.
    printf("Insira um valor para A: ");
    scanf("%d", &a); //Essa função lê um número no terminal e substitui o valor de 'a'.
    printf("O valor de A mudou para %d \n", a);

    float b = 5.5; //Define a variável 'b' como decimal.
    printf("O valor de B é = %f \n", b); //Subtitui o '%f' pelo valor da variável 'b'.
    printf("Insira um valor para B: ");
    scanf("%f", &b); //Essa função lê um número no terminal e substitui o valor de 'b'.
    printf("O valor de B mudou para %f \n", b);

    char letra = 'P'; //Define a variável 'c' como uma letra unitária.
    printf("O valor de C é = %c \n", letra); //Subtitui o '%c' pelo valor da variável 'letra'.
    fflush(stdin); //Comando para limpar o buffer(espaço na memória), permitindo uma nova variável.
    printf("Insira um letra: ");
    scanf("%c", &letra); //Essa função lê um letra no terminal e substitui o valor de 'letra'.
    printf("O valor de C mudou para %c", letra);
}
