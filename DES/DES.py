#Ichou Aymane 
#Projet DES , mode ECB 
#Code qu'un seul bloc  
import sys 
import random

#--------------------Variable globales------------------------------- 

_debug = False

_partie_gauche =   [58,  50,  42,  34,  26,  18,  10,  2,
                    60,  52,  44,  36,  28,  20,  12,  4,
                    62,  54,  46,  38,  30,  22,  14,  6,
                    64,  56,  48,  40,  32,  24,  16,  8]

_partie_droite =   [57,  49,  41,  33,  25,  17,  9 ,  1,
                    59,  51,  43,  35,  27,  19,  11,  3,
                    61,  53,  45,  37,  29,  21,  13,  5,
                    63,  55,  47,  39,  31,  23,  15,  7]

_tab_permut_init = [58 , 50 , 42 , 34 , 26 , 18 , 10 , 2 , 
                    60 , 52 , 44 , 36 , 28 , 20 , 12 , 4 ,
                    62 , 54 , 46 , 38 , 30 , 22 , 14 , 6 ,
                    64 , 56 , 48 , 40 , 32 , 24 , 16 , 8 ,
                    57 , 49 , 41 , 33 , 25 , 17 , 9  , 1 ,
                    59 , 51 , 43 , 35 , 27 , 19 , 11 , 3 , 
                    61 , 53 , 45 , 37 , 29 , 21 , 13 , 5 ,
                    63 , 55 , 47 , 39 , 31 , 23 , 15 , 7 ]

_tab32_permut =    [16 ,  7 ,  20,  21,  29,  12,  28,  17,
                    1  ,  15,  23,  26,  5 ,  18,  31,  10,
                    2  ,  8 ,  24,  14,  32,  27,  3 ,  9 ,
                    19 ,  13,  30,  6 ,  22,  11,  4 ,  25]

_inverse_permut =  [40 ,  8 , 48 , 16 , 56 , 24 , 64 , 32,
                    39 ,  7 , 47 , 15 , 55 , 23 , 63 , 31, 
                    38 ,  6 , 46 , 14 , 54 , 22 , 62 , 30, 
                    37 ,  5 , 45 , 13 , 53 , 21 , 61 , 29, 
                    36 ,  4 , 44 , 12 , 52 , 20 , 60 , 28,
                    35 ,  3 , 43 , 11 , 51 , 19 , 59 , 27, 
                    34 ,  2 , 42 , 10 , 50 , 18 , 58 , 26, 
                    33 ,  1 , 41 , 9  , 49 , 17 , 57 , 25]  

_expansion_table = [32 ,  1 ,  2 ,  3 ,  4 ,  5 , 
                     4 ,  5 ,  6 ,  7 ,  8 ,  9 , 
                     8 ,  9 , 10 , 11 , 12 , 13 , 
                    12 , 13 , 14 , 15 , 16 , 17 , 
                    16 , 17 , 18 , 19 , 20 , 21 , 
                    20 , 21 , 22 , 23 , 24 , 25 , 
                    24 , 25 , 26 , 27 , 28 , 29 , 
                    28 , 29 , 30 , 31 , 32 ,  1 ]  

_permut_32_bits =  [16 , 7  , 20 , 21 , 29 , 12 , 28 , 17,
                    1  , 15 , 23 , 26 , 5  , 18 , 31 , 10,
                    2  , 8  , 24 , 14 , 32 , 27 , 3  , 9 ,
                    19 , 13 , 30 , 6  , 22 , 11 , 4  , 25]
_sbox_1 = [
            [14 , 4 , 13 , 1 ,  2 , 15 , 11 ,  8 ,  3 , 10 ,  6 , 12 , 5 ,  9 ,  0 ,  7],
            [ 0 ,15 ,  7 , 4 , 14 ,  2 , 13 ,  1 , 10 ,  6 , 12 , 11 , 9 ,  5 ,  3 ,  8],
            [ 4 , 1 , 14 , 8 , 13 ,  6 ,  2 , 11 , 15 , 12 ,  9 ,  7 , 3 , 10 ,  5 ,  0],
            [15 ,12 ,  8 , 2 ,  4 ,  9 ,  1 ,  7 ,  5 , 11 ,  3 , 14 ,10 ,  0 ,  6 , 13]
          ]

_sbox_2 = [
            [15 , 1 ,  8 , 14 , 6 , 11 ,  3 ,  4 ,  9 ,  7 ,  2 , 13 ,12 ,  0 ,  5 , 10],
            [ 3 ,13 ,  4 ,  7 ,15 ,  2 ,  8 , 14 , 12 ,  0 ,  1 , 10 , 6 ,  9 , 11 ,  5],
            [ 0 ,14 ,  7 , 11 ,10 ,  4 , 13 ,  1 ,  5 ,  8 , 12 ,  6 , 9 ,  3 ,  2 , 15],
            [13 , 8 , 10 ,  1 , 3 , 15 ,  4 ,  2 , 11 ,  6 ,  7 , 12 , 0 ,  5 , 14 ,  9]
          ]

_sbox_3 = [
           [10,  0 ,  9 ,  14,  6 ,  3 ,  15,  5 ,  1 ,  13,  12,  7 ,  11,  4 ,  2 ,  8],
           [13,  7 ,  0 ,  9 ,  3 ,  4 ,  6 ,  10,  2 ,  8 ,  5 ,  14,  12,  11,  15,  1],
           [13,  6 ,  4 ,  9 ,  8 ,  15,  3 ,  0 ,  11,  1 ,  2 ,  12,  5 ,  10,  14,  7],
           [1 ,  10,  13,  0 ,  6 ,  9 ,  8 ,  7 ,  4 ,  15,  14,  3 ,  11,  5 ,  2 , 12]
          ]

_sbox_4 = [
           [7 ,  13,  14,  3 ,  0 ,  6 ,  9 ,  10,  1 ,  2 ,  8 ,  5 ,  11,  12,  4 , 15],
           [13,  8 ,  11,  5 ,  6 ,  15,  0 ,  3 ,  4 ,  7 ,  2 ,  12,  1 ,  10,  14,  9],
           [10,  6 ,  9 ,  0 ,  12,  11,  7 ,  13,  15,  1 ,  3 ,  14,  5 ,  2 ,  8 ,  4],
           [3 ,  15,  0 ,  6 ,  10,  1 ,  13,  8 ,  9 ,  4 ,  5 ,  11,  12,  7 ,  2 , 14]
          ]

_sbox_5 = [
           [2 ,  12,  4 ,  1 ,  7 ,  10,  11,  6 ,  8 ,  5 ,  3 ,  15,  13,  0 ,  14,  9],
           [14,  11,  2 ,  12,  4 ,  7 ,  13,  1 ,  5 ,  0 ,  15,  10,  3 ,  9 ,  8 ,  6],
           [4 ,  2 ,  1 ,  11,  10,  13,  7 ,  8 ,  15,  9 ,  12,  5 ,  6 ,  3 ,  0 , 14],
           [11,  8 ,  12,  7 ,  1 ,  14,  2 ,  13,  6 ,  15,  0 ,  9 ,  10,  4 ,  5 ,  3]
          ]

_sbox_6 = [
           [12,  1 ,  10,  15,  9 ,  2 ,  6 ,  8 ,  0 ,  13,  3 ,  4 ,  14,  7 ,  5 , 11],
           [10,  15,  4 ,  2 ,  7 ,  12,  9 ,  5 ,  6 ,  1 ,  13,  14,  0 ,  11,  3 ,  8],
           [9 ,  14,  15,  5 ,  2 ,  8 ,  12,  3 ,  7 ,  0 ,  4 ,  10,  1 ,  13,  11,  6],
           [4 ,  3 ,  2 ,  12,  9 ,  5 ,  15,  10,  11,  14,  1 ,  7 ,  6 ,  0 ,  8 , 13]
          ]

_sbox_7 = [ 
           [4 ,  11,  2 ,  14,  15,  0 ,  8 ,  13,  3 ,  12,  9,   7 ,  5 ,  10,  6 ,  1],
           [13,  0 ,  11,  7 ,  4 ,  9 ,  1 ,  10,  14,  3 ,  5,   12,  2 ,  15,  8 ,  6],
           [1 ,  4 ,  11,  13,  12,  3 ,  7 ,  14,  10,  15,  6,   8 ,  0 ,  5 ,  9 ,  2],
           [6 ,  11,  13,  8 ,  1 ,  4 ,  10,  7 ,  9 ,  5 ,  0,   15,  14,  2 ,  3 , 12]
          ]

_sbox_8 = [
           [13,  2 ,  8 ,  4 ,  6 ,  15,  11,  1 ,  10,  9 ,  3 ,  14,  5 ,  0 ,  12,  7],
           [1 ,  15,  13,  8 ,  10,  3 ,  7 ,  4 ,  12,  5 ,  6 ,  11,  0 ,  14,  9 ,  2],
           [7 ,  11,  4 ,  1 ,  9 ,  12,  14,  2 ,  0 ,  6 ,  10,  13,  15,  3 ,  5 ,  8],
           [2 ,  1 ,  14,  7 ,  4 ,  10,  8 ,  13,  15,  12,  9 ,  0 ,  3 ,  5 ,  6 , 11]          
          ]

all_sbox = []
all_sbox.append(_sbox_1)
all_sbox.append(_sbox_2)
all_sbox.append(_sbox_3)
all_sbox.append(_sbox_4)
all_sbox.append(_sbox_5)
all_sbox.append(_sbox_6)
all_sbox.append(_sbox_7)
all_sbox.append(_sbox_8)
#transforme la clé de 64 en 56 bits 
_CP1 = [
        57, 49,  41,  33,  25,  17,  9 ,  1 ,  58,  50,  42,  34,  26,  18,
        10,  2,  59,  51,  43,  35,  27,  19,  11,  3 ,  60,  52,  44,  36,
        63, 55,  47,  39,  31,  23,  15,  7 ,  62,  54,  46,  38,  30,  22,
        14,  6,  61,  53,  45,  37,  29,  21,  13,  5 ,  28,  20,  12,  4 ]

#transforme la subkey de 56 bits en 48 bits 
_CP2 = [
        14,  17,  11,  24,  1 ,  5 ,  3 ,  28,  15,  6 ,  21,  10,
        23,  19,  12,  4 ,  26,  8 ,  16,  7 ,  27,  20,  13,  2 ,
        41,  52,  31,  37,  47,  55,  30,  40,  51,  45,  33,  48,
        44,  49,  39,  56,  34,  53,  46,  42,  50,  36,  29,  32]

_number_of_shift = [1,1,2,2,
                    2,2,2,2,
                    1,2,2,2,
                    2,2,2,1]



#--------------------Fonctions---------------------------------------


#Prend un tableau source, un second tableau d'indice(meme taille que le tab source), et change les positions 
#Exemple si tableader[0] = 43 , tab_source echange son element position 0 avec son element postion 43 , V
def permut_tab(tab_source , tab_leader) : 
    res = [] 
    for i in range(0,len(tab_leader)): 
        res.append(tab_source[tab_leader[i]-1]) #Ne pas oublier -1, la permut table commence les positions a partir de 1
    return res 

def permut_tab_sans_1(tab_source , tab_leader) : 
    res = [] 
    for i in range(0,len(tab_leader)): 
        res.append(tab_source[tab_leader[i]]) #Ne pas oublier -1, la permut table commence les positions a partir de 1
    return res 


# Convertir l'objet 'bin' en une chaîne binaire (en supprimant le préfixe '0b'), V
def bin_to_bits(binary_obj):
    binary_string = str(binary_obj)
    binary_string = binary_string[2:]
    # print(binary_string)

    # Convertir la chaîne binaire en un tableau de bits
    bits = []
    for i in binary_string:
        bits.append(int(i))

    return bits

#Transforme un tableau de bits -> un nombre(int) || ecriture binaire (0b111) -> 7 , V
def bits_to_binary(tableau_des_bits):
    nombre_binaire = int(''.join(map(str, tableau_des_bits)), 2)
    # print("Le nombre binaire est :", nombre_binaire)
    # print(nombre_binaire)
    # print(type(nombre_binaire))
    return nombre_binaire 

#Prend un tableau de bits et le complete de bits à gauche jusqu'à la taille desiré , V
def bourrage_bits_left(tab_bits, taille_desire): 
    if(tab_bits == taille_desire):
        return tab_bits
    diff = taille_desire - len(tab_bits) 
    diff_tab = []
    for i in range(0,diff): 
        diff_tab.append(0)
    tab_bits = diff_tab + tab_bits
    return tab_bits

#Genere une clé de 64 bits, fait de 0 et 1 , V
def gen_main_key(taille) :
    key = []
    for i in range(0,taille) : 
        nombre_aleatoire = random.randint(0,1) 
        key.append(nombre_aleatoire) 
    return key 

#Genere une sous clé à partir d'une clé de 64 bits, et retire les bits de parité (8,16,24...), V
# def gen_sub_key(key): 
#     subkey = [] 
#     for i in range(0,len(key)) : 
#         if( i % 8 != 0 ) :
#             subkey.append(key[i-1])
#     return subkey

def subkey(key):
    subkey = permut_tab(key,_CP1)
    return subkey

def gen_round_key(key): 
    round_keys = []
    subkey = permut_tab(key,_CP1)
    left_part = subkey[0:28]
    right_part= subkey[28:56]

    for i in range(0,16):
        left_part = list_shift_gauche(left_part)
        right_part= list_shift_gauche(right_part)
        if(_number_of_shift[i] == 2):
            left_part = list_shift_gauche(left_part)
            right_part= list_shift_gauche(right_part)

        entire_temp_key = left_part + right_part 
        entire_temp_key = permut_tab(entire_temp_key,_CP2)
        round_keys.append(entire_temp_key)

    return round_keys


#Fais un shift gauche dans une liste de bits , V
def list_shift_gauche(tab_bits):
    premier_bit = tab_bits[0]
    tab_bits.pop(0)
    tab_bits.append(premier_bit)
    return tab_bits

#Fais un shift droit dans une liste de bits , V
def list_shift_droit(tab_bits) : 
    tab_bits.pop(-1)
    liste = [0]
    tab_bits = liste + tab_bits
    return tab_bits

#Fonction annexe pour créer une sortie(deboggage), V
def stop(): 
    print("Une erreur s'est produite")
    sys.exit()

#Fonction annexe pour créer un tableau de 0 à "longueur", V
def tab_test(longeur):
    res = []
    for i in range(0,longeur):
        res.append(i)
    return res 

#Fonction annexe de deboggage, pour compter le nombre de 1 au sein d'un tab bits, et renvoie la value
def nb_1(tab_bits): 
    compteur = 0 
    for i in tab_bits:
        if(i == 1):
            compteur +=1
    return compteur

#Fonction qui effectue un XOR logique(ou exclusif), entre deux bits données , V
def XOR(bit_0 , bit_1): 
    if (bit_0 > 1 or bit_1> 1):
        stop()
    if(bit_1 == bit_0):
        return 0 
    else:
        return 1 

#Fonction qui fait le XOR bit à bit entre deux tableaux de bits 
def apply_XOR(expanded_message , act_round_key) : 
    res = []
    for i in range(0,len(expanded_message)):
        res.append(XOR(expanded_message[i], act_round_key[i]))
    return res 

#Fonction qui prend un tableau de 48 bits et le decoupes en tableau de 6 bits 
def decouper_tableau(tab_48b):
    decoupes = []
    for i in range(0, len(tab_48b), 6):
        decoupes.append(tab_48b[i:i+6])
    
    return decoupes

def tab6_to_sbox(indice_sbox,tab):
    ligne = []
    ligne.append(tab[0])
    ligne.append(tab[-1])

    colonne= []
    colonne.append(tab[1])
    colonne.append(tab[2])
    colonne.append(tab[3])
    colonne.append(tab[4])

    ligne = bits_to_binary(ligne)
    #print("ligne->",ligne)
    colonne = bits_to_binary(colonne)
    #print("colonne->",colonne)
    res = all_sbox[indice_sbox][ligne][colonne]
    res = bin(res)
    res = bin_to_bits(res)
    res = bourrage_bits_left(res,4)
    return res 

def string_to_bits_tab(text): 
    res = []
    #ord(x) , donne l'ascii de x 
    for char in text:
        #print(char)
        temp = char
        temp = ord(temp)
        temp = bin(temp)
        temp_en_bits = bin_to_bits(temp)
        temp_en_bits = bourrage_bits_left(temp_en_bits,8)
        res = res + temp_en_bits
    #print("longeuur",len(res))
    return res 


def bits_to_string(bit_tab) : 
    mot = ""
    for i in range(0,64,8):
        temp = bit_tab[i:i+8]
        #print("temp vaut :", temp)
        mot = mot + chr(bits_to_binary(temp))
    return mot 


# --------------Main------------------------- 

#Demande et traitement du message 
message = input("Entrer un message de 8 caractères ou moins: \n")
message = str(message)
while(len(message) >8):
    print("Le message entré est trop long, recommencez !")
    message = input("Entrer un message de 8 caractères ou moins: \n")
    message = str(message)

print("Le message choisi est :", message)
message_en_bits = string_to_bits_tab(message)
message_en_bits = bourrage_bits_left(message_en_bits,64)


#gen key 
choix = input("Voulez vous choisir la clé ?\n0 -> Non / 1 -> Oui \n")
choix = int(choix)
while(choix > 1 or choix < 0 ):
    print("Entrer une valeur valide (0 ou 1)")
    choix = int(input(""))

if(choix == 1): 
    print("----Choix de clé arbitraire----")
    cle = input("Entrer une clé de 8 caractères ou moins: \n")
    cle = str(cle)
    while(len(cle) >8):
        print("Le clé entré est trop longue, recommencez !")
        cle = input("Entrer une clé de 8 caractères ou moins: \n")
        cle = str(cle)

    print("Le clé choisi est :", cle)
    cle_en_bits = string_to_bits_tab(cle)
    main_key = bourrage_bits_left(cle_en_bits,64)
    

if(choix == 0):
    print("----Choix de clé aléatoire----") 
    main_key = gen_main_key(64)
    

#first_subkey = subkey(main_key)
r_keys = gen_round_key(main_key)

#Permutation initiale 
message_en_bits_permute = permut_tab(message_en_bits, _tab_permut_init) 

#Separation en deux du message 
g0 = permut_tab(message_en_bits_permute,_partie_gauche)
d0 = permut_tab(message_en_bits_permute,_partie_droite)
g_list = [] 
d_list = [] 
g_list.append(g0)
d_list.append(d0)

#Rounds de chiffrement , le round 0 est l'initialisation (gen_key et separation du message)
for i in range(1,16): 
        #Expansion 
    d_act = d_list[i-1] 
    d_act = permut_tab(d_act, _expansion_table)

        #XOR du message avec la clé de tour 
    d_act = apply_XOR(d_act,r_keys[i-1])
    #print("d_act :", len(d_act))

        #Scindement en 8 blocs de 6 bits
    d_act_coupe = decouper_tableau(d_act)
    if (_debug):
        print("len: ", len(d_act_coupe))
        print(d_act_coupe)
        #1er et dernier bit donne la ligne , les 2/3/4/5 bit donne la colonne
    passage_sbox = []

    for n in range(0,8): 
        if (_debug):
            print("n vaut :",n)
            print("d_act_coupe : ", d_act_coupe[n])

        passage_sbox = passage_sbox + tab6_to_sbox(n, d_act_coupe[n])

    if(_debug):
        print(passage_sbox)

    #Derniere permutation 
    passage_sbox = permut_tab(passage_sbox , _permut_32_bits)

    #Application du XOR 
    passage_sbox = apply_XOR(passage_sbox,g_list[i-1]) #Obtention de D1 

    #Ajout dans la liste(utile pour le dechiffremement)
    d_list.append(passage_sbox)
    g_list.append(d_list[i-1])
    

#Concatenation des derniers elements de chaque liste 
message_chiffre = g_list[15] + d_list[15]
message_chiffre = permut_tab(message_chiffre, _inverse_permut)

print("----Message chiffré en bit----")
print(message_chiffre)
print("------------------------------")
print("Le message chiffré est :", bits_to_string(message_chiffre))


