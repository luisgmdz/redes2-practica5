from xmlrpc.server import SimpleXMLRPCServer#l mosulo ocupa una clase que se llama server
from xmlrpc.server import SimpleXMLRPCRequestHandler#RequestHandler esta a la escucha de solicitudes de informacion
import os

localhost='127.0.0.1'
port=8065
# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)#atiende la ruta de las solicitudes que va a estar escuchando

with SimpleXMLRPCServer((localhost, port), #nos ayuda a abrir un flujo de archivo #sin with se usa el try-catch
                        requestHandler=RequestHandler) as server:#segundo param. usa el metodo handler y se le asigna un alias que en este caso es "server"
    server.register_introspection_functions()
    print("Server in host", localhost, "port:", port)
    
    def crearArchivo(nombre, mensaje):
        file = open("/home/luis/Escritorio/redes2/practica5/"+nombre+".txt", "w")
                # la "w" indica que se va a crear un documento
        file.write(mensaje)# write escribe el mensaje en el documento
        file.close()
        return 'archivo creado'
    server.register_function(crearArchivo, 'crearArchivo')

    def leerArchivo(nombre):
        file = open("/home/luis/Escritorio/redes2/practica5/"+nombre+".txt", "r")
                #la "r" indica que el archivo sera abierto en modo lectura
        mensaje=file.read()#read extrae el contenido del archivo
        file.close()
        return mensaje
    server.register_function(leerArchivo, 'leerArchivo')

    def escribirEnArchivo(nombre, mensaje):
        file = open("/home/luis/Escritorio/redes2/practica5/"+nombre+".txt", "a")
                #la "a" como parametro indica que se va a agregar texto al final del 
                #archivo que se ha abierto con open
        file.write("\n"+mensaje)
        file.close()
        return 'Archivo modificado'
    server.register_function(escribirEnArchivo, 'escribir')

    def renombrarArchivo(nombre, nuevoNombre):
        os.rename("/home/luis/Escritorio/redes2/practica5/"+nombre+".txt", 
            "/home/luis/Escritorio/redes2/practica5/"+nuevoNombre+".txt")
            #rename cambia el nombre a un documento
        return 'Archivo renombrado'
    server.register_function(renombrarArchivo, 'renombrar')

    def nuevaCarpeta(nombre):
        try:
            os.mkdir(nombre)#mkdir crea una carpeta
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
        return 'Carpeta creada'
    server.register_function(nuevaCarpeta, 'nuevaCarpeta')

    def eliminarCarpeta(nombre):
        try:
            os.rmdir(nombre)#rmdir en un metodo utilizado para eliminar archivos y carpetas
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
        return 'Carpeta eliminada'
    server.register_function(eliminarCarpeta, 'eliminarCarpeta')

    def verCarpeta(nombre):
        try:
            docs=os.listdir(nombre)#listdir regresa una lista de los archivos y carpetas
                                    #que estan dentro de una ubicacióm
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
        return docs
    server.register_function(verCarpeta, 'verCarpeta')

    
    # Run the server's main loop
    server.serve_forever() #usamos TCP como capa de transporte
