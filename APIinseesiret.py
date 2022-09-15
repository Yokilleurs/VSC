import random
from api_insee import ApiInsee
import time

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

for i in range(2):
    sir = random.randint(10000000000000, 22222222222222)
    nombre = str(sir)
    start_time = time.time()
    appel('50352114800042')
    print(i, (time.time() - start_time))
