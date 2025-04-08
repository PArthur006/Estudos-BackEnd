# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado.
# Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(),
# mas com uma validação de dados para aceitar apenas valores que sejam monetários


from Modulo.utiliadesCeV import dado, moeda
n = dado.leiaDinheiro('Digite um número:R$')
moeda.resumo(n, 10, 8)
