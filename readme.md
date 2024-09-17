# Machine Learning Blackjack

## Description
Ce projet consiste à développer un algorithme d'intelligence artificielle capable de jouer au blackjack de manière optimale. L'objectif principal de cet algorithme est de maximiser les gains en se connectant à une API de jeu de blackjack et en utilisant des techniques de machine learning pour apprendre les meilleures stratégies au fur et à mesure du jeu.

## Fonctionnalités
**Connexion à l'API Blackjack** : L'algorithme se connecte automatiquement à une API de blackjack, récupère les données en temps réel et envoie les actions de jeu (tirer, rester, doubler, etc.).

**Apprentissage automatique (Machine Learning)** : L'algorithme utilise des modèles d'apprentissage supervisé ou par renforcement pour optimiser ses décisions en fonction des résultats des parties précédentes.

**Optimisation des gains** : L'objectif est de maximiser les gains au fil du temps en affinant les stratégies de jeu.

## Fonctionnement

L'application possède 2 modes de fonctionnements :
- Learning Mode = true : Jouer des coups aléatoire et enregistrer le résultats de ces coups dans un fichier csv.
- Learning Mode = false : Jouer des coups en fonctions des résultats qui ont été enregistrer dans le fichier csv.

Lorsque l'application n'est pas en phase d'apprentissage, 3 stratégie sont possible : 
- V0 : Jouer des coups aléatoire 
- V1 : Jouer des coups en fonctions des résultats qui ont été enregistrer dans le fichier csv (les seules chose qui sont enregistrées sont les cartes du dealer, les cartes du player, la décision prise par le player et le nombre de fois que la décision a été bonne)
- V2: Comme la V1 mais nous enregistrons le nombre de face restante dans le packet en plus.


## Fichier de config

Le fichier config.py permet de modifier : 
- Si l'application est en apprentissage ou non
- La stratégie utilisée (v0, v1, v2)
- L'affichage graphique dans la console