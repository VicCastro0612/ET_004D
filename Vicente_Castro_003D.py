productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
             '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
             'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
             'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
             '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
             'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
        'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]}



def opciones(mensaje):
    while True:
        try:
            print("***Menú Principal***")
            print("1. Stock marca")
            print("2. Búsqueda por precio.")
            print("3. Actualizar precio")
            print("4. Salir")

            opc = int(input(mensaje))
        except Exception:
            print("Valor no válido.")



def validacion_numero_enteros(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            if numero < 0:
                print("Debes ingresar un valor valido.")
        except Exception:
            print("Debe ingresar valores enteros.")



def stock_marca(marca):
     lista_marcas = []
     numero_de_productos = 0

     for i in productos:
         lista_marcas.append(productos[i][0].upper())

     if marca in lista_marcas:
        for i in productos:
            if productos[i][0].upper() == marca:
                for n in stock:                    
                    if i == n:
                        numero_de_productos += stock[n][1]
        print(f"El stock es: {numero_de_productos}.")
     else:
        print(f"El stock es: {numero_de_productos}.")


def busqueda_precio(p_min,p_max):
    
    p_min = validacion_numero_enteros(p_min)
    p_max = validacion_numero_enteros(p_max)

    lista_busqueda_precios = []

    for i in stock:
        if stock[i][0] >= p_min and stock[i][0] <= p_max:
            marca_modelo = f"{productos[i][0]}----{i}"
            lista_busqueda_precios.append(marca_modelo)
            lista_busqueda_precios.sort()


    if len(lista_busqueda_precios) == 0:
            print("No hay notebooks en ese rango de precio.")
    else:
        print(F"Los notebooks entre los precios consultas son: { lista_busqueda_precios}")


precio_min = validacion_numero_enteros("Ingrese precio minimo:")
precio_max = validacion_numero_enteros("Ingrese precio maximo:")


def actualizar_precio(modelo, p):
    lista_modelos = []
    for i in stock:
        lista_modelos.append(stock[i])
        if modelo in lista_modelos:
            for n in stock:
                stock[n][0] = p
            return True
        else:
            return False


def seguir_actualizando():
    while True:
        siguiente = input("Desea actualizar otro precio? (Si/No): ")

        if siguiente == "Si" or siguiente == "si":
            continue
        elif siguiente == "No" or siguiente == "no":
            break
        else:
            print("De ingresar Si o No.")

while True:

    opc = opciones("Seleccione una opción (1-4): ")

    if opc == 1:
        marca = input("Ingrese marca a consultar: ")
        stock_marca(marca)

    elif opc == 2:
        while True:
            try:
                precio_min = int(input("Ingrese precio mínimo: "))
                precio_max = int(input("Ingrese precio máximo: "))

                if (precio_min < 0) or (precio_max < 0):
                    print("Los rangos ingresados deben ser numeros enteros.")

            except Exception:
                print("Valor no válido.")

    elif opc == 3:
        while True:
            modelo = input("Ingrese modelo a actualizar: ")

            retorno_de_mensaje = actualizar_precio(modelo)
            if retorno_de_mensaje == True:
                print("Precio actualizado!!")
            else:
                print("El modelo no existe")
            seguir_actualizando()
                


    elif opc == 4:
        print("Programa Finalizado.")
        break

    else:
        print("Debe seleccionar una opcion válida.")