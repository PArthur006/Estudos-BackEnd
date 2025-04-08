 #include <stdio.h>
 #include <stdlib.h>
 #include <locale.h>

 //Crie um algoritmo que imprima os números
    //pares de 10 a 20 (usando While, Do While ou For)
void main(){
    int i = 10;
    while(i <= 20){
        if (i % 2 == 0){
            printf("%d ", i);
        }
        i++;
    }
    printf("\n");
    i = 10;
    do{
        if (i % 2 == 0){
            printf("%d ", i);
        }
        i++;
    }
    while(i <= 20);
    printf("\n");
    for(i = 10; i <= 20; i++){
        if (i % 2 == 0){
            printf("%d ", i);
        }
    }
system("pause");
}
