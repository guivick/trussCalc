# Programa trussCalc

trussCalc é um programa escrito em Python que calcula os esforços e deslocamentos em treliças planas. Seu caráter é estritamente didático, por isso algumas questões mais sofisticadas como a entrada de dados por meio de uma GUI ou tratamento de exceções ainda não foram implementadas. O objetivo principal, que consistia no aprendizado de Python através de uma aplicação prática foi atingido. Compartilho este código para quem tiver interesse ou curiosidade no assunto.


# Referência

Deixo aqui o pdf que usei como referência para implementação do programa: a apostila dos professores Senatore e Diogo, da Escola Politécnica da USP (a quem agradeço imensamente!). [Apostila Análise Matricial de Estruturas](lhttps://github.com/guivick/trussCalc/blob/main/Notas%20de%20aula-%20v2.pdf)

# Entrada de dados
Todos os dados devem ser editados em seu respectivo arquivo csv, como descrito a seguir.
Deixei os arquivos preenchidos no Git para usar como exemplo.

## Nós

Os nós devem ser editados no arquivo **pontos.csv**
Deve-se inserir um nó por linha com a seguinte convenção:

***a, x, y***

Onde: 

 - a é o número do nó (recomenda-se iniciar pelo número 0 e inserir os demais em ordem crescente) 
 - x é a coordenada x do nó 
 - y é a coordenada y do nó

## Vínculos

Os vínculos (apoios) devem ser editados no arquivo **vinculos.csv**
Devem-se inserir os graus de liberdade restritos separados por vírgula em uma única linha.

Por exemplo: 

**0, 1, 10, 11**

Os graus de liberdade (GDL) 0, 1, 10 e 11 estão restringidos. Como cada nó da treliça tem 2 graus de liberdade (x e y), tem-se:
- 0 corresponde ao GDL x do nó 0
- 1 corresponde ao GDL y do nó 1
- 10 corresponde ao GDL x do nó 5
- 11 corresponde ao GDL y do nó 5

Se ficar complicado fazer essa associação, nada melhor que desenhar sua estrutura no papel e contar os graus de liberdade (2 por nó)

## Carregamentos

Os carregamentos devem ser editados no arquivo **carregamentos.csv**
Devem-se inserir os carregamentos em todos os GDL, na ordem, separados por vírgula em uma única linha. Se não houver carregamento deve-se incluir o valor 0.

Exemplo:

**0, 0, 0, 0, 0, -25, 0, 0, 0, -50, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0**

Há um carregamento de -25 no GDL 5 (não esqueça que contamos a partir do zero!). É o GDL y do nó 2.
Há um carregamento de -50 no GDL 9. É o GDL y do nó 4.
Há um carregamento de 10 no GDL 18. É o GDL x do nó 9.

## Barras

As barras devem ser editadas no arquivo **barras.csv**
Deve-se inserir uma barra por nó com a seguinte convenção:

**E, A, p1, p2**

Onde:

 - E é o módulo de elasticidade
 - A é a área da barra
 - p1 é o número do nó inicial da barra
 - p2 é o número do nó final da barra

# Saída
Para saída de dados basta clicar nos botões do menu.
Se o programa for rodado direto do Python todos os dados de entrada, saída, matrizes, etc são descritos no console. Em versões futuras pretendo salvar essas informações num arquivo de texto.

## Geometria

Mostra a geometria da treliça com os números dos nós e das barras.

## Deformada

Mostra a geometria deformada. Os valores dos deslocamentos dos pontos aparecem no console.

## Esforços

Mostra os esforços nas barras, sendo tração positiva (em azul) e compressão negativa (em vermelho).
