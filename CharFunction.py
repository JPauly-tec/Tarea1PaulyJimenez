def char_check(x):    # revisa dato ENTRADA: carácter a revisar SALIDA: 0 o 1
    global ER        # crea variable global de error
    if isinstance(x, str):  # revisa que la entrada sea un string
        if x.isalpha() is True:  # revisa que la entrada sea del alfabeto
            if len(x) == 1:  # revisa que la extension sea igual a 1 digito
                return 0   # si todo se cumple, devuelve 0
            else:
                ER = "ERROR CODE: 003; cáracter debe ser un unico caracter"
                print(ER)
                return 1
        else:
            ER = "ERROR CODE 002; cáracter debe ser letra"
            print(ER)
            return 1
    else:
        ER = "ERROR CODE: 001; cáracter debe ser String"
        print(ER)
        return 1


def caps_switch(y):  # cambiar carácter entre MAYUS y MINUS,
    # ENTRADA: un carácter, SALIDA: carácter invertido
    CP = char_check(y)  # corre chr check con la variable ingresada
    if CP == 0:  # si todo check_char se cumple, invierte la entrada
        if y.isupper():
            return y.lower()
        else:
            return y.upper()
    else:  # si no, solo se devuelve el codigo de error pertinente
        print(ER)
        return
