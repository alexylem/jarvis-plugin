#!/bin/bash
# Here you can create functions which will be available from the commands file
# You can also use here user variables defined in your config file
jarvis_lights () {
    echo $(python ${PWD}/plugins/jarvis-light-lifx/fr/light.py $*)
}
