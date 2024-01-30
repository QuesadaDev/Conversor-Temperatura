def conver(temperatura):

    temp_intro = float(''.join(filter(lambda x: x.isdigit() or x in ['.', '-'], temperatura)))

    if "ºC" in temperatura:
        resul = (1.8 * temp_intro) + 32
        return print(f"{resul:.2f}ºF")

    elif "ºF" in temperatura:
        resul = (temp_intro - 32) * 5/9
        return print(f"{resul:.2f}ºC")
    else:
        return print("Error: La unidad no es válida")


temp = input("Introduce la temperatura que quieras en ºF o ºC: ")
conver(temp)
