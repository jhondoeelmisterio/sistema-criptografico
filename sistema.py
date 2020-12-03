# sistema-criptografico

from sympy.crypto.crypto import encipher_shift, decipher_shift
import os, sys, time
from random import *

def sutil(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(12. / 150)

def corrida(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(3. / 250)

def valletta(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(2. / 120)

def saludo(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(3. / 100)

def medio(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(8. / 200)

def lento(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(10. / 200)

def proceso(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(15. / 150)

#COLORES

GL = "\033[96;1m" # Blue aqua
BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33;1m"  # Yellow
G = "\033[32m"    # Green
W = "\033[0;1m"   # White
R = "\033[31m"    # Red
C = "\033[36;1m"  # Cyan
M = "\033[35;1m"  # Morado

os.system("clear")

corrida("■■■■■■■■■■■■■■■■■")
corrida("■   ■■■■■■■■■   ■")
corrida("■     ■■■■■     ■")
lento("■ CR1PT0GR4F14S ■")
lento("■     ▪▪▪▪▪     ■")
corrida("■■■■■■■■■■■■■■■■■")

print (CC+"    ¡Bienvenido!   "+WW)
print (" ")
sutil(GG+"¿Que quieres hacer?"+WW)
print (" ")
corrida(CC+"1)Encriptar archivo"+WW)
print (" ")
corrida(CC+"2)Encriptar palabra"+WW)
print (" ")
corrida(CC+"3)Desencriptar palabra"+WW)
print (" ")
variable = int(input(GG+"Elige una opcion: "+WW))

print (" ")

if variable == 1:
        archivo = open("archivo.txt","r")

        cifrado = encipher_shift(archivo.txt, 13)

        archivo = open("archivo.txt","w")

        archivo.write(cifrado)

elif variable == 2:
        c1 = medio(CC+"Ponga la frase y el tipo de root con el que desea encriptar"+GG)
        os.system("sleep 1")
        c2 = str(input("frase >>>>> "))
        os.system("sleep 1")
        c3 = int(input("root >>>>> "))

        print (CC+"Vale, en breve se le dara su frase encriptada")
        os.system("sleep 1")
        print ("encriptando frase......")
        os.system("sleep 3")

        r1 = encipher_shift(c2, c3)

        print (GG+"Frase encriptada >>>>>", r1+WW)

elif variable == 3:
        print (CC+"Ponga la frase y tipo de cifrado root que desea desencriptar"+GG)
        system.os("sleep1")
        d2 = str(input("frase >>>>> "))
        system.os("sleep 1")
        d3 = int(input("root >>>>> "))

        print (CC+"En breve se desencriptara su frase")
        print ("desencriptando frase.....")
        system.os("sleep 3")

        r2 = decipher_shift(d2, d3)
        print (GG+"Frase desencriptada >>>>>", r2+WW)

else:
        print (RR+"Respuesta incorrecta"+WW)


#SALIDA

os.system("sleep 1")

proceso("Saliendo del programa...")

os.system("sleep 1")

os.system("clear")

os.system("figlet VALLETTA")
