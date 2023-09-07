import temperatura
import masa
import tiempo

def convertir_temperatura(valor, unidad_origen, unidad_destino):
    if unidad_origen == "celsius" and unidad_destino == "fahrenheit":
        return temperatura.celsius_a_fahrenheit(valor)

def convertir_masa(valor, unidad_origen, unidad_destino):
    if unidad_origen == "kilogramos" and unidad_destino == "gramos":
        return masa.kilogramos_a_gramos(valor)

def convertir_tiempo(valor, unidad_origen, unidad_destino):
    if unidad_origen == "segundos" and unidad_destino == "minutos":
        return tiempo.segundo_a_minuto(valor)

if __name__=="__main__":
    valor = float(input("ingrese la temperatura : "))
    unidad_origen = "celsius"
    unidad_destino = "fahrenheit"
    resultado = convertir_temperatura(valor, unidad_origen, unidad_destino)
    print(f"{valor} de grados {unidad_origen} son equivalentes {resultado} grados {unidad_destino} ")


if __name__=="__main__":
    valor = float(input("ingrese los kilogramos : "))
    unidad_origen = "kilogramos"
    unidad_destino = "gramos"
    resultado = convertir_masa(valor, unidad_origen, unidad_destino)
    print(f"{valor} kilogramos {unidad_origen} son equivalentes {resultado} gramos {unidad_destino} ")


if __name__=="__main__":
    valor = float(input("ingrese los segundos : "))
    unidad_origen = "segundos"
    unidad_destino = "minutos"
    resultado = convertir_tiempo(valor, unidad_origen, unidad_destino)
    print(f"{valor} segundos {unidad_origen} son equivalentes {resultado} minutos {unidad_destino} ")
