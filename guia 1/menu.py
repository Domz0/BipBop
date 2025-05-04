mascota=input("¿Qué mascota tienes? (perro/gato/pez)").lower()
try:
    if mascota=="perro":
        print("¡Guau! Los perros son geniales.")
        raza=input("Cual es la raza de tu perro? (Labrador, Bulldog, Poodle, Pastor Alemán, Chihuahua)").lower()

        if raza == "labrador": 
            print("Temperamento del Labrador: Amigable, extrovertido y dócil. ¡Muy inteligentes y buenos para familias!")
        elif raza == "bulldog": 
            print("Temperamento del Bulldog: Calmado, valiente y amigable, aunque a veces un poco testarudo. ¡Mucha personalidad!")
        elif raza == "poodle" or raza == "caniche": 
            print("Temperamento del Poodle/Caniche: Muy inteligente, activo y elegante. Aprenden rápido.")
        elif raza == "pastor aleman": 
            print("Temperamento del Pastor Alemán: Leal, seguro de sí mismo, valiente y muy inteligente. ¡Excelentes guardianes!")
        elif raza == "chihuahua": 
            print("Temperamento del Chihuahua: Vivaz, alerta y con una gran personalidad en un cuerpo pequeño.")

    elif mascota=="gato":
        print("¡Miau! Un felino muy elegante y misterioso.")
    elif mascota=="pez":
        print("¡Glup! Silencioso pero relajante.")
except:
    print(f"Vaya, no conozco mucho sobre las mascotas '{mascota}'.")