"""Esse módulo é utilizado para realizar testes automáticos dos exercícios."""

import unittest
import random
from unittest.mock import patch
import main


class Test(unittest.TestCase):
    """Classe para agregar os métodos que serão utilizados para testar."""
    def test_main(self):
        """Função que testa se a saída do programa corresponde ao que foi especificado."""
        # Lista de valores que serão retornados pela função input.
        temp_c = random.uniform(-100, 100)
        input_returns = [temp_c]
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            # O teste se a saída corresponde ao especificado fica aqui.
            assert mock_input.call_count == 1
            temperatura = temp_c * 9 / 5 + 32
            mock_print.assert_called_with(
                f'A temperatura em Fahrenheit é {temperatura}.')


if __name__ == '__main__':
    unittest.main()
