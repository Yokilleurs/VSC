def mails(nombre, t, n):
    for i in range(n):
        nombre = nombre * (1 + t /100)
    return nombre