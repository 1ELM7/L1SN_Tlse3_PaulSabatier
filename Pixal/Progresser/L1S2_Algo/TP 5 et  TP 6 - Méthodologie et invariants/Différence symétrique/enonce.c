Enoncé
Considérons deux listes L1, L2 triées dans l’ordre strictement croissant. Ecrire un programme qui nécessite au plus len(L1)+len(L2) itérations permettant de connaître le nombre des éléments non communs aux deux listes, ce qu'on appelle la différence symétrique.

Le programme doit être instrumenté à l'aide d'assert pour vérifier invariant/objectif.

Le modèle de solution proposé ici est en deux étapes :
Nous utilisons un modèle qui synchronise l’avancement dans les deux listes L1 et L2. A chaque itération on se trouve à l'indice i1 dans L1 et i2 dans L2. Pour savoir si l'élément courant d'une liste appartient à l'autre, il suffit qu'il soit égal à l'élément courant de l'autre liste. Ceci permettra d'avancer l'indice approprié dans la liste correspondante tout en comptant si l'élement est présent ou non. La boucle s’arrête à la terminaison de l’une des deux listes.
Le nombre des élements restants de la liste non terminée est ajouté au calcul en cours.

Entrée du programme
Deux listes d'entiers (déjà triées), lues à l'aide du classique liste = eval(input())

Sortie du programme
Un entier.
