<!---
IMPORTANT
=========
This README.md is displayed in the WebStore as well as within Jarvis app
Please do not change the structure of this file
Fill-in Description, Usage & Author sections
Make sure to rename the [en] folder into the language code your plugin is written in (ex: fr, es, de, it...)
For multi-language plugin:
- clone the language directory and translate commands/functions.sh
- optionally write the Description / Usage sections in several languages
-->
## Description:
Plugin pour [Jarvis](https://github.com/alexylem/jarvis)

Celui ci permet de controler vos lumières [lifx](http://www.lifx.com/)

## Usage:
* [ALLUME LA LUMIERE]
* [ETEINT LA LUMIERE]
* [INFO*LUMIERE]
* [AUGMENTE*LUMIERE] [Couleur] [Label_lifx] [Power]
* [DIMINUE*LUMIERE] [Couleur] [Label_lifx] [Power]
* [LUMIERE] [Couleur] [Label_lifx] [Power]

## Example:
```
Vous: Jarvis, eteint la lumiere
Jarvis: J'eteint la lumiere

Vous: J'aimerais bien avoir une lumière bleu mais seulement à 60 pourcents
Jarvis: J'allume la lumiere en bleu avec une intensite de 60 pourcents

Vous: finalement met la lumière à 75 % en vert
Jarvis: J'allume la lumiere en vert avec une intensite de 75 pourcents

Vous: change pour une lumière aléatoire
Jarvis: J'allume la lumiere avec une couleur aleatoire qui sera blanc chaud

Vous: une autre lumière aléatoire
Jarvis: J'allume la lumiere avec une couleur aleatoire qui sera rouge

Vous: donne moi les informations que tu as des lumières
Jarvis: le nom des lumieres sont cuisine, couloir, lit haut, wc,

Vous: met la lumière de la cuisine en or
Jarvis: J'allume la lumiere de la cuisine en or

Vous: Augmente la lumière de 15 pourcent
Jarvis: J'allume la lumiere avec une intensite de +15 pourcents

Vous: Diminue la lumière de 17 pourcent tout en la mettant en bleu
Jarvis: J'allume la lumiere en bleu avec une intensite de -17 pourcents

Vous: Augmente la lumière
Jarvis: J'allume la lumiere en changeant l'intensite de +10

Vous: Diminue la lumière
Jarvis: J'allume la lumiere en changeant l'intensite de -10

Vous: Et pour conclure, change la lumière du lit haut en aléatoire
Jarvis: J'allume la lumiere de la lit haut avec une couleur aleatoire qui sera vert
```

## Author
[Cedric Devaux](https://github.com/devauxa)

See other plugins on the Jarvis store:
http://domotiquefacile.fr/jarvis/
