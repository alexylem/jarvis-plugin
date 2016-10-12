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
## Description
Permet d'allumer ou d'éteindre un serveur (compatible wake on lan pour 
l'éveil et disposant du ssh pour l'extinction).

Les trois php sont dans le dossier du store

Pour l'installation : 
    - Dans utils.php il faut mettre l'ip de la machine à allumer, 
    le user et le pass ssh de la machine distante. Pensez ensuite à réduire 
    les droits d'accès en lecture écriture à ce fichier.

    - Dans wakenas.php mettre l'adresse mac de la machine à allumer et si votre machine est sur 
    une IP différente de 192.168.0.X comme par exemple 192.168.1.X, pensez à modifier l'adresse de 
    broadcast de 192.169.0.255 à 192.168.1.255

    - Dans shutdown.php pensez à modifier le chemin d'accès à utils.php si vous le mettez dans un répertoire
    différent. Modifier la variable $commande avec la commande ssh à éxecuter sur la machine distante. 
    "poweroff" par défaut

    - Dans le fichier de commande les chemins d'accès des fichiers php seront peut être à adapter


Turn on or off a server (need to supports wake on lan and with ssh for extinction).

The three php are in the store folder

For installation:
    - In utils.php must put the IP of the machine to turn on,
    the user ssh and password of the remote machine. then consider reducing
    the access rights to that file.

    - In wakenas.php put the mac address of the machine to wake and if your machine is on
    a different IP like 192.168.0.X or 192.168.1.X, consider changing address the broadcast address
    192.169.0.255 to 192.168.1.255

    - In shutdown.php consider changing the path to utils.php if you put it in a directory
    different. Change the variable $command ssh with the command to execute on the remote machine.
    "Poweroff" Default

    - In the command file the file access paths php may have to be changed


## Usage
```
Vous: Allume le serveur s'il te plait
Jarvis: allumage en cours
Vous : Eteint le serveur s'il te plait
jarvis : Extinction en cours

You: Turn on the server please
Jarvis: OK, waking the server
You: Off the server please
Jarvis: OK, I shutdown the server
```

## Author & Contributors
Rbillon
