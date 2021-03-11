# ERR2 -2.5
# ERR5x3 -4.5
import pytest  # modulo necesrio para pytest
import CharFunction  # importa el modulo con las funciones
import string  # permite usar string.ascii_lowercase y string.ascii_uppercase, que son una listaa que contiene todas las letras del alfabeto latin en minuscula y mayuscul, respectivmente


def test_char_check_positive():  # revisa por medio de un for de todo el alfabeto, enb minuscula y mayuscula, que se cumpln las 3 condiciones de check_char
    for i in list(string.ascii_lowercase):  # letras miniculas
        assert CharFunction.char_check(i) == 0
    for T in list(string.ascii_uppercase):  # letras myusculas
        assert CharFunction.char_check(T) == 0


def test_caps_switch_positive():  # revisa que se cumpla la inversion de Cap_switch,tanto para mayuscula como minuscula
    for i in list(string.ascii_lowercase):  # minuscula
        assert CharFunction.caps_switch(i) == i.upper()
    for T in list(string.ascii_uppercase):  # mayuscula
        assert CharFunction.caps_switch(T) == T.lower()


def test_char_check_negative_1():  # confirma que char_check no acepta info que no sea un string o caracter
    assert CharFunction.char_check(1234567890) == 0, "ERROR CODE: 001; El caracter debe ser un String"


def test_char_check_negative_2():  # confirma que char_check no acepte digitos que no sean letras
    assert CharFunction.char_check("1234567890") == 0, "ERROR CODE 002; El parametro debe ser una letra del alfabeto latin"


def test_char_check_negative_3():  # confirma que char_check no acepte texto con mas de un digito
    assert CharFunction.char_check("AB") == 0, "ERROR CODE: 003; El parametro debe ser un unico caracter"
