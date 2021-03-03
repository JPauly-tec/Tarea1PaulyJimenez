max_length = 2048  # max text length
user_input = ""  # input from user
counter_1 = 0
right_length = False


print("Bienvenido al Transmisor de código morse")
print("Pulse [ENTER] para continuar")
input()  # solicita input
while right_length is False:  # revisa condiciones y retorna error
    counter_1 = 0
    print("Ingrese el texto que desea convertir a código morse a continuación")
    print("Recuerde max 2048 caracteres, Solo use letras, numeros o espacio")
    user_input = input()
    for letter in user_input:  # contador para avanzar a siguiente letra
        counter_1 = counter_1+1
    if counter_1 < 2048:
        right_length = True
    if counter_1 > 2048:  # revisa que codigo no supere tamaño max
        print("Su texto supera la cantidad máxima de caracteres soportados.")
        print("Pulse [ENTER] para continuar")
        input()
user_input = user_input.upper()
file = open('archivo.txt', 'w')
for letter in user_input:  # transforma a hexadecimal
    letter_hex = ord(letter)
    letter_hex = hex(letter_hex)
    letter_hex = str(letter_hex)
    letter_hex = letter_hex[2:]
    letter_hex = letter_hex.upper()
    file.write(letter_hex)  # escribe en archivo
    file.write('\n')
file.write('00')
file.close()
print("El Texto ha sido ingresado con exito")
print("Pulse [ENTER] para finalizar")
input()

# Código propio utilizado en el Laboratorio de Electrónica Digital
