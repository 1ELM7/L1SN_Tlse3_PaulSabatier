from __future__ import print_function

from htrees import *
from htree_dot_noviz import display_htree

a = Node(0.5, Leaf(0.2, 'a'), Leaf(0.3, 'b'))
b = Node(0.5, Leaf(0.2,'a'), Node(0.3, Leaf(0.2,'c'), Leaf(0.3,'b')))
c = Node(0.7, Node(0.4, Leaf(0.2,'c'), Leaf(0.2,'b')),Leaf(0.3,'c'))




def somme (ht):
    if isinstance(ht, Leaf):
        return(ht.val)
    else:
        return(ht.val + somme(ht.low) + somme(ht.high))

def profondeur(arbre):
    if isinstance(arbre, Leaf):
        return 0
    else:
        return (1+profondeur(arbre.low)+profondeur(arbre.high))

def membre(arbre, car):
    if isinstance(arbre, Leaf):
        return arbre.code == car
    else :
        return (membre(arbre.low,car) or membre(arbre.high,car))

def print_indent(indent):
    for i in range (0,indent):
        print("   ",end="")

def afficher_arbre_tmp(indent,ht):
    if isinstance(ht,Leaf):
        print_indent(indent)
        print(ht.val,":",ht.code)
    else:
        print_indent(indent)
        print(ht.val)
        afficher_arbre_tmp(indent+1,ht.low)
        afficher_arbre_tmp(indent+1,ht.high)

def afficher_arbre(ht):
    afficher_arbre_tmp(0,ht)

def nb_feuilles(arbre):
    if isinstance(arbre, Leaf):
        return 1
    else:
        return (nb_feuilles(arbre.low)+nb_feuilles(arbre.high))

def nb_nds_int(arbre):
    if isinstance(arbre, Leaf):
        return 0
    else:
        return (1+nb_nds_int(arbre.low)+nb_nds_int(arbre.high))

def nb_noeuds(arbre):
    if isinstance(arbre, Leaf):
        return 1
    else:
        return (1+nb_noeuds(arbre.low)+nb_noeuds(arbre.high))
