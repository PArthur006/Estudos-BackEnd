 #include <stdio.h>
 #include <stdlib.h>
 #include <locale.h>

 //Crie um algoritmo que informe se o valor lido � primo ou n�o

 void main(){
    setlocale(LC_ALL, "");

    //Definindo as vari�veis.
    int i, valor, cont = 0;

    //Escaneando o n�mero digitado
    printf("Digite um valor: ");
    scanf("%d", &valor);

    //Iniciando oi la�o de repeti��o com o contador.
    for(i = 1; i <= valor; i++){
        if(valor%i==0){
            cont++;
        }
    }

    //Condicional para imprimir se o valor � ,ou n�o, um primo.
    if (cont == 2){
        printf("O n�mero %d � primo", valor);
    }
    else{
        printf("O n�mero %d N�O � primo", valor);
    }

 }
