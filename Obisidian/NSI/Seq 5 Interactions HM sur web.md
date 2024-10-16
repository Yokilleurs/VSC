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
	L'attribut ID (Identifiant unique)
	Le côté dynamique dce la page web est assuré par la possible modification des valeurs des attributs des composants graphiques.
	Pour pouvoir accéder indépendamment à chacun des composants, il faut pouvoir les identifier de manière unique : c'est le rôle de l'attribut ``id``. Chaque composant peut posséder un identifiant unique noté ``id``, composé d'une chaîne de caractères.
	![[Pasted image 20230407111950.png]]
	Chaque composant devient alors manipulabe abec un script. On peut aussi modifier l'aspect d'un composant avec du code CSS.
	Le DOM (Document Object Model) d'une page HTML est la représentation de la page sous forme d'objets qu'il est possible de manipuler. On peut le modéliser avec la structure d'un arbre, composé de branches et de feuilles, qui représentent les parents et leurs enfants.
	Les objets du DOM peuvent représenter une fenêtre, un document, une phrase, un style etc...
	Le DOM représente le document affiché par une structure en arbre, comportant des noeuds.
	Le DOM est présent dans le navigateurs. Sa manipulation peut être facilitée par des bibliothèques JS, comme jQuery.
	
	La méthode getElementById
	Cette méthode est l'une des onctions les plus utiles du DOM HTML car elle permet de renvoyer l'objet dont l'identifiant id est donné en paramètre de la fonction.
	Il est alors possible de modifier par un scriupt les attributs de l'objet, la page devient dynamique.
	document.getElementById("texte1").value; renvoie "Hello !" : c'est la valeur de l'attribut value du composant ayant pour identifiant "texte1"
	document.getElementById("texte1").value = "Bonjour"; change le contenu du composant ayant pour identifiant "texte1" et le remplace par "Bonjour".

5. Ecrire une fonction en JS
	Le langage JS permet l'écriture de scripts côté client, il deveient possible de calculer ou d'interagir avec tous les composants graphiques de la page. Il est préférable d'enregistrer les scripts JS dans un fichier JS externe à la page web.
	Les scripts JS doivent être écrits avec précision, car ils sont sensibles à la casse (majuscules et minuscules.)
	En JS, il est obligatoire de déclarer une variable avant son affectation. Plusieurs mots clés sont possibles, comme var let et const. Le mot clé let donne à la vriable une portée locale, c'est à dire qu'elle ne sera accessible que dans le corps de la fontion. 

| évènement       | description                                              |     |
| --------------- | -------------------------------------------------------- | --- |
| ```on change``` | un composant HTML a été changé                           |     |
| `onclick`       | L'utilisateur a cliqué sur un composant HTML             |     |
| `onmouseover`   | L'utilisateur a survolé un composant HTML avec la souris |     |
| `onmouseout`    | L'utulisateur appuie sur une touche du clavier.          |     |
| `onkeydown`     | L'utilsateur appuie sur une touche du clavier            |     |
| `onload`        | Le navigateur web a fini de charger la page HTML         |     |


Exemples: L'instruction suivante permet d'appeler la fonction JS Date() à chaque chargement de la page web : 
	`<body onload="Date()">`

L'instruction suivante permet d'appeler la fonction Calcul() à chaque clic sur un bouton :
```
	<input type="button" onclick="Calcul()"
	value="Convertir">
```

L'analyse et le traitement du formulaire devnat être effectués côté serveur, la page du formulaire sera écrite en langage PHP. Un 
un fomulaire simple est introduit dans une page web avec la balise ``<form>``
```
<form method="post" action="cible.php">
</form>
```

En cliquant sur un bouton envoyer, les contenus des zones de texte du formulaire seront transmis à une page cible.php sous forme de paramètres directement intégrés dans le requête HTTP envoyée par le client au serveur.

Le protocole SSL, ou plus récemment TLS, foncctionne également sur un modèle client serveur. Il assure : 
- L'intégrité des données échangées entre le client et le serveur ;
- L'authentification du serveur ;
- La confidentialité des données échangées grâce à une transmission chiffrée (numéro de carte bancaire, mot de passe, etc...)

Une transmission chiffrée se reconnaît de la manière suivante : 
- présence d'un cadenas dans la barre d'adresse du navigateur web :
- mention HTTPS au lieu de HTTP au début de l'URL
Il faut noter que le côté sécurisé de la transmission ne doit pas dispenser l'utilisateur d'exercer son sens critique. 

VOIR PHOTO EXEMPLE
Un cadenas et la mention HTTPS sont bien présents. Pourtant l'URL véritable du site est avec un .fr. L'extension est remplacée par .app ce qui indique que le site web est un site pirate de phishing.