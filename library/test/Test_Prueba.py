import pytest
from Hospital import cHospital
from datetime import datetime, timedelta #

def test_test1():
	suma = cHospital.suma_numeros(100,4)
	assert(cHospital.suma_numeros(100,4) == 104)

