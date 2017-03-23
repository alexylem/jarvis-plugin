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
This plugin uses mochad to control your X10 devices.
It will allow you to simply turn on and off your devices.
For now needs mochad pre-installed, this will be automated in an update.
See https://www.domoticz.com/wiki/X10_devices,_CM15_Pro

## Configuration

1. Indicate the port mochad uses (default is 1099):
   
   ```
   pg_x10_mochad_port=1099
   ```
   
2. List your device names & corresponding addresses in `json` format
   
   ```
   pg_hc_config='{ "devices":[
       { "name": "BEDROOM", "address": "A1"},
       { "name": "LIVING ROOM", "address": "A2"},
       { "name": "BAR", "address": "A3"}
   ]}'
   ```

## Usage
    
   Français
    
   ```
   Vous: allume le bar
   Jarvis: J'allume le bar...
   # > echo "pl A3 on" | nc localhost 1099
   ```
    
   English
    
   ```
   You: turn on the bar
   Jarvis: Switching on the bar...
   # > echo "pl A3 on" | nc localhost 1099
   ```

## Author
[alexylem](https://github.com/alexylem)
