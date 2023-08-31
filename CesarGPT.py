def cifrado_cesar(texto, corrimiento):
    resultado = ""
    for letra in texto:
        if letra.isalpha():
            mayuscula = letra.isupper()
            letra = letra.lower()
            codigo = ord(letra)
            codigo += corrimiento
            if codigo > ord('z'):
                codigo -= 26
            resultado += chr(codigo).upper() if mayuscula else chr(codigo)
        else:
            resultado += letra
    return resultado

texto = input("Ingresa el texto a cifrar: ")
corrimiento = int(input("Ingresa el número de corrimiento: "))
print("Texto cifrado:", cifrado_cesar(texto, corrimiento))
