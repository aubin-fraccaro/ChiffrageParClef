# Programme de Chiffrement Affine
Documentation rédigée par claude.ai et non par moi même
## Description

Ce programme Python implémente un chiffrement affine, une méthode de chiffrement par substitution mono-alphabétique où chaque lettre est transformée selon la formule : `(ax + b) mod 26`, où x est la position de la lettre dans l'alphabet.

## Fonctionnalités

* Chiffrement d'un caractère unique
* Chiffrement d'un mot complet
* Interface utilisateur en ligne de commande
* Support des lettres majuscules (saisie peut être en minuscules)

## Prérequis

* Python 3.x

## Installation

Clonez ce dépôt ou téléchargez le fichier source directement. Aucune dépendance externe n'est requise.

## Utilisation

Exécutez le programme en utilisant Python :

```bash
python chiffrement.py
```

Le programme propose deux options :

1. Coder un caractère unique
2. Coder un mot complet

### Paramètres de chiffrement

Pour les deux options, vous devrez fournir :

* La valeur de `a` (multiplicateur)
* La valeur de `b` (décalage)

### Exemples d'utilisation

#### Pour chiffrer un caractère

1. Choisissez l'option 1
2. Entrez les valeurs de `a` et `b`
3. Saisissez la lettre à chiffrer

#### Pour chiffrer un mot

1. Choisissez l'option 2
2. Entrez les valeurs de `a` et `b`
3. Saisissez votre mot lettre par lettre
4. Tapez 'fin' pour terminer la saisie

## Structure du code

Les fonctions principales sont :

* `ClearScreen()` : Nettoie l'affichage
* `coderchr(a,b,lettreAchiffer)` : Effectue le chiffrement d'un caractère
* `CoderUnMot()` : Gère le chiffrement d'un mot complet

## Notes techniques

* Le programme utilise les codes ASCII (65-90) pour les lettres majuscules
* La formule de chiffrement est : `(a * x + b) mod 26`
* Les entrées sont automatiquement converties en majuscules

## Limitations

* Ne gère que les lettres majuscules de l'alphabet (A-Z)
* Ne prend pas en charge les caractères spéciaux ou les espaces



