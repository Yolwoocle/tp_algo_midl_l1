#!/usr/bin/env python3

# FONCTIONS DE BASE
def creer_liste_vide():
  return None

def creer_liste(t,q):
  return t,q

def tete(liste):
  assert liste!=None, 'Pré-condition (tete)'
  return liste[0]

def queue(liste):
  assert liste!=None, 'Pré-condition (queue)'
  return liste[1]

def est_vide(liste):
  return liste==None

# EXERCICE
def partitionner_pivot(liste,pivot):
  if est_vide(liste):
    return creer_liste_vide(), creer_liste_vide()
  
  x = tete(liste)
  liste_infeq, liste_sup = partitionner_pivot(queue(liste), pivot)
  if x <= pivot:
    return creer_liste(x, liste_infeq), liste_sup
  else:
    return liste_infeq, creer_liste(x, liste_sup)

def test_partitionner_pivot():
  print('Test de la fonction partitionner_pivot')
  # print(partitionner_pivot(None,5), (None,None))
  # print(partitionner_pivot((4,None),5), ((4,None),None))
  # print(partitionner_pivot((5,None),5), ((5,None),None))
  # print(partitionner_pivot((6,None),5), (None,(6,None)))
  # print(partitionner_pivot((4,(3,(8,(2,(5,None))))),8), ((4,(3,(8,(2,(5,None))))),None))
  # print(partitionner_pivot((4,(3,(8,(2,(5,None))))),1), (None,(4,(3,(8,(2,(5,None)))))))
  # print(partitionner_pivot((4,(3,(8,(2,(5,None))))),4), ((4,(3,(2,None))),(8,(5,None))))
  
  assert partitionner_pivot(None,5)==(None,None)
  assert partitionner_pivot((4,None),5)==((4,None),None)
  assert partitionner_pivot((5,None),5)==((5,None),None)
  assert partitionner_pivot((6,None),5)==(None,(6,None))
  assert partitionner_pivot((4,(3,(8,(2,(5,None))))),8)==((4,(3,(8,(2,(5,None))))),None)
  assert partitionner_pivot((4,(3,(8,(2,(5,None))))),1)==(None,(4,(3,(8,(2,(5,None))))))
  assert partitionner_pivot((4,(3,(8,(2,(5,None))))),4)==((4,(3,(2,None))),(8,(5,None)))
  print('  OK')

test_partitionner_pivot()
