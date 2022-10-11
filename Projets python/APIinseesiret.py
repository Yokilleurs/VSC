#from api_insee import ApiInsee # Pour gros PC
import time
from APIinseesiret import ApiInsee # Pour petit PC 

fic = open("sirets.txt", "r")

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
    # sir = random.randint(13000545700325, 13000548109417)
    # nombre = str(sir)
    start_time = time.time()
    appel(sir)
    print(i, (time.time() - start_time), sir)

fic.close()
