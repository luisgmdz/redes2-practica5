import xmlrpc.client #hace una llamada a procedimiento remoto (el mensaje lo trbaja como xml)
import datetime

localhost='127.0.0.1'
port=8065
accion=''
s = xmlrpc.client.ServerProxy('http://localhost:8065')#direccion del servidor
#se usa un socket tipo TCP/IP por que usa el metodo HTTP
#Se usa el ojeto tipo server proxy
print("Cliente conectado a servidor")

while accion != 0:
    print("1)Crear un nuevo archivo\n2)Leer un archivo\n3)Reescribir archivo"
        +"\n4)Renombrar un archivo\n5)Crear carpeta\n6)Eliminar carpeta\n"
        +"7)Leer lista de directorios\n0)Salir")
    accion=int(input("Ingrese el numero de la accion que desea realizar: "))
    if accion == 0:
        break;
    else:
        if accion == 1:
            nombre=input("Ingresa el nombre del documento a crear: ")
            #print(type(nombre))
            mensaje=input("Ingresa el mensaje: ")
            #print(type(mensaje))
            status=s.crearArchivo(nombre,mensaje)
            print("status:", status)
            print("\n\n")
        elif accion == 2:
            nombre=input("Ingresa el nombre del documento a leer: ")
            print(type(nombre))
            contenido=s.leerArchivo(nombre)
            print("Contenido: ", contenido)   
            print("\n\n")     
        elif accion == 3:   
            nombre=input("Ingresa el nombre del documento que desea modificar: ")
            mensaje=input("Ingresa el mensaje: ")
            status=s.escribir(nombre,mensaje)
            print("status:", status)
            print("\n\n")
        elif accion == 4:
            nombre=input("Ingresa el nombre del documento que desea renombrar: ")
            nuevoNombre=input("Ingresa el nombre nuevo del documento: ")
            status=s.renombrar(nombre, nuevoNombre)
            print("status:", status)
            print("\n\n")
        elif accion == 5:
            nombre=input("Ingresa el nombre de la carpeta nueva: ")
            status=s.nuevaCarpeta(nombre)
            print("status:", status)
            print("\n\n")
        elif accion == 6:
            nombre=input("Ingresa el nombre de la carpeta a eliminar: ")
            status=s.eliminarCarpeta(nombre)
            print("status:", status)
            print("\n\n")
        elif accion == 7:
            nombre=input("Ingresa el nombre de la carpeta a examinar: ")
            status=s.verCarpeta(nombre)
            print("status:", status)
            print("\n\n")
            
