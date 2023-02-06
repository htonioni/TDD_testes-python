# Testes Unitários com Python

Este repositório visa demonstrar a implementação de testes unitários com Python, utilizando como exemplo um banco fictício chamado bytebank.

## Funcionário

A classe Funcionário é responsável por armazenar informações sobre um funcionário do banco, como nome, data de nascimento e salário.

### Testes

Para garantir a qualidade e correção do código, foram criados os seguintes testes unitários:

* `test_idade_recebe_13_03_2000_deve_retornar_22`: Testa se a função idade retorna a idade correta a partir da data de nascimento do funcionário.
* `test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_apenas_Carvalho`: Testa se a função sobrenome retorna o sobrenome correto do funcionário.
* `test_quando_decrescimo_de_salario_recebe_100000_deve_retornar_90000`: Testa se a função decrescimo_salario corretamente decrementa o salário do funcionário.
* `test_quando_calcular_bonus_recebe_1000_deve_retornar_100`: Testa se a função calcular_bonus retorna o valor correto do bônus a ser recebido pelo funcionário.
* `test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception`: Testa se a função calcular_bonus retorna uma exceção quando o salário do funcionário é maior que o valor permitido.

## Conclusão

Com a implementação destes testes unitários, podemos ter mais confiança na correção e qualidade do código da classe Funcionário. Além disso, ao realizar mudanças no código, os testes servem como uma forma de garantir que tudo ainda está funcionando corretamente.

Projeto proposto no curso: _Python e TDD: explorando testes unitários_ na platarorma online de ensino [Alura](https://www.alura.com.br)