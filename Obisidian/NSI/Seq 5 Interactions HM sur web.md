1. Modèle client serveur
	Le modèle client serveur est une architexture de communication entre deux machines le plus souvent disctinctes : le client et le serveur

Définitions :
	Client : le client est la machine (ordinateur, smartphone) qui demande l'exécution d'un service (comme, par ex, l'affichage d'une page web). Le client envoie des requêtes au serveur. Les clients web sont souvent des navigateurs web.
	Serveur : Un serveur est une machine robuste et rapide chargée de réponde à la demande (requête) du client en lui fournissant le service demandé.
	Requête : la requête est le message transmis par le client au serveur, décrivant le service à rendre. 
	Réponse : La réponse est le message transmis par le serveur au client suite à l'exécution d'un service.

Dans le modèle client serveur, les deux ont des rôles.
	Après l'envoi d'une requête, le client se met en pause
	Le serveur renvoie une réponse au client, composée d'un code d'état (1XX,2XX etc...) et du contenu demandé si la requête est un succès.

2. Description d'une page web.
	Ce langage autorise une certaine souplesse de syntaxe ; il est alors parfois possible d'ouvrir une balise HTML sans la fermer ou de deonner la valeur d'un attribut entre guillemets ou apostrophes. Il est donc possible que la page web n'ait pas toujours le même aspect visuel selon le navigateur web utiliser.
	Le langage CSS est utilisé pour donner du style à la page, pour mettre en forme le texte, centrer un texte ou une image, mettre en gras la police de caractère...

Interactivité de la page
	Son contenu pourra alors varier selon l'heure de la requête, le nom de l'utilisateur ou encore le remplissage d'un formulaire par l'utilisateur, etc.
	Remarque, La techno AJAX permet le transfert de données en arrièreplan entre le client et le serveur, sans avoir à recharger la page web. Les suggestions de recherche sur Google utilisent cette technologie.

3. Scripts côtés serveur et côté client
	Le web est basé sur un principe simple ; tous les contenus sont fournis par les serveurs web et peuvent être récupérés à distance par les clients. Ainsi un contenu statique sera t il simplement téléchjargé par le client, tandis qu'un contenu dynamique ne pourra fontionner que grâce à l'existence de scripts, des petits bouts de code chargés d'exécuter une action prédéfinie programmée à l'avance. Ces scripts peuvent ainsi être exécuités soit du côté serveur soit du côté client. 
	Les scripts côté serveurs néxessitent une communication avec le serveur et ne permettent pas une interactivité immédiate. L'exécution côté serveur est souvent nécessaire, pour gérer les droits des utilisateurs par exemple.
	Les scirpts côtés navitgateurs s"exécutent directemenet sur la machine. Il est donc possible d'avoir une interactivité immédiate, pour des jeux par exemple.
	Côté serveur, le langage le plus utilisé est le PHP. 
	Un script côté client sera exécuté par le client, dans le navigateur web, pour apporter un côté dynamique au site web.
	Le script sera donc directement intégré dans le code HTML de la page ou alors inséré dans un fichier externe. Les machines clientes étant généralement relativement puissantes, cette exécution de scripts côté clients permet de soulager les serveur sans ralentir le processus global.
	Bloquer l'exécution d'un script sera cependant toujours possible via une extension intallée dans le navigateur web, comme NoScript de Firefox. 
	Javascript est le langage souvent utilisé pour ce genre de scripts. 

4. Composants graphiques d'une page web
	L'attribut Value
	L'attrbiut value définit lma valeur par défaut qui sera affichée dans l'élément au cahrgement de la page web. Cette valeur est accessible et modifiable, notamment grâce à la méthode getElementById() (voir ci-après)
	L'attribut