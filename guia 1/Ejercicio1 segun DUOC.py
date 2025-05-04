print("Test del buen estudiante:")
print("Resdponda usando s para si, y n para no.")
task1 = input("¿Deja para después lo que puede hacer ahora? ")
task2 = input("¿Presta atención en clases? ")
task3 = input("¿Resuelve sus dudas con el profesor? ")
task4 = input("¿Prueba sus hipótesis antes de preguntar? ")
task5 = input("¿Utiliza su tiempo libre para aprender cosas nuevas?")
task6 = input("¿Utiliza otra fuente de información para resolver dudas? ")
task7 = input("¿Estudia solo un día antes de la prueba? ")
task8 = input("¿A sus amigos solo les gusta pasar el rato? ")
task9 = input("¿A menudo realiza acciones que no son importantes? ")
task10 = input("¿Le gustaría no tener que trabajar? ")
task11 = input("¿Le gusta leer? ")
task12 = input("¿Le gustan las redes sociales? ")

puntaje_si = 0
puntaje_no = 0
if task1 == "s":
    puntaje_si += 1
if task2 == "n" :
    puntaje_no += 1
if task3 == "n" :
    puntaje_no += 1
if task4 == "n" :
    puntaje_no += 1
if task5 == "n" :
    puntaje_no += 1
if task6 == "n" :
    puntaje_no += 1
if task7 == "s":
    puntaje_si += 1
if task8 == "s":
    puntaje_si += 1
if task9 == "s":
    puntaje_si += 1
if task10 == "s":
    puntaje_si += 1
if task11 == "n" :
    puntaje_no += 1
if task12 == "s":
    puntaje_si += 1
total = puntaje_no + puntaje_si
print("")
if total < 4 :
    print("Usted es un alumno de buen desempeño")
if total >= 4 and total < 7 :
    print("Usted es un alumno que puede mejorar")
if total >= 7 and total < 10 :
    print("Usted es un alumno con algunos desafíos")
if total >= 10 :
    print("Usted alumno con muchos desafíos")
print("")