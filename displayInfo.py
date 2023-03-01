# Despliega informacion y revisa la consistencia de los archivos
print("------------------")
print("Revisión de consistencia del repositorio de pruebas")
print("------------------")
files = ["AUTHOR.txt", 
         "SYSTEM.info",
         "VERSION.info",
         "CONTRIBUTE.txt"]
info_msgs = []
puntaje = 0

print("Verificando que todos los archivos existen...")
for file in files:
    try:
        file_info = open(file)
        print("--> se ha encontrado el archivo:", file)
        if file == "AUTHOR.txt": info_msgs.append("Autor: " + file_info.read().rstrip())
        if file == "SYSTEM.info": info_msgs.append("Sistema: " + file_info.read().rstrip())
        if file == "VERSION.info": info_msgs.append("Repositorio: testrepo-actividad " + file_info.read().rstrip())
        if file == "CONTRIBUTE.txt": info_msgs.append("Contribuye: " + file_info.read().rstrip())
        file_info.close()
    except FileNotFoundError:
        print("--> ERROR: no se ha encontrado el archivo:", file)

print("Ha concluido la revisión de archivos")
print("------------------")
print("La información recopilada es la siguiente:")
for msg in info_msgs:
    print("   " + msg)
print("------------------")
print("Verificando el contenido de los archivos...")
if info_msgs[1] != "Sistema: Windows 10": 
    print("--> OK: La información de sistema ha sido actualizada")
    puntaje += 1
else: 
    print("--> ERROR: La información de sistema no ha sido actualizada")
if info_msgs[2] != "Repositorio: testrepo-actividad version 0.3": 
    print("--> OK: La información de versión ha sido actualizada")
    puntaje += 1
else: 
    print("--> ERROR: La información de versión no ha sido actualizada")
if len(info_msgs) == 4:
    print("--> OK: Se ha incluido información de contribución")
    puntaje += 2
else:
    print("--> ERROR: No se ha incluido información de contribución")

print("------------------")
print("El puntaje obtenido en la actividad es:", puntaje, "de 4 puntos")
print("------------------")
