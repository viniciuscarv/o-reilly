# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest

#os teste estao organizados em classes
#que herdam de unittest.TestCase
class NewVisitorTest(unittest.TestCase):

    #setUp e tearDown sao metodos especiais executados antes e depois de cada teste e serao
    #executados mesmo que haja erros no test propiamente dito

    #cria o atributo browser e inicializa o navegador
    def setUp(self):
        self.browser = webdriver.Firefox()

    #fecha o navegador
    def tearDown(self):
        self.browser.quit()

    #todo método inicado por test é um método de teste e será
    #executado pelo executor de teste (test runner)
    def test_can_start_a_list_and_retrive_it_later(self):
        # inicializa o browser no endereço especificado
        self.browser.get('http://localhost:8000')

        #O assert é uma verificação em tempo de execução de uma condição qualquer.
        #Se a condição não for verdadeira, uma exceção AssertionError acontece e o programa pára.
        self.assertIn('Django',self.browser.title)

        #o método self.fail simplesmente falha independente do que houver, gerando messagem de AssertionError
        #nesse caso foi usado como lembrete para finalizar o TestCase
        self.fail('Feche o Teste!!')

if  __name__ == '__main__':
    unittest.main()
