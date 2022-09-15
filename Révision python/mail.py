
def mails(nombre, t, n):
    total_mails = nombre
    for i in range(n):
        nombre = nombre * (1 + t /100)
        total_mails = total_mails + nombre
    return nombre, total_mails

