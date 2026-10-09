import mysql.connector

conexion = mysql.connector.connect(
    host = "localhost",
    user ="root",
    password = "1234",
    database = "Hotel"
)

def create():
    while True:
        try:

            print("BIENVENIDO AL SISTEMA DE HOTEL")
            print("Necesitamos lo siguiente: ")
            name=input("Nombre: ")
            print("----------------------")
            apellido=input("Apellido: ")
            print("----------------------")
            number=int(input("Cantidad de huespeds: "))
            print("----------------------")

            lista=["Standard","Deluxe","Suite"]
            for listas in lista:
                print(listas)

            typp=input("Tipo de habitación: ").lower()
            break

        except ValueError:
            print("Error")

    if conexion.is_connected():
        cursor=conexion.cursor()
        query="INSERT INTO reservas(firstName,lastName,numberOfGuests,roomType) VALUES (%s,%s,%s,%s)"
        cursor.execute(query,(name,apellido,number,typp))
        conexion.commit()

        print("Reservacion guardada")



def read():
    print("Revisar reservaciones")
    if conexion.is_connected():
        cursor=conexion.cursor()
        query="SELECT * FROM reservas"
        cursor.execute(query,)
        hotel=cursor.fetchall()
        for fila in hotel:
            print(fila)


def update():
    print("__ ACTUALIZAR __")
    id=int(input("Ingrese el número de ID de la reservación: "))
    if conexion.is_connected():
        cursor=conexion.cursor()
        cursor.execute("SELECT * FROM reservas WHERE idreservas=%s",(id,) )  
        hotel=cursor.fetchall()
        for fila in hotel:
            print(fila)

        if hotel:
            print("Reservacion encontrada")

            new_name=input("Nombre: ")
            new_last=input("Apellido: ")
            new_number=int(input("Número de huespeds: "))
            print("___________________")
            lista=["Standard","Deluxe","Suite"]
            for listas in lista:
                print(listas)
            
            new_typ=input("Tipo: ").lower()
        else:
            print("No se econtró el número de ID")
                    

        query="""
            UPDATE reservas
            SET firstName=%s,
                lastName=%s,
                numberOfGuests=%s,
                roomType=%s

            WHERE idreservas=%s

"""
        cursor.execute(query,(new_name,new_last,new_number,new_typ,id))
        conexion.commit()
        print("Actualizacion guardada")



def delete():
    print("__ ELIMINAR __")

    id=int(input("Ingrese el número de ID: "))

    if conexion.is_connected():
        cursor=conexion.cursor()
        query="DELETE FROM reservas WHERE idreservas = %s"
        cursor.execute(query,(id,))
        conexion.commit()
        print("¡ Se eleminó correctamente !")


   




def menu():
    print("BIENVENIDO AL SISTEMA DE HOTEL")

    while True:
        try:
            lista=["1. Reservar habitacion","2. Revisar reservaciones", "3. Actualizar reservación","4. Eliminar reservación"]
            for listas in lista:
                print(listas)

            desi=int(input("Ingrese el número de opción a trabajar: "))
            break
        except ValueError:
            print("__Error__")


    if desi== 1:
        create()
    elif desi ==2:
        read()
    elif desi ==3:
        update()
    elif desi ==4:
        delete()
    else:
        print("Esta no es una de las opciones")

menu()
