#include <stdio.h>
#include <string.h>

struct palavra{
    int ordem;
    char letra;
    char texto[255];
};

int main () {

    //Criar uma palavra
    struct palavra primeiraPalavra;

    //Modificando os campos
    primeiraPalavra.ordem = 10;
    primeiraPalavra.letra = 'p';
    strcpy(primeiraPalavra.texto,"palavrinha");

    //Mostrando valores do Struct
    printf("Ordem: %d, Primeira Letra: %c, Palavra: %s", primeiraPalavra.ordem,primeiraPalavra.letra, primeiraPalavra.texto);

    //Fazendo uma lista de structs
    struct palavra listaDePalavras[3];

    //Modificando os campos
    listaDePalavras[0].ordem = 0;
    listaDePalavras[1].ordem = 1;
    listaDePalavras[2].ordem = 2;
    listaDePalavras[0].letra = 'd';
    listaDePalavras[1].letra = 'l';
    listaDePalavras[2].letra = 'b';
    strcpy(listaDePalavras[0].texto,"Dahora");
    strcpy(listaDePalavras[1].texto,"Legal");
    strcpy(listaDePalavras[2].texto,"Bacana");

    //Percorrendo o vetor
    int cont;
    for(cont = 0; cont < 3; cont++){
        printf("\nOrdem: %d, Primeira Letra: %c, Palavra: %s", listaDePalavras[cont].ordem,listaDePalavras[cont].letra, listaDePalavras[cont].texto);
    }

    return 0;
}
