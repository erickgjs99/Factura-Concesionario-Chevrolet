veh = "0"
while veh < "1" or veh > "4":
	print("-------------Bienvenido a Chevrolet--------------")
	print("----------------Find New Roads-------------------")
	print("Bienvenido a la personalizacion de autos del consecionario Chevrolet")
	print("Elija uno de nuestros cuatros vehiculos disponibles")
	print(" 1._ Sail Sedan")
	print(" 2._ Sail Hatchback")
	print(" 3._ Aveo Family")
	print(" 4._ Aveo Emotion")
	veh= input("Digite el numero de vehiculo que desea ")
	if veh < "1" or veh > "4":
		print(" --------Usuario, ingrese un numero de vehiculo valido------- ")
		print(" -------------------------------------------------------------")
if veh == "1":
	print("Perfecto usted escogio el vehiculo Sail Sedan, el cual tiene las siguientes caracteristicas ")
	print ("Su vehiculo tiene una capacidad de carga de 375 Kg")
	print ("El cilindraje es de 1398.4 cc")
	print("Aros acero R14")
	print("Elevavidrios eléctricos")
	print("Espejos eléctricos")
	print("Llantas R14 ")
	print("Luces Antiniebla")
	print("Radio MP3-USB-IPOD")
	print("Tapicería tela")
	precsiniva = 16750
	cargaVeh = 375
	print(" El precio del vehiculo Sail Sedan es de " + str(precsiniva) + " USD")
else:
	if veh == "2":
		print("Perfecto, usted escogió el vehiculo Sail Hatchback, el cual tiene las siguientes caracteristicas")
		print ("Su vehiculo tiene una capacidad de carga de 384 Kg")
		print ("El cilindraje es de 1398.4 cc")
		print("Aire acondicionado")
		print("Alarma")
		print("Aros acero R14")
		print("Elevavidrios eléctricos")
		print("Espejos eléctricos")
		print("Llantas R14")
		print("luces Antiniebla")
		print("Radios MP3-USB-IPOD")
		print("tapiceria tela")
		precsiniva = 17080
		cargaVeh = 384
		print (" El precio del vehiculo Sail Hatchback es de: " +str(precsiniva)+" USD")
	else:
		if veh == "3":
			print("Perfecto usted escogio el vehiculo Aveo Family, el cual tiene las siguientes caracteristicas ")
			print ("Su vehiculo tiene una capacidad de carga de 325 Kg")
			print ("El cilindraje es de 1498 cc")
			print("Aros acero R14")
			print("Espejos manuales")
			print("Llantas R14 ")
			print("Radio CD")
			print("Tapicería tela")
			precsiniva = 15435
			cargaVeh = 325
			print ("El precio del vehiculo Aveo Family es de: " +str(precsiniva)+ " USD")
		else:
			if veh == "4":
				print("Perfecto usted escogio el vehiculo Aveo Emotion, el cual tiene las siguientes caracteristicas ")
				print ("Su vehiculo tiene una capacidad de carga de 410 Kg")
				print ("El cilindraje es de 1598 cc")
				print("Aire acondicionado")
				print("Alarma")
				print("Aros acero R15")
				print("Elevavidrios eléctricos")
				print("Espejos manuales")
				print("Llantas R15 ")
				print("Luces Antiniebla")
				print("Radio CD")
				print("Tapicería tela")
				precsiniva = 18490
				cargaVeh = 410
				print (" El precio del vehiculo Aveo Emotion es de: "+ str(precsiniva) + " USD")
modif = "0"
print("------------------Modificaciones para su Vehiculo Chevrolet-------------------")
print("Desea personalizar su vehículo Chevrolet :) ")
print("1.- Si")
print("2.- No")
modif = input("Seleccione una opcion 1 o 2   ")
print("-------------------------------------------------------------------------------")
#modificaciones para el primer auto
if modif == "1" and veh == "1":
		#Aire acondicionado
	pVeh = precsiniva
	print("El vehículo seleccionado tiene las siguientes modificaciones disponibles")
	print("Aire acondicionado")
	print("1.- Añadirlo")
	print("2.- No Añadirlo")
	aireAcond = input("Que accion desea realizar con el aire acondicionado seleccione una opción: ")
	if aireAcond =="1":
		precaireAcond = 315
		pVeh = precsiniva + precaireAcond
		print(" El precio adicional es de " +str (precaireAcond)+" USD")
		print("El precio del vehiculo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con la alarma de su vehículo")
		print("------------------------------------------------")
	if aireAcond == "2":
		print("El precio del vehiculo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con la alarma de su vehículo")
		print("------------------------------------------------")
	#Alarma
	print("Alarma")
	print("1.- Añadirlo")
	print("2.- No Añadirlo")
	alarma = input ("Que acción desea realizar con la alarma, seleccione una opción: ")
	if 	alarma == "1":
		precalarma = 160
		pVeh = pVeh + precalarma
		print(" El precio adicional es de " +str (precalarma)+" USD")
		print ("El precio del vehiculo es de: " + str(pVeh)+" USD")
		print("A continuación seguiremos con el kit de aros y llantas de su vehículo ")
		print ("------------------------------------------------")
	if alarma == "2":
		print("El precio del vehiculo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con el kit de aros y llantas de su vehículo")
		print ("------------------------------------------------")
	#Unir aros con llantas en un solo kit
	print("Kit de aros y llantas")
	print ("1.- Modificar a aros acero R15 + llantas R15")
	print ("2.- Modificar a aros aluminio R14 + llantas R14")
	print ("3.- Modificar a aros aluminio R15 + llantas R15")
	print ("4.- Mantener aros de acero R14 + llantas R14")
	aros = input("Que acción desea realizar con el kit, seleccione una opción:  ")
	if 	aros == "1":
		precaros = 580
		pVeh = pVeh -510 + precaros
		print(" El precio adicional es de " +str (precaros)+" USD")
		print ("El precio del vehículo es de: " + str(pVeh)+" USD")
		print("A continuación seguiremos con el ChevyStar Connect de su vehículo ")
		print ("------------------------------------------------")
	if 	aros == "2":
		precaros = 690
		pVeh = pVeh - 510 + precaros
		print(" El precio adicional es de " +str (precaros)+" USD")
		print ("El precio del vehiculo es de: " + str(pVeh)+" USD")
		print("A continuación seguiremos con el ChevyStar Connect de su vehículo ")
		print ("------------------------------------------------")
	if 	aros == "3":
		precaros = 780
		pVeh = pVeh - 510 + precaros
		print(" El precio adicional es de " +str (precaros)+" USD")
		print ("El precio del vehiculo es de: " + str(pVeh)+" USD")
		print("A continuación seguiremos con el ChevyStar Connect de su vehículo ")
		print ("------------------------------------------------")
	if aros == "4":
		print("El precio del vehículo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con el ChevyStar Connect de su vehículo ")
		print ("------------------------------------------------")
	#ChevyStar Connect
	print("ChevyStar Connect")
	print ("1.- Añadirlo")
	print ("2.- No añadirlo")
	chevyStar = input ("Que acción desea realizar con el ChevyStar Connect, seleccione una opción: ")
	if 	chevyStar == "1":
		pchevyStar = 90
		pVeh = pVeh + pchevyStar
		print(" El precio adicional es de " +str (pchevyStar)+" USD")
		print("El precio del vehiculo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con el elevavidrios eléctricos de su vehículo ")
		print ("------------------------------------------------")
	if chevyStar == "2":
		print("El precio del vehiculo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con el elevavidrios eléctricos de su vehículo")
		print ("------------------------------------------------")
	#Elevavidrios eléctricos
	print("Elevavidrios eléctricos")
	print ("1.- Desea mantenerlos")
	print ("2.- Desea eliminarlos")
	vidrioelec = input ("Que acción desea realizar con el elevavidrios eléctrico, seleccione una opción: ")
	if 	vidrioelec == "1":
		print("El precio del vehiculo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con el emblema ""Chevrolet"" de su vehículo ")
		print ("------------------------------------------------")
	if vidrioelec == "2":
		pvidrioelec = 45
		pVeh = pVeh - pvidrioelec
		print("El precio del vehiculo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con el emblema ""Chevrolet"" de su vehículo")
		print ("------------------------------------------------")
	#Emblema Chevrolet
	print("Emblema ""Chevrolet""")
	print ("1.- Añadirlo")
	print ("2.- No modificar")
	emblema = input ("Que acción desea realizar con el emblema ""Chevrolet"", seleccione una opción: ")
	if 	emblema == "1":
		pemblema = 20
		pVeh = pVeh + pemblema
		print(" El precio adicional es de " +str (pemblema)+" USD")
		print("El precio del vehiculo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con el kit de herramientas de su vehículo ")
		print ("------------------------------------------------")
	if 	emblema == "2":
		print("El precio del vehiculo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con el kit de herramientas de su vehículo")
		print ("------------------------------------------------")
	#Kit de herramientas
	print("Kit de herramientas")
	print ("1.- Añadirlo")
	print ("2.- No añadirlo")
	kitHerra = input ("Que acción desea realizar con el Kit de herramientas, seleccione una opción: ")
	if 	kitHerra == "1":
		pkitHerra = 60
		pVeh = pVeh + pkitHerra
		print(" El precio adicional es de " +str (pkitHerra)+" USD")
		print("El precio del vehiculo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con las lucen antiniebla de su vehículo ")
		print ("------------------------------------------------")
	if kitHerra == "2":
		print("El precio del vehiculo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con las luces antiniebla de su vehículo")
		print ("------------------------------------------------")
#Luces antiniebla
	print("Luces antiniebla")
	print ("1.- Desea mantenerlos")
	print ("2.- Desea eliminarlos")
	luAntin = input ("Que acción desea realizar con las luces antiniebla, seleccione una opción: ")
	if 	luAntin == "1":
		pluAntin = 110
		print("El precio del vehiculo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con la Moqueta rigida del baul de su vehículo")
		print ("------------------------------------------------")
	if luAntin == "2":
		pluAntin = 110
		pVeh = pVeh - pluAntin
		print("El precio del vehiculo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con la Moqueta rigida del baul de su vehículo")
		print ("------------------------------------------------")
#Moqueta rígida baul
	print("Moqueta rígida baul")
	print ("1.- Añadirlo")
	print ("2.- No añadirlo")
	moqueta = input ("Que acción desea realizar con la Moqueta rígida del baul, seleccione una opción: ")
	if 	moqueta == "1":
		pmoqueta = 85
		pVeh = pVeh + pmoqueta
		print(" El precio adicional es de " +str (pmoqueta)+" USD")
		print("El precio del vehiculo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con el Protector de carter de su vehículo ")
		print ("------------------------------------------------")
	if moqueta == "2":
		print("El precio del vehiculo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con el Protector de carter de su vehículo")
		print ("------------------------------------------------")
#Protector de carter
	print("Protector de carter")
	print ("1.- Añadirlo")
	print ("2.- No añadirlo")
	proteCart = input ("Que acción desea realizar con el Protector de carter, seleccione una opción: ")
	if 	proteCart == "1":
		pproteCart= 75
		pVeh = pVeh + pproteCart
		print(" El precio adicional es de " +str (pproteCart)+" USD")
		print("El precio del vehículo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con el radio de su vehículo")
		print ("------------------------------------------------")
	if proteCart == "2":
		print("El precio del vehículo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con el radio de su vehículo")
		print ("------------------------------------------------")
#Radio
	print ("Radio")
	print ("1.-Desea mantener la Radio MP3-USB-IPOD")
	print ("2.-Desea cambiarlo por la Radio Cd")
	radio = input ("Que acción desea realizar con la radio, seleccione una opción: ")
	if radio =="1":
		print("El precio del vehículo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con el sensor de reversa de su vehículo")
		print ("------------------------------------------------")
	if radio == "2":
		pradioc = 205
		pVeh = pVeh - 345 + pradioc
		print("El precio del vehículo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con el sensor de reversa de su vehículo")
		print ("------------------------------------------------")
#Sensor de reversa
	print ("Sensor de reversa")
	print ("1.- Añadirlo")
	print ("2.- No añadirlo")
	sensor = input ("Que acción desea realizar con el sensor de reversa, seleccione una opción: ")
	if sensor == "1":
		psensor= 85
		pVeh = pVeh + psensor
		print(" El precio adicional es de " +str (psensor)+" USD")
		print("El precio del vehículo es de: " + str(pVeh) + " USD")
		print("Finalmente seguiremos con la tapiceria de su vehículo")
		print ("------------------------------------------------")
	if sensor == "2":
		print("El precio del vehículo es de: " + str(pVeh) + " USD")
		print("Finalmente seguiremos con la tapiceria de su vehículo")
		print ("------------------------------------------------")
#Tapiceria
	print("Tapiceria")
	print("1.-Desea mantener la tapiceria de tela")
	print ("2.-Desea modificarla por la Tapiceria de cuero")
	tapiceria =input ("Que acción desea realizar con la tapiceria , seleccione una opción: ")
	if tapiceria == "1":
		print ("------------------------------------------------")
		print("El precio del vehículo es de: " + str(pVeh) + " USD")
		print ("------------------------------------------------")
	if tapiceria ==	"2":
		ptapicuero = 760
		pVeh = pVeh - 520 + ptapicuero
		print ("------------------------------------------------")
		print("El precio del vehículo es de: " + str(pVeh) + " USD")
		print ("------------------------------------------------")
if veh =="1":
	if modif == "1" or modif == "2":
		#Seguro primer vehiculo Sail Sedan
		print("Verifique los seguros disponibles para su vehiculo Chevrolet")
		print("-------------------Tipo de Seguro---------------------------")
		print("1._ Cobertura Amplia de 1100 a 1399 cc")
		print("2._ Cobertura Limitada de 1100 a 1399 cc")
		print("3._ Cobertura Responsabilidad Civil de 1100 a 1399 cc")
		print("4._ No adquirir seguro")
		segu = input ("Ingrese el numero de tipo de seguro que dedea adquirir para su vehiculo ")
		if veh == "1" and segu == "1":
			pSegu = cargaVeh*2
			print("------------------------------------------------")
			print("El costo del seguro para su Chevrolet es de " + str(pSegu) +" USD")
			print("------------------------------------------------")
		else:
			if veh == "1" and segu == "2":
				pSegu = cargaVeh *1.4
				print("------------------------------------------------")
				print("El costo del seguro para su Chevrolet es de " + str(pSegu)  +" USD")
				print("------------------------------------------------")
			else:
				if veh == "1" and segu == "3" :
					pSegu = cargaVeh *0.8
					print("------------------------------------------------")
					print("El costo del seguro para su Chevrolet es de " + str(pSegu) +" USD")
					print("------------------------------------------------")
				else:
					if veh == "1" and segu == "4" and modif == "1":
						pSegu = 0
						print("El costo del vehiculo actual es de: "+ str(pVeh)+" USD")
						print("------------------------------------------------")
					else:
						if veh == "1" and segu == "4" and modif == "2":
							pSegu = 0
							print("El costo del vehiculo actual es de: "+ str(precsiniva)+ "USD")
#modificaciones para el segundo vehículo
if modif == "1" and veh == "2":
#Aire acondicionado
	pVeh = precsiniva
	print("El vehículo seleccionado tiene las siguientes modificaciones disponibles")
	print("Aire acondicionado")
	print("1.- Desea mantenerlo ")
	print("2.- Desea eliminarlo")
	aireAcond = input("Que accion desea realizar con el aire acondicionado seleccione una opción: ")
	if aireAcond =="1":
		print("El precio del vehiculo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con la alarma de su vehículo")
		print("------------------------------------------------")
	if aireAcond == "2":
		precaireAcond = 315
		pVeh = precsiniva - precaireAcond
		print("El precio del vehiculo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con la alarma de su vehículo")
		print("------------------------------------------------")
	#Alarma
	print("Alarma")
	print("1.- Mantenerla")
	print("2.- Desea eliminarla")
	alarma = input ("Que acción desea realizar con la alarma, seleccione una opción: ")
	if 	alarma == "1":
		print ("El precio del vehiculo es de: " + str(pVeh)+" USD")
		print("A continuación seguiremos con el kit de aros y llantas de su vehículo ")
		print ("------------------------------------------------")
	if alarma == "2":
		precalarma = 160
		pVeh = pVeh - precalarma
		print("El precio del vehiculo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con el kit de aros y llantas de su vehículo")
		print ("------------------------------------------------")
	#Unir aros con llantas en un solo kit
	print("Kit de aros y llantas")
	print ("1.- Modificar a aros acero R15 + llantas R15")
	print ("2.- Modificar a aros aluminio R14 + llantas R14")
	print ("3.- Modificar a aros aluminio R15 + llantas R15")
	print ("4.- Mantener aros de acero R14 + llantas R14")
	aros = input("Que acción desea realizar con el kit, seleccione una opción:  ")
	if 	aros == "1":
		precaros = 580
		pVeh = pVeh -510 + precaros
		print(" El precio adicional es de " +str (precaros)+" USD")
		print ("El precio del vehículo es de: " + str(pVeh)+" USD")
		print("A continuación seguiremos con el ChevyStar Connect de su vehículo ")
		print ("------------------------------------------------")
	if 	aros == "2":
		precaros = 690
		pVeh = pVeh - 510 + precaros
		print(" El precio adicional es de " +str (precaros)+" USD")
		print ("El precio del vehiculo es de: " + str(pVeh)+" USD")
		print("A continuación seguiremos con el ChevyStar Connect de su vehículo ")
		print ("------------------------------------------------")
	if 	aros == "3":
		precaros = 780
		pVeh = pVeh - 510 + precaros
		print(" El precio adicional es de " +str (precaros)+" USD")
		print ("El precio del vehiculo es de: " + str(pVeh)+" USD")
		print("A continuación seguiremos con el ChevyStar Connect de su vehículo ")
		print ("------------------------------------------------")
	if aros == "4":
		print("El precio del vehículo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con el ChevyStar Connect de su vehículo ")
		print ("------------------------------------------------")
	#ChevyStar Connect
	print("ChevyStar Connect")
	print ("1.- Añadirlo")
	print ("2.- No añadirlo")
	chevyStar = input ("Que acción desea realizar con el ChevyStar Connect, seleccione una opción: ")
	if 	chevyStar == "1":
		pchevyStar = 90
		pVeh = pVeh + pchevyStar
		print(" El precio adicional es de " +str (pchevyStar)+" USD")
		print("El precio del vehiculo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con el kit de herramientas ""Chevrolet"" de su vehículo ")
		print ("------------------------------------------------")
	if chevyStar == "2":
		print("El precio del vehiculo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con el kit de herramientas ""Chevrolet"" de su vehículo")
		print ("------------------------------------------------")
#Kit de herramientas
	print("Kit de herramientas")
	print ("1.- Añadirlo")
	print ("2.- No añadirlo")
	kitHerra = input ("Que acción desea realizar con el Kit de herramientas, seleccione una opción: ")
	if 	kitHerra == "1":
		pkitHerra = 60
		pVeh = pVeh + pkitHerra
		print(" El precio adicional es de " +str (pkitHerra)+" USD")
		print("El precio del vehiculo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con las luces antiniebla de su vehículo ")
		print ("------------------------------------------------")
	if kitHerra == "2":
		print("El precio del vehiculo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con las luces antiniebla de su vehículo")
		print ("------------------------------------------------")
#Luces antiniebla
	print("Luces antiniebla")
	print ("1.- Desea mantenerlos")
	print ("2.- Desea eliminarlos")
	luAntin = input ("Que acción desea realizar con las luces antiniebla, seleccione una opción: ")
	if 	luAntin == "1":
		pluAntin = 110
		print("El precio del vehiculo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con el protector de carter del baul de su vehículo")
		print ("------------------------------------------------")
	if luAntin == "2":
		pluAntin = 110
		pVeh = pVeh - pluAntin
		print("El precio del vehiculo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con la el protector de carter de su vehículo")
		print ("------------------------------------------------")
#Protector de carter
	print("Protector de carter")
	print ("1.- Añadirlo")
	print ("2.- No añadirlo")
	proteCart = input ("Que acción desea realizar con el Protector de carter, seleccione una opción: ")
	if 	proteCart == "1":
		pproteCart= 75
		pVeh = pVeh + pproteCart
		print(" El precio adicional es de " +str (pproteCart)+" USD")
		print("El precio del vehículo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con el radio de su vehículo")
		print ("------------------------------------------------")
	if proteCart == "2":
		print("El precio del vehículo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con el radio de su vehículo")
		print ("------------------------------------------------")
#Radio
	print ("Radio")
	print ("1.-Desea mantener la Radio MP3-USB-IPOD")
	print ("2.-Desea cambiarlo por la Radio Cd")
	radio = input ("Que acción desea realizar con la radio, seleccione una opción: ")
	if radio =="1":
		print("El precio del vehículo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con el sensor de reversa de su vehículo")
		print ("------------------------------------------------")
	if radio == "2":
		pradioc = 205
		pVeh = pVeh - 345 + pradioc
		print("El precio del vehículo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con el sensor de reversa de su vehículo")
		print ("------------------------------------------------")
#Sensor de reversa
	print ("Sensor de reversa")
	print ("1.- Añadirlo")
	print ("2.- No añadirlo")
	sensor = input ("Que acción desea realizar con el sensor de reversa, seleccione una opción: ")
	if sensor == "1":
		psensor= 85
		pVeh = pVeh + psensor
		print(" El precio adicional es de " +str (psensor)+" USD")
		print("El precio del vehículo es de: " + str(pVeh) + " USD")
		print("Finalmente seguiremos con la tapiceria de su vehículo")
		print ("------------------------------------------------")
	if sensor == "2":
		print("El precio del vehículo es de: " + str(pVeh) + " USD")
		print("Finalmente seguiremos con la tapiceria de su vehículo")
		print ("------------------------------------------------")
#Tapiceria
	print("Tapiceria")
	print("1.-Desea mantener la tapiceria de tela")
	print ("2.-Desea modificarla por la Tapiceria de cuero")
	tapiceria =input ("Que acción desea realizar con la tapiceria , seleccione una opción: ")
	if tapiceria == "1":
		print ("------------------------------------------------")
		print("El precio del vehículo es de: " + str(pVeh) + " USD")
		print ("------------------------------------------------")
	if tapiceria ==	"2":
		ptapicuero = 760
		pVeh = pVeh - 520 + ptapicuero
		print ("------------------------------------------------")
		print("El precio del vehículo es de: " + str(pVeh) + " USD")
		print ("------------------------------------------------")
if veh =="2":
	if modif =="1"  or modif == "2":
	#Seguro segundo vehiculo Sail Hatchback
		print("Verifique los seguros disponibles para su vehiculo Chevrolet")
		print("-------------------Tipo de Seguro---------------------------")
		print("1._ Cobertura Amplia de 1100 a 1399 cc")
		print("2._ Cobertura Limitada de 1100 a 1399 cc")
		print("3._ Cobertura Responsabilidad Civil de 1100 a 1399 cc")
		print("4._ No adquirir seguro")
		segu = input ("Ingrese el numero de tipo de seguro que dedea adquirir para su vehiculo ")
		if veh == "2" and segu == "1" :
			pSegu = cargaVeh*2
			print("------------------------------------------------")
			print("El costo del seguro para su Chevrolet es de " + str(pSegu) +" USD")
			print ("------------------------------------------------")
		else:
			if veh == "2" and segu == "2":
				pSegu = cargaVeh *1.4
				print("------------------------------------------------")
				print("El costo del seguro para su Chevrolet es de " + str(pSegu) +" USD")
				print ("------------------------------------------------")
			else:
				if veh == "2" and segu == "3" :
					pSegu = cargaVeh *0.8
					print("------------------------------------------------")
					print("El costo del seguro para su Chevrolet es de " + str(pSegu)+" USD")
					print ("------------------------------------------------")
				else:
					if veh == "2" and segu == "4" and modif == "1":
						pSegu = 0
						print("------------------------------------------------")
						print("El costo del vehiculo actual es de: "+ str(pVeh)+" USD")
						print ("------------------------------------------------")
					else:
						if veh == "2" and segu == "4" and modif == "2":
							pSegu = 0
							print("------------------------------------------------")
							print("El costo del vehiculo actual es de: "+ str(precsiniva)+ " USD")
							print ("------------------------------------------------")
#Modificaciones tercer vehículo
if modif == "1" and veh == "3":
#Aire acondicionado
	pVeh = precsiniva
	print("El vehículo seleccionado tiene las siguientes modificaciones disponibles")
	print("Aire acondicionado")
	print("1.- Añadirlo")
	print("2.- No añadirlo")
	aireAcond = input("Que accion desea realizar con el aire acondicionado seleccione una opción: ")
	if aireAcond =="1":
		precaireAcond = 315
		pVeh =  precsiniva + precaireAcond
		print("El precio del vehiculo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con la alarma de su vehículo")
		print("------------------------------------------------")
	if aireAcond == "2":
		print("El precio del vehiculo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con la alarma de su vehículo")
		print("------------------------------------------------")
#Alarma
	print("Alarma")
	print("1.- Añadirlo")
	print("2.- No Añadirlo")
	alarma = input ("Que acción desea realizar con la alarma, seleccione una opción: ")
	if 	alarma == "1":
		precalarma = 160
		pVeh = pVeh + precalarma
		print(" El precio adicional es de " +str (precalarma)+" USD")
		print ("El precio del vehiculo es de: " + str(pVeh)+" USD")
		print("A continuación seguiremos con el kit de aros y llantas de su vehículo ")
		print ("------------------------------------------------")
	if alarma == "2":
		print("El precio del vehiculo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con el kit de aros y llantas de su vehículo")
		print ("------------------------------------------------")
#Unir aros con llantas en un solo kit
	print("Kit de aros y llantas")
	print ("1.- Modificar a aros acero R15 + llantas R15")
	print ("2.- Modificar a aros aluminio R14 + llantas R14")
	print ("3.- Modificar a aros aluminio R15 + llantas R15")
	print ("4.- Mantener aros de acero R14 + llantas R14")
	aros = input("Que acción desea realizar con el kit, seleccione una opción:  ")
	if 	aros == "1":
		precaros = 580
		pVeh = pVeh -510 + precaros
		print(" El precio adicional es de " +str (precaros)+" USD")
		print ("El precio del vehículo es de: " + str(pVeh)+" USD")
		print("A continuación seguiremos con el ChevyStar Connect de su vehículo ")
		print ("------------------------------------------------")
	if 	aros == "2":
		precaros = 690
		pVeh = pVeh - 510 + precaros
		print(" El precio adicional es de " +str (precaros)+" USD")
		print ("El precio del vehiculo es de: " + str(pVeh)+" USD")
		print("A continuación seguiremos con el ChevyStar Connect de su vehículo ")
		print ("------------------------------------------------")
	if 	aros == "3":
		precaros = 780
		pVeh = pVeh - 510 + precaros
		print(" El precio adicional es de " +str (precaros)+" USD")
		print ("El precio del vehiculo es de: " + str(pVeh)+" USD")
		print("A continuación seguiremos con el ChevyStar Connect de su vehículo ")
		print ("------------------------------------------------")
	if aros == "4":
		print("El precio del vehículo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con el ChevyStar Connect de su vehículo ")
		print ("------------------------------------------------")
	#ChevyStar Connect
	print("ChevyStar Connect")
	print ("1.- Añadirlo")
	print ("2.- No añadirlo")
	chevyStar = input ("Que acción desea realizar con el ChevyStar Connect, seleccione una opción: ")
	if 	chevyStar == "1":
		pchevyStar = 90
		pVeh = pVeh + pchevyStar
		print(" El precio adicional es de " +str (pchevyStar)+" USD")
		print("El precio del vehiculo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con el emblema ""Chevrolet"" de su vehículo ")
		print ("------------------------------------------------")
	if chevyStar == "2":
		print("El precio del vehiculo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con el el emblema ""Chevrolet"" de su vehículo")
		print ("------------------------------------------------")
#Emblema Chevrolet
	print("Emblema ""Chevrolet""")
	print ("1.- Añadirlo")
	print ("2.- No modificar")
	emblema = input ("Que acción desea realizar con el emblema ""Chevrolet"", seleccione una opción: ")
	if 	emblema == "1":
		pemblema = 20
		pVeh = pVeh + pemblema
		print(" El precio adicional es de " +str (pemblema)+" USD")
		print("El precio del vehiculo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con el kit de herramientas de su vehículo ")
		print ("------------------------------------------------")
	if 	emblema == "2":
		print("El precio del vehiculo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con el kit de herramientas de su vehículo")
		print ("------------------------------------------------")
	#Kit de herramientas
	print("Kit de herramientas")
	print ("1.- Añadirlo")
	print ("2.- No añadirlo")
	kitHerra = input ("Que acción desea realizar con el Kit de herramientas, seleccione una opción: ")
	if 	kitHerra == "1":
		pkitHerra = 60
		pVeh = pVeh + pkitHerra
		print(" El precio adicional es de " +str (pkitHerra)+" USD")
		print("El precio del vehiculo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con las lucen antiniebla de su vehículo ")
		print ("------------------------------------------------")
	if aireAcond == "2":
		print("El precio del vehiculo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con las luces antiniebla de su vehículo")
		print ("------------------------------------------------")
#Luces antiniebla
	print("Luces antiniebla")
	print ("1.- Añadirlas")
	print ("2.- No añadirlas")
	luAntin = input ("Que acción desea realizar con las luces antiniebla, seleccione una opción: ")
	if 	luAntin == "1":
		pluAntin = 110
		pVeh = pVeh + pluAntin
		print("El precio del vehiculo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con la radio de su vehículo")
		print ("------------------------------------------------")
	if luAntin == "2":
		print("El precio del vehiculo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con la radio de su vehículo")
		print ("------------------------------------------------")
#Radio
	print ("Radio")
	print ("1.-Desea mantener la Radio Cd")
	print ("2.-Desea cambiarlo por la Radio MP3-USB-IPOD")
	radio = input ("Que acción desea realizar con la radio, seleccione una opción: ")
	if radio =="1":
		print("El precio del vehículo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con la tapiceria de su vehículo")
		print ("------------------------------------------------")
	if radio == "2":
		pradioc = 345
		pVeh = pVeh - 205 + pradioc
		print("El precio del vehículo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con la tapiceria de su vehículo")
		print ("------------------------------------------------")
#Tapiceria
	print("Tapiceria")
	print("1.-Desea mantener la tapiceria de tela")
	print ("2.-Desea modificarla por la Tapiceria de cuero")
	print ("3.- Desea modificarla por la Tapiceria corrosil")
	tapiceria =input ("Que acción desea realizar con la tapiceria , seleccione una opción: ")
	if tapiceria == "1":
		print ("------------------------------------------------")
		print("El precio del vehículo es de: " + str(pVeh) + " USD")
		print ("------------------------------------------------")
	if tapiceria ==	"2":
		ptapicuero = 760
		pVeh = pVeh - 520 + ptapicuero
		print ("------------------------------------------------")
		print("El precio del vehículo es de: " + str(pVeh) + " USD")
		print ("------------------------------------------------")
	if tapiceria ==	"3":
		ptapicorrosil = 400
		pVeh = pVeh - 520 + ptapicorrosil
		print ("------------------------------------------------")
		print("El precio del vehículo es de: " + str(pVeh) + " USD")
		print ("------------------------------------------------")
if veh=="3":
	if modif =="1"  or modif == "2":
		#Seguro tercer vehiculo Aveo Family
		print("Verifique los seguros disponibles para su vehiculo Chevrolet")
		print("-------------------Tipo de Seguro---------------------------")
		print("1._ Cobertura Amplia de 1400 a 1799 cc")
		print("2._ Cobertura Limitada de 1400 a 1799 cc")
		print("3._ Cobertura Responsabilidad Civil de 1400 a 1799 cc")
		print("4._ No adquirir seguro")
		segu = input ("Ingrese el numero de tipo de seguro que dedea adquirir para su vehiculo ")
		if veh == "3" and segu == "1" :
			pSegu = cargaVeh*2.5
			print("------------------------------------------------")
			print("El costo del seguro para su Chevrolet es de " + str(pSegu)+" USD")
			print("------------------------------------------------")
		else:
			if veh == "3" and segu == "2":
				pSegu = cargaVeh *1.8
				print("------------------------------------------------")
				print("El costo del seguro para su Chevrolet es de " + str(pSegu)+" USD")
				print("------------------------------------------------")
			else:
				if veh == "3" and segu == "3" :
					pSegu = cargaVeh *1
					print("------------------------------------------------")
					print("El costo del seguro para su Chevrolet es de " + str(pSegu)+" USD")
					print("------------------------------------------------")
				else:
					if veh == "3" and segu == "4" and modif == "1":
						pSegu = 0
						print("------------------------------------------------")
						print("El costo del vehiculo actual es de: "+ str(pVeh)+" USD")
						print ("------------------------------------------------")
					else:
						if veh == "3" and segu == "4" and modif == "2":
							pSegu = 0
							print("------------------------------------------------")
							print("El costo del vehiculo actual es de: "+ str(precsiniva)+ " USD")
							print ("------------------------------------------------")
#Modificaciones cuarto vehículo
if modif == "1" and veh == "4":
#Aire acondicionado
	pVeh = precsiniva
	print("El vehículo seleccionado tiene las siguientes modificaciones disponibles")
	print("Aire acondicionado")
	print("1.- Desea mantenerlo")
	print("2.- Desea eliminarlo")
	aireAcond = input("Que accion desea realizar con el aire acondicionado seleccione una opción: ")
	if aireAcond =="1":
		print("El precio del vehiculo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con la alarma de su vehículo")
		print("------------------------------------------------")
	if aireAcond == "2":
		precaireAcond = 315
		pVeh = pVeh - precaireAcond
		print("El precio del vehiculo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con la alarma de su vehículo")
		print("------------------------------------------------")
	#Alarma
	print("Alarma")
	print("1.- Desea mantenerla")
	print("2.- Desea eliminarla")
	alarma = input ("Que acción desea realizar con la alarma, seleccione una opción: ")
	if 	alarma == "1":
		print ("El precio del vehiculo es de: " + str(pVeh)+" USD")
		print("A continuación seguiremos con los aros de su vehículo ")
		print ("------------------------------------------------")
	if alarma == "2":
		precalarma = 160
		pVeh = pVeh - precalarma
		print("El precio del vehiculo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con los aros de su vehículo")
		print ("------------------------------------------------")
	#Aros
	print("Aros")
	print ("1.-Mantener los aros acero R15")
	print ("2.- Modificar a aros aluminio R15")
	aros = input("Que acción desea realizar con los aros, seleccione una opción:  ")
	if 	aros == "1":
		print ("El precio del vehículo es de: " + str(pVeh)+" USD")
		print("A continuación seguiremos con el ChevyStar Connect de su vehículo ")
		print ("------------------------------------------------")
	if 	aros == "2":
		precaros = 380
		pVeh = pVeh - 180 + precaros
		print(" El precio adicional es de " +str (precaros)+" USD")
		print ("El precio del vehiculo es de: " + str(pVeh)+" USD")
		print("A continuación seguiremos con el ChevyStar Connect de su vehículo ")
		print ("------------------------------------------------")
	#ChevyStar Connect
	print("ChevyStar Connect")
	print ("1.- Añadirlo")
	print ("2.- No añadirlo")
	chevyStar = input ("Que acción desea realizar con el ChevyStar Connect, seleccione una opción: ")
	if 	chevyStar == "1":
		pchevyStar = 90
		pVeh = pVeh + pchevyStar
		print(" El precio adicional es de " +str (pchevyStar)+" USD")
		print("El precio del vehiculo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con el emblema ""Chevrolet"" de su vehículo ")
		print ("------------------------------------------------")
	if chevyStar == "2":
		print("El precio del vehiculo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con el emblema ""Chevrolet"" de su vehículo")
		print ("------------------------------------------------")
#Emblema Chevrolet
	print("Emblema ""Chevrolet""")
	print ("1.- Añadirlo")
	print ("2.- No modificar")
	emblema = input ("Que acción desea realizar con el emblema ""Chevrolet"", seleccione una opción: ")
	if 	emblema == "1":
		pemblema = 20
		pVeh = pVeh + pemblema
		print(" El precio adicional es de " +str (pemblema)+" USD")
		print("El precio del vehiculo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con los espejos de su vehículo ")
		print ("------------------------------------------------")
	if 	emblema == "2":
		print("El precio del vehiculo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con los espejos de su vehículo")
		print ("------------------------------------------------")
# Espejos
	print("Espejos")
	print ("1.- Mantener espejos manuales ")
	print ("2.- Modificar a espejos eléctricos")
	espejos = input ("Que acción desea realizar con los espejos de su vehiculo, seleccione una opción: ")
	if espejos =="1":
		print("El precio del vehiculo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con el kit de herramientas de su vehículo")
		print ("------------------------------------------------")
	if espejos =="2":
		espejoselec= 135
		pVeh = pVeh - 80 + espejoselec
		print("El precio del vehiculo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con el kit de herramientas de su vehículo")
		print ("------------------------------------------------")
	#Kit de herramientas
	print("Kit de herramientas")
	print ("1.- Añadirlo")
	print ("2.- No añadirlo")
	kitHerra = input ("Que acción desea realizar con el Kit de herramientas, seleccione una opción: ")
	if 	kitHerra == "1":
		pkitHerra = 60
		pVeh = pVeh + pkitHerra
		print(" El precio adicional es de " +str (pkitHerra)+" USD")
		print("El precio del vehiculo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con las lucen antiniebla de su vehículo ")
		print ("------------------------------------------------")
	if kitHerra == "2":
		print("El precio del vehiculo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con las luces antiniebla de su vehículo")
		print ("------------------------------------------------")
#Luces antiniebla
	print("Luces antiniebla")
	print ("1.- Desea mantenerlos")
	print ("2.- Desea eliminarlos")
	luAntin = input ("Que acción desea realizar con las luces antiniebla, seleccione una opción: ")
	if 	luAntin == "1":
		pluAntin = 110
		print("El precio del vehiculo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con la radio de su vehículo")
		print ("------------------------------------------------")
	if luAntin == "2":
		pluAntin = 110
		pVeh = pVeh - pluAntin
		print("El precio del vehiculo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con la radio de su vehículo")
		print ("------------------------------------------------")
#Radio
	print ("Radio")
	print ("1.-Desea mantener la Radio Cd")
	print ("2.-Desea cambiarlo por la Radio MP3-USB-IPOD")
	radio = input ("Que acción desea realizar con la radio, seleccione una opción: ")
	if radio =="1":
		print("El precio del vehículo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con la tapiceria de su vehículo")
		print ("------------------------------------------------")
	if radio == "2":
		pradioc = 345
		pVeh = pVeh - 205 + pradioc
		print("El precio del vehículo es de: " + str(pVeh) + " USD")
		print("A continuación seguiremos con la tapiceria de su vehículo")
		print ("------------------------------------------------")
#Tapiceria
	print("Tapiceria")
	print("1.-Desea mantener la tapiceria de tela")
	print ("2.-Desea modificarla por la Tapiceria de cuero")
	tapiceria =input ("Que acción desea realizar con la tapiceria , seleccione una opción: ")
	if tapiceria == "1":
		print ("------------------------------------------------")
		print("El precio del vehículo es de: " + str(pVeh) + " USD")
		print ("------------------------------------------------")
	if tapiceria ==	"2":
		tapicuero = 760
		pVeh = pVeh - 520 + tapicuero
		print ("------------------------------------------------")
		print("El precio del vehículo es de: " + str(pVeh) + " USD")
		print ("------------------------------------------------")
#Seguro cuarto vehiculo Aveo Emotion
if veh =="4":
	if modif =="2" or modif == "1":
		print("Verifique los seguros disponibles para su vehiculo Chevrolet")
		print("-------------------Tipo de Seguro---------------------------")
		print("1._ Cobertura Amplia de 1400 a 1799 cc")
		print("2._ Cobertura Limitada de 1400 a 1799 cc")
		print("3._ Cobertura Responsabilidad Civil de 1400 a 1799 cc")
		print("4._ No adquirir seguro")
		segu = input ("Ingrese el numero de tipo de seguro que dedea adquirir para su vehículo ")
		if veh == "4" and segu == "1" :
			pSegu = cargaVeh*2.5
			print("------------------------------------------------")
			print("El costo del seguro para su Chevrolet es de " + str(pSegu)+" USD")
			print("------------------------------------------------")
		else:
			if veh == "4" and segu == "2":
				pSegu = cargaVeh *1.8
				print("------------------------------------------------")
				print("El costo del seguro para su Chevrolet es de " + str(pSegu)+" USD")
				print("------------------------------------------------")
			else:
				if veh == "4" and segu == "3" :
					pSegu = cargaVeh *1
					print("------------------------------------------------")
					print("El costo del seguro para su Chevrolet es de " + str(pSegu)+" USD")
					print("------------------------------------------------")
				else:
					if veh == "4" and segu == "4" and modif == "1":
						pSegu = 0
						print("------------------------------------------------")
						print("El costo del vehiculo actual es de: "+ str(pVeh)+" USD")
						print("------------------------------------------------")
					else:
						if veh == "4" and segu == "4" and modif == "2":
							pSegu = 0
							print("El costo del vehiculo actual es de: "+ str(precsiniva)+ " USD")
if modif=="1":
	pfiva = pVeh * 0.12
	pfsinsegu= pVeh + pfiva
	pfinal = pfsinsegu + pSegu
if modif =="2":
	pVeh = precsiniva
	pfiva = pVeh * 0.12
	pfsinsegu= pVeh + pfiva
	pfinal = pfsinsegu + pSegu
#Factura de primer auto
if veh == "1":
	if modif == "1" or modif == "2":
		print("========================================================================================|")
		print("|                                | CHEVROLET |                                          |")
		print("|                             |  FIND NEW ROADS  |                                      |")
		print("|=======================================================================================|")
		print("| Nombre del Producto                   |     Cantidad     |           Precio           |")
		print("|Sail Sedan                             |     1            |"+ str(precsiniva) +"                       |")
		if modif == "1":
			if veh == "1" and aireAcond == "1":
				print("|Aire acondicionado                     |     1            |"+ str(precaireAcond) +"                         |")
			if veh == "1"  and alarma == "1":
				print("|Alarma                                 |     1            |"+ str(precalarma) +"                         |")
			if veh == "1" and aros == "1":
				print("|Aros acero R15, llantas R15            |     1            |"+ str(precaros) +"                         |")
			if veh == "1" and aros == "2":
				print("|Aros aluminio R14 + llantas R14        |     1            |"+ str(precaros) +"                         |")
			if veh == "1" and aros == "3":
				print("|Aros aluminio R15 + llantas R15        |     1            |"+ str(precaros) +"                           |")
			if veh == "1" and chevyStar == "1":
				print("|ChevyStar                              |     1            |"+ str(pchevyStar) +"                          |")
			if veh == "1" and emblema == "1":
				print("|Emblema                                |     1            |"+ str(pemblema) +"                          |")
			if veh == "1" and kitHerra == "1":
				print("|Kit de herramientas                    |     1            |"+ str(pkitHerra) +"                          |")
			if veh == "1" and moqueta == "1":
				print("|Moqueta rigida de baul                 |     1            |"+ str(pmoqueta) +"                          |")
			if veh == "1" and proteCart == "1":
				print("|Protector de carter                    |     1            |"+ str(pproteCart) +"                          |")
			if veh == "1" and radio == "2":
				print("|Radio CD                               |     1            |"+ str(pradioc) +"                          |")
			if veh == "1" and sensor == "1":
				print("|Sensor de reversa                      |     1            |"+ str(psensor) +"                          |")
			if veh == "1" and tapiceria == "2":
				print("|Tapiceria de cuero                     |     1            |"+ str(ptapicuero) +"                          |")
				print("|=========================================================================================|")
		if veh =="1" and segu == "1":
			print("|Seguro Cobertura amplia                                   |"+str(pSegu)+"                         |")
			print("|=======================================================================================|")
			print("|Su iva es de                                              |" +str(pfiva)+"           |")
			print("|Precio final                                              |"+str(pfinal)+"               |")
			print("|=======================================================================================|")
			print("|===============================GRACIAS POR SU COMPRA===================================|")
			print("|==========================CHEVROLET SIEMPRE SU MEJOR OPCION============================|")
		if veh =="1" and segu == "2":
			print("|Seguro Cobertura limitada                                 |"+str(pSegu)+"                         |")
			print("|=======================================================================================|")
			print("|Su iva es de                                              |" +str(pfiva)+"           |")
			print("|Precio final                                              |"+str(pfinal)+"               |")
			print("|=======================================================================================|")
			print("|===============================GRACIAS POR SU COMPRA===================================|")
			print("|==========================CHEVROLET SIEMPRE SU MEJOR OPCION============================|")
		if veh =="1" and segu == "3":
			print("|Seguro Responsabilidad Civil                              |"+str(pSegu)+"                          |")
			print("|=======================================================================================|")
			print("|Su iva es de                                              |" +str(pfiva)+"           |")
			print("|Precio final                                              |"+str(pfinal)+"               |")
			print("|=======================================================================================|")
			print("|===============================GRACIAS POR SU COMPRA===================================|")
			print("|==========================CHEVROLET SIEMPRE SU MEJOR OPCION============================|")
		if veh =="1" and segu == "4":
			print("|=======================================================================================|")
			print("|Su iva es de                                              |" +str(pfiva)+"           |")
			print("|Precio final                                              |"+str(pfinal)+"               |")
			print("|=======================================================================================|")
			print("|===============================GRACIAS POR SU COMPRA===================================|")
			print("|==========================CHEVROLET SIEMPRE SU MEJOR OPCION============================|")
if modif=="1":
	pfiva = pVeh * 0.12
	pfsinsegu= pVeh + pfiva
	pfinal = pfsinsegu + pSegu
if modif =="2":
	pVeh = precsiniva
	pfiva = pVeh * 0.12
	pfsinsegu= pVeh + pfiva
	pfinal = pfsinsegu + pSegu
#Factura de segundo auto
if veh == "2":
	if modif == "1" or modif == "2":
		print("========================================================================================|")
		print("|                                | CHEVROLET |                                          |")
		print("|                             |  FIND NEW ROADS  |                                      |")
		print("|=======================================================================================|")
		print("| Nombre del Producto                   |     Cantidad     |           Precio           |")
		print("|Sail Hatchback                             |     1            |"+ str(precsiniva) +"                       |")
		if modif == "1":
			if veh == "2" and aros == "1":
				print("|Aros acero R15, llantas R15            |     1            |"+ str(precaros) +"                         |")
			if veh == "2" and aros == "2":
				print("|Aros aluminio R14 + llantas R14        |     1            |"+ str(precaros) +"                         |")
			if veh == "2" and aros == "3":
				print("|Aros aluminio R15 + llantas R15        |     1            |"+ str(precaros) +"                           |")
			if veh == "2" and chevyStar == "1":
				print("|ChevyStar                              |     1            |"+ str(pchevyStar) +"                          |")
			if veh == "2" and kitHerra == "1":
				print("|Kit de herramientas                    |     1            |"+ str(pkitHerra) +"                          |")
			if veh == "2" and proteCart == "1":
				print("|Protector de carter                    |     1            |"+ str(pproteCart) +"                          |")
			if veh == "2" and radio == "2":
				print("|Radio CD                               |     1            |"+ str(pradioc) +"                          |")
			if veh == "2" and sensor == "1":
				print("|Sensor de reversa                      |     1            |"+ str(psensor) +"                          |")
			if veh == "2" and tapiceria == "2":
				print("|Tapiceria de cuero                     |     1            |"+ str(ptapicuero) +"                          |")
				print("|=========================================================================================|")
		if veh =="2" and segu == "1":
			print("|Seguro Cobertura amplia                                   |"+str(pSegu)+"                         |")
			print("|=======================================================================================|")
			print("|Su iva es de                                              |" +str(pfiva)+"           |")
			print("|Precio final                                              |"+str(pfinal)+"               |")
			print("|=======================================================================================|")
			print("|===============================GRACIAS POR SU COMPRA===================================|")
			print("|==========================CHEVROLET SIEMPRE SU MEJOR OPCION============================|")
		if veh =="2" and segu == "2":
			print("|Seguro Cobertura limitada                                 |"+str(pSegu)+"                         |")
			print("|=======================================================================================|")
			print("|Su iva es de                                              |" +str(pfiva)+"           |")
			print("|Precio final                                              |"+str(pfinal)+"               |")
			print("|=======================================================================================|")
			print("|===============================GRACIAS POR SU COMPRA===================================|")
			print("|==========================CHEVROLET SIEMPRE SU MEJOR OPCION============================|")
		if veh =="2" and segu == "3":
			print("|Seguro Responsabilidad Civil                              |"+str(pSegu)+"                          |")
			print("|=======================================================================================|")
			print("|Su iva es de                                              |" +str(pfiva)+"           |")
			print("|Precio final                                              |"+str(pfinal)+"               |")
			print("|=======================================================================================|")
			print("|===============================GRACIAS POR SU COMPRA===================================|")
			print("|==========================CHEVROLET SIEMPRE SU MEJOR OPCION============================|")
		if veh =="2" and segu == "4":
			print("|=======================================================================================|")
			print("|Su iva es de                                              |" +str(pfiva)+"           |")
			print("|Precio final                                              |"+str(pfinal)+"               |")
			print("|=======================================================================================|")
			print("|===============================GRACIAS POR SU COMPRA===================================|")
			print("|==========================CHEVROLET SIEMPRE SU MEJOR OPCION============================|")
if modif=="1":
	pfiva = pVeh * 0.12
	pfsinsegu= pVeh + pfiva
	pfinal = pfsinsegu + pSegu
if modif =="2":
	pVeh = precsiniva
	pfiva = pVeh * 0.12
	pfsinsegu= pVeh + pfiva
	pfinal = pfsinsegu + pSegu
#Factura de tercer auto
if veh == "3":
	if modif == "1" or modif == "2":
		print("========================================================================================|")
		print("|                                | CHEVROLET |                                          |")
		print("|                             |  FIND NEW ROADS  |                                      |")
		print("|=======================================================================================|")
		print("| Nombre del Producto                   |     Cantidad     |           Precio           |")
		print("|Aveo Family                             |     1            |"+ str(precsiniva) +"                       |")
		if modif == "1":
			if veh == "3" and aireAcond == "1":
				print("|Aire acondicionado                     |     1            |"+ str(precaireAcond) +"                         |")
			if veh=="3"and alarma == "1":
				print("|Alarma                                 |     1            |"+ str(precalarma) +"                         |")
			if veh == "3" and aros == "1":
				print("|Aros acero R15, llantas R15            |     1            |"+ str(precaros) +"                         |")
			if veh == "3" and aros == "2":
				print("|Aros aluminio R14 + llantas R14        |     1            |"+ str(precaros) +"                         |")
			if veh == "3" and aros == "3":
				print("|Aros aluminio R15 + llantas R15        |     1            |"+ str(precaros) +"                           |")
			if veh == "3" and chevyStar == "1":
				print("|ChevyStar                              |     1            |"+ str(pchevyStar) +"                          |")
			if veh == "3" and emblema == "1":
				print("|Emblema                                |     1            |"+ str(pemblema) +"                          |")
			if veh == "3" and kitHerra == "1":
				print("|Kit de herramientas                    |     1            |"+ str(pkitHerra) +"                          |")
			if veh =="3" and luAntin =="1":
				print("|Luces antiniebla                       |     1            |"+ str(pluAntin) +"                          |")
			if veh == "3" and radio == "2":
				print("|Radio MP3-USB-IPOD                     |     1            |"+ str(pradioc) +"                          |")
			if veh == "3" and tapiceria == "2":
				print("|Tapiceria de cuero                     |     1            |"+ str(tapicuero) +"                          |")
			if veh == "3" and tapiceria == "3":
				print("|Tapiceria de cuero                     |     1            |"+ str(ptapicorrosil) +"                          |")
				print("|=========================================================================================|")
		if veh =="3" and segu == "1":
			print("|Seguro Cobertura amplia                                   |"+str(pSegu)+"                         |")
			print("|=======================================================================================|")
			print("|Su iva es de                                              |" +str(pfiva)+"           |")
			print("|Precio final                                              |"+str(pfinal)+"               |")
			print("|=======================================================================================|")
			print("|===============================GRACIAS POR SU COMPRA===================================|")
			print("|==========================CHEVROLET SIEMPRE SU MEJOR OPCION============================|")
		if veh =="3" and segu == "2":
			print("|Seguro Cobertura limitada                                 |"+str(pSegu)+"                         |")
			print("|=======================================================================================|")
			print("|Su iva es de                                              |" +str(pfiva)+"           |")
			print("|Precio final                                              |"+str(pfinal)+"               |")
			print("|=======================================================================================|")
			print("|===============================GRACIAS POR SU COMPRA===================================|")
			print("|==========================CHEVROLET SIEMPRE SU MEJOR OPCION============================|")
		if veh =="3" and segu == "3":
			print("|Seguro Responsabilidad Civil                              |"+str(pSegu)+"                          |")
			print("|=======================================================================================|")
			print("|Su iva es de                                              |" +str(pfiva)+"           |")
			print("|Precio final                                              |"+str(pfinal)+"               |")
			print("|=======================================================================================|")
			print("|===============================GRACIAS POR SU COMPRA===================================|")
			print("|==========================CHEVROLET SIEMPRE SU MEJOR OPCION============================|")
		if veh =="3" and segu == "4":
			print("|=======================================================================================|")
			print("|Su iva es de                                              |" +str(pfiva)+"           |")
			print("|Precio final                                              |"+str(pfinal)+"               |")
			print("|=======================================================================================|")
			print("|===============================GRACIAS POR SU COMPRA===================================|")
			print("|==========================CHEVROLET SIEMPRE SU MEJOR OPCION============================|")
if modif=="1":
	pfiva = pVeh * 0.12
	pfsinsegu= pVeh + pfiva
	pfinal = pfsinsegu + pSegu
if modif =="2":
	pVeh = precsiniva
	pfiva = pVeh * 0.12
	pfsinsegu= pVeh + pfiva
	pfinal = pfsinsegu + pSegu
#Factura de cuarta auto
if veh == "4":
	if modif == "1" or modif == "2":
		print("========================================================================================|")
		print("|                                | CHEVROLET |                                          |")
		print("|                             |  FIND NEW ROADS  |                                      |")
		print("|=======================================================================================|")
		print("| Nombre del Producto                   |     Cantidad     |           Precio           |")
		print("|Aveo Emotion                             |     1            |"+ str(precsiniva) +"                       |")
		if modif == "1":
			if veh == "4" and aros == "2":
				print("|Aros aluminio R15         |     1            |"+ str(precaros) +"                           |")
			if veh == "4" and chevyStar == "1":
				print("|ChevyStar                              |     1            |"+ str(pchevyStar) +"                          |")
			if veh == "4" and emblema == "1":
				print("|Emblema                                |     1            |"+ str(pemblema) +"                          |")
			if veh=="4" and espejos =="2":
				print("|Espejos eléctricos                     |     1            |"+ str(espejoselec) +"                          |")
			if veh == "4" and kitHerra == "1":
				print("|Kit de herramientas                    |     1            |"+ str(pkitHerra) +"                          |")
			if veh == "4" and radio == "2":
				print("|Radio MP3-USB-IPOD                     |     1            |"+ str(pradioc) +"                          |")
			if veh == "4" and tapiceria == "2":
				print("|Tapiceria de cuero                     |     1            |"+ str(tapicuero) +"                          |")
				print("|=========================================================================================|")
		if veh =="4" and segu == "1":
			print("|Seguro Cobertura amplia                                   |"+str(pSegu)+"                         |")
			print("|=======================================================================================|")
			print("|Su iva es de                                              |" +str(pfiva)+"           |")
			print("|Precio final                                              |"+str(pfinal)+"               |")
			print("|=======================================================================================|")
			print("|===============================GRACIAS POR SU COMPRA===================================|")
			print("|==========================CHEVROLET SIEMPRE SU MEJOR OPCION============================|")
		if veh =="4" and segu == "2":
			print("|Seguro Cobertura limitada                                 |"+str(pSegu)+"                         |")
			print("|=======================================================================================|")
			print("|Su iva es de                                              |" +str(pfiva)+"           |")
			print("|Precio final                                              |"+str(pfinal)+"               |")
			print("|=======================================================================================|")
			print("|===============================GRACIAS POR SU COMPRA===================================|")
			print("|==========================CHEVROLET SIEMPRE SU MEJOR OPCION============================|")
		if veh =="4" and segu == "3":
			print("|Seguro Responsabilidad Civil                              |"+str(pSegu)+"                          |")
			print("|=======================================================================================|")
			print("|Su iva es de                                              |" +str(pfiva)+"           |")
			print("|Precio final                                              |"+str(pfinal)+"               |")
			print("|=======================================================================================|")
			print("|===============================GRACIAS POR SU COMPRA===================================|")
			print("|==========================CHEVROLET SIEMPRE SU MEJOR OPCION============================|")
		if veh =="4" and segu == "4":
			print("|=======================================================================================|")
			print("|Su iva es de                                              |" +str(pfiva)+"           |")
			print("|Precio final                                              |"+str(pfinal)+"               |")
			print("|=======================================================================================|")
			print("|===============================GRACIAS POR SU COMPRA===================================|")
			print("|==========================CHEVROLET SIEMPRE SU MEJOR OPCION============================|")
