#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

/*
 Faça um programa que leia do usuário o tamanho de um
 vetor (inteiros) a ser lido e faça a sua alocação dinâmica
 de memória. Depois, leia do usuário seus valores e
 imprima o vetor lido e mostre quantos dos números
 são pares e quantos são ımpares.
*/

//'Avisa' ao programa da existência dessa função;
int* tamVetor(int tam);

void main(){
    setlocale(LC_ALL, "");

    //Declarando o vetor como ponteiro e as variáveis;
    int *vetor, tam, i;
    int impar = 0, par = 0;

    //Lendo o tamanho do vetor;
    printf("Digite o tamanho do vetor: ");
    scanf("%d", &tam);

    //O vetor recebe o tamanho alocado na função;
    vetor = tamVetor(tam);

    printf("Digite o valor dos vetores:\n");

    //Laço de repetição para receber os valores do vetor;
    for(i = 0; i < tam; i++){
        printf("Vetor[%d]: ", i);
        scanf("%d", &vetor[i]);

    //Condicional para guardar o quantitativo de pares e impares imprimidos;
        if (vetor[i] % 2 == 0){
            par++;
        }
        else{
            impar++;
        }
    }

    printf("\n");

    //Laço para imprimir na tela o conteúdo em cada fração do vetor;
    for(i = 0; i < tam; i++){
        printf("Vetor[%d] = %d\n", i, vetor[i]);
    }

    //Imprime a quantidade de números Impares e pares;
    printf("\nNumeros impares: %d", impar);
    printf("\nNumeros pares: %d", par);

}

//Função para alocar o tamanho do vetor;
int* tamVetor(int tam){
    int *vtr;

    vtr = (int*) malloc (tam * sizeof(int));

    return vtr;
}
