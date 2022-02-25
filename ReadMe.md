# Treinando Python 🖥️
<div style="text-align: justify">Repositório criado para meus exercícios e anotações (resumidas) de Python referentes ao curso Introdução à Ciência da Computação com Python, da USP. Utilizei também o conteúdo e exercícios aprendidos durante a minha graduação na disciplina Fundamentos de Programação, disponibilizados nas Notas de Aula (Prof. Armando Luiz N. Delgado, 2017).  

Os exercícios estão separados de acordo com o conteúdo estudado, sendo possível acessá-los no índice abaixo.</div>

========================================================

## Índice

<!--ts-->
- [*Input*](#Input)
- [Expressões booleanas](#Expressões-booleanas)
- [Execução condicional](#Execução-condicional)
- [Repetição com WHILE](#Repetição-com-WHILE)
- [Variáveis booleanas](#Variáveis-booleanas)
- [Funções](#Funções)
<!--te-->

_________________________________________________________________


## Input
<div style="text-align: justify"> Usa-se *input* para que o usuário insira os dados solicitados pelo programa. A saída é sempre um *string*, sendo preciso alterar o tipo de dado (caso seja numérico) para utilizá-o em uma operação.

### Exercícios usando *input*:
>- [Contador de segundos](https://github.com/MilenaSateles/TreinandoPython/blob/main/ContadorSegundos.py)
>- [Contador de segundos 2](https://github.com/MilenaSateles/TreinandoPython/blob/main/ContadorSegundos2.py)
>- [Conversor de temperatura](https://github.com/MilenaSateles/TreinandoPython/blob/main/ConversorDeTemperatura.py)
>- [Dígito das dezenas](https://github.com/MilenaSateles/TreinandoPython/blob/main/D%C3%ADgitoDezenas.py)
>- [Fatura do cartão](https://github.com/MilenaSateles/TreinandoPython/blob/main/FaturaCart%C3%A3o.py)
>- [Média aritmética](https://github.com/MilenaSateles/TreinandoPython/blob/main/MediaAritmetica.py)
>- [Perímetro e área](https://github.com/MilenaSateles/TreinandoPython/blob/main/PerimetroArea.py)

_____

## Expressões booleanas
São expressões que observam dois valores e verificam se existe - ou não - uma relação entre eles. O nome deriva do criador da lógica booleana, George Bool. Quando calculadas, essas expressões geram o valor final *True* ou *False*. A relação entre os valores pode ser verificada utilizando os seguintes operadores relacionais:</div>

<div style="text-align: center">

Símbolo  |  Operação
:-------:|:----------:
(>)      | maior que
(<)      | menor que
(>=)     | maior ou igual que
(<=)     | menor ou igual que
(==)     | igual a
(!=)     | não igual a
*in*     | pertinência de *string*

</div>

Quando mais de uma condição precisa ser testada, faz-se uso dos operadores lógicos. Esses são: **AND, OR e NOT**.
Dessa maneira, agrupamos as expressões para verificar a relação enre elas. Tendo *exp1* como "expressão 1" e *exp2* como "expressão 2", observe as tabelas abaixo:

AND | exp1 = *True* | exp1 = *False*
:------:|:-------------:|:-------------:
exp2 = *True* | **True** | **False**
exp2 = *False* | **False** | **False**

OR| exp1 = *True* | exp1 = *False*
:------:|:-------------:|:-------------:
exp2 = *True* | **True** | **True**
exp2 = *False* | **True** | **False**

NOT | exp1 = *True* | exp1 = *False*
:------:|:-------------:|:-------------:
. | **False** | **True**

### Precedência de operadores
Tendo observado a utilização de operadores aritméticos, relacionais e lógicos, é possível montar uma tabela de precedência de operadores:

Nível | Categoria | Operadores
:----:|:---------:|:-----------:
7 (alto) | exponenciação|**
6 | multiplicação | * , / , // , %
5 | adição | + , -
4 | relacional | == , != , <= , >= , <>
3 |lógico | not
2 | lógico | and
1 (baixo) | lógico | or


### Exercícios usando expressões booleanas:
- 
-
-


____

## Execução condicional
<div style="text-align: justify"> Em todos os exemplos até este momento, as sentenças de um programa são executadas sequencialmente. Há, porém, casos em que a ordem sequencial de execução precisa ser alterada se certas condições forem satisfeitas durante a execução do programa. Isto é chamado desvio condicional ou execução condicional. 



- ### Comando IF
Determinado trecho do código (conjunto de instruções) só será executado ***se*** a condição for verdadeira. Para se submeterem a condição, todas as linhas do bloco devem estar igualmente indentadas.

- ### Comando ELSE

Forma a estrutura IF-ELSE. Indica um segundo bloco de sentenças que somente serão executadas se a condição estabelecida pelo *if* for falsa. Desta maneira: ***se*** condição 1 = verdadeira, execute primeiro bloco de comandos; caso contrário (***else***), execute segundo bloco de comandos.

 - ### Comando ELIF
 
Compõe a estrutura IF-ELIF-ELSE. Indica diferentes decisões que podem ser tomadas em alternativas excludentes entre si. Assim: ***if*** apenas a condição 1 = verdadeira, execute primeiro bloco de comandos; ***elif*** apenas a condição 2 = verdadeira, execute segundo bloco de comandos; ***else*** (caso as condições anteriores sejam falsas), execute terceiro bloco de comandos.

### Exercícios usando IF-ELIF-ELSE:
>- [Fórmula de Bhaskara 1](https://github.com/MilenaSateles/TreinandoPython/blob/main/Bhaskara.py)
>- [Fórmula de Bhaskara 2](https://github.com/MilenaSateles/TreinandoPython/blob/main/Bhaskara2.py)
>- [Distância entre coordenadas](https://github.com/MilenaSateles/TreinandoPython/blob/main/DistanciaCoordenadas.py)
>- [Ordem crescente](https://github.com/MilenaSateles/TreinandoPython/blob/main/OrdemCrescente.py)
>- [Par ou Ímpar](https://github.com/MilenaSateles/TreinandoPython/blob/main/ParOuImpar.py)

----

## Repetição com WHILE
Os laços de repetição ou *loopings* são utilizados para repetir uma sequência de instruções. O comando *while* tem duas partes: a expressão e o bloco de sentenças da repetição. No caso do comando ***while***, o computador continua executando o laço ***enquanto***a condição for verdadeira. Quando se tornar falsa, o comando seguinte é executado.

### Exercícios utilizado WHILE:
>- [Ordem decrescente](https://github.com/MilenaSateles/TreinandoPython/blob/main/Decrescente.py)
 >- [Números ímpares](https://github.com/MilenaSateles/TreinandoPython/blob/main/ImprimeImpar.py)
 >- [Multiplicador](https://github.com/MilenaSateles/TreinandoPython/blob/main/Multiplicador.py)
 >- [N Fatorial](https://github.com/MilenaSateles/TreinandoPython/blob/main/Nfatorial.py)
 >- [Números adjacentes](https://github.com/MilenaSateles/TreinandoPython/blob/main/NumAdjacentes.py)
 >- [Números primos](https://github.com/MilenaSateles/TreinandoPython/blob/main/NumerosPrimos.py)
 >- [Soma até zero](https://github.com/MilenaSateles/TreinandoPython/blob/main/SomaAteZero.py)
 >- [Soma números inteiros](https://github.com/MilenaSateles/TreinandoPython/blob/main/SomaNumInteiros.py)


-----

## Funções

As funções são utilizadas, principalmente, para evitar repetições dentro de um código e reduzir sua complexidade. As funções "encapsulam" alguns detalhes do processamento, e, quando são necessárias, são invocadas. Existem funções da biblioteca padrão em Python, como print(), input() e sqrt(), já observadas. Porém, é possível também definir novas funções, utilizando a palavra reservada ***def***.  
De maneira geral, o formato de definição de uma função é:  

>**def** *nome-da-função (lista-de-parâmetros):*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *declarações e sentenças*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *retorno dos resultados* 

As funções podem ou não ter parâmetros atribuidos a ela, e podem ou não retornar resultados para o usuário.

### Exercícios usando funções:
>- 
>- 


