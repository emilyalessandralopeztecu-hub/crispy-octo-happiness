import mysql.connector

conexion=mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="sistema_GYM"

)

def create():
    print("__ INSCRIPCION __")
    name=input("Nombre: ")
    agee=int(input("Edad: "))
    print("================")
    print("Pagos por mes ___")
    lista=["1.Basic = Q120","2.Premium = Q190","3.VIP = Q270"]
    for lista in lista:
        print(lista)
    member=int(input("Ingres el número de Tipo: "))
    meses=int(input("Ingrese la cantidad de meses: "))
    act="Active Plus" if meses >= 6 else "Active"
    if member == 1 :
        total=meses * 120

    elif member == 2:
        total= meses * 190 

    elif member == 3 :
        total=meses * 270
    else:
        print("INVALIDO")

    if conexion.is_connected():
        cursor=conexion.cursor()
        query="INSERT INTO inscripciones(clienteName,age,membershipType,months,finalPrice,status) VALUES (%s,%s,%s,%s,%s,%s)"
        cursor.execute(query, (name,agee,member,meses,total,act))
        conexion.commit()
        print("¡ OFICIALMENTE INSCRITO !") 
        print(f"Total: {total}")
        print(f"Su número de ID: {cursor.lastrowid}")
        



def read():
    print("__ REVISAR __")
    if conexion.is_connected():
        cursor=conexion.cursor()
        query="SELECT * FROM inscripciones "
        cursor.execute(query,)
        date=cursor.fetchall()
        for fila in date:
            print(fila)


def update():
    print("__ACTUALIZAR__")
    id_buscar=int(input("Ingrese el número de ID: "))

    if conexion.is_connected():
        cursor=conexion.cursor()
        cursor.execute("SELECT * FROM inscripciones WHERE idinscripciones = %s",(id_buscar,))
        date= cursor.fetchone()
        if date:
            print("Registro encontrado")
            print(date)

            new_name=input("Nuevo nombre: ")
            new_edad=int(input("Edad: "))
            lista=["1. Basic = Q120","2. Premium = Q190","3. VIP = Q270"]
            for listas in lista:
                print(listas)
            new_member=int(input("Nuevo tipo: "))
            new_meses=int(input("Meses: "))
            act="Active Plus" if new_meses >= 6 else "Active"
            

            if new_member == 1 :
                    typp="Basic"
                    total=new_meses * 120
            
            elif new_member == 2:
                    typp="Premium"
                    total= new_meses * 190 
            
            elif new_member == 3 :
                    typp="VIP"
                    total=new_meses * 270
            else:
                    print("INVALIDO")
            

            query="""
                UPDATE inscripciones
                SET clienteName=%s,
                    age=%s,
                    membershipType=%s,
                    months=%s,
                    finalPrice=%s,
                    status=%s


                WHERE idinscripciones = %s
"""
        

            cursor.execute(query,(new_name,new_edad,new_member,new_meses,total,act,id_buscar))
            conexion.commit()
            print("Registro actualizado")
            print(f"Tipo {typp}")
            print(f"Total: {total}")

            
    else:
        print("Registro no encontrado")




def delete():
     print("__ ELIMINAR __")
     id=int(input("Ingrese el numero de ID a eliminar: "))
     if conexion.is_connected():
          cursor=conexion.cursor()
          query="DELETE FROM inscripciones WHERE idinscripciones=%s"
          cursor.execute(query,(id,))
          conexion.commit()
          print("¡ Se eliminó correctamente !")



def menu ():
    print("--- BIENVENIDO AL GYM  ---")

    while True:
        try:

            lista=["1. Inscribirse ","2. Revisar ","3. Actualizar","4. Eliminar"]
            for lista in lista:
                print(lista)

            desi= int(input("Ingrese el número de opción a trabajar: "))
            break
        except ValueError:
            print("Opción no válida")

    if desi == 1:
        create()
    elif desi  == 2:
        read()
    elif desi == 3:
        update()
    elif desi == 4:
         delete()
    else:
        pass


menu()