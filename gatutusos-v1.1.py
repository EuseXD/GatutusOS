import time
encendido = False
print("Encendiendo...")
time.sleep(1)
print("Gatutus")
time.sleep(0.5)
print("OS")
time.sleep(0.2)
# Esta es la estructura del codigo
time.sleep(5)
encendido = True
try:
 if encendido == True:
		 print("¡Bienvenido a GatutusOS!")
		 print("Help para todos los comandos.")
		 print("Coloca tu usuario:")
		 user = input().lower()
# Mientras encendido sea verdadero, se pediran comandos :P
 while encendido == True:
	 print(user + "~$:")
	 comando = input().lower()
	 if comando == "help":
	 	print("Comandos: propiedades, print, change, juegos, cmr, cat, for")
	 elif comando == "miau":
	 	print("Miau, ¡miau!, em, miau. :)")
	 	time.sleep(0.01)
	 	print("Miau, em... ¡miau!")
	 	time.sleep(0.01)
	 elif comando == "propiedades":
	 	print("/ __/")
	 	print("|  ั⁠ω  ⁠ั|")
	 	print("OS: GatutusOS")
	 	print("Version: 1.1")
	 	print("Creador: Jnanilol en TikTok, EuseOMG en YT.")
	 	print("Repositorio: EuseXD/GatutusOS en GitHub.")
	 	print("Bienvenido a GatutusOS. :3")
	 elif comando == "print":
	 	a_imprimir = input()
	 	print(a_imprimir)
	 elif comando == "change":
	 	print("Argumentos: user, state")
	 	argumento = input().lower()
	 	if argumento == "user":
	 		print("Nuevo nombre de usuario:")
	 		user = input().lower()
	 	elif argumento == "state":
	 		print("Argumentos: off")
	 		argumento = input().lower()
	 		if argumento == "off":
	 			print("Apagando GatutusOS...")
	 			time.sleep(2)
	 			encendido = False
	 		else:
	 			print("Argumento no encontrado. :(")
	 	else:
	 		print("Argumento no encontrado. :(")
	 elif comando == "juegos":
	 	print("Bienvenido a Juegos.")
	 	print("Lista de juegos: Elecciones, Regalos")
	 	print("Ingresa tu argumento.")
	 	argumento = input().lower()
	 	if argumento == "elecciones":
	 		print("Hoy son las elecciones, hay 3 candidatos, ¿por cúal votarás?")
	 		time.sleep(1)
	 		print("1) Gato feo. 2) Gato gordo. 3) Gato helicoptero volador.")
	 		eleccion = input()
	 		if eleccion == "1":
	 			print("Te ha dado media fortuna por votar por el.")
	 		elif eleccion == "2":
	 			print("Te ha asesinado y robado pertenencias, incluido todo el atún y pescado que contenia tu casa")
	 		elif eleccion == "3":
	 		 print("Te agradecio y te dio una de sus colecciones de bombas nucleares como recompensa.")
	 		else:
	 			print("Ingresa 1, 2 o 3")
	 	elif argumento == "regalos":
	 		print("Es el cumpleaños de 5 años de tu gato Felix, ¿qué le daras?")
	 		time.sleep(1)
	 		print("1) Pescado cocinado. 2) Caca. 3) Atún.")
	 		eleccion = input()
	 		if eleccion == "1":
	 			print("Desde ese dia nunca más orino tu almohada.")
	 		elif eleccion == "2":
	 			print("En la noche de ese mismo dia, Felix te asesino.")
	 		elif eleccion == "3":
	 			print("Te dio caricias con la cabeza, a tu gato le encanto el atún.")
	 		else:
	 			print("Ingresa 1, 2 o 3.")
	 	else:
	 		print("Argumento no encontrado. :(")
	 elif comando == "woof":
	 	print("Woof, woof.")
	 elif comando == "cmr":
	 	print("CoMandos Raros")
	 	print("Lista de CMR: woof, miau, cat")
	 elif comando == "cat":
	 	print("/ __/")
	 	print("|  ั⁠ω  ⁠ั|")
	 elif comando == "for":
	 	print("Cadena a repetir")
	 	palabra_for = input()
	 	for iteracion in range(100):
	 		iteracion = iteracion + 1
	 		time.sleep(0.01)
	 		print(palabra_for)
	 else:
	 	print("Orden no encontrada. :( Usa help para más informacion.")
# Este bloque de codigo informa sobre una excepcion que impide ejecutar GatutusOS correctamente.
except:
	print("/ __/")
	time.sleep(0.01)
	print("|  ั⁠ω  ⁠ั|")
	time.sleep(0.01)
	print("Panic!")
	time.sleep(0.01)
	print("System error:")
	time.sleep(0.01)
	print("A line in the code has a exception and the execution is impossible")
