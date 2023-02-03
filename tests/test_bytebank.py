from codigo.bytebank  import Funcionario
import pytest
from pytest import mark

class TestClass:
    def test_idade_recebe_13_03_2000_deve_retornar_22(self):
        
        entrada = '13/03/2000' # Given-contexto
        esperado = 23

        funcionario_teste = Funcionario('Teste', entrada, 2000)
        
        resultado = funcionario_teste.idade() # When-Ação

        assert resultado == esperado # Then-desfexo_esperado

    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_apenas_Carvalho(self):
        
        entrada = ' Lucas Carvalho ' # Given
        esperado = 'Carvalho'

        lucas = Funcionario(entrada, '13/03/2000', 999) 
        resultado = lucas.sobrenome() # When


        assert resultado == esperado # then

    @mark.calcular_bonus
    def test_quando_decrescimo_de_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000
        entrada_nome = 'Paulo Bragança'
        esperado  = 90000

        funcionario_test = Funcionario(entrada_nome, '13/06/2000', entrada_salario)

        funcionario_test.decrescimo_salario() # when 
 
        resultado = funcionario_test._salario


        assert esperado == resultado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        
        entrada_salario = 1000 # Given
        esperado = 100

        fun_teste = Funcionario('Teste', '13/02/2000', entrada_salario)
        resultado = fun_teste.calcular_bonus() # When

        assert esperado == resultado # Then


    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self):
        # Para testar se um metodo retorna Exception (como esperado)
        with pytest.raises(Exception):
            funcionario = Funcionario('Lucas', '13/03/2200', 1000000)

            resultado = funcionario.calcular_bonus()

            assert resultado

