# Séquence 1

Représentation des nombres.

1. Représentation des nombres en machine.

- Définitions :

    **Numération positionnelle :** La numéraion positionnelle est une façon d'écrire un nombre où la position de chaque chiffre est importante.

    **Base :** Une base est un entier positif supérieur ou égal à 2 qui permet de décomposer un nombre entier dans une numération positionnelle.

    **Bit :** Le bit est l'unité de mesure en informatique désignant la quantité élémentaire d'information. Un bit ne peut prendre que deux valeurs, notées par convention 0 et 1, appelés chiffres binaires.

    **Octet :** Un octet est une unité de mesure de quantité de données. C'est un ensemble de 8 bits.

    **Division euclidienne :** La division euclidienne ou division entière est une opération sur deux entiers naturels, appelés dividende et diviseur, auxquels on associe deux entiers appelés quotient et reste.

2. Ecriture d'un entier positif dans une base.

- Cours :
    Avec nos dix doigts, nous comptons et représentons naturellement les nombres dans la base 10. Appelée base décimale.
    En informatique, les bases les plus utilisées sont les bases 2 et 16. Quelle que soit la base utilisée, la position appelée rang est enssentielle dans l'écirture de la valeur.

- La base binaire :
    En représentation machine, les données sont stockées en base 2 appelée base binaire. L'écriture en base binaire est composée uniquement des chiffres binaires : 0 et 1.

- La base hexadécimale
    Les nombres sont représentés en machine en base binaire. La base 16, appelée base hexadécimale, permet à l'humain de les manipuler facilement tout en facilitant leur conversion.
    Pour écrire un entier positif dans la base hexa, il faut pouvoir écrire 10, 11, 12, 13, 14, 15 avec un seul caractère. Comme les 10 chiffres de 0 à 9 ne suffisent plus, il faut utiliser en plus les six premières lettres de l'alphabet : 
    10 = A
    11 = B
    12 = C 
    13 = D 
    14 = E
    15 = F
    (Les lettres peuvent être écrites en minuscules ou majuscules.)

    La base hexa est une des bases puissance de la base 2, donc les conversions de la base 2 à la base 16 et inversement sont facilitées.
    En langage Python, on peut saisir un entier directement en écriture hexadécimale précédée de 0x.

    Si l'on veut faire des calculs sur des valeurs exprimées sous forme de chaînes de caractères comme 0b1011, il faut les convertir avec la fonction Python int() quo prend pour arguments un chaîne de caractères et la base utilisée.
     
    La fonction Python native hex(x) convertit la variable x de type entier en une chaîne de caractères hexadécimaux précédée de 0x.

3. Evaluation du nombre de bits nécessaires

- Pour un entier positif
    Sur n bits, on peut stocker 2^n entiers postiifs. Comme on doit coder l'entier nul, le plus grand entier positif que l'on puisse représenter est 2^n-1.
    Pour évaluer le nombre de bits minimum nécessaires à l'écriture en base 2 d'un entier positif, il faut trouver la plus petite puissance de 2 qui soit strictement supérieure à l'entier à écrire.
     Exemple : 
     Comme 2^7 = 128 et 2^8 = 256 on a besoin de 8 bits pour écrire 200 en base binaire.

- Pour la somme de deux nombres entiers
    Sans connaître le résultat au préalable, le nombre de bits néxessaires pour stocker la somme de deux entiers positifs stockés sur n bits est n+1 bits.
     Démonstration :
     Sur n bits, le plus grand entier positif a pour valeur 2^n - 1. La plus grande somme possible de deux entiers sur n bits est le double de 2^n-1 donc 2x(2^n-1) = 2 x 2^n - 2 = 2^(n+1)-2
     Or 2^(n+1)-2 < 2^(n+1)

- Pour le produit de deux nombres entiers
    Sans connaître le résultat au préalable, le nombre de bits nécessaires pour représenter le produit de deux entiers positifs représentés sur n bits est 2n bits.
     Démonstration :
     Sur n bits, le plus grand entier positif a pour valeur 2^n-1. Le plus grand produit est donc (2n-1)².
     Identité remarquable blabla / ça donne 2^(2n) - 2^(n+1) + 1 < 2^(2n)
    
4. Addition binaire

- De deux entiers positifs.
    Pour additionner deux entiers positifs en base binaire, l'algorithme de calcul est le même qu'en base décimale, selon la table d'addition ci-contre : 
     ```
     0 + 0 = 1
     0 + 1 = 1
     1 + 1 = 0 et 1 de retenue.
     Ce qui donnerais :   
       0 0 1 1
     + 0 1 1 0
     ---------
       1 0 0 1
    ```

- De deux entiers relatifs.
    Pour effectuer l'addition de deux entiers relatifs (positifs et négatifs) dits aussi 'signés', avec le même algorithme que pour les entiers positifs, il faut utiliser la représentation en complément à 2n (ou complément à 2) où *n* est un nombre de bits fixé à l'avance.
     
    En effet, le nombre de bits utiliés pour cette représentation doit toujours être précisé. Par convention, le bit le plus à gauche vaut 1 pour les entiers négatifs et 0 pour les entiers positifs, ce qui permet de reconnaître immédiatement le signe d'un entier relatif.

    Méthode de calcul du complément à 2.
    -   Pour représenter un nombre positif, on utilise sa représentation en binaire, précédée d'autant de 0 que nécessaire pour avoir *n* bits au total.
    -   Pour représenter un nombre négatif *- m* :
        1. Coder en binaire le nombre *m* comme précédement ;
        2. Inverser tous ses bits ( ce qu'on appelle prendre le "complément à 1") ;
        3. Additionner 1 au nombre binaire obtenu, sans oublier les retenues éventuelles.

    ```
    Exemple : 
      0 0 1 0  0 1 1 0
      1 1 0 1  1 0 0 1
    + 0 0 0 0  0 0 0 1
    = 1 1 0 1  1 0 1 0 = -38
    ```

    Pour évaluer le nombre de bits nécessaires pour représenter un nombre en complément à 2,il faut prévoir un bit supplémentaire pour le bit de signe par raport à la représentation en base binaire. Ainsi, en complément à 2,on peut rerprésenter sur *n* bits les valeur sentières de -2^*n* à 2^(*n*-1)-1

    Méthode rapide.
    - Pour transformer un nomber en son complément à deux sans poser de calcul, il suffit de garder tous les bits depuis la droite jusqu'au premier 1 compris, puis d'inverser tous ceux qui sont à gauche du premier 1.
    Exemple : 
     Pour le nombre 38 en binaire : 0010 0110,
     - On garde la partie à droite : 0010 01*10*;
     - On inverse la partie de gauche après le premier un : *1101 10*10
     L'écriture de -38 en complément à 2 est : 1101 1010

5. Représentation approximative des nombres réels
    En informatique, les nombres non entiers sont souvent représentés en nombres à virgule flottante, encore appelés nombres flottants.

- Représentation approximative des nombres réels.
    Compte tenu du nombre limité de bits en mémoire, tous les nombres réels ne sont pas exactement représentables en binaire. Ainsi, certains n nombres réels ont-ils un représentation binaire infinie.

    Exemple : 
     La représentation de 0,1 e base binaire est 0,0*0011* *0011*

    Pour convertir la partie décimale d'un nombre flottant de la base décimale à la base binaire :
    1. Multiplier par 2 la partie décimale ;
    2. La partie entière du nombre obtenu donne le prochain chiffre après la virgule ;
    3. Ne garder que la partie décimale du nombre obtenu et recommencer les calculs avec cette nouvelle valeur tant que celle-ci n'est pas nulle.

    Exemple : 
     Conversion de 5,125 en base binaire : La partie entière est 5 qui s'écrit 101 en binaire.
      Multiplication par 2          Partie entière du produit       Partie décimale du produit
     de la partie décimale     
     ```
     0,125 x 2 = 0,25          0              25
     0,25 x 2 = 0,5                            5
     0,5 x 2 = 1               1               0
     ```

- Le test d'égalité sur les nombres flottants
    Il faut éviter de tester l'égalité sur deux nombres flottants
     Exemple :
     En python, et dans la plupart des langages de programmation, 0.1 + 0.2 n'est pas exactement égal à 0.3. 
    
    L'instruction isclose(7.00000001, 7) renvoie True.
    L'importation du module Python math ou numpy est indispensable.
    
    Une autre possibilité ocnsiste à modifier le test a == b en calculant la valeur absolue de la différence entre a et b avec la précision souhaitée (ici 10**-9) ce qui donne abs(a - b) <= 10**-9

    L'instruction abs(a - 5) <= 10**-8 permet de tester si la varialb e a de type float a une valeur proche de 5 avec une précision de 10**-8.

    L'affichage d'un nombre flottant peut prêter à confusion à cause de sa représentation potentiellement approximative, et donc non exacte.
    La fonction native round() permet de calculer des arrondis en précisant en arguements la valeur à arrondir et le nombre de décimales souhaitées

# Séquence 2

Encodage des caractères et expressions booléennes.

1. Le calcul booléen

- Définitions :
    
    **Variable booléenne :** Une variable booléenne est une variable qui ne peut prendre que deux valeurs : True (vrai) ou False (faux). Ces deux valeurs peuvent également être notées 1 ou 0 ou encore oui ou non.

    **Opérateur booléen :** Un opérateur booléen est un opérateur mathématique qui relie deux variables binaires ou deux expressions binaires.

    **Expression booléenne :** Une expression booléenne est une expression dont l'évaluation ne peut être que True ou False.

    **Opérande :** Un opérande est un élément sur lequel s'applique un opératuer booléen.

    **Table de vérité d'une expression booléenne :** La table de vérité d'une expression booléenne est un tableau qui comporte une colonne par variable d'entrée (ou opérande) et une colonne pour le résultat de l'opération appliqué aux opérandes. Puisque les variables booléennes ne peuvent prendre que deux valeurs, on peut dresser la liste de tous les cas possibles pour chacun des opérateurs.

2. Quelques opérateurs booléens

- L'opérateur **and**
    L'opérateur booléen **and** est un opérateur de conjonction, noté &. Soit *a* et *b* deux variables booléeenes, *a* and *b* renvoie **True** quand les deux opérandes *a* et *b* ont pour valeur **True** toutes les deux, et **False** sinon.
        Table de vérité de l'opérateur **and** :
	
| a     | b     | a and b |
| ----- | ----- | ------- |
| False | False | False   |
| False | True  | False   |
| True  | False | False   |
| True  | True  | True    |

- L'opérateur **or**
    L'opérateur booléen **or** est un opérateur de disjonction, noté | ou +. Soit *a* et *b* deux variables booléennes, *a* or *b* renvoie **True** quand au moins un des deux opérandes *a* ou *b* a pour valeur **True**, et **False** sinon.
        Table de vérité de l'opérateur **or** :
           
| a     | b     | a and b |
| ----- | ----- | ------- |
| False | False | False   |
| False | True  | True    |
| True  | False | True    |
| True  | True  | True    |

- L'opérateur **not**
    L'opérateur booléen **not** est un opérateur de négation, noté ~ ou NON.
    Soit *a* une variable booléenne, *not a* renvoie la négation de l'opérande *a*.

 | a     | not a |
 | ----- | ----- |
 | True  | False |
 | False | True  |

- L'opérateur **xor**
    L'opérateur booléen **xor** (appelé "ou exclusif") est un opérateur de disjonction exclusive (XOR pour eXclusive OR), noté (plus dans un rond) ou v souligné.
    Soit *a* et *b* deux variables booléennes, *a xor b* renvoie **True** si un seul des deux opérandes *a* ou *b* a pour valeur **True**, et **False** sinon.
    
| a     | b     | a xor b |
| ----- | ----- | ------- |
| True  | True  | False   |
| True  | False | True    |
| False | True  | True    |
| False | False | False   |

3. Comment évaluer une expression booléenne ?

Comme dans une expression mathématique classique, il faut tenir compte des parenthèses. Les opérateurs booléens prioritaires sont **not** puis **and** et enfin **or** ou **xor**.

- Expression comportant uniquement des valeusr booléennes.
    Dans une expression comportant uniquement des valeurs booléennes, il faut simplifier l'expression en tenant compte des parenthèses et des règles de priorité entre les opérateurs.
     Exemple :
     - True and True or (not False and False)
     - True and True or (True and False)
     - True and True or False
     - True or False
     - True

- Expression comportant des variables booléennes
    Pour évaluer une expression booléenne comportant des variables booléennes, on peut dresser une table de vérité de chaque partie de l'expression en tenant compte des parenthèses et des priorités entre les expressions.

a or b and not a:

| A     | B     | not A | not B | A or B and not A | 
| ----- | ----- | ----- | ----- | ---------------- |
| False | False | True  | True  | False            |
| False | True  | True  | False | True             |
| True  | False | False | True  | True             |
| True  | True  | False | False | True             |

- Caractère séquentiel de certains opérateurs en Python
	Dans certains cas, l'interpréteur Python peut court-circuiter une partie d'une expression booléenne qui se situe à la droite d'un opérateur booléen. Ce raccourci ne peut se faire que lorsque l'évaluation de la partie de droite ne change pas le résultat final.
	 Exemple :
```Python
def test(retour, texte):
	print(texte)
	return retour

KeyboardInterrupt
	a = test(True, "1") or test(False, "2")
```
Comme le premier appel à la fonction test() renvoie True, l'interpréteur Python n'évalue pas l'expression 
```python
	def test(retour, texte):
	Print(texte)
	return retour
	a = test(True, "1") or test(False, "2")
	1
```
après l'opérateur **or**. Ainsi on peut lire la valeur affichée par le premier appel à la fonction `test()` qui est 1 mais pas la deuxième qui devrait être 2.

4. Représentation d'un texte en machine

Afin de représenter tout type de caractère  (lettre, symbole ou chiffre), il est indispensable d'utiliser un système de codage informatique, appelé encodage. L'encodage assure la correspondance entre les caractères et les nombres binaires stockés dans la mémoire de l'ordinateur.

- Le codage ASCII est simple mais limité en termes de caractères à encoder, ce qui ne le rend pas universel. 7 bits suffisent pour coder un caractère.
- La *norme ISO 8859-1* (ou Latin-1) permet d'encoder tous les caractères des principales langues européennes. Chaque caractère est codé sur 1 octet. Certains alphabets comme le cyrillique ou le polonais ont leur propre norme.
- Le standart Unicode est universel et extensible si besoin. En revanche, il nécessite l'utilisation de 4 à 6 octets par caractères à encoder, ce qui allonge la taille du message.
- La *norme UTF-8* est une représentation d'Unicode dont elle possède les avantages. Cet encodage est de taille variable, ce qui lui permet d'être moins gourmand en espace mémoire qu'Unicode. De plus, il est compatible avec ASCII, mais il est plus compliqué à gérer en machine.

Le nombre de symboles hexadécimaux étant variabl,e le nombre de caractère contenus dans un fichier texte n'est pas déductible à partir de la taille du fichier. En octobre 2020, 95% des sites web étaient encodés en UTF8, ce qui permettait une uniformisation des pages et des navigateurs web.

5. Ce qu'il faut savoir et savoir faire
- [ ] Dresser la table d'une expression booléenne avec les opérateurs booléens : `and, or, not et xor`
- [ ] Comprendre l'intérêt des différetnts systèmes d'encodage d'un texte en machine : les encodages ASCII, ISO 8859-1 et Unicode.
- [ ] Convertir un fichier texte dans différents formats d'encodage

# Séquence 3

Les types construits.

1. Types construits

A partir des types de bases, il est possible de façonner de nouveaux types de variables, appelés **types construits**. Ceux-ci ont chacun leurs particularités. Choisir le bon type de variable est essentiel pour implémenter un algorithme dans un langage de programmation. Les trois types **p-uplet**, **tableau** et **dictionnaire** présentés ici sont génériques et peuvent être mis en oeuvre dans de nombreux langages de programmation. Ce chapitre utilise les appellations spécifiques du langage Python.

2. Le p-uplet et le p-uplet nommé

Définition : 
	P-uplet : Un p-uplet (ou *tuple* en anglais) est une collection ordonnée d'éléments, appelés *composantes* ou *termes*. Chaque terme peut être de n'importe quel type.

Le p-uplet est de type `tuple`
Les termes du p-uplet ne sont pas modifiables par affection.

On parlera d'un doublet pour un p-uplet avec 2 éléments(p = 2), d'un triplet pour 3 éléments (p =3), etc...

Création d'un p-uplet 
En langage Python, les termes d'un p-uplet sont séparés par des virgules. Les **parenthèses** ne sont pas obligatoires mais sont fortement conseillées pour la lisibité du code. 

Exemple : 
	Les instructions `t = (1, 2, 3)` ou encore `t = 1, 2, 3` créent le triplet `t`.
	Un p-uplet ne contenant qu'un seul élément s'écrit également avec une virgule. Ceci permet d'éviter la confusion avec les parenthèses d'une expression mathématique, qui ne possède pas de virgule.
Exemple : 
	`t = (1, )` et non pas `t = (1)`

Indexation des éléments d'un p-uplet
	Pour un p-uplet de n éléments, les termes sont indexés de 0 à *n-1*
Exemple :
	Pour ``t = (1, 5, 8)``
	``t[1]`` désigne le deuxième élément du triplet ``t`` qui vaut 5 et ``t[-1]`` ou ``t[len(t)-1]`` vaut 8.
	Dans un p-uplet dit nommé, il est possible d'accéder aux éléments grâce à un nom plutôt qu'à un indice.
	 Ce type de p-uplet n'existe pas dans Python, il doit être implémenté par un dictionnaire.

Modification d'un p-uplet
	Il n'est pas possible de modifier par affectation les termes d'un p-uplet après sa création. Un p-uplet est dit **non-muable**.
	Si les valeurs des termes du p-uplet doivent être changées au fil du programme, alors il faudra choisir un autre type de variable, comme le tableau.

Fonction renvoyant un p-uplet de valeurs
	En programmation fonctionnalle, il est indispensable d'utiliser des fonctions pouvant renvoyer un ensemble de valeurs réutilisables, contenues dans un p-uplet ou une liste.
	Par exemple, on souhaite calculer les coordonnées $(x_1,x_2)$ du point I, milieu de $[AB]$ grâce à la fonction `milieu()` suivante :

```py
def milieu(A, B):
	xI = (A[0] + B[0]) / 2
	yI = (A[1] + B[1]) / 2
	return (xI, yI)
``` 

Cette fonction renvoie les coordonnées $(x_1,y_1)$ du milieu du segment $[AB]$ sous forme d'un doublet $(x_1,y_1)$.
Afin de pouvoir réutiliser les coordonnées $(x_1,y_1)$ du point I, il est possible de les afffecter à une unique variable ``coordonnees`` avec l'instruction Python suivante : `coordonnees = milieu((2,1), (3,5))`.
La variable `coordonnees` sera alors de type `tuple` et les coordonnées du point I seront accessibles avec les deux instructions `coordonnees[0]` pour son abscisse et `coordonnees[1]` pour son ordonnée.


3. Le tableau (appelé liste en Python)

Définition: 
	Tableau : un tableau eswt une collection ordonnée d'éléments de n'importe quel type organisés séquentiellement (les uns à la suite des autres.)

En Python, un tableau est appelé liste, il est de type `list`.
Le tableau est modifiable par affection, on dit qu'il est muable, ou mutable.

Création d'une liste:
	Dnas une liste, les termes doivent être séparés par des virgules et entourés de crochets.

Exemple : 
	L'instruction `L = [1, 5, 8]` crée la liste `L`

Création d'une liste de liste :
	Un tableau à double entrée, appelée matrice, peut être représentée par une liste de listes

Exemple : 
	L'instruction `L2 = [[3, 4], [8,1]]` crée la liste L2, représentant le tableau ci-dessous

 | 3   | 4   |
 | --- | --- |
 | 8   | 1   |

Indexation des éléments de la liste :
	Les termes d'une liste sont idexés de 0 à n-1 pour une liste de n éléments. On peut accéder en lecture à l'élément de rang ``i`` gràce à la syntaxe ``L[i]`` 

Exemple : 
	`L[1]` désigne le deuxième élément de la liste qui vaut 5. La valeur 1 de l'instruction est appelée l'indice, ou l'index, de position.

Modification de la liste par affectation : 
	Les termes d'une liste peuvent être modifiés par affectation au fil du programme.

Exemple : 
	L'instruction ``L[2] = 14`` remplace le troisième élément, qui vaut ``8``, par la valeur ``14``. La liste L devient alors ``[1,5,14]``

Création d'une liste par compréhension : 
	Il est possible et élégant de construire uneliste en compréhension avec le langage Python. C'est très pratique pour créer, transformer ou filtrer une liste.
	Pour créer une liste en compréhension avec python, on utilise la syntaxe ``for i in range()`` et éventuellement une condition de filtrage

Exemple :
	``L3 = [i**2 for i in range(5) if i**2 % 2 == 0]``
	La liste ci dessus contient les valeurs de i² pour i variant de 0 à 4, à condition que i² soit divisible par 2. La variable `L3` contient la liste ``[0, 4, 16]``

Les itérables :
	Un itérable est un objet dont les valeurs sont accessibles grâce à une boucle for, par exemple. les types str, tuple, list et dict sont des itérables fréquents en Python.

Condition de filtrage :
	Ajotuer une condition de filtrage permet de ne sélectionner que certains éléments de la liste, grâce à une expression booléeene ne pouvant prendre que deux états : True ou False. Si la condition est vraie, les éléments seront ajoutés à la liste.

4. Le dictionnaire

Définition : 
	Dictionnaire : Un dictionnaire est une collection nion ordonnée d'éléments. Ces éléments sont constitués d'une clé assciée à une valeur.

Les clés peuvent être de n'importe quel type non muable : entier, chaîne de caractères, p-uplet.

Création d'un dictionnaire
	Un nouveau dictionnaire est créé par affectation et nécessite l'utilisation d'accolades, ce qui le différencie du puplet et du tableau (appelé liste en Python). Une valeur est associée à une clé selon la syntaxe ``clé: valeur``.

Exemple : 
	L'instruction ``annuaire = {10 : 'Paul', 20 : 'Tom', 30 : 'Nadia'`` crée e dictionnaire ``annuaire``

Accès aux éléments du dictionnaire
	Les éléments du dictionnaire ne sont pas indexés. Il est donc impossible d'afficher son n-ième élément. On accède ç une valeur grâce à la clé qui lui est associée.
C'est la raison pour laquelle les clés d'un dictionnaire doivent êtres toutes différentes.

Exemple : 
	``annuaire[0]`` renvoie ainsi une erreu de clé "KeyError", tandis que ``annuaire[10]`` renvoie 'Paul' car le nombre 10 est la clé du dictionnaire à laquelle esst associée la valeur ``'Paul'``

Modification du dictionnaire ;
	L'instruction del annuaire[10] supprimera l'entrée ``10: 'Paul'`` du dictionnaire ``annuaire``. L'instruction ``annuaire[30] = 'Hamza'`` remplace la valeur ``"Nadia"`` par la valeur ``'Hamza'`` ou crée une nouvelle entrée dans le dictionnaire si la clé 30 n'existait pas.

Methodes specifiques du dictionnaire :
	En Python, les méthodes items(), keys() et values() permettent d'accéder aux éléments du dictionnaire. 

Exemple : 
	annuaire.items() renvoie la collection de tous les objets du dictionnaire annuaire. 
	annuaire.keys() renvoie la collection itérable de toutes les clés du dictionnaire annuaire. 
	annuaire.values() renvoie la collection itérable de toutes les valeurs du dictionnaire annuaire.

|                                       | Puplet      | Tableau    | Dictionnaire                                     |
| ------------------------------------- | ----------- | ---------- | ------------------------------------------------ |
| Notation                              | (1,2,3)     | [1,2,3]    | {'key':'value'}                                  |
| Construction                          | Puplet Vide | Liste vide | Dictionnaire vide                                |
|                                       | t=()        | t=[]       | t={}                                             |
| Elements internes de différents types | Oui         | Oui        | Oui, à condition que les key soient du même type |
| Lecture du contenu                    | Classique   | Classique  | Only avec key                                    |

# Séquence 4

Dans cette séquence, il s'agit de manipuler des tableaux doublement indexés (ou tables), implémentés en Python avec une liste de listes.
	Exemple :
	Dans le tableau doublement indexé ci-dessous, les pensionnaires d'un zoo et leurs caractéristiques sont rangés en lignes et en colonnes.

| id  | Nom    | Race   |
| --- | ------ | ------ |
| 1   | Wanita | Tigre  |
| 2   | Punk   | Loutre |
| 3   | Toko   | Toucan | 

1. Omporter ou exporter une table

Le format CSV
	Définition:
	Format CSV : Le format CSV (de l'anglais Comma Separated Values) est un format de fichiers facile à manipuler avec Excel et qui permet d'échanger des données entre différents systèmes ou logiciels.

Dans une table au format CSV, la première ligne est composée de descripteurs. Sur les lignes suivantes, les données correspondant aux descripteurs sont rangées en lignes. Chaque descripteur définit un ensemble de champs.
Sur chaque ligne, les descripeurs et les données sont séparés par des virgules ou des points-virgules, qui jouent ici le rôle de caractère séparateur.

id, nom, race
1, Wanita, Tigre
2, Punk, Loutre
3, Toko, Toucan

Importer une table depuis un fichier csv :
	Définition :
	Importer un fichier : importer un fichier est une opérration qui consiste à lire les informations d'un fichier externe au programme, de manière à pouvoir effectuer un traitement informatique sur les valeurs lues.
	fichier.csv -------importation----> liste de listes en python.
.
	Exemple :
	Après importation, la liste de listes suivante contient toutes les informations du fichier CSV initial.
	*Remarque* : Pour créer une liste de listes en Python, il est égalemen possible d'importer un fichioer texte tabulé.
.
	Définition : 
	Exporter une table vers un fichier : Exporter une table vers un fichier est une opération qui consiste à enregistrer les valeurs d'une table puthon dans un fichier externe au programme. C'est l'opération inverse d'une importation.
	liste de listes en python ------exportation------> fichier.csv

LES COURS QUE J'AI SKIIIIP

6. Construire une nouvelle table.
* Construction d'une table
	Il est possible de construire une nouvelle table en combinant les données des deux tables différentes

Définition : 
	Fusion : une opération de fusion consiste à rassembler les données issues de deux tables différentes en une seule table.

* Limites
	Pour pouvoir fussionner deux tables, il est nécessaire qu'elles partagent les mêmes descritpeurs et que les descripteurs soient rangés dans le même ordre.

Exemple : 
	Les deux tables t1 et t2 peuvent fusionner grâce à un opérateur de concaténation +, car elles partagent les mêmes descripteurs.