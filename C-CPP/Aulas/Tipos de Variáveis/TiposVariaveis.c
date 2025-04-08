#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

void main(){
    setlocale(LC_ALL, ""); //Permite utilizar acentos em conjunto com o 'include <locale.h>'.

    printf("Ol� mundo \n"); //Printa algo na tela. O '\n' � utilizado para pular uma linha

    int a = 50; //Define a vari�vel 'a' como inteira.

    printf("O valor de A � = %d \n", a); //Subtitui o '%d' pelo valor da vari�vel 'a'.
    printf("Insira um valor para A: ");
    scanf("%d", &a); //Essa fun��o l� um n�mero no terminal e substitui o valor de 'a'.
    printf("O valor de A mudou para %d \n", a);

    float b = 5.5; //Define a vari�vel 'b' como decimal.
    printf("O valor de B � = %f \n", b); //Subtitui o '%f' pelo valor da vari�vel 'b'.
    printf("Insira um valor para B: ");
    scanf("%f", &b); //Essa fun��o l� um n�mero no terminal e substitui o valor de 'b'.
    printf("O valor de B mudou para %f \n", b);

    char letra = 'P'; //Define a vari�vel 'c' como uma letra unit�ria.
    printf("O valor de C � = %c \n", letra); //Subtitui o '%c' pelo valor da vari�vel 'letra'.
    fflush(stdin); //Comando para limpar o buffer(espa�o na mem�ria), permitindo uma nova vari�vel.
    printf("Insira um letra: ");
    scanf("%c", &letra); //Essa fun��o l� um letra no terminal e substitui o valor de 'letra'.
    printf("O valor de C mudou para %c", letra);
}
