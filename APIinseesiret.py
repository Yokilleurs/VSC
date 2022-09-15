import random
from api_insee import ApiInsee
import time

api = ApiInsee(
    key = "o_kfvxFzWwDucmQrJqF7qA31Qp0a",
    secret = "WPidT3P05AtZVSNuf9R2VfqCt9Qa"
)

def appel(siret):
    data = api.siret(siret).get()
    return data

for i in range(10):
    sir = random.randint(10000000000000, 22222222222222)
    nombre = str(sir)
    start_time = time.time()
    appel('50352114800042')
    print("%d --- %s seconds" % i, (time.time() - start_time))

appel(str(10000000000000))