# Permite usar la funcion "random" para elejir palabras al azar
import random

def choise_word():
    #Elije una palabra al azar de las escritas
    return random.choice(words)

def show_word(word, correct_letter):
    # Mostramos la palabra oculta con guiones bajos, y a medida que se adivinan letras, se van remplazando las letras adivinadas por los guiones correspondientes
    show = ""
    for letter in word:
        if letter in correct_letter:
            show += letter
        else:
            show += "_"
    return show

def play_game():
    maximum_attempts = 6
    secrtet_word = choise_word()
    guessed_letter = []
    attemps = maximum_attempts

    print("Comencemos el ahorcado!")
    print("Tenés que adivinar una palabra, letra por letra.")
    print(f"Tenés {maximum_attempts} intentos para adivinar la palabra.")

    while attemps > 0:
        #Mostramos la palabra oculta
        chosen_word = show_word(secrtet_word, guessed_letter)
        print("\nPalabra actual:", chosen_word)
        
        #Una vez que completemos la palabra, mostraremos el mensaje de victoria y con un break saldremos de la ejecución 
        if chosen_word == secrtet_word:
            print("\n¡Felicidades! Adivinaste la palabra:", secrtet_word, "!")
            break
        
        #Pedimos que se ingrese una letra y corroboramos que sea valida
        letter_selected = input("Ingresá una letra: ").lower()

        if len(letter_selected) != 1 or not letter_selected.isalpha():
            print("Por favor, ingresá una letra válida.")
            continue

        #Si la letra ya ha sido ingresada, mostraremos este mensaje
        if letter_selected in guessed_letter:
            print("Ya has adivinado esa letra.")
            continue

        guessed_letter.append(letter_selected)

        #Cada vez que se adivine una letra, mostraemos este mensaje
        if letter_selected in secrtet_word:
            print("¡Adivinaste una letra correctamente!")
        else:
            #En caso contrario restaremos un intento y mostramos el siguiente mensaje
            attemps -= 1
            print("Letra incorrecta, te quedan", attemps, "intentos.")

    #Al acabarse los intentos mostramos el mensaje de derrota
    if attemps == 0:
        print("\n¡Perdiste! La palabra secreta era:", secrtet_word)


# Lista de palabras para adivinar
words = ["messi", "tecnicatura", "programacion", "teclado", "hamburguesa", "ahorcado", "estufa", "otorrinolaringologo"]
# Ejecucción del juego
play_game()