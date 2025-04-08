#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

 //Crie um algoritmo que leia 3 notas e calcule a média entre elas.
    //Se o valor for maior que 7 informe que o aluno foi aprovado,
    //senão foi reprovado.

void main(){
    setlocale(LC_ALL, ""); //Comando utilizado para abilitar acentuações.
    float n1, n2, n3, media; //Definindo variáveis.

    //Lendo e guardando as notas.
    printf("Digite a primeira nota: ");
    scanf("%f", &n1);
    printf("\nDigite a segunda nota: ");
    scanf("%f", &n2);
    printf("\nDigite a terceira nota: ");
    scanf("%f", &n3);

    //Definindo a média do aluno e imprimindo na tela.
    media = (n1 + n2 + n3) / 3;
    printf("\nA média do aluno foi %.2f", media);

    //Defindindo a condição para se o aluno foi ou não aprovado.
    if(media >= 7){
        printf("\nAluno aprovado!");
    }
    else{
        printf("\nAluno reprovado!\n");
    }
system("pause"); //Pausando o sistema
}
