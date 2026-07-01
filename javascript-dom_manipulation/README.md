# JavaScript - DOM Manipulation
 
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow)
![Holberton](https://img.shields.io/badge/Holberton-School-red)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
 
## Description du projet
 
Ce projet est une introduction à la manipulation du DOM (Document Object Model) en JavaScript. L'objectif est d'apprendre à sélectionner, modifier et interagir avec les éléments HTML d'une page directement depuis un script JS, sans jamais recharger la page.
 
Le projet couvre également l'utilisation de la **Fetch API** pour récupérer des données depuis des serveurs distants (API Star Wars et API de traduction) et les afficher dynamiquement dans le DOM.
 
---
 
## Objectifs pédagogiques
 
A la fin de ce projet, je suis capable d'expliquer sans aide extérieure :
 
* Comment sélectionner des éléments HTML en JavaScript
* Les différences entre les sélecteurs par ID, par classe et par balise
* Comment modifier le style CSS d'un élément HTML
* Comment récupérer et mettre à jour le contenu d'un élément HTML
* Comment modifier la structure du DOM (ajouter des éléments)
* Comment faire une requête avec `XmlHTTPRequest`
* Comment faire une requête avec la `Fetch API`
* Comment écouter et réagir aux événements du DOM
* Comment écouter et réagir aux événements utilisateur (clic, chargement de page...)
---
 
## Prérequis
 
* Navigateur Chrome, version 57.0 ou supérieure
* Editeurs autorisés : n'importe lequel
* Code conforme au style **semistandard**
* Interdiction d'utiliser `var` (uniquement `let` et `const`)
* Aucun rechargement de page autorisé pour effectuer une action
---
 
## Structure du projet
 
| Fichier | Description |
| --- | --- |
| `0-script.js` | Change la couleur du texte du `header` en rouge |
| `1-script.js` | Change la couleur du `header` en rouge au clic sur `red_header` |
| `2-script.js` | Ajoute la classe `red` au `header` au clic sur `red_header` |
| `3-script.js` | Bascule entre les classes `red` et `green` sur le `header` |
| `4-script.js` | Ajoute un élément `li` à une liste au clic sur `add_item` |
| `5-script.js` | Change le texte du `header` au clic sur `update_header` |
| `6-script.js` | Récupère le nom d'un personnage Star Wars via l'API et l'affiche |
| `7-script.js` | Récupère et liste les titres des films Star Wars via l'API |
| `8-script.js` | Récupère une traduction du mot "hello" via une API externe |
 
Chaque script est associé à un fichier `X-main.html` permettant de le tester directement dans le navigateur.
 
---
 
## Concepts clés utilisés
 
### Sélection d'éléments
 
```javascript
document.querySelector('header');       // par balise
document.querySelector('#red_header');  // par ID
document.querySelector('.my_list');     // par classe
```
 
`querySelector` fonctionne avec n'importe quel sélecteur CSS, ce qui le rend plus flexible que `getElementById` ou `getElementsByClassName`.
 
### Modification du style
 
```javascript
element.style.color = '#FF0000';
```
 
### Gestion des classes
 
```javascript
element.classList.add('red');
element.classList.toggle('red');
element.classList.toggle('green');
```
 
### Modification du contenu
 
```javascript
element.textContent = 'New Header!!!';
```
 
### Création et ajout d'éléments
 
```javascript
const li = document.createElement('li');
li.textContent = 'Item';
parent.appendChild(li);
```
 
### Ecoute d'événements
 
```javascript
element.addEventListener('click', () => {
  // action à exécuter
});
```
 
### Requêtes avec Fetch API
 
```javascript
fetch(url)
  .then((response) => response.json())
  .then((data) => {
    // traitement des données
  });
```
 
La Fetch API repose sur les **Promises**, un mécanisme permettant de gérer des opérations asynchrones (comme une requête réseau) sans bloquer l'exécution du reste du code.
 
---
 
## Ce que j'ai appris
 
* Le DOM représente la page HTML sous forme d'arbre d'objets manipulables en JavaScript
* Il existe plusieurs façons de sélectionner un élément, mais `querySelector` est la plus polyvalente car elle accepte n'importe quel sélecteur CSS
* Manipuler le DOM permet de rendre une page interactive sans rechargement
* Les événements (`click`, `DOMContentLoaded`...) permettent de déclencher du code en réaction aux actions de l'utilisateur ou à l'état de la page
* La Fetch API simplifie grandement les appels réseau par rapport à `XmlHTTPRequest`, grâce aux Promises et à la syntaxe `.then()`
* Un script placé dans le `<head>` s'exécute avant que le DOM soit chargé, il faut donc attendre l'événement `DOMContentLoaded` avant de manipuler des éléments
---
 
## Auteur
 
Projet réalisé dans le cadre du cursus Holberton School, projet original par Javier Valenzani.