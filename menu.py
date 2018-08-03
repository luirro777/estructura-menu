#!/usr/bin/python3
#-*- coding: utf-8 -*-

import os
import psutil

def menu():	
	print ("Seleccione una opcion")
	print("1-Listar los PIDs actuales")
	print("2-Mostrar el nombre de un proceso, seleccionando el PID")
	print("3-Mostrar la ruta de dicho proceso")
	
	# Aca deben agregar las opciones
	
	print("17-Salir")
	
	opcion = input ("Opcion seleccionada: ")
	return opcion


def select_PID():
	try:
		pid = input("Seleccione el PID ")
		return pid
	except SyntaxError:
		pass
	

def press_key():
	try:
		input("Press enter to continue")
	except SyntaxError:
		pass
		
selected_pid = 0

while True:
	os.system("clear")
	if (selected_pid == 0):
		print ("No se ha seleccionado ningun proceso")
	else:
		print ("Proceso seleccionado:")
		print (selected_pid)
	opcion = menu()
	if (opcion == "1"):
		print (psutil.pids())	
		press_key()	
	elif (opcion == "2"):
		selected_pid = select_PID()
		print ("PID seleccionado: ")
		print (selected_pid)
		try:
			p = psutil.Process(int(selected_pid))
			print ("Nombre:")
			print (p.name())
		except (psutil.NoSuchProcess):
			print ("No existe proceso con ese PID")
			selected_pid = 0
		press_key()
	elif (opcion == "3"):
		if (selected_pid != 0):
			print ("Ruta:")
			print (p.exe())
		else:
			print ("no hay PID seleccionado")
		press_key()		
		
	# Aca van el resto de las opciones
	
	elif (opcion == "17"):
		exit()
	else:
		print ("Opcion no valida")
		press_key()
		 


	
