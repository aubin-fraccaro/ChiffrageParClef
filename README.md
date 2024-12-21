# Chiffrement de Caractères et de Mots

Ce programme en Python permet de chiffrer des caractères et des mots en utilisant une méthode de chiffrement basée sur des coefficients `a` et `b`. Le chiffrement est effectué en transformant chaque lettre en une nouvelle lettre selon une formule mathématique.

## Fonctionnalités

- **Chiffrement de Caractères** : Chiffre un caractère unique en utilisant les coefficients `a` et `b`.
- **Chiffrement de Mots** : Chiffre un mot entier en utilisant les coefficients `a` et `b`.
- **Menu Principal** : Permet à l'utilisateur de choisir entre chiffrer un caractère ou un mot.

## Comment Utiliser

1. **Démarrer le Programme** : Exécutez le programme. Le menu principal s'affichera avec les options de chiffrement.
2. **Choisir une Option** : Entrez `1` pour chiffrer un caractère ou `2` pour chiffrer un mot.
3. **Entrer les Coefficients** : Entrez les valeurs des coefficients `a` et `b`.
4. **Entrer le Caractère ou le Mot** : Entrez le caractère ou le mot à chiffrer.
5. **Obtenir le Résultat** : Le programme affichera le caractère ou le mot chiffré.

## Aperçu du Code

### Fonctions

- **coderchr** : Chiffre un caractère unique en utilisant les coefficients `a` et `b`.
  - **Paramètres** :
    - `a` : Coefficient `a`.
    - `b` : Coefficient `b`.
    - `lettreAchiffer` : Le caractère à chiffrer.
  - **Retourne** : Le caractère chiffré.

- **CoderUnMot** : Chiffre un mot entier en utilisant les coefficients `a` et `b`.
  - **Fonctionnement** :
    - Demande à l'utilisateur d'entrer le mot lettre par lettre.
    - Chiffre chaque lettre en utilisant la fonction `coderchr`.
    - Affiche le mot chiffré.

### Fonctionnement

1. **Initialisation** : Le programme affiche le menu principal avec les options de chiffrement.
2. **Choix de l'Utilisateur** :
   - Si l'utilisateur choisit de chiffrer un caractère (option `1`), le programme demande les coefficients `a` et `b`, ainsi que le caractère à chiffrer, puis affiche le caractère chiffré.
   - Si l'utilisateur choisit de chiffrer un mot (option `2`), le programme demande les coefficients `a` et `b`, puis appelle la fonction `CoderUnMot` pour chiffrer le mot entier.
3. **Chiffrement** :
   - Pour un caractère, la fonction `coderchr` est utilisée pour chiffrer le caractère.
   - Pour un mot, la fonction `CoderUnMot` demande à l'utilisateur d'entrer le mot lettre par lettre, chiffre chaque lettre en utilisant `coderchr`, et affiche le mot chiffré.

