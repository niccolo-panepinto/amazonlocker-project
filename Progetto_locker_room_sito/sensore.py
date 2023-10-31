import serial                                #Import della Libreria Serial per la comunicazione con la porta seriale 
import time                                   #Import della Libreria Time per poter dare itervalli di tempo tra un comando e l'altro
import queue




class dato():

 def __init__(self) -> None:
    pass
 
 def messaggio():

    port = serial.Serial("COM5", 9600)            #Inizializazzione della variabile "port" nella porta serial COM4 e con il baudrate a 9600
    port.timeout = 1 

    if port.isOpen():
        input_data=port.readline().decode()	
        return input_data
        



    