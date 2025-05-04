mascota=input("¿Qué mascota tienes? (perro/gato/pez)").lower()
print(mascota)
'''Sensibilidad a Mayúsculas: La respuesta del usuario debe funcionar independientemente de si escribe "perro", "Perro" o "PERRO". (Pista: ¿recuerdas cómo convertir texto a minúsculas?).
Respuestas Generales:
Si el usuario responde "gato", el programa debe imprimir: ¡Miau! Un felino muy elegante y misterioso.
Si el usuario responde "pez", el programa debe imprimir: ¡Glup! Silencioso pero relajante.
Si el usuario responde cualquier otra cosa que no sea "perro", "gato" o "pez", el programa debe imprimir: Vaya, no conozco mucho sobre las mascotas '[nombre_mascota]'. (Reemplaza [nombre_mascota] con lo que el usuario escribió).
Lógica para Perros (Anidamiento):
Si el usuario responde "perro", el programa primero debe imprimir: ¡Guau! Los perros son geniales.
Luego, debe hacer una segunda pregunta: ¿Qué raza es tu perro? (Ej: Labrador, Bulldog, Poodle, Pastor Alemán, Chihuahua):
Nuevamente, la raza debe compararse sin importar mayúsculas/minúsculas.
Usando una nueva estructura if/elif/else dentro de la sección del perro, el programa debe mostrar información específica para al menos estas razas:
Labrador: Imprimir Temperamento del Labrador: Amigable, extrovertido y dócil. ¡Muy inteligentes y buenos para familias!
Bulldog: Imprimir Temperamento del Bulldog: Calmado, valiente y amigable, aunque a veces un poco testarudo. ¡Mucha personalidad!
Poodle (o si el usuario escribe Caniche): Imprimir Temperamento del Poodle/Caniche: Muy inteligente, activo y elegante. Aprenden rápido.
Pastor Alemán: Imprimir Temperamento del Pastor Alemán: Leal, seguro de sí mismo, valiente y muy inteligente. ¡Excelentes guardianes!
Chihuahua: Imprimir Temperamento del Chihuahua: Vivaz, alerta y con una gran personalidad en un cuerpo pequeño.'''