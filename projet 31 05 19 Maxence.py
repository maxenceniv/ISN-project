# Créé par Maxence et Corentin , le 21/12/2018 en Python 3.2
import copy
import pygame,sys
import time
import random
from pygame.locals import *
import pickle        #pour les sauvegardes

pygame.init()
pygame.font.init()
mainclock= pygame.time.Clock()
MENU=True
MODE1=False
MODE2=False
TUTO1=False
TUTO2=False
FIN1=False
FIN2=False
ChoixDif=False
EcranHightcsore=False
FinHightscore=False
curseur=0
curseur1=0
window=pygame.display.set_mode((1240,700),0,32)
pygame.display.set_caption('projet')
police1=pygame.font.Font("Pixel NES.otf",30)
police2=pygame.font.Font("Pixel NES.otf",60)
Clock = pygame.time.Clock()

direction=[[0,1],[0,-1],[1,0],[-1,0]]              #les quatres directions possibles
minisol=pygame.image.load('minisol.png')
minimur=pygame.image.load('minimur.png')
titre11=pygame.image.load('titre 1.1.png')
titre12=pygame.image.load('titre 1.2.png')
titre13=pygame.image.load('titre 1.3.png')
titre14=pygame.image.load('titre 1.4.png')
titre15=pygame.image.load('titre 1.5.png')
animtitre1=[titre11,titre12,titre13,titre14,titre15]
tanimtitre1=0
titre21=pygame.image.load('titre 2.1.png')
tanimtitre2=0
blanc=(255,255,255)
rouge=(200,0,0)

fondecrantitre1=pygame.image.load("fond ecran titre1.png")
fondecrantitre2=pygame.image.load("fond ecran titre2.png")
fondecrantitre3=pygame.image.load("fond ecran titre3.png")
fondecrantitre4=pygame.image.load("fond ecran titre4.png")
fondecrantitre5=pygame.image.load("fond ecran titre5.png")
fondecrantitre6=pygame.image.load("fond ecran titre6.png")
fondecrantitre7=pygame.image.load("fond ecran titre7.png")
fondecrantitre8=pygame.image.load("fond ecran titre8.png")
fondecrantitre9=pygame.image.load("fond ecran titre9.png")
fondecrantitre10=pygame.image.load("fond ecran titre10.png")
fondecrantitre11=pygame.image.load("fond ecran titre11.png")
fondecrantitre12=pygame.image.load("fond ecran titre12.png")
fondecrantitre13=pygame.image.load("fond ecran titre13.png")
fondecrantitre14=pygame.image.load("fond ecran titre14.png")
fondecrantitre=[fondecrantitre1,fondecrantitre2,fondecrantitre3,fondecrantitre4,fondecrantitre5,fondecrantitre6,fondecrantitre7,
fondecrantitre8,fondecrantitre9,fondecrantitre10,fondecrantitre11,fondecrantitre12,fondecrantitre13,fondecrantitre14]
fondecranhight1=pygame.image.load("fond ecran hight1.png")
fondecranhight2=pygame.image.load("fond ecran hight2.png")
fondecranhight3=pygame.image.load("fond ecran hight3.png")
fondecranhight4=pygame.image.load("fond ecran hight4.png")
fondecranhight5=pygame.image.load("fond ecran hight5.png")
fondecranhight6=pygame.image.load("fond ecran hight6.png")
fondecranhight7=pygame.image.load("fond ecran hight7.png")
fondecranhight8=pygame.image.load("fond ecran hight8.png")
fondecranhight9=pygame.image.load("fond ecran hight9.png")
fondecranhight10=pygame.image.load("fond ecran hight10.png")
fondecranhight11=pygame.image.load("fond ecran hight11.png")
fondecranhight12=pygame.image.load("fond ecran hight12.png")
fondecranhight13=pygame.image.load("fond ecran hight13.png")
fondecranhight14=pygame.image.load("fond ecran hight14.png")
fondecranhight=[fondecranhight1,fondecranhight2,fondecranhight3,fondecranhight4,fondecranhight5,fondecranhight6,fondecranhight7,
fondecranhight8,fondecranhight9,fondecranhight10,fondecranhight11,fondecranhight12,fondecranhight13,fondecranhight14]




chargeur=police1.render(" ",30,(blanc))
iconchargeur=pygame.image.load("chargeur.png")
vieon=pygame.image.load('vie1.png')
vieoff=pygame.image.load('vie0.png')

bonusmissile=pygame.image.load("bonusmissile.png")
bonusvitesse=pygame.image.load("bonusvitesse.png")
bonusvie=pygame.image.load("bonusvie.png")

sol=pygame.image.load('Sol.png')
mur=pygame.image.load('Murv2.png')

maps=[[
[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],            ##colonne 1 de la premiére map
[0,1,1,0,1,1,1,1,1,0,0,1,0,1,1,1,1,0],
[0,1,1,0,0,0,0,0,1,0,0,1,0,1,1,1,1,0],
[0,1,1,1,1,1,1,0,1,0,0,1,0,1,0,0,0,0],
[0,1,1,1,1,1,1,0,1,1,1,1,0,1,0,1,1,1],            ##colonne 5
[0,0,0,0,0,1,1,0,0,0,0,0,0,1,0,1,0,0],
[1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,1,0,1],
[0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,1],
[0,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,0,1],
[0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,0,0,0],            ##colonne 10
[0,1,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,0],
[0,0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0],
[1,1,0,1,0,1,0,1,1,1,0,1,1,1,1,1,1,1],
[1,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,1,1,1,1,1,1,1,0,1,1,1,1,1],           ##colonne 15
[0,1,1,1,0,0,0,0,0,0,0,1,0,1,0,0,0,1],
[0,1,0,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1],
[0,1,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,0],
[0,1,0,1,1,1,0,1,1,1,0,1,0,1,1,1,0,1],
[0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1],          ##colonne 20
[0,1,0,0,0,1,1,1,1,1,1,1,1,1,1,0,1,1],
[0,1,1,1,0,1,0,0,0,0,0,0,0,1,1,0,1,1],
[0,0,0,1,0,1,0,1,1,1,1,1,0,1,1,0,1,1],
[1,1,0,1,0,1,0,1,0,0,0,0,0,1,1,0,1,1],
[0,0,0,0,0,0,0,1,0,1,1,1,0,0,0,0,0,1]],
[
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0],
[0,1,1,1,0,1,0,0,0,0,0,0,1,1,1,0,0,0],
[0,1,0,0,0,1,0,1,1,1,1,0,0,1,0,0,0,0],
[0,1,0,1,1,1,0,1,1,0,1,1,0,1,0,1,1,1],
[0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,1,0,0],
[0,1,0,1,1,1,1,1,1,0,1,1,0,1,0,1,0,1],
[0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,1],
[0,1,1,1,1,0,1,1,1,0,0,1,1,1,0,1,0,1],
[0,0,0,1,1,0,0,0,1,1,1,1,0,0,0,1,0,0],
[0,1,0,0,1,1,1,0,0,0,0,0,0,1,0,0,0,0],
[0,1,1,0,0,1,1,0,1,0,0,1,0,1,0,0,1,0],
[0,0,1,1,0,0,0,0,1,0,1,1,0,1,0,1,1,1],
[1,1,1,1,1,0,1,0,1,0,1,0,0,1,0,0,0,0],
[0,0,0,0,0,0,1,0,1,0,1,0,1,1,1,1,0,1],
[0,1,1,1,1,1,1,0,0,0,1,0,1,0,0,0,0,1],
[0,0,0,0,0,0,1,0,0,1,1,0,1,0,1,1,0,1],
[1,1,1,1,1,0,1,1,1,1,0,0,1,0,1,0,0,0],
[0,0,0,0,1,0,0,0,1,0,0,1,1,0,1,1,1,1],
[0,1,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,1],
[0,0,1,0,1,0,1,1,0,0,0,1,0,1,0,1,0,1],
[0,0,1,0,0,0,1,1,0,1,1,1,0,1,0,1,0,1],
[0,1,1,1,0,0,0,0,0,1,0,0,0,1,0,1,0,1],
[0,1,0,0,0,1,1,1,0,1,0,1,1,1,0,1,0,1],
[1,1,0,1,1,1,0,1,0,1,0,1,0,0,0,1,1,1]],
[
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,0],
[0,1,1,0,0,0,0,0,0,0,0,0,1,0,1,1,0,0],
[0,1,0,0,1,0,1,1,0,1,1,0,0,0,0,1,0,0],
[0,1,1,0,1,0,0,1,1,1,0,0,1,1,0,1,1,1],
[0,1,1,0,1,1,0,0,0,1,1,0,0,1,0,1,0,0],
[0,1,0,0,0,1,1,1,0,1,0,0,1,1,1,1,0,1],
[0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1],
[0,1,0,0,0,0,0,0,0,0,1,1,1,0,1,0,1,1],
[0,1,0,1,1,1,1,0,1,0,1,0,0,0,1,0,1,0],
[0,1,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0],
[0,1,0,1,1,1,0,1,1,0,1,0,1,0,1,0,0,0],
[0,1,0,1,0,1,0,0,1,1,1,0,1,0,1,1,1,1],
[0,0,0,1,0,1,1,0,1,0,0,0,1,0,0,0,0,0],
[1,0,0,0,0,0,1,0,1,0,1,0,1,1,1,1,0,1],
[1,1,0,1,0,1,1,0,1,1,1,0,0,0,1,1,0,1],
[1,1,0,1,1,1,1,0,1,1,1,1,1,0,0,1,0,1],
[1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,0,0],
[1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,1,1,1],
[0,0,1,0,1,0,1,0,1,0,1,0,0,1,0,0,0,1],
[0,0,1,0,1,0,1,0,1,0,1,1,0,1,0,0,1,1],
[0,0,1,0,1,0,1,0,1,0,0,1,0,1,1,0,0,1],
[0,1,1,0,1,1,1,0,1,1,0,0,0,1,1,1,0,1],
[0,1,0,0,0,1,0,0,0,1,1,1,1,1,0,0,0,1],
[0,1,1,1,1,1,0,1,0,0,0,0,0,1,1,1,1,1]],
[
[0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,1,0],
[0,1,1,1,0,0,0,1,0,1,1,1,1,1,1,0,1,0],
[0,1,0,1,1,1,0,1,0,0,1,0,0,0,1,1,1,0],
[0,1,0,0,0,1,0,1,1,0,1,0,1,0,0,1,0,0],
[0,1,0,1,0,1,0,0,0,0,0,0,1,0,1,1,0,1],
[0,1,1,1,0,1,1,1,1,0,1,1,1,0,1,1,0,0],
[0,0,0,1,0,1,0,1,0,0,0,0,1,0,0,1,0,1],
[1,1,0,1,0,0,0,1,1,1,1,0,1,0,1,1,0,1],
[0,0,0,1,1,1,0,1,0,0,1,1,1,0,1,1,0,1],
[0,1,0,0,1,1,0,1,0,0,0,0,1,0,0,1,0,0],
[0,1,1,0,1,1,0,1,0,1,1,0,1,1,0,1,1,0],
[0,0,1,0,1,0,0,1,0,1,1,0,1,1,0,1,0,0],
[1,1,1,0,1,0,1,1,0,1,0,0,1,1,0,1,0,0],
[0,0,0,0,1,0,0,0,0,1,1,0,0,1,0,1,0,1],
[0,1,1,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1],
[0,1,1,1,1,1,1,1,0,1,1,0,1,1,0,1,0,1],
[0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,1],
[1,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,0],
[1,1,0,0,0,0,0,1,0,1,0,1,0,1,1,0,0,1],
[0,1,0,1,1,0,1,1,0,0,0,1,0,0,0,0,1,1],
[0,1,1,1,1,0,0,1,0,1,0,1,1,1,1,0,1,1],
[0,1,1,0,1,1,1,1,0,1,0,0,0,0,1,0,1,1],
[0,0,1,0,0,0,0,1,0,1,1,1,1,1,1,0,0,1],
[1,0,1,1,1,1,0,1,0,0,0,0,0,1,1,1,1,1],
[1,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,1]],
[
[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
[0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,0],
[0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0],
[0,1,0,1,0,1,1,1,0,0,0,1,0,1,1,1,1,0],
[0,1,1,1,0,0,0,0,0,1,1,1,0,0,0,1,1,1],
[0,1,0,1,0,0,1,1,0,0,0,1,0,0,1,1,0,0],
[1,1,0,1,1,0,0,1,0,1,1,1,0,1,1,1,0,1],
[0,0,0,0,1,1,0,1,0,0,1,1,0,0,1,1,1,1],
[1,0,1,0,0,1,1,1,1,1,1,1,0,1,1,0,0,1],
[1,1,1,1,0,0,1,0,0,0,1,1,0,1,1,1,0,0],
[0,1,0,1,0,0,0,0,0,1,1,1,0,0,1,0,0,0],
[0,1,0,1,1,1,0,1,0,0,0,1,0,0,0,0,0,0],
[0,1,0,0,1,0,0,1,1,0,0,1,0,1,1,1,1,1],
[0,1,1,0,0,0,1,1,1,1,0,0,0,0,1,0,0,0],
[0,1,1,1,0,0,0,0,1,1,1,0,1,0,1,1,0,1],
[0,0,0,1,1,0,1,0,0,0,1,0,1,0,1,1,1,1],
[0,1,0,0,0,0,1,1,1,1,1,1,1,0,0,1,0,1],
[1,1,1,0,1,1,0,0,1,1,0,0,1,1,0,0,0,0],
[1,0,0,0,1,0,0,1,1,0,0,0,0,1,1,0,0,1],
[1,0,1,1,1,1,0,1,0,0,1,1,0,0,1,1,0,1],
[0,0,1,0,0,1,0,1,0,0,1,1,0,0,1,1,0,1],
[0,0,0,0,1,1,0,1,1,0,0,0,0,1,1,1,1,1],
[0,1,0,0,0,0,0,0,1,1,0,0,1,1,0,1,0,1],
[1,1,0,1,1,0,1,0,0,1,1,0,1,0,0,0,0,1],
[1,0,0,0,1,1,1,1,0,0,0,0,0,0,1,1,0,1]]]



def voisin(node):                                   #permet de trouver les voisins d'une case (4 direction)
    dirs = [[1,0],[-1,0],[0,1],[0,-1]]
    result = []
    for i in range (0,4):
        if node[0]+ dirs[i][0]>=0 and node[0]+ dirs[i][0]<50:
            if node[1]+dirs[i][1]>=0 and node[1]+dirs[i][1]<35:
                if labirynthe[node[0]+ dirs[i][0]][node[1]+dirs[i][1]]==0:
                    result.append([node[0]+ dirs[i][0],node[1]+dirs[i][1]])
    return result
def lumiere(a,b):                                           #fonction qui permet d'éclairer devant le joueur
    c=0
    d=0
    champsdevision1=7
    champsdevision2=7
    arret1=False
    arret2=False
    vision=[goal]
    if (goal[0]+1)<50:                                      #éclairer autour du joueur
        vision.append([(goal[0]+1),goal[1]])
    if (goal[0]-1)>-1:
        vision.append([(goal[0]-1),goal[1]])
    if (goal[1]+1)<35:
        vision.append([goal[0],(goal[1]+1)])
    if (goal[1]-1)>-1:
        vision.append([goal[0],(goal[1]-1)])
    while c<8:
        if (goal[0]+c*a+d*b)<50 and (goal[0]+c*a+d*b)>-1 and (goal[1]+b*c+d*a)<35 and (goal[1]+b*c+d*a)>-1:  #vérifier si c'est toujour sur l'écran
            if labirynthe[goal[0]+a*c+d*b][goal[1]+b*c+d*a] == 0:                                         #vérifier si la lumiere peut se propager
                for i in range(7-c):
                    if (goal[0]+a*i+c*a+d*b)<50 and (goal[0]+a*i+c*a+d*b)>-1 and (goal[1]+b*i+b*c+d*a)<35 and (goal[1]+b*i+b*c+d*a)>-1 and champsdevision1>=i:
                        if labirynthe[goal[0]+a*i+c*a+d*b][goal[1]+b*i+b*c+d*a]==0 and arret1==False:
                            if [(goal[0]+a*i+c*a+d*b),(goal[1]+b*i+b*c+d*a)] not in vision:
                                vision.append([(goal[0]+a*i+c*a+d*b),(goal[1]+b*i+b*c+d*a)])
                            if [(goal[0]+a*i+c*a+d*b+1*b),(goal[1]+b*i+b*c+d*a+1*a)] not in vision:
                                vision.append([(goal[0]+a*i+c*a+d*b+1*b),(goal[1]+b*i+b*c+d*a+1*a)])
                        elif arret1==False:
                            if [(goal[0]+a*i+c*a+d*b),(goal[1]+b*i+b*c+d*a)] not in vision:
                                vision.append([(goal[0]+a*i+c*a+d*b),(goal[1]+b*i+b*c+d*a)])
                            if [(goal[0]+a*i+c*a+d*b+1*b),(goal[1]+b*i+b*c+d*a+1*a)] not in vision:
                                vision.append([(goal[0]+a*i+c*a+d*b+1*b),(goal[1]+b*i+b*c+d*a+1*a)])
                            champsdevision1=i
                            break          #il y a un mur devant inutile de continuer ou en dehors de la map
                    else:
                        break
            else:
                arret1=True                       #si la lumiere ne peut plus se propager on arrete d'illuminer de ce côté
        else:
            arret1=True
        if (goal[0]+c*a-d*b)<50 and (goal[0]+c*a-d*b)>-1 and (goal[1]+b*c-d*a)<35 and (goal[1]+b*c-d*a)>-1:             #pareil mais de l'autre coté
            if labirynthe[goal[0]+a*c-d*b][goal[1]+b*c-d*a] == 0:                                                       # une symétrie
                for i in range(7-c):
                    if (goal[0]+a*i+c*a+d*b)<50 and (goal[0]+a*i+c*a+d*b)>-1 and (goal[1]+b*i+b*c+d*a)<35 and (goal[1]+b*i+b*c+d*a)>-1 and champsdevision2>=i:
                        if labirynthe[goal[0]+a*i+c*a-d*b][goal[1]+b*i+b*c-d*a]==0 and arret2==False:
                            if [(goal[0]+a*i+c*a-d*b),(goal[1]+b*i+b*c-d*a)] not in vision:
                                    vision.append([(goal[0]+a*i+c*a-d*b),(goal[1]+b*i+b*c-d*a)])
                            if [(goal[0]+a*i+c*a-d*b-1*b),(goal[1]+b*i+b*c-d*a-1*a)]not in vision :
                                vision.append([(goal[0]+a*i+c*a-d*b-1*b),(goal[1]+b*i+b*c-d*a-1*a)])
                        elif arret2==False:
                            if [(goal[0]+a*i+c*a-d*b),(goal[1]+b*i+b*c-d*a)] not in vision:
                                vision.append([(goal[0]+a*i+c*a-d*b),(goal[1]+b*i+b*c-d*a)])
                            if [(goal[0]+a*i+c*a*-d*b-1*b),(goal[1]+b*i+b*c-d*a-1*a)]not in vision :
                                vision.append([(goal[0]+a*i+c*a-d*b-1*b),(goal[1]+b*i+b*c-d*a-1*a)])
                            champsdevision2=i
                            break
                    else:
                        break
            else:
                arret2=True
        else :
            arret2=True
        if arret1 and arret2:
            return vision
        c+=1
        d+=1
def suprimerhightscore ():
    Hightscore=[0,0,0,0,0,0]
    Fichier = open('Hightscore.sav','wb')
    pickle.dump(Hightscore,Fichier)
    Fichier.close()

frontier=[]
start= [49,24]
tmarche=0
tmarche1=0
tmarche2=0


VienDe=[]
positionjoueur=[-1,-1]
def breadth_search(goal,Viende,start):                  #programme pour trouver le chemin de l'ia
    frontier=voisin(goal)
    Viende= []
    current=goal
    while True:
        for next in voisin(current):
            if next not in Viende:
                frontier.append(next)
                Viende.append(current)                  #Viende permet de savoir dans quelle case il faut aller pour arriver jusqu'au joueur
                Viende.append(next)
                if next==start:
                    return Viende                       #si on fini de trouver le chemin (attend l'ennemis(commencer par le joueur))

        current=[]
        if len(frontier)==0:                            #arreter si il n'y a plus de case a explorer
            break
        current=frontier.pop(0)
    if len(Viende)==0:
        Viende=[-1,-1]
        return Viende
while True:

    pygame.mixer.music.load("musique4.mp3")
    pygame.mixer.music.play()
    tanimfondecran=0
    tanimfondhight=0

    while MENU:
        tanimfondecran+=0.33

        if int(tanimfondecran)==14:
            tanimfondecran=0
        window.blit(fondecrantitre[int(tanimfondecran)],(0,0))
        for event in pygame.event.get():			# Traiter les évènements du clavier début
            if event.type== KEYDOWN:
                if event.key==K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key==K_UP:
                    curseur-=1
                if event.key==K_DOWN:
                    curseur+=1
                if event.key==K_SPACE and curseur==0:
                    MENU=False
                    TUTO1=True
                if event.key==K_SPACE and curseur==1:
                    MENU=False
                    TUTO2=True
        if curseur==-1:                         #déplacer le curseur et changer la couleur (il faut choisir le mode de jeu n°1 pour jouer)
            curseur=0
        if curseur==2:
            curseur=1
        if curseur==0 :
            tanimtitre1+=1
            if tanimtitre1==5:
                tanimtitre1=0
        else:
             tanimtitre1=0
        if curseur==1:
            tanimtitre2+=1
        else:
            tanimtitre2=0
        window.blit(animtitre1[tanimtitre1],(500,300))
        window.blit(titre21,(500,400))
        titrejeu=police2.render("Flee the Vampire",30,(rouge))
        info=police1.render("press space to select",170,(blanc))
        window.blit(titrejeu,(300,200))
        window.blit(info,(450,600))




        pygame.display.update()
        Clock.tick(30)
    while TUTO1:
        tanimfondecran+=0.33

        if int(tanimfondecran)==14:
            tanimfondecran=0
        window.blit(fondecrantitre[int(tanimfondecran)],(0,0))
        for event in pygame.event.get():			# Traiter les évènements du clavier début
            if event.type== KEYDOWN:
                if event.key==K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key==K_SPACE:
                    TUTO1=False
                    ChoixDif=True
        window.blit(bonusvitesse,(50,50))
        textbonusvitesse=police1.render("double votre vitesse temporairement",20,(blanc))
        window.blit(textbonusvitesse,(80,50))
        window.blit(iconchargeur,(50,105))
        textbonusmissile=police1.render("recharge votre arme",20,(blanc))
        window.blit(textbonusmissile,(80,100))
        texttirer=police1.render("press space to shoot",20,(blanc))
        window.blit(texttirer,(50,150))
        textskip=police1.render("press space to skip tuto",20,(blanc))
        window.blit(textskip,(50,200))


        pygame.display.update()
        Clock.tick(30)





    Dif="rien"

    while ChoixDif:
        tanimfondecran+=0.33

        if int(tanimfondecran)==14:
            tanimfondecran=0
        window.blit(fondecrantitre[int(tanimfondecran)],(0,0))
        textchoixdif=police2.render("Choix de la difficulté",20,(rouge))
        window.blit(textchoixdif,(100,100))

        for event in pygame.event.get():			# Traiter les évènements du clavier début
            if event.type== KEYDOWN:
                if event.key==K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key==K_UP:
                    curseur1-=1
                if event.key==K_DOWN:
                    curseur1+=1
                if event.key==K_q:
                    suprimerhightscore()
                if event.key==K_SPACE and curseur1==0:
                    ChoixDif=False
                    MODE1=True
                    Dif="easy"
                if event.key==K_SPACE and curseur1==1:
                    ChoixDif=False
                    MODE1=True
                    Dif="normal"
                if event.key==K_SPACE and curseur1==2:
                    ChoixDif=False
                    MODE1=True
                    Dif="hard"
                if event.key==K_SPACE and curseur1==3:
                    ChoixDif=False
                    MODE1=True
                    Dif="infini"
        if curseur1==-1:                         #déplacer le curseur et changer la couleur (il faut choisir le mode de jeu n°1 pour jouer)
            curseur1=0
        if curseur1==4:
            curseur1=3
        if curseur1==0 :
            textchoixfacile=police1.render("easy",20,(rouge))
            textchoixnormal=police1.render("normal",20,(blanc))
            textchoixdifficile=police1.render("hard",20,(blanc))
            textchoixinfini=police1.render("unlimited",20,(blanc))
            window.blit(textchoixfacile,(500,200))
            window.blit(textchoixnormal,(500,300))
            window.blit(textchoixdifficile,(500,400))
            window.blit(textchoixinfini,(500,500))
        if curseur1==1 :
            textchoixfacile=police1.render("easy",20,(blanc))
            textchoixnormal=police1.render("normal",20,(rouge))
            textchoixdifficile=police1.render("hard",20,(blanc))
            textchoixinfini=police1.render("unlimited",20,(blanc))
            window.blit(textchoixfacile,(500,200))
            window.blit(textchoixnormal,(500,300))
            window.blit(textchoixdifficile,(500,400))
            window.blit(textchoixinfini,(500,500))
        if curseur1==2 :
            textchoixfacile=police1.render("easy",20,(blanc))
            textchoixnormal=police1.render("normal",20,(blanc))
            textchoixdifficile=police1.render("hard",20,(rouge))
            textchoixinfini=police1.render("unlimited",20,(blanc))
            window.blit(textchoixfacile,(500,200))
            window.blit(textchoixnormal,(500,300))
            window.blit(textchoixdifficile,(500,400))
            window.blit(textchoixinfini,(500,500))
        if curseur1==3 :
            textchoixfacile=police1.render("easy",20,(blanc))
            textchoixnormal=police1.render("normal",20,(blanc))
            textchoixdifficile=police1.render("hard",20,(blanc))
            textchoixinfini=police1.render("unlimited",20,(rouge))
            window.blit(textchoixfacile,(500,200))
            window.blit(textchoixnormal,(500,300))
            window.blit(textchoixdifficile,(500,400))
            window.blit(textchoixinfini,(500,500))


        pygame.display.update()
        Clock.tick(30)


    y=[]
    if Dif=="easy" or Dif=="normal":
        quart1=0
        quart2=0
    else:
        quart1=random.randint(0,4)
        quart2=random.randint(0,4)
    labirynthe=maps[quart1]
    for c in range (0,25):                          #pour bloquer en haut à gauche et en bas à droite
        for l in range (0,17):
            labirynthe[24-c].append(maps[quart2][24-c][16-l])     #crée la map
        y=labirynthe[24-c][:]
        y.reverse()
        labirynthe.append(y)


    while TUTO2:
        tanimfondecran+=0.33

        if int(tanimfondecran)==14:
            tanimfondecran=0
        window.blit(fondecrantitre[int(tanimfondecran)],(0,0))
        for event in pygame.event.get():			# Traiter les évènements du clavier début
            if event.type== KEYDOWN:
                if event.key==K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key==K_SPACE:
                    TUTO2=False
                    MODE2=True
        window.blit(bonusvitesse,(50,50))
        textbonusvitesse=police1.render("double votre vitesse temporairement",20,(blanc))
        window.blit(textbonusvitesse,(80,50))
        window.blit(iconchargeur,(50,105))
        textbonusmissile=police1.render("donne 3 munitions suplémentaires",20,(blanc))
        window.blit(textbonusmissile,(80,100))
        texttire1=police1.render("press G to shoot for player 1",20,(blanc))
        window.blit(texttire1,(50,150))
        texttire2=police1.render("press 0 to shoot for player 2",20,(blanc))
        window.blit(texttire2,(50,200))
        textdeplace1=police1.render("pour le joueur 1 déplace toi avec Z,Q,S,D ",20,(blanc))
        window.blit(textdeplace1,(50,250))
        textdeplace2=police1.render("pour le joueur 2 déplace toi avec les flèches",20,(blanc))
        window.blit(textdeplace2,(50,300))
        textskip=police1.render("press space to skip tuto",20,(blanc))
        window.blit(textskip,(50,350))

        pygame.display.update()
        Clock.tick(30)
    tdebut=0
    t=0
    b=0
    b1=0
    b2=0
    a=0
    a1=0
    a2=0
    anciena=0
    ancienb=0
    xs=0						# coordonnées de départ du vaisseau
    ys=0
    xs1=980						# coordonnées de départ du vaisseau
    ys1=680
    xs2=0						# coordonnées de départ du vaisseau
    ys2=0
    vitesse=2                    #vitesse du joueur
    vitesse1=3
    vitesse2=3
    Bonus=[[1,0,0]]                                       #emplacement des bonus
    boost=False
    boost1=False
    boost2=False
    dureeboost=0
    dureeboost2=0
    dureeboost1=0

    NewHightscore=False
    chightscore=[blanc,blanc,blanc,blanc,blanc,blanc]
    CalculHightscore=True

    Time=0.0
    Visite=[]                                          #liste des lieux visité
    couleur1=(255,255,0)
    couleur2=(255,255,255)


    Gauche=False
    Droite=False
    Haut=False
    Bas=False
    gaucheia=False
    droiteia=False
    hautia=False
    basia=False
    pause1=False
    pause2=False
    stun=False

    stun1=False
    Gauche1=False
    Droite1=False
    Haut1=False
    Bas1=False

    stun2=False
    Gauche2=False
    Droite2=False
    Haut2=False
    Bas2=False

    joueur2=pygame.image.load('joueur1.1.png')
    joueur1=pygame.image.load('joueur1.2.png')
    joueur3=pygame.image.load('joueur1.3.png')
    joueur12=pygame.image.load('joueur3.1.png')
    joueur11=pygame.image.load('joueur3.2.png')
    joueur13=pygame.image.load('joueur3.3.png')
    joueur22=pygame.image.load('joueur2.1.png')
    joueur21=pygame.image.load('joueur2.2.png')
    joueur23=pygame.image.load('joueur2.3.png')
    animarche=[joueur1,joueur2,joueur3]
    animarche1=[joueur11,joueur12,joueur13]
    animarche2=[joueur21,joueur22,joueur23]
    marche=False
    marche1=False
    marche2=False
    ennemis1=pygame.image.load('ennemis2.1.png')
    ennemis2=pygame.image.load('ennemis2.2.png')
    ennemis3=pygame.image.load('ennemis2.3.png')
    iamarche=[ennemis1,ennemis2,ennemis3]
    marcheia=False
    tmarcheia=0
    angleactuia=0
    angleia=0
    ennemisvue=True


    missile=[]
    missile1=[]
    missile2=[]
    nombretire=0
    nombretire1=5
    nombretire2=5
    Missile=pygame.image.load("missile.png")
    rotationTirActu=0
    rotationTirActu1=0
    rotationTirActu2=0
    tTire1=0
    tTire2=0

    vie=3
    vie1=3
    vie2=3


    frontier=[]
    start= [49,24]
    tmarche=0
    tmarche1=0
    tmarche2=0



    xmilieu=0
    ymilieu=0
    xmilieu1=0
    ymilieu1=0
    xmilieu2=49
    ymilieu2=34
    angle=90
    angle1=90
    angle2=90
    anglevoulue=90
    anglevoulue1=90
    anglevoulue2=90

    attaque1=pygame.image.load("attaque1.png")
    attaque2=pygame.image.load("attaque2.png")
    attaque3=pygame.image.load("attaque3.png")
    attaqueia=False
    attaqueia2=False
    champsdevision=[]
    while MODE1:
        goal=[xmilieu,ymilieu]
        window.fill (0)
        if Dif=="easy":
            chrono=120
        elif Dif=="normal":
            chrono=180
        elif Dif=="hard":
            chrono=300
        elif Dif=="infini":
            chrono=int(time.clock()-tdebut)
        if tdebut==0:
            tdebut=time.clock()
            pygame.mixer.music.stop()
            pygame.mixer.music.load("musique.wav")
            pygame.mixer.music.play()

        if Dif!="infini":
            chrono=chrono-int(time.clock()-tdebut)

        azerty=time.strftime('%M:%S',time.gmtime(chrono))
        affichchrono=police1.render(azerty,30,(blanc))
        window.blit(affichchrono,(1050,100))

        tempsrest=police1.render("Temps:",30,(blanc))
        window.blit(tempsrest,(1050,50))
        if Dif!="infini":
            if chrono==0:
                FIN1=True
                MODE1=False


        for c in range(0,50):
            for l in range (0,35):
                if champsdevision!=[] and champsdevision!=None:                   #afficher les blocs seulement si dans la liste champs de vision
                    if [c,l] in champsdevision:
                        if labirynthe[c][l]==1:
                            window.blit(mur,(c*20,l*20))
                        if labirynthe[c][l]==0:
                            window.blit(sol,(c*20,l*20))
        if positionjoueur!=goal or anciena!=a or ancienb!=b:                #savoir si le champs de vision a changer
            champsdevision=lumiere(a,b)                                     # et donc de l'actualiser
            anciena=a
            ancienb=b

        if positionjoueur!=goal and t==0 and goal!=start:                   #savoir si la position du joueur a changer
            positionjoueur=goal                                             # et donc de l'actualiser
            VienDe=[]
            VienDe=breadth_search(goal,VienDe,start)
        elif t==0 and goal==start:                                          #si l'ennemis est sur la meme case que le joueur il attaque
            attaqueia=True
            window.blit(attaque1,(xs,ys))


        if goal not in Visite:                                              #minimap
            Visite.append([goal,0])
            for suivant in direction:
                apres=[(goal[0]+suivant[0]),(goal[1]+suivant[1])]
                if apres not in Visite and -1<apres[0]<50 and -1<apres[1]<35:
                    Visite.append([apres,labirynthe[apres[0]][apres[1]]])
        for casemini in Visite:
            if casemini[1]==0:
                window.blit(minisol,(1020+(casemini[0][0]*4),460+(casemini[0][1]*4)))
            else:
                window.blit(minimur,(1020+(casemini[0][0]*4),460+(casemini[0][1]*4)))



        if stun and Time==0.0 and t==0:
            Time=time.clock()
        elif stun and Time!=0.0:
            if time.clock()>=Time+10.0:
                if t==0:
                    stun=False
                    Time=0.0

        elif t==0 and pause1==False and pause2==False:
             for i in range(len(VienDe)):
                if VienDe[i]==start:                                    #trouver la case de l'ennemi
                    if VienDe[i-1]==goal:                                   #savoir si l'ennemis est a une case du joueur pour l'attaquer
                        attaqueia=True
                        window.blit(attaque1,(xs,ys))
                        break
                    if start==goal:
                        break
                    if VienDe[i-1][0]-start[0]<0:                           #savoir de quelle coté aller pour trouver le joueur
                        start[0]-= 0.125
                        gaucheia=True
                        angleia=90
                    if VienDe[i-1][0]-start[0]>0:
                        start[0]+=0.125
                        droiteia=True
                        angleia=-90
                    if VienDe[i-1][1]-start[1]<0:
                        start[1]-=0.125
                        hautia=True
                        angleia=0
                    if VienDe[i-1][1]-start[1]>0:
                        start[1]+=0.125
                        basia=True
                        angleia=180
                    else:
                        break
        elif t==0 and pause1 :
            pause1=False
            pause2=True
        elif t==0 and pause2:
            pause2=False

        else:
            if random.randint(0,200)==0:                                              #bonus sur la map
                randomc=random.randint(0,49)
                randoml=random.randint(0,34)
                if labirynthe[randomc][randoml]==0:
                    randombonus=random.randint(0,1)                                     #type de bonus
                    Bonus.append([randomc,randoml,randombonus])
            if t==1 and attaqueia:                                  #continuer l'anim de l'attaque
                window.blit(attaque2,(xs,ys))
                attaqueia=False
                attaqueia2=True
            if t==2 and attaqueia2:
                window.blit(attaque3,(xs,ys))
                attaqueia2=False
                pause1 =True
                vie-=1

            if gaucheia==True:                                      #continuer dans la meme direction jusqu'a la prochaine case
                start[0]-=0.125
            if droiteia==True:
                start[0]+=0.125
            if hautia==True:
                start[1]-=0.125
            if basia==True:
                start[1]+=0.125
        if t==7:
            t=-1
            gaucheia=False
            droiteia=False
            hautia=False
            basia=False
            attaqueia=False
        t+=1
        for bonus in Bonus:
            if bonus[2]==0:
                window.blit(bonusvitesse,(bonus[0]*20,bonus[1]*20))
            if bonus[2]==1:
                window.blit(bonusmissile,(bonus[0]*20,bonus[1]*20))
            if bonus[0:2]==goal:
                Bonus.remove(bonus)
                if bonus[2]==0:
                    vitesse+=2
                    boost=True
                if bonus[2]==1:
                    nombretire=0
        if boost:
            if dureeboost==100:
                boost=False
                dureeboost=-1
                vitesse-=2
            dureeboost+=1




        iamarche[0] = pygame.transform.rotate(iamarche[0],angleia-angleactuia)       #tourner les images a afficher en fonction de l'orientation du joueur
        iamarche[1] = pygame.transform.rotate(iamarche[1],angleia-angleactuia)
        iamarche[2] = pygame.transform.rotate(iamarche[2],angleia-angleactuia)
        angleactuia=angleia
        if Dif=="hard" and champsdevision!=None and t==0 :
            if start  not in champsdevision:
                ennemisvue=False
            else :
                ennemisvue=True
        elif t==0 :
            ennemisvue=True
        if ennemisvue:
            if marcheia:
                window.blit(iamarche[tmarcheia//10],(start[0]*20,start[1]*20))                      #afficher l'ennemis
            if tmarcheia==29:                             #animation de la marche
                tmarcheia=-1
            tmarcheia+=1
            if marcheia==False:
                window.blit(iamarche[1],(start[0]*20,start[1]*20))       #si le joueur ne bouge pas afficher l'anime où il ne bouge pas
                tmarcheia=0
            marcheia=True
            if stun:
                marcheia=False




        if nombretire == 0:                             #afficher les balles qui reste
            chargeur=police1.render("X3",30,(blanc))
            window.blit(iconchargeur,(1020,205))
            window.blit(chargeur,(1050,200))
        if nombretire == 1:
            chargeur=police1.render("X2",30,(blanc))
            window.blit(iconchargeur,(1020,205))
            window.blit(chargeur,(1050,200))
        if nombretire == 2:
            chargeur=police1.render("X1",30,(blanc))
            window.blit(iconchargeur,(1020,205))
            window.blit(chargeur,(1050,200))
        if nombretire == 3:
            chargeur=police1.render("X0",30,(blanc))
            window.blit(iconchargeur,(1020,205))
            window.blit(chargeur,(1050,200))



        if vie ==3:                                 # Vie debut
            window.blit(vieon,(1020,300))
            window.blit(vieon,(1050,300))
            window.blit(vieon,(1080,300))
        if vie == 2:
            window.blit(vieon,(1020,300))
            window.blit(vieon,(1050,300))
            window.blit(vieoff,(1080,300))
        if vie == 1:
            window.blit(vieon,(1020,300))
            window.blit(vieoff,(1050,300))
            window.blit(vieoff,(1080,300))

        if vie <= 0:
            window.blit(vieoff,(1020,300))
            window.blit(vieoff,(1050,300))
            window.blit(vieoff,(1080,300))
                    ##        print("TU ES MORT !")                   # Vie fin


        #positionjoueur = [xs, ys]
        positionxgaucheex=((xs+24)//20)                     #pour connaitre la position des pixels en case (la ligne de pixel en haut du perso
        positionxdroiteex=((xs-4)//20)                      # n'est pas forcement la même qua la ligne du bas
        positionyhautex=((ys+24)//20)
        positionybasex=((ys-4)//20)
        positionxgaucheint=((xs+8)//20)
        positionxdroiteint=((xs+13)//20)
        positionyhautint=((ys+8)//20)
        positionybasint=((ys+13)//20)
        xmilieu=((xs+9)//20)
        ymilieu=((ys+9)//20)
        goal=[xmilieu,ymilieu]

        for event in pygame.event.get():			# Traiter les évènements du clavier début
            if event.type== KEYDOWN:
                if event.key==K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key==K_RIGHT:
                    Droite = True
                if event.key==K_LEFT:
                    Gauche = True
                if event.key==K_UP:
                    Haut=True
                if event.key==K_DOWN:
                    Bas=True
                if event.key==K_s:
                    print("STOOOOOOOOOOP")                          # pour arreter le programme avec le mode dbg pas a pas
                    nombretire=0
                if event.key==K_z:
                    print("DEAD!!!!!!")
                    vie=0
                if event.key==K_SPACE and missile==[]: #tiré
                    if nombretire != 3:                     #tire limité
                        missile=pygame.Rect(xs+9,ys+9,6,16)
                        directiontirx=a
                        directiontiry=b
                        nombretire=nombretire+1

            if event.type== KEYUP:
                if event.key==K_RIGHT:
                    Droite = False
                if event.key==K_LEFT:
                    Gauche = False
                if event.key==K_UP:
                    Haut=False
                if event.key==K_DOWN:
                    Bas=False                       # Traiter les évènement du clavier fin

        if missile!=[]:
            missilexgauche=((missile.left)//20)
            missilexdroite=((missile.left+6)//20)
            missileyhaut=((missile.top)//20)
            missileybas=((missile.top+6)//20)
            if missilexgauche==int(start[0]) and missileybas==int(start[1]) or missilexdroite==int(start[0]) and missileyhaut==int(start[1]) or missilexdroite==int(start[0]) and missileybas==int(start[1]) or missilexgauche==int(start[0]) and missileyhaut==int(start[1]):                           #vérifier si le missile est en collision avec l'ennemis
                stun=True
                missile=[]



            elif directiontiry == -1:              #pour missileer en haut
                missileyfuture=missileyhaut-1
                if missileyfuture!=-1:
                    if labirynthe[missilexgauche][ missileyfuture]==1 or labirynthe[missilexdroite][missileyfuture]==1:				# si le missile touche un mur
                        missile=[]
                    else:
                        missile.top-=10				# soustraire 10 à la coordonnée du point haut
                        Missile=pygame.transform.rotate(Missile,0-rotationTirActu)
                        rotationTirActu=0
                        window.blit(Missile,missile)  # afficher le missile
                else:
                    missile=[]


            elif directiontiry == 1 :                #pour missileer en bas
                missileyfuture=missileybas+1
                if missileyfuture!=35:
                    if labirynthe[missilexgauche][ missileyfuture]==1 or labirynthe[missilexdroite][missileyfuture]==1:				# si le missile touche un mur
                        missile=[]
                    else:
                        missile.top+=10				# soustraire 10 à la coordonnée du point bas
                        Missile=pygame.transform.rotate(Missile,-180-rotationTirActu)
                        rotationTirActu=-180
                        window.blit(Missile,missile)  # afficher le missile
                else:
                    missile=[]


            elif directiontirx == 1 :                 #pour missileer à droite
                missilexfuture=missilexdroite+1
                if missilexfuture!=50:
                    if labirynthe[missilexfuture][ missileybas]==1 or labirynthe[missilexfuture][missileyhaut]==1:				# si le missile touche un mur
                        missile=[]
                    else:
                        missile.left+=10				# soustraire 10 à la coordonnée du point droite
                        Missile=pygame.transform.rotate(Missile,-90-rotationTirActu)
                        rotationTirActu=-90
                        window.blit(Missile,missile)  # afficher le missile
                else:
                    missile=[]



            elif directiontirx == -1 :                 #pour missileer à gauche
                missilexfuture=missilexgauche-1
                if missilexfuture!=-1:
                    if labirynthe[missilexfuture][ missileybas]==1 or labirynthe[missilexfuture][missileyhaut]==1:				# si le missile touche un mur
                        missile=[]
                    else:
                        missile.left-=10				# soustraire 10 à la coordonnée du point gauche
                        Missile=pygame.transform.rotate(Missile,90-rotationTirActu)
                        rotationTirActu=90
                        window.blit(Missile,missile)  # afficher le missile
                else:
                    missile=[]




        if Gauche and xs>0 :                                    #Colision gauche
            futurexs=positionxgaucheex-1
            if labirynthe[futurexs][positionybasint]==0:
                if labirynthe[futurexs][positionyhautint]==0:
                    xs-=vitesse
                    anglevoulue=180                             #l'angle d'orientation du perso dépend de la direction du déplasement du joueur
                    marche=True                                 #marche pour savoir si le joueur marche et donc faire une animation

        if Droite and xs<980 :                                  #Colision droite
            futurexs=positionxdroiteex+1
            if labirynthe[futurexs][positionybasint]==0:
                if labirynthe[futurexs][positionyhautint]==0:
                    xs+=vitesse
                    anglevoulue=0
                    marche=True

        if Haut and ys>0 :                                      #Colision haut
            futureys=positionyhautex-1
            if labirynthe[positionxdroiteint][futureys]==0:
                if labirynthe[positionxgaucheint][futureys]==0:
                    ys-=vitesse
                    anglevoulue=90
                    marche=True

        if Bas and ys<680 :                                     #Colision bas
            futureys=positionybasex+1
            if labirynthe[positionxdroiteint][futureys]==0:
                if labirynthe[positionxgaucheint][futureys]==0:
                    ys+=vitesse
                    anglevoulue=-90
                    marche=True

        animarche[0] = pygame.transform.rotate(animarche[0],anglevoulue-angle)       #tourner les images a afficher en fonction de l'orientation du joueur
        animarche[1] = pygame.transform.rotate(animarche[1],anglevoulue-angle)
        animarche[2] = pygame.transform.rotate(animarche[2],anglevoulue-angle)
        angle=anglevoulue
        if marche:
            window.blit(animarche[tmarche//10],(xs,ys))
        if tmarche==29:                             #animation de la marche
            tmarche=-1
        tmarche+=1
        if marche==False:
            window.blit(animarche[1],(xs,ys))       #si le joueur ne bouge pas afficher l'anime où il ne bouge pas
            tmarche=0
        marche=False
        if angle==0:                        #a correspond à droite ou gauche
            a=1
        elif angle==180:
            a=-1
        else:
            a=0
        if angle==90:                       #b correspond à haut ou bas
            b=-1
        elif angle==-90:
            b=1
        else:
            b=0
        if vie==0:    #ou temps
            if Dif!= "infini":
                MODE1=False
                FIN1=True
            else:
                MODE1= False
                EcranHightcsore=True

        pygame.display.update()
        Clock.tick(30)
    while FIN1:
        tanimfondecran+=0.33

        if int(tanimfondecran)==14:
            tanimfondecran=0
        window.blit(fondecrantitre[int(tanimfondecran)],(0,0))
        for event in pygame.event.get():			# Traiter les évènements du clavier début
            if event.type== KEYDOWN:
                if event.key==K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key==K_UP:
                    curseur-=1
                if event.key==K_DOWN:
                    curseur+=1
                if event.key==K_SPACE and curseur==0:
                    MENU=True
                    FIN1=False
                if event.key==K_SPACE and curseur==1:
                    ChoixDif=True
                    FIN1=False
        pygame.mixer.music.stop()
        if vie == 0:
            écriturefin1="tu as perdue"
        else:
            écriturefin1="tu as survécu"
        titrefin=police2.render(écriturefin1,30,(rouge))
        window.blit(titrefin,(300,200))
        info=police1.render("press space to select",170,(blanc))
        window.blit(info,(450,600))
        if curseur==0:
            couleur1=rouge
            couleur2=blanc
        if curseur==1:
            couleur1=blanc
            couleur2=rouge
        ecrit1fin1=police1.render("menu",30,(couleur1))
        ecrit2fin1=police1.render("rejouer",30,(couleur2))
        window.blit(ecrit1fin1,(500,300))
        window.blit(ecrit2fin1,(500,400))
        pygame.display.update()
        Clock.tick(30)
    while EcranHightcsore:
        tanimfondhight+=0.33

        if int(tanimfondhight)==14:
            tanimfondhight=0
        window.blit(fondecranhight[int(tanimfondhight)],(0,0))


        for event in pygame.event.get():			# Traiter les évènements du clavier début
            if event.type== KEYDOWN:
                if event.key==K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key==K_SPACE :
                    EcranHightcsore=False
                    FinHightscore=True

        if CalculHightscore:
            Fichier = open('Hightscore.sav','rb')
            Hightscore = pickle.load(Fichier)    # désérialisation
            Fichier.close()
            for i in range (0,6):
                if chrono > Hightscore[i]:
                    for k in range (0,5-i):
                        Hightscore[5-k]=Hightscore[4-k]
                    Hightscore[i]=chrono
                    NewHightscore=True
                    chightscore[i]=(0,0,0)
                    break
            Hightscore1=police1.render(time.strftime('%M:%S',time.gmtime(Hightscore[0])),30,(chightscore[0]))
            Hightscore2=police1.render(time.strftime('%M:%S',time.gmtime(Hightscore[1])),30,(chightscore[1]))
            Hightscore3=police1.render(time.strftime('%M:%S',time.gmtime(Hightscore[2])),30,(chightscore[2]))
            Hightscore4=police1.render(time.strftime('%M:%S',time.gmtime(Hightscore[3])),30,(chightscore[3]))
            Hightscore5=police1.render(time.strftime('%M:%S',time.gmtime(Hightscore[4])),30,(chightscore[4]))
            Hightscore6=police1.render(time.strftime('%M:%S',time.gmtime(Hightscore[5])),30,(chightscore[5]))
            CalculHightscore=False
            Fichier = open('Hightscore.sav','wb')
            pickle.dump(Hightscore,Fichier)    # sérialisation
            Fichier.close()
        if NewHightscore:
            titrefin=police2.render("tu as survécu "+azerty+" min",30,(rouge))
            titrenewhightscore=police2.render("NEW HIGHTSCORE!!!!",30,(rouge))
            window.blit(titrenewhightscore,(175,225))
        else:
            titrefin=police2.render("tu as survécu "+azerty+" min",30,(rouge))
        window.blit(Hightscore1,(560,342))
        window.blit(Hightscore2,(560,387))
        window.blit(Hightscore3,(560,431))
        window.blit(Hightscore4,(560,476))
        window.blit(Hightscore5,(560,520))
        window.blit(Hightscore6,(560,565))

        window.blit(titrefin,(100,150))
        pygame.display.update()
        Clock.tick(30)
    while FinHightscore:
        tanimfondecran+=0.33

        if int(tanimfondecran)==14:
            tanimfondecran=0
        window.blit(fondecrantitre[int(tanimfondecran)],(0,0))
        for event in pygame.event.get():			# Traiter les évènements du clavier début
            if event.type== KEYDOWN:
                if event.key==K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key==K_UP:
                    curseur-=1
                if event.key==K_DOWN:
                    curseur+=1
                if event.key==K_SPACE and curseur==0:
                    MENU=True
                    FinHightscore=False
                if event.key==K_SPACE and curseur==1:
                    ChoixDif=True
                    FinHightscore=False
        pygame.mixer.music.stop()
        info=police1.render("press space to select",170,(blanc))
        window.blit(info,(450,600))
        if curseur==0:
            couleur1=rouge
            couleur2=blanc
        if curseur==1:
            couleur1=blanc
            couleur2=rouge
        ecrit1fin1=police1.render("menu",30,(couleur1))
        ecrit2fin1=police1.render("rejouer",30,(couleur2))
        window.blit(ecrit1fin1,(500,300))
        window.blit(ecrit2fin1,(500,400))
        if NewHightscore:
            titrefin=police2.render("tu as survécu "+azerty+" min",30,(rouge))
        else:
            titrefin=police2.render("tu as survécu "+azerty+" min",30,(rouge))
        window.blit(titrefin,(100,200))
        pygame.display.update()
        Clock.tick(30)






































    while MODE2:
        window.fill(0)
        goal1=[xmilieu1,ymilieu1]
        goal2=[xmilieu2,ymilieu2]
        if tdebut==0:
            tdebut=time.clock()
            pygame.mixer.music.stop()
            pygame.mixer.music.load("musique3.mp3")
            pygame.mixer.music.play()


        try:
            for c in range(0,50):
                for l in range (0,35):
                    if labirynthe[c][l]==1:
                        window.blit(mur,(c*20,l*20))
                    if labirynthe[c][l]==0:
                        window.blit(sol,(c*20,l*20))
        except:
            print(c,l)
        if random.randint(0,50)==0:                                              #bonus sur la map
                randomc=random.randint(0,49)
                randoml=random.randint(0,34)
                if labirynthe[randomc][randoml]==0:
                    randombonus=random.randint(0,2)                                     #type de bonus
                    Bonus.append([randomc,randoml,randombonus])
        for bonus in Bonus:
            if bonus[2]==0:
                window.blit(bonusvitesse,(bonus[0]*20,bonus[1]*20))
            if bonus[2]==1:
                window.blit(bonusmissile,(bonus[0]*20,bonus[1]*20))
            if bonus[2]==2:
                window.blit(bonusvie,(bonus[0]*20,bonus[1]*20))
            if bonus[0:2]==goal1:
                Bonus.remove(bonus)
                if bonus[2]==0 and boost1==False:
                    vitesse1+=2
                    boost1=True
                elif bonus[2]==0:
                    dureeboost1=0
                if bonus[2]==1:
                    nombretire1+=3
                if bonus[2]==2:
                    if vie2<3:
                        vie2+=1
            if bonus[0:2]==goal2:
                Bonus.remove(bonus)
                if bonus[2]==0 and boost2==False:
                    vitesse2+=2
                    boost2=True
                elif bonus[2]==0:
                    dureeboost1=0
                if bonus[2]==1:
                    nombretire2+=3
                if bonus[2]==2:
                    if vie1<3:
                        vie1+=1
        if boost1:
            if dureeboost1==100:
                boost1=False
                dureeboost1=-1
                vitesse1-=2
            dureeboost1+=1
        if boost2:
            if dureeboost2==100:
                boost2=False
                dureeboost2=-1
                vitesse2-=2
            dureeboost2+=1

        strnombredetir2=("X"+str(nombretire2))                                                     #afficher les balles qui reste
        chargeur=police1.render(strnombredetir2,30,(blanc))
        window.blit(iconchargeur,(1020,155))
        window.blit(chargeur,(1050,150))


        strnombredetir1=("X"+str(nombretire1))                                                     #afficher les balles qui reste
        chargeur=police1.render(strnombredetir1,30,(blanc))
        window.blit(iconchargeur,(1020,330))
        window.blit(chargeur,(1050,325))








        if vie1 ==3:                                 # Vie debut du joueur1
            window.blit(vieon,(1020,200))
            window.blit(vieon,(1050,200))
            window.blit(vieon,(1080,200))
        if vie1 == 2:
            window.blit(vieon,(1020,200))
            window.blit(vieon,(1050,200))
            window.blit(vieoff,(1080,200))
        if vie1 == 1:
            window.blit(vieon,(1020,200))
            window.blit(vieoff,(1050,200))
            window.blit(vieoff,(1080,200))

        if vie1 <= 0:
            window.blit(vieoff,(1020,200))
            window.blit(vieoff,(1050,200))
            window.blit(vieoff,(1080,200))


        if vie2 ==3:                                 # Vie debut du joueur 2
            window.blit(vieon,(1020,300))
            window.blit(vieon,(1050,300))
            window.blit(vieon,(1080,300))
        if vie2 == 2:
            window.blit(vieon,(1020,300))
            window.blit(vieon,(1050,300))
            window.blit(vieoff,(1080,300))
        if vie2 == 1:
            window.blit(vieon,(1020,300))
            window.blit(vieoff,(1050,300))
            window.blit(vieoff,(1080,300))

        if vie2 <= 0:
            window.blit(vieoff,(1020,300))
            window.blit(vieoff,(1050,300))
            window.blit(vieoff,(1080,300))

        #positionjoueur = [xs1, ys1]
        positionxgaucheex1=((xs1+24)//20)                     #pour connaitre la position des pixels en case (la ligne de pixel en haut du perso1
        positionxdroiteex1=((xs1-4)//20)                      # n'est pas forcement la même qua la ligne du bas
        positionyhautex1=((ys1+24)//20)
        positionybasex1=((ys1-4)//20)
        positionxgaucheint1=((xs1+9)//20)
        positionxdroiteint1=((xs1+12)//20)
        positionyhautint1=((ys1+9)//20)
        positionybasint1=((ys1+12)//20)
        xmilieu1=((xs1+9)//20)
        ymilieu1=((ys1+9)//20)
        goal1=[xmilieu1,ymilieu1]


        positionxgaucheex2=((xs2+24)//20)                     #pour connaitre la position des pixels en case (la ligne de pixel en haut du perso2
        positionxdroiteex2=((xs2-4)//20)                      # n'est pas forcement la même qua la ligne du bas
        positionyhautex2=((ys2+24)//20)
        positionybasex2=((ys2-4)//20)
        positionxgaucheint2=((xs2+9)//20)
        positionxdroiteint2=((xs2+12)//20)
        positionyhautint2=((ys2+9)//20)
        positionybasint2=((ys2+12)//20)
        xmilieu2=((xs2+9)//20)
        ymilieu2=((ys2+9)//20)
        goal2=[xmilieu2,ymilieu2]


        for event in pygame.event.get():			# Traiter les évènements du clavier début
            if event.type== KEYDOWN:
                if event.key==K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key==K_RIGHT:
                    Droite1 = True
                if event.key==K_LEFT:
                    Gauche1 = True
                if event.key==K_UP:
                    Haut1=True
                if event.key==K_DOWN:
                    Bas1=True

                if event.key==K_d:
                    Droite2=True
                if event.key==K_a:
                    Gauche2=True
                if event.key==K_w:
                    Haut2=True
                if event.key==K_s:
                    Bas2=True                         # mouvement du joueur n°2
                if event.key==K_g and missile2==[]: #tiré
                    if nombretire2 >= 1 and tTire2+1<time.clock():                     #tire limité
                        missile2=pygame.Rect(xs2+9,ys2+9,6,16)
                        directiontirx2=a2
                        directiontiry2=b2
                        nombretire2=nombretire2-1
                        tTire2=time.clock()

                if event.key==K_KP0 and missile1==[]: #tiré
                    if nombretire1 >= 1 and tTire1+1<time.clock():                     #tire limité
                        missile1=pygame.Rect(xs1+9,ys1+9,6,16)
                        directiontirx1=a1
                        directiontiry1=b1
                        nombretire1=nombretire1-1
                        tTire1=time.clock()



            if event.type== KEYUP:
                if event.key==K_RIGHT:
                    Droite1 = False
                if event.key==K_LEFT:
                    Gauche1 = False
                if event.key==K_UP:
                    Haut1=False
                if event.key==K_DOWN:
                    Bas1=False                       # Traiter les évènement du clavier fin

                if event.key==K_d:
                    Droite2=False
                if event.key==K_a:
                    Gauche2=False
                if event.key==K_w:
                    Haut2=False
                if event.key==K_s:
                    Bas2=False

        if missile1!=[]:
            missilexgauche1=((missile1.left)//20)
            missilexdroite1=((missile1.left+6)//20)
            missileyhaut1=((missile1.top)//20)
            missileybas1=((missile1.top+6)//20)
            if missilexgauche1==int(goal2[0]) and missileybas1==int(goal2[1]) or missilexdroite1==int(goal2[0]) and missileyhaut1==int(goal2[1]) or missilexdroite1==int(goal2[0]) and missileybas1==int(goal2[1]) or missilexgauche1==int(goal2[0]) and missileyhaut1==int(goal2[1]):                           #vérifier si le missile est en collision avec l'ennemis
                vie1-=1
                missile1=[]



            elif directiontiry1 == -1:              #pour missileer en haut
                missileyfuture1=missileyhaut1-1
                if missileyfuture1!=-1:
                    if labirynthe[missilexgauche1][ missileyfuture1]==1 or labirynthe[missilexdroite1][missileyfuture1]==1:				# si le missile touche un mur
                        missile1=[]
                    else:
                        missile1.top-=10				# soustraire 10 à la coordonnée du point haut
                        Missile=pygame.transform.rotate(Missile,0-rotationTirActu)
                        rotationTirActu=0
                        window.blit(Missile,missile1)  # afficher le missile
                else:
                    missile1=[]


            elif directiontiry1 == 1 :                #pour missileer en bas
                missileyfuture1=missileybas1+1
                if missileyfuture1!=35:
                    if labirynthe[missilexgauche1][ missileyfuture1]==1 or labirynthe[missilexdroite1][missileyfuture1]==1:				# si le missile touche un mur
                        missile1=[]
                    else:
                        missile1.top+=10				# soustraire 10 à la coordonnée du point bas
                        Missile=pygame.transform.rotate(Missile,180-rotationTirActu)
                        rotationTirActu=180
                        window.blit(Missile,missile1)  # afficher le missile
                else:
                    missile1=[]


            elif directiontirx1 == 1 :                 #pour missileer à droite
                missilexfuture1=missilexdroite1+1
                if missilexfuture1!=50:
                    if labirynthe[missilexfuture1][ missileybas1]==1 or labirynthe[missilexfuture1][missileyhaut1]==1:				# si le missile touche un mur
                     missile1=[]
                    else:
                        missile1.left+=10				# soustraire 10 à la coordonnée du point droite
                        Missile=pygame.transform.rotate(Missile,-90-rotationTirActu)
                        rotationTirActu=-90
                        window.blit(Missile,missile1)  # afficher le missile
                else:
                    missile1=[]


            elif directiontirx1 == -1 :                 #pour missileer à gauche
                missilexfuture1=missilexgauche1-1
                if missilexfuture1!=-1:
                    if labirynthe[missilexfuture1][ missileybas1]==1 or labirynthe[missilexfuture1][missileyhaut1]==1:				# si le missile touche un mur
                        missile1=[]
                    else:
                        missile1.left-=10				# soustraire 10 à la coordonnée du point gauche
                        Missile=pygame.transform.rotate(Missile,90-rotationTirActu)
                        rotationTirActu=90
                        window.blit(Missile,missile1)  # afficher le missile
                else:
                    missile1=[]

        if missile2!=[]:
            missilexgauche2=((missile2.left)//20)
            missilexdroite2=((missile2.left+6)//20)
            missileyhaut2=((missile2.top)//20)
            missileybas2=((missile2.top+6)//20)
            if missilexgauche2==int(goal1[0]) and missileybas2==int(goal1[1]) or missilexdroite2==int(goal1[0]) and missileyhaut2==int(goal1[1]) or missilexdroite2==int(goal1[0]) and missileybas2==int(goal1[1]) or missilexgauche2==int(goal1[0]) and missileyhaut2==int(goal1[1]):                           #vérifier si le missile est en collision avec l'ennemis
                vie2-=1
                missile2=[]



            elif directiontiry2 == -1:              #pour missileer en haut
                missileyfuture2=missileyhaut2-1
                if missileyfuture2!=-1:
                    if labirynthe[missilexgauche2][ missileyfuture2]==1 or labirynthe[missilexdroite2][missileyfuture2]==1:				# si le missile touche un mur
                        missile2=[]
                    else:
                        missile2.top-=10				# soustraire 10 à la coordonnée du point haut
                        Missile=pygame.transform.rotate(Missile,0-rotationTirActu)
                        rotationTirActu=0
                        window.blit(Missile,missile2)  # afficher le missile
                else:
                    missile2=[]


            elif directiontiry2 == 1 :                #pour missileer en bas
                missileyfuture2=missileybas2+1
                if missileyfuture2!=35:
                    if labirynthe[missilexgauche2][ missileyfuture2]==1 or labirynthe[missilexdroite2][missileyfuture2]==1:				# si le missile touche un mur
                        missile2=[]
                    else:
                        missile2.top+=10				# soustraire 10 à la coordonnée du point bas
                        Missile=pygame.transform.rotate(Missile,180-rotationTirActu)
                        rotationTirActu=180
                        window.blit(Missile,missile2)  # afficher le missile
                else:
                    missile2=[]


            elif directiontirx2 == 1 :                 #pour missileer à droite
                missilexfuture2=missilexdroite2+1
                if missilexfuture2!=50:
                    if labirynthe[missilexfuture2][ missileybas2]==1 or labirynthe[missilexfuture2][missileyhaut2]==1:				# si le missile touche un mur
                        missile2=[]
                    else:
                        missile2.left+=10				# soustraire 10 à la coordonnée du point droite
                        Missile=pygame.transform.rotate(Missile,-90-rotationTirActu)
                        rotationTirActu=90
                        window.blit(Missile,missile2)  # afficher le missile
                else:
                    missile2=[]


            elif directiontirx2 == -1 :                 #pour missileer à gauche
                missilexfuture2=missilexgauche2-1
                if missilexfuture2!=-1:
                    if labirynthe[missilexfuture2][ missileybas2]==1 or labirynthe[missilexfuture2][missileyhaut2]==1:				# si le missile touche un mur
                        missile2=[]
                    else:
                        missile2.left-=10				# soustraire 10 à la coordonnée du point gauche
                        Missile=pygame.transform.rotate(Missile,90-rotationTirActu)
                        rotationTirActu=90
                        window.blit(Missile,missile2)  # afficher le missile
                else:
                    missile2=[]



        if Gauche1 and xs1>0 :                                    #Colision gauche
            futurexs1=positionxgaucheex1-1
            if labirynthe[futurexs1][positionybasint1]==0:
                if labirynthe[futurexs1][positionyhautint1]==0:
                    xs1-=vitesse1
                    anglevoulue1=180                             #l'angle d'orientation du perso dépend de la direction du déplasement du joueur
                    marche1=True                                 #marche pour savoir si le joueur marche et donc faire une animation

        if Droite1 and xs1<980 :                                  #Colision droite
            futurexs1=positionxdroiteex1+1
            if labirynthe[futurexs1][positionybasint1]==0:
                if labirynthe[futurexs1][positionyhautint1]==0:
                    xs1+=vitesse1
                    anglevoulue1=0
                    marche1=True

        if Haut1 and ys1>0 :                                      #Colision haut
            futureys1=positionyhautex1-1
            if labirynthe[positionxdroiteint1][futureys1]==0:
                if labirynthe[positionxgaucheint1][futureys1]==0:
                    ys1-=vitesse1
                    anglevoulue1=90
                    marche1=True

        if Bas1 and ys1<680 :                                     #Colision bas
            futureys1=positionybasex1+1
            if labirynthe[positionxdroiteint1][futureys1]==0:
                if labirynthe[positionxgaucheint1][futureys1]==0:
                    ys1+=vitesse1
                    anglevoulue1=-90
                    marche1=True

        animarche1[0] = pygame.transform.rotate(animarche1[0],anglevoulue1-angle1)       #tourner les images a afficher en fonction de l'orientation du joueur
        animarche1[1] = pygame.transform.rotate(animarche1[1],anglevoulue1-angle1)
        animarche1[2] = pygame.transform.rotate(animarche1[2],anglevoulue1-angle1)
        angle1=anglevoulue1
        if marche1:
            window.blit(animarche1[tmarche//10],(xs1,ys1))
        if tmarche==29:                             #animation de la marche
            tmarche=-1
        tmarche+=1
        if marche==False:
            window.blit(animarche1[1],(xs1,ys1))       #si le joueur ne bouge pas afficher l'anime où il ne bouge pas
            tmarche=0
        marche1=False
        if angle1==0:                        #a correspond à droite ou gauche
            a1=1
        elif angle1==180:
            a1=-1
        else:
            a1=0
        if angle1==90:                       #b correspond à haut ou bas
            b1=-1
        elif angle1==-90:
            b1=1
        else:
            b1=0






        if Gauche2 and xs2>0 :                                    #Colision gauche
            futurexs2=positionxgaucheex2-1
            if labirynthe[futurexs2][positionybasint2]==0:
                if labirynthe[futurexs2][positionyhautint2]==0:
                    xs2-=vitesse2
                    anglevoulue2=180                             #l'angle d'orientation du perso dépend de la direction du déplasement du joueur
                    marche2=True                                 #marche pour savoir si le joueur marche et donc faire une animation

        if Droite2 and xs2<980 :                                  #Colision droite
            futurexs2=positionxdroiteex2+1
            if labirynthe[futurexs2][positionybasint2]==0:
                if labirynthe[futurexs2][positionyhautint2]==0:
                    xs2+=vitesse2
                    anglevoulue2=0
                    marche2=True

        if Haut2 and ys2>0 :                                      #Colision haut
            futureys2=positionyhautex2-1
            if labirynthe[positionxdroiteint2][futureys2]==0:
                if labirynthe[positionxgaucheint2][futureys2]==0:
                    ys2-=vitesse2
                    anglevoulue2=90
                    marche2=True

        if Bas2 and ys2<680 :                                     #Colision bas
            futureys2=positionybasex2+1
            if labirynthe[positionxdroiteint2][futureys2]==0:
                if labirynthe[positionxgaucheint2][futureys2]==0:
                    ys2+=vitesse2
                    anglevoulue2=-90
                    marche2=True

        animarche2[0] = pygame.transform.rotate(animarche2[0],anglevoulue2-angle2)       #tourner les images a afficher en fonction de l'orientation du joueur
        animarche2[1] = pygame.transform.rotate(animarche2[1],anglevoulue2-angle2)
        animarche2[2] = pygame.transform.rotate(animarche2[2],anglevoulue2-angle2)
        angle2=anglevoulue2
        if marche2:
            window.blit(animarche2[tmarche2//10],(xs2,ys2))
        if tmarche2==29:                             #animation de la marche
            tmarche2=-1
        tmarche2+=1
        if marche2==False:
            window.blit(animarche2[1],(xs2,ys2))       #si le joueur ne bouge pas afficher l'anime où il ne bouge pas
            tmarche2=0
        marche2=False
        if angle2==0:                        #a correspond à droite ou gauche
            a2=1
        elif angle2==180:
            a2=-1
        else:
            a2=0
        if angle2==90:                       #b correspond à haut ou bas
            b2=-1
        elif angle2==-90:
            b2=1
        else:
            b2=0

        if vie1==0 or vie2==0:
            MODE2=False
            FIN2=True




        pygame.display.update()
        Clock.tick(30)
    while FIN2:
        tanimfondecran+=0.33

        if int(tanimfondecran)==14:
            tanimfondecran=0
        window.blit(fondecrantitre[int(tanimfondecran)],(0,0))
        for event in pygame.event.get():			# Traiter les évènements du clavier début
            if event.type== KEYDOWN:
                if event.key==K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key==K_UP:
                    curseur-=1
                if event.key==K_DOWN:
                    curseur+=1
                if event.key==K_SPACE and curseur==0:
                    MENU=True
                    FIN2=False
                if event.key==K_SPACE and curseur==1:
                    MODE2=True
                    FIN2=False
        pygame.mixer.music.stop()
        if vie1 == 0 and vie2!=0 :
            écriturefin2="joueur 2, tu as gagné"
        elif vie2==0 and vie1!=0:
            écriturefin2="joueur 1, tu as gagné"
        else :
            écriturefin2="égalité"
        titrefin2=police2.render(écriturefin2,30,(rouge))
        info=police1.render("press space to select",170,(blanc))
        window.blit(titrefin2,(200,200))
        window.blit(info,(450,600))
        if curseur==0:
            couleur1=(255,255,0)
            couleur2=(255,255,255)
        if curseur==1:
            couleur1=(255,255,255)
            couleur2=(255,255,0)
        ecrit1fin1=police1.render("menu",30,(couleur1))
        ecrit2fin1=police1.render("rejouer",30,(couleur2))
        window.blit(ecrit1fin1,(500,300))
        window.blit(ecrit2fin1,(500,400))


        pygame.display.update()
        Clock.tick(30)
