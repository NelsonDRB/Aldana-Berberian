import pytest  # importa la librería de pytest

# se define la función de las operaciones básicas con 3 parámetros
# OPS es la operación, Op1 es el operando 1 y Op2 es el operando 2
# se usan condicionales para la elección de cada operación distinta.


def basic_operations(OPS, Op1, Op2):
    try:  # se utiliza la función try-except para validar las operaciones
        if int(OPS) == 1:  # con la operación igual a 1, es una suma
            return Op1+Op2  # se retorna la operación suma
        elif int(OPS) == 2:  # con la operación igual a 2, es una resta
            return Op1-Op2  # se retorna la operación resta
        elif int(OPS) == 3:  # con la operación igual a 3, es una división
            return Op1/Op2  # se retorna la operación división
        else:  # se ejecuta en cualquier otro caso
            return ("Error 4")  # corresponde a operación no soportada
    except ZeroDivisionError:  # excepción con el error de división por 0
        return ("Error 2")  # se retorna el Error 2 de división por 0
    except ValueError:  # excepción con el error de digitar valor erróneo
        return ("Error 1")  # se retorna el Error 1
# "Error 1" es equivalente a digitar un caracter diferente a un número


def count_char(sentence):  # se define otra función con un único parámetro
    count = 0  # se define la varible count con un valor de cero
    if sentence.isnumeric():  # este comando verifica si es un valor númerico
        return ("Error 3")  # se retorna el Error 3 si sentence no es un string
    for i in sentence:  # se hace un recorrido para contar los caracteres
        count = count + 1  # se suma una unidad por cada caracter
    return (count)  # se retorna la suma total de caracteres


# se definen 3 tuplas con los valores de operación, operandos y resultados
# esperados para comprobar que las operaciones se realizan de forma correcta
@pytest.mark.parametrize(  # función de parametrización de pytest
    "Op, Op_1, Op_2, Res",  # los 4 parámetros de las tuplas
    [
        (1, 2, 3, 5),  # tupla 1 suma
        (2, 3, 2, 1),  # tupla 2 resta
        (3, 2, 2, 1)  # tupla 3 división
    ]
    )
# se define una función con 4 parámetros para probar las operaciones
# el comando assert verifica si la función se comporta correctamente
def test_basic_operations_correc(Op, Op_1, Op_2, Res):
    assert basic_operations(Op, Op_1, Op_2) == Res


# se definen 3 tuplas con los valores de operación y operandos.
# se da como entrada un string en cada caso para verificar que
# se retorne el error esperado
@pytest.mark.parametrize(  # función de parametrización de pytest
    "operacion, operando_1, operando_2",  # los 3 parámetros de las tuplas
    [
        ("a", 2, 3),  # tupla 1: error, operando 1, operando 2
        (1, "a", 3),  # tupla 2: operación, error, operando 2
        (1, 2, "a")  # tupla 3: operación, operando 1, error
    ]
    )
# se define una función con 3 parámetros para probar que se retorne
# el error 1 de parámetro inválido.
# el comando assert verifica si se devuelve el error correspondiente
def test_basic_operations_error1(operacion, operando_1, operando_2):
    assert basic_operations(operacion, operando_1, operando_2) == "Error 1"


# se define una función para verificar el error de la división por cero.
# en el assert se utiliza un 0 en el denominador de la división para
# provocar que se verifique el error 2.
def test_basic_operations_div0():
    assert basic_operations(3, 5, 0) == "Error 2"


# se define una función para verificar que se cuenta adecuadamente
# la cantidad de caracteres de un string dado.
# se usa la palabra "prueba", que tiene 6 caracteres.
# el assert debe verificar que lo anterior es correcto.
def test_count_char_tam():
    assert count_char("prueba") == 6


# se define una función para verificar el error 3.
# en el assert se inserta el número "12", por lo que no es un string
# y debe devolver el error 3.
def test_count_char_error3():
    assert count_char("12") == "Error 3"
