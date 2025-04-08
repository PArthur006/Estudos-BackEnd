 #include <stdio.h>
 #include <stdlib.h>
 #include <locale.h>

 //Crie um algoritmo que informe se o valor lido é primo ou não

 void main(){
    setlocale(LC_ALL, "");

    //Definindo as variáveis.
    int i, valor, cont = 0;

    //Escaneando o número digitado
    printf("Digite um valor: ");
    scanf("%d", &valor);

    //Iniciando oi laço de repetição com o contador.
    for(i = 1; i <= valor; i++){
        if(valor%i==0){
            cont++;
        }
    }

    //Condicional para imprimir se o valor é ,ou não, um primo.
    if (cont == 2){
        printf("O número %d é primo", valor);
    }
    else{
        printf("O número %d NÃO é primo", valor);
    }

 }
