print("Test del buen estudiante:")
print("Responda usando s para si, y n para no.")

preguntas=["¿Deja para después lo que puede hacer ahora? "
           ,"¿Presta atención en clases? "
           ,"¿Resuelve sus dudas con el profesor? "
           ,"¿Prueba sus hipótesis antes de preguntar? "
           ,"¿Utiliza su tiempo libre para aprender cosas nuevas?"
           ,"¿Utiliza otra fuente de información para resolver dudas? "
           ,"¿Estudia solo un día antes de la prueba? "
           ,"¿A sus amigos solo les gusta pasar el rato? "
           ,"¿A menudo realiza acciones que no son importantes? "
           ,"¿Le gustaría no tener que trabajar? "
           ,"¿Le gusta leer? "
           ,"¿Le gustan las redes sociales? "]
puntajecompleto=["s","n","n","n","n","n","s","s","s","s","n","s"]

puntaje=0
for x in range(len(preguntas)):
    ask=input(preguntas[x])
    if ask==puntajecompleto[x]:
        puntaje+=1

print("")
if puntaje < 4 :
    print("Usted es un alumno de buen desempeño")
elif puntaje >= 4 and puntaje < 7 :
    print("Usted es un alumno que puede mejorar")
elif puntaje >= 7 and puntaje < 10 :
    print("Usted es un alumno con algunos desafíos")
elif puntaje >= 10 :
    print("Usted alumno con muchos desafíos")