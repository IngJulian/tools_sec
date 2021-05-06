#!/bin/python

import sys
import socket
from datetime import datetime

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])

else: 
    print("Se ingreso un argumento invalido")
    print("""Se debe ingresar de la siguiente forma:
    python3 scan.py 192.168.0.1
    """)

print("-"*50)
print("Ejecutando escaneo al objetivo " + target )
print("Dia y hora de la ejecucion: " + str(datetime.now()))
print("-"*50)

try:
    for port in range(79,83):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        print(result)
        if result == 0:
            print("Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\n Saliando del programa.")
    sys.exit()
except socket.gaierror:
    print("El nombre del equipo no se pudo resolver.")
    sys.exit()
except socket.error:
    print("Dispositivo fuera de alcance.")
    sys.exit()