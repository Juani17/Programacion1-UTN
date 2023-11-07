def is_mutant(matrix):
    count = 0
    long = len(matrix)
    
    # creo una funcion llamada fill_matrix que sirve para rellenar la matriz, y si se ingresan caracteres invalidos, o si se ingresan mas o menos de 6 volvera a llamar a la funcion            
    # creo la funcion rows_in_matrix que sirve para comprobar filas
    def rows_in_matrix(matrix):
        count2 = 0
        for i in range(6): 
            char = ''
            consecutive1 = 0

            for j in range(6):
                if matrix[i][j] == char: 
                    consecutive1 += 1
                else:
                    char = matrix[i][j] 
                    consecutive1 = 1
                if consecutive1 == 4:
                    count2 += 1
                    break

        if count2 >= 1:
            return True

        return False
           
    
    # creo la funcion columns_in_matrix que sirve para comprobar columnas
    def columns_in_matrix(matrix):
        count1 = 0
        for i in range(6):
            char = ''
            consecutive = 0

            for j in range(6):
                if matrix[j][i] == char:
                    consecutive += 1
                else:
                    char = matrix[j][i]
                    consecutive = 1
                if consecutive == 4:
                    count1 += 1
                    break
                    
        if count1 >= 1:
            return True

        return False
    
    # Creo la funcion check_diagonals_left_right para comprobar diagonales que comiencen en la izquierda y vayan a la derecha
    def check_diagonals_left_right(matrix):
        count3 = 0
        for i in range(len(matrix) - 3):
            for j in range(len(matrix[0]) - 3):
                if matrix[i][j] == matrix[i+1][j+1] == matrix[i+2][j+2] == matrix[i+3][j+3]:
                    count3 += 1

        if count3 >= 1:
            return True
        
        return False

    # Creo la funcion check_diagonals_right_left para comprobar diagonales que comiencen en la derecha y vayan a la izquierda
    def check_diagonals_right_left(matrix):
        count4 = 0
        for i in range(3, len(matrix)):
            for j in range(len(matrix[0]) - 3):
                if matrix[i][j] == matrix[i-1][j+1] == matrix[i-2][j+2] == matrix[i-3][j+3]:
                    count4 += 1

        if count4 >= 1:
            return True
        
        return False

    # Aca llamamos desde adentro de la funcion, a las otras funciones para que compruebe diagonales, filas y columnas        
    print(matrix)      
    if columns_in_matrix(matrix):
        count =+1
            
    if rows_in_matrix(matrix):
        count += 1

    if check_diagonals_left_right(matrix):
        count += 1

    if check_diagonals_right_left(matrix):
        count += 1

    if count >= 2:
        
        return True
    else:
        
        return False
   
 
# creo el main
print("Hola, soy Magneto, necesito que ingreses tu adn para saber si eres mutante o no. ")
dna_matrix = [['A', 'T', 'G', 'C', 'G', 'A'],
              ['C', 'A', 'G', 'T', 'G', 'C'],
              ['T', 'T', 'A', 'T', 'T', 'T'],
              ['A', 'G', 'A', 'C', 'G', 'G'],
              ['G', 'C', 'G', 'T', 'C', 'A'],
              ['T', 'C', 'A', 'C', 'T', 'G']]


if is_mutant(dna_matrix):
    print("Eres mutante")
else:
    print("No eres mutante")