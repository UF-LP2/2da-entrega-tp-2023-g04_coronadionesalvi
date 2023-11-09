import datetime
import unittest
from unittest import TestCase
from unittest.mock import patch
from library.Enfermero import cEnfermero
import pytest

class TestSetEstado(TestCase):

    @patch('builtins.print')
    @patch('datetime.datetime.now')
    def test_set_estado_turno_actual_no_atendiendo_paciente(self, mock_now, mock_print):
        from datetime import datetime
        from your_module import TuClase
        
        # Mockear el valor de retorno de datetime.now()
        mock_now.return_value = datetime(2022, 1, 1, 9, 0, 0)

        # Inicializar objetos y atributos relevantes
        instance = TuClase()
        instance.turno = datetime(2022, 1, 1, 9, 0, 0)
        instance.atendiendo_paciente = False

        # Ejecutar la función
        instance.set_estado()

        # Comprobar los resultados esperados
        mock_print.assert_called_with(True)

    @patch('builtins.print')
    @patch('datetime.datetime.now')
    def test_set_estado_turno_actual_atendiendo_paciente(self, mock_now, mock_print):
        from datetime import datetime
        from your_module import TuClase
        
        # Mockear el valor de retorno de datetime.now()
        mock_now.return_value = datetime(2022, 1, 1, 9, 0, 0)

        # Inicializar objetos y atributos relevantes
        instance = TuClase()
        instance.turno = datetime(2022, 1, 1, 9, 0, 0)
        instance.atendiendo_paciente = True

        # Ejecutar la función
        instance.set_estado()

        # Comprobar los resultados esperados
        mock_print.assert_called_with(False)


if __name__ == '__main__':
    unittest.main()
