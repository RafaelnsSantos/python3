#dentro do pacote utilidadesCeV que foi criado no desafio 111, 
# temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() 
# que seja capaz de funcionar como a função input(), mas com uma validação 
# de dados para aceitar apenas valores que sejam monetários.
from utilidadesCev import dados
from utilidadesCev import moeda

p = dados.leiaDinheiro("Digite um preço R$ ")
moeda.resumo(p,80,35)