'''Un instituto de inglés necesita un programa que le permita, cada día, procesar 
observaciones sobre las clases de ese día. El instituto dicta clases a estudiantes de
distintos niveles y cada nivel tiene clases en un día de la semana diferente: los lunes se
dicta nivel inicial, los martes el nivel intermedio, los miércoles el nivel avanzado, los
jueves son para práctica hablada y los viernes se dicta inglés para viajeros.
Se debe comenzar por solicitar al usuario que ingrese la fecha actual en formato “día,
DD/MM”, donde [día] es un día de la semana, DD es el número de día y MM es el
número de mes. Si el usuario ingresa un día de la semana inexistente o una fecha cuyo
día supere el número 31 o el mes supere el número 12, finalizar el programa indicando
que se produjo un error. Debe permitirse que ingrese el día de la semana en
minúsculas o mayúsculas indistintamente. Como precondición se tiene que lo
ingresado por el usuario tendrá la forma <[alfanumérico], [numérico]/[numérico]>.
Una vez indicada la fecha el usuario necesita poder indicar si ese día se tomaron los
exámenes, pero eso solo si se trata de los niveles inicial, intermedio o avanzado, ya
que las prácticas habladas y el inglés para viajeros no tienen exámenes. Si hubo
exámenes, el usuario ingresará cuántos alumnos aprobaron y cuantos no, y el
programa le mostrará el porcentaje de aprobados.
Si el día fue el correspondiente a práctica hablada, el usuario deberá ingresar el
porcentaje de asistencia a clase y el programa le indicará ‘asistió la mayoría’ en caso de
que la asistencia sea mayor al 50% o ‘no asistió la mayoría’ si no es así.
Si se trata del inglés para viajeros y la fecha actual corresponde al día 1 del mes 1 o del
mes 7, se deberá imprimir ‘Comienzo de nuevo ciclo’ y solicitar al usuario que ingrese
la cantidad de alumnos del nuevo ciclo y el arancel en $ por cada alumno, para luego
imprimir el ingreso total en $.'''


def validar_fecha(fecha):
    dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes"]
    dia_mes = fecha.split(", ")[1].split("/")
    dia = int(dia_mes[0])
    mes = int(dia_mes[1])
    
    if dia > 31 or mes > 12:
        return False
    
    dia_semana = fecha.split(", ")[0].lower()
    if dia_semana not in dias_semana:
        return False
    
    return True

def main():
    fecha_actual = input("Ingrese la fecha actual en el siguiente formato: [dia, DD/MM] ")
    if validar_fecha(fecha_actual):
        dia_semana = fecha_actual.split(", ")[0].lower()
        dia_mes = fecha_actual.split(", ")[1]
        dia = int(dia_mes.split("/")[0])
        mes = int(dia_mes.split("/")[1])
        
        print(dia_semana.capitalize(), dia, mes)
    else:
        print("Error al ingresar datos")

    if dia_semana == "lunes" or dia_semana == "miércoles" or dia_semana == "martes":
        rta = input("Tomo examen, responda con S/N ")
        rta = rta.upper()
        if rta == "S":
            apro = int(input("Ingrese la cantidad de aprobados "))
            desapro = int(input("Ingrese la cantidad de desaprobados "))
            porto = int((apro * 100)/(apro + desapro))
            print(f"El porcentaje de aprobados es",{porto},"%")
    else:
        print("No hubo examen")

    if dia_semana == "jueves":
        asist = int(input("Ingrese la cantidad de alumnos que asistieron a clases "))
        asist_comp = int(input("Ingrese la cantidad de alumnos que tiene en su clase "))
        por_asist = int((asist * 100)/(asist_comp))
        if por_asist > 50:
            print(f"Asistio la mayoria")
        else:
            print("No asistio la mayoria")
    
    if dia_semana == "viernes":
        if dia == 1:
            if mes == 1 or mes == 7:
                print("COMIENZO DE NUEVO CICLO")
                c_alum = int(input("Ingrese la cantidad de alumnos del nuevo ciclo "))
                p_alum = int(input("Ingrese el arancel en $ por alumno "))
                p_tot = c_alum * p_alum
                print(f"El arancel total em $ es: ",{p_tot})
            

        

    

if __name__ == "__main__":
    main()
