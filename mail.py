
def mails(nombre, t, n):
    for i in range(n):
        nombre = nombre * (1 + t /100)
        if i < 1:
            nombre_final = nombre
        else:
            nombre_final = nombre_final + nombre
    return nombre_final

