# pour obtenir l'api insee (dans un powershell) : pip install api-insee
import time
from api_insee import ApiInsee  

fic = open("sirets.txt", "r") # Ouverture des fichiers contenant 1000 sirets et le fichier de save de la latence (respectivement en 'read' et 'append').
out = open("latency.csv", "a")

api = ApiInsee(
    key = "o_kfvxFzWwDucmQrJqF7qA31Qp0a",
    secret = "WPidT3P05AtZVSNuf9R2VfqCt9Qa"
) # authentification à l'api de l'insee

def appel(siret):
    try:
        api.siret(siret).get() #tentative d'appel à l'api
        print('siret trouvé')
    except OSError as err: #OSError correspond à un crash des serveurs SIREN, donc on cherche à relever ces erreurs et à les gérer pour éviter un arrêt du programme...
        print(err)
    return 1


for i in range(100):
    sir = fic.readline() # permet de lire dans le fichier contenant 1000 sirets
    start_time = time.time() # début du timer pour la latence
    appel(sir) # appel à l'api SIREN
    print(i, (time.time() - start_time), sir) # Impression du run + latence + siret
    latence = round((time.time() - start_time), 2) # calcul de la latence
    out.write(str(latence)) # ajout de la latence au fichier de csv
    out.write("\n") # nouvelle ligne csv
    #time.sleep(60) # sleep 1 minute pour éviter de surcharger les serveurs de demandes (il est désactivé pour pouvoir tester le programme rapidement)...

fic.close() # fermeture des fichiers ouverts au début du programme
out.close()

# Suite du projet : ajouter l'heure française à chaque test renvoyant une OSError pour identifier l'heure du crash des serveurs.