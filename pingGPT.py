import subprocess

def generate_ping_command(character):
    # Genera un comando ping con el carácter dado en el campo de datos
    return f"ping -c 1 -p {character.encode().hex()} 8.8.8.8"

def main():
    input_string = input("Introduce una cadena de texto: ")

    for char in input_string:
        ping_command = generate_ping_command(char)
        try:
            subprocess.run(ping_command, shell=True, check=True)
        except subprocess.CalledProcessError:
            print(f"Error al ejecutar el comando ping para el carácter: {char}")

if __name__ == "__main__":
    main()

