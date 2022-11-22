def calcule_score_jeu(ijeu, liste_jeux):
  if jeu_est_un_spare(liste_jeux[ijeu])==True:
      score = calcule_score_jeu_cas_spare(ijeu, liste_jeux)
  elif jeu_est_un_strike(liste_jeux[ijeu]):
      score = 10 + calcule_bonus_strike(ijeu, liste_jeux)
  else: 
    coup1, coup2 = liste_jeux[ijeu]
    score = coup1 + coup2
  return score


def calcule_score_partie(liste_jeux):
  score = 0
  for indice in range (0,10):
    score += calcule_score_jeu(indice,liste_jeux)
  return score

def jeu_est_un_spare(jeu):
  coup1, coup2 = jeu
  if coup1+coup2==10 and coup1!=10:
    score = True
  else:
    score = False
  return score

def calcule_bonus_spare(indice_jeu, liste_jeux):
  indice_jeu += 1
  coup1, coup2 = liste_jeux[indice_jeu]
  return coup1

def calcule_score_jeu_cas_spare(ijeu, listjeu):
  score = 10 + calcule_bonus_spare(ijeu,listjeu)
  return score

def jeu_est_un_strike(jeu):
  coup1, coup2 = jeu
  score = coup1 ==10
  return score

def calcule_bonus_strike(indice_jeu, liste_jeux):
  coup1, coup2 = liste_jeux[indice_jeu+1]
  if indice_jeu != 9 and coup1 == 10:
    nombre = liste_jeux[indice_jeu+2]
    coup1, coup2 = nombre
    bonus = 10 + coup1
  else:
    bonus = coup1 + coup2
  return bonus
