# Auxiliary functions for constructing a Huffman tree from a string
from htrees import *
from htree_dot_noviz import display_htree

from bitstring import *
from htrees import *

display_tree_constant = True


fn_cod_suffix_constant = "_coded"
fn_dec_suffix_constant = "_decoded"


def read_file_latin1 (filename):
    with open(filename + ".txt", encoding='ISO-8859-1') as fn:
        return (fn.read())


def increment(dict, cle):
    dict[cle] += 1

def ch_distrib (str):
    chd = {}
    total = 0
    for c in str:
        if c in chd:
            chd[c] += 1
        else :
            chd[c] = 1
        total += 1
    for l in chd:
        chd[l] /= total
    return chd
# print(ch_distrib(read_file_latin1("miserables")))


def afficher_arbre(ht, prof=1):
    if isinstance(ht, Leaf):
        print(ht.val, ":", ht.code)
    else:
        print(ht.val)
        print("    "*prof, end="")
        afficher_arbre(ht.low, prof+1)
        print("    "*prof, end="")
        afficher_arbre(ht.high, prof+1)

def display_htree(list_tree):
    for i in list_tree:
        afficher_arbre(i)

def init_treeset(dico):
    liste = []
    for i in dico:
        liste.append(Leaf((dico[i]), i))
    return liste


def combine_two(ht1, ht2):
    return Node(ht1.val+ht2.val, ht1, ht2)

#a1 = Leaf(0.3, 'b')
#a2 = Leaf(0.2, 'a')
#a1 = Node(0.5, Leaf(0.2, 'a'), Leaf(0.3, 'b'))
#a2 = Node(0.5, Leaf(0.2, 'a'), Node(0.3, Leaf(0.2, 'c'), Leaf(0.3, 'b')))
#afficher_arbre(combine_two(a1,a2))

def combine_all_trees(tree):
    if len(tree)==1:
        return tree[0]
    else:
        tree_sorted=sorted(tree,lambda x:x.val)
        return combine_all_trees([combine_two(tree[0],tree[1])]+tree[2:])

a1 = Node(0.5, Leaf(0.2, 'a'), Leaf(0.3, 'b'))
# a2 = Node(0.5, Leaf(0.2, 'a'), Node(0.3, Leaf(0.2, 'c'), Leaf(0.3, 'b')))
# a3 = Node(0.7, Node(0.4, Leaf(0.2, 'a'), Leaf(0.2, 'b')), Leaf(0.3, 'c'))
# list = [a1, a2, a3]
# afficher_arbre(combine_all_trees(list))

def construct_huffman_tree (dico):
    return combine_all_trees(combine_all_trees(init_treeset(dico)))


#?-------------------------Partie 4------------------------------

def dict_merge_f (d1, d2):
    dres = d1.copy()
    dres.update(d2)
    return dres


def tab_cod(m, tree):
    if isinstance(tree, Leaf):
        di = {}
        di[tree.code] = m
        return di
    else :
        d1 = tab_cod(m+[0], tree.low)
        d2 = tab_cod(m+[1], tree.high)
        d1 = dict_merge_f(d1,d2)
        return d1

#print(tab_cod([], Node (1.0, Leaf (0.5, 'a'), Node (0.5, Leaf(0.3, 'b'), Leaf(0.2, 'c')))))

def htree_to_coding_tab(tree):
    return tab_cod([],tree)

def code_source_string_to_bit_list(char, cod_table):
    sentence = []
    for letter in char:
        sentence.extend(cod_table[letter])
    return sentence

#table = {'a': [0], 'b': [1, 0], 'c': [1, 1]}
#print(code_source_string_to_bit_list('abacb',table))

def decode_bit_list_to_char(bit, tree, pos):
    if isinstance(tree, Leaf):
        return tree.code
    else:
        if bit[pos]==0:
            return decode_bit_list_to_char(bit, tree.low, pos+1)
        else:
            return decode_bit_list_to_char(bit, tree.high, pos+1)



def decode_bit_list_to_string(bit_list, tree):
    sentence = ""
    for i in range(len(bit_list)):
        sentence += decode_bit_list_to_char(bit_list, tree, i)
    return sentence

