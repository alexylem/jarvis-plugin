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
## Tuto pour pouvoir utilisé mpack
Il faut aussi installer ssmtp :
`sudo apt-get install ssmpt`
Ouvrir le fichier ssmtp.conf:
`nano /etc/ssmpt/ssmtp.conf`
Puis le configurer en ajoutant c'est quelques lignes avec vos infos (là c'est pour gmail):
root=adresse@gmail.com
mailhub=smtp.gmail.com:587
hostname=raspberry
AuthUser=adresse@gmail.com
AuthPass=MotDePasseGmail
FromLineOverride=YES
UseSTARTTLS=YES
Puis sauvegarder : Ctrl+X puis O pour oui et entrer

## Description
Gestion de la liste des courses

Pensez à modifier "VOTREEMAIL" et "VOTREPRENOM"

## Usage
```
`*AJOUTE (*) A LA LISTE*==echo "(1)" >> ~/listedescourses.txt && say "J'ai ajouté (1) à la liste"`
`*SUPPRIME*LA LISTE*|*VIDE*LA LISTE*==say "Veux tu confirmer la supression de la liste des courses?"`
`>*OUI*==echo "" > ~/listedescourses.txt && say "Ok la liste est effacée"`
`>*NON*==say "Je ne la supprime pas"`
`*LIS LA LISTE*|*QUOI*DANS*LA*LIS*COUR*==say "elle contient $(cat ~/listedescourses.txt)"`
`*ENVOI*LA*LIST*MAIL*==mpack -s "Contenu de la liste des courses" /home/pi/listedescourses.txt VOTREMAIL@hotmail.com && say "La liste des courses a été envoyer à VOTREPRENOM"`

You: Ajoute du pain à la liste des courses
Jarvis: J'ai ajouté du pain à la liste
You: Supprime la liste des courses
Jarvis: Veux tu confirmer la supression de la liste des courses?
You: Oui
Jarvis: Ok la liste est effacée
ou
You: Non
Jarvis: Je ne la supprime pas
You: Lis la liste des courses
Jarvis: elle contient du pain
You: Envoi moi la liste des courses
Jarvis: La liste des courses a été envoyer à VOTREPRENOM
```

## Author
[tchoul] et [godinperson] (https://github.com/tchoul)
