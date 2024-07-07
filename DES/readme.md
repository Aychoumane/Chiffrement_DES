Créateur : Ichou Aymane L3B ,  
Projet : Chiffrement DES 64 bits, mode ECB 

Ce projet a été codé en python car ce langage permet facilement la manipulation de liste,  et le typage dynamique m'a été fort utile et nécessaire pour la clarification du code. 
A la vue du nombre de table de permutation et substitution, je pense que ce langage est plus 
judicieux et apte pour ce problème.
Ce programme permet de chiffrer un message selon une clé donné ou non. 

Les seuls bibliothèques importés sont sys et random, sinon tout le reste a été fait par moi-même 

Fonctionnement : 

Un message est demandé à l'utilisateur, équivalent à 64 bits, soit 8 caractères ou moins. 
L'utilisateur choisi ensuite si il souhaite ou non, choisir la clé de chiffrement. 
	Si oui : 
		L'utilisateur entre sa propre clé en format texte, exemple : "pirate".
		La clé doit elle aussi faire 64 bits, soit 8 caractères ou moins.
	Si l'utilisateur choisi, de ne pas choisir de clé, une clé aléatoire est généré. 

Le message est ensuite chiffré en suivant l'algorithme de DES pour le chiffrer. 

Le résultat en bits, ainsi que le message dorénavant chiffré sont affichés à l'utilisateur. 


Fonctionnement approfondi : 
Une fois le message choisi, il est transformé en tableau de bits(64). Je procède à un bourrage de bits par la gauche, si le message n'est pas assez long. 
Le message subit une permutation initial. 
Le message est ensuite coupé en deux, de manière égal. 
On obtient donc g0 et d0, respectivement la partie gauche et la partie droite du message 

Cependant, nous devons obtenir les g et d suivant et ceux, jusqu'à 16, car il y a 16 tours de chiffrement afin de rendre le message assez sécurisé.

Si,  i un indice à un temps donné et i compris dans [1;16[  : 
gi+1 = di 
di+1 = gi XOR F(Di,Ki), K = clé de tour / F = Fonction de feisnell 

Fonction de feisnell :
	Dans cet algorithme, il est appliqué uniquement sur les parties droites du message. 
	Il consiste à étendre la partie droite du message grâce à une boîte d'expansion. 
	Appliquer un XOR entre la clé de tour et le message étendu 
	Une fonction de compression va venir scinder le tableau de 48 bits en 8 tableau de 6 bits 
	Ces sous tableaux vont passer dans l'ordre dans des sbox : 
		Le premier et dernier bit du sous tableau donne la ligne dans la Sbox en question en binaire
		Et le 2,3,4,5eme bit donne la colonne dans la Sbox, en binaire 
		On obtient donc une ligne et une colonne, qui va donner un nombre sur 4 bits(On passe de 6 à 4 bits)
		Et l'ensemble de ces sous tableaux vont ensuite etre concatener pour former un tableau de 32 bits 

	Ce tableau est ensuite soumis à une table de permutation. 

On fait enfin un XOR entre gi et ce tableau obtenu pour obtenir di+1 

Et on réitère ces opérations pendant 16 rounds, et à chaque round est clé de tour différente est utilisé.


Génération de clé de tour : 
Une première clé de 64 bits est décidé arbitrairement. 
Les bits de parités (8,16,24... ) sont retirés donnant une clé de 56 bits. 
Cette clé de 56 est divisé en 2 parties égales. 
Selon le tour, ces 2 parties subirement un shift par la gauche(le dernier bit->premier, le premier->2eme etc)
Elles sont ensuite recollés , puis passer dans une boite de compression pour donner une clé de taille 48 bits.
Ainsi est obtenu une premiere clé de tour , puis l'opération est réitéré sur les parties de la clés avant concaténation pour obtenir les 15 autres clés. 

A la fin, g15 et d15 (on commence de 0) sont concaténés. 
Puis passé dans une boite de permutation inverse, ainsi est obtenu le message chiffré. 


Remarque: 

Je n'ai pas pu trouver de site de chiffrement DES en ligne obtenant le même résultat que moi. 
J'ai d'ailleurs différencier plusieurs sites de chiffrement DES, en leurs appliquant les mêmes options de chiffrement , le même messsage ainsi que la même clé. Mais le chiffré obtenu diffère sur l'ensemble des sites.   
Ressources : 

Explication de l'algorithme DES : 
https://web.maths.unsw.edu.au/~lafaye/CCM/crypto/des.htm

Explication de la génération de clé : 
https://www.tutorialspoint.com/what-are-the-following-steps-for-the-key-generation-of-des-in-information-security

Informations générales sur DES en général et son fonctionnement : 

https://www.youtube.com/playlist?list=PLBlnK6fEyqRiOCCDSdi6Ok_8PU2f_nkuf
