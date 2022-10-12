import time
from api_insee import ApiInsee  

fic = open("sirets.txt", "r")
out = open("latency.csv", "a")

api = ApiInsee(
    key = "o_kfvxFzWwDucmQrJqF7qA31Qp0a",
    secret = "WPidT3P05AtZVSNuf9R2VfqCt9Qa"
)

def appel(siret):
    try:
        data = api.siret(siret).get()
        print('siret trouvé')
    except OSError as err:
        print(err)
    return 1


for i in range(100):
    sir = fic.readline() 
    start_time = time.time()
    appel(sir)
    print(i, (time.time() - start_time), "secondes")
    latence = round((time.time() - start_time), 2) 
    out.write(str(latence))
    out.write("\n")
    pause(10)

fic.close()
out.close()